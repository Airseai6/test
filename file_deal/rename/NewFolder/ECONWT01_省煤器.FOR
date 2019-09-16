C************************************************************************
C   Module code: ECONWT01                                          
C   Module  Chinese  Name: 省煤器
C   Execution Rate:    
C   Version :1.0
C   Updated:   D/M/Y     Engineer:          
C   General Description /Purpose:
C************************************************************************
	SUBROUTINE ECONWT01( STEP  , !R*4 ,   S  ,计算步长,
C    INLET MASS PORT 1
     &           PWE    , !R*4 ,PI ,  MPA ,水进口压力,
     &           TWE    , !R*4 ,PI ,  .C  ,水进口温度,
     &           WWE    , !R*4 ,PI ,  .C  ,水进口流量,
C    INLET MASS PORT 2
     &           WGE    , !R*4 ,PO ,  KG/S,烟气进口流量,
     &           TGE    , !R*4 ,PI ,  .C  ,烟气进口温度,
C    INLET MASS PORT 3
     &           Wsbl   , !R*4 ,PI ,  KG/S,吹灰蒸汽流量,
     &           Hsbl   , !R*4 ,PI , KJ/KG,吹灰蒸汽焓.
C    OUTLET MASS PORT 1
     &           PWL    , !R*4 ,PI ,  MPA ,水出口压力,
     &           TWL    , !R*4 ,PI ,  .C  ,水出口温度,
     &           WWL    , !R*4 ,PI ,  KG/S,水出口流量,
     &           HWL    , !R*4 ,PO , KJ/KG,水出口焓,
C    OUTLET MASS PORT 2
     &           WGL    , !R*4 ,PO ,  KG/S,烟气出口流量,
     &           TGL    , !R*4 ,PI ,  .C  ,烟气出口温度,
C    BRANCH PROPERTY 1 WATER
     &           RB1    , !R*4 ,PO , ---  ,支路特性系数,
     &           RB2    , !R*4 ,PO , ---  ,支路特性系数,
     &           CB     , !R*4 ,PO , ---  ,支路特性系数,
     &           WLK    , !R*4 ,PO ,  KG/S,泄漏流量,
C    INTERNAL
     &           E1     , !R*4 ,PI ,  --- ,泄漏事故(0-100)
     &           E2     , !R*4 ,PI ,  --- ,积灰事故(0-100)
     &           E3     , !R*4 ,PI ,  --- ,备用
     &           E4     , !R*4 ,PI ,  --- ,备用
     &           TMC    , !R*4 ,PO ,  .C  ,冷端金属温度,
     &           TMH    , !R*4 ,PO ,  .C  ,热端金属温度,
     &           GMFH   , !R*4 ,PI ,  --- ,热端烟气与金属换热系数
     &           GMFC   , !R*4 ,PI ,  --- ,冷端烟气与金属换热系数
     &           WMFH   , !R*4 ,PI ,  --- ,热端水与金属换热系数
     &           WMFC   , !R*4 ,PI ,  --- ,冷端水与金属换热系数
     &           GMQH   , !R*4 ,PI ,  kJ/s,热端烟气对金属传热量
     &           GMQC   , !R*4 ,PI ,  kJ/s,冷端烟气对金属传热量
     &           WMQH   , !R*4 ,PI ,  kJ/s,热端金属对水传热量
     &           WMQC   , !R*4 ,PI ,  kJ/s,冷端金属对水传热量
     &           EMCH   , !R*4 ,PI ,  kJ/.C,热端金属比热
     &           EMCC   , !R*4 ,PI ,  kJ/.C,冷端金属比热
     &           ROLWE  , !R*4 ,PI ,  kg/m3,介质入口密度
C    CONSTANT
     &           EMM    , !R*4 , PI , KG  ,金属质量,
     &           COEF   , !R*4 ,PI ,  --- ,出口烟温迟延系数
     &           EC1    , !R*4 ,PI ,  --- ,泄漏程度标志
     &           CVMAX  , !R*4 ,PO , ---  ,最大通流能力,
C    ARRAY
     &           AWGL   , !R*4 ,PO , KG/S,各工况烟气流量数组
     &           AWWL   , !R*4 ,PO , KG/S,各工况水出口流量数组
     &           AGMFH  , !R*4 ,PO , －－,各工况热端烟气与金属换热系数数组
     &           AGMFC  , !R*4 ,PO , －－,各工况冷端烟气与金属换热系数数组
     &           AWMFH  , !R*4 ,PO , －－,各工况热端水与金属换热系数数组
     &           AWMFC  , !R*4 ,PO , －－,各工况冷端水与金属换热系数数组
     &           AGKQ   ,  !R*4 ,PO , －－,各工况烟气修正系数数组
     &           HWE    ,    !R*4 ,PI ,  .C  ,水进口焓
     &           TADD   ,   !R*4 ,PI ,  .C  ,再燃烧温升
C    Atmosphere
     &    Tatmw,   !  R*4,  C,  水环境温度
     &    Patmw,   !  R*4,  C,  水环境压力	
     &    Tatma,   !  R*4,  C,  风环境温度
     &    Patma,   !  R*4,  C,  风环境压力	
     &    Tatmo,   !  R*4,  C,  油环境温度
     &    Patmo   !  R*4,  C,  油环境压力

     &             )		
       
      DIMENSION       AWGL(4)   ,AWWL(4)   ,AGMFH(4)  ,
     &                AGMFC(4)  ,AWMFH(4)  ,AWMFC(4)  ,AGKQ(4)    
	 
      REAL*4   TGE   ,WGL  ,TGL  ,PWE  ,TWE  , WGE ,WWE,  
     &         PWL  ,TWL   ,WWL  ,HWL  ,TMC  ,TMH  ,EMM  ,
     &         COEF ,E1    ,EC1  ,WLK ,E2   ,Wsbl ,Hsbl ,
     &         RB1 ,RB2  ,CB  ,CVMAX,STEP,HWE ,TADD,
     &	Tatmw  , Patmw,   Tatma	, Patma  ,Tatmo	, Patmo

C--- Constant limit
      IF(EMM.LT.1.0E-05) EMM=1.0E-05

	 XE1=E1*0.01   !2006.8.29
	 XE2=E2*0.01   !
       WGL = WGE      
c       WWL = WWE      
           IF(WGL.LT.0.0) WGL = 0.0
           IF(WWL.LT.0.0) WWL = 0.0
C----------------------------------------------
C       Calculates heat transfer coeffience
C----------------------------------------------
	CALL BNCSM1(AWGL,AGMFH,WGL,XGMFH,4) !2006.12.06
	CALL BNCSM1(AWGL,AGMFC,WGL,XGMFC,4)
	CALL BNCSM1(AWWL,AWMFH,WWL,WMFH,4)
	CALL BNCSM1(AWWL,AWMFC,WWL,WMFC,4)
	CALL BNCSM1(AWGL,AGKQ,WGL,GKQ,4)   
c-------------------------------------------------------------        
c       The effects of ash blowing and E2 
c-------------------------------------------------------------

C	IF (WGL.gt.0.and.E2.gt.0.5)then
	IF (WGL.gt.0.and.XE2.gt.0.005) then  !2006.8.29
	    if (Wsbl.gt.0.1)then
	       GMFH=GMFH+0.01
	       GMFC=GMFC+0.01
	       if(GMFH.GT.AGMFH(1)) GMFH=AGMFH(1)
	       if(GMFC.GT.AGMFC(1)) GMFC=AGMFC(1)
	    ELSE
	       GMFH=GMFH-0.05  !0.01  !2006.12.07
	       GMFC=GMFC-0.05
	       
	       XX1=1-XE2  !2006.8.29
		   if(GMFH.LT.AGMFH(4)*XX1) GMFH=AGMFH(4)*XX1 
	       if(GMFC.LT.AGMFC(4)*XX1) GMFC=AGMFC(4)*XX1

	       if(GMFH.LT.AGMFH(4)*0.05) GMFH=AGMFH(4)*0.05 !2006.12.07
	       if(GMFC.LT.AGMFC(4)*0.05) GMFC=AGMFC(4)*0.05
	    ENDIF  
	ELSE
	  GMFH = XGMFH  !2006.12.06
	  GMFC = XGMFC 	 
	ENDIF
C----------------------------------------------
C       Calculates heat flow transfer
C----------------------------------------------
	
	GMQH=GMFH*WGL**0.65*(TGE-TMH)          !热端烟气对金属传热量,kJ/s
	WMQH=WMFH*WWL**0.8*(TMH-TWL)           !热端金属对水传热量,kJ/s
	GMQC=GMFC*WGL**0.65*(TGL-TMC)          !冷端烟气对金属传热量,kJ/s
	WMQC=WMFC*WWL**0.8*(TMC-TWE)           !冷端金属对水传热量,kJ/s
C----------------------------------------------
C       Calculates specific heat for metal
C----------------------------------------------
	
	CALL T_MC(TMH,EMCH)
	DMTH=(GMQH-WMQH)/(EMM*EMCH) 
	TMH=TMH+DMTH*STEP
C      XTMH=XTMH+DMTH*STEP
C	TMH=0.9*TMH+0.1*XTMH

C	IF(TMH.GT.TGE-1.0) TMH = TGE - 1.0
      IF(TMH.LT.Tatmw) TMH = Tatmw

	CALL T_MC(TMC,EMCC)
	DMTC=(GMQC-WMQC)/(EMM*EMCC)
	TMC=TMC+DMTC*STEP
C      XTMC=XTMC+DMTC*STEP
C	TMC=0.9*TMC+0.1*XTMC

C	IF(TMC.GT.TGE-1.0) TMC = TGE - 1.0
      IF(TMC.LT.Tatmw) TMC = Tatmw

C----------------------------------------------------------
C       Calculates water pressure and temperature in outlet
C----------------------------------------------------------
	
C        PWL=PWE-DWPN*WWL*WWL/(WWLN*WWLN)-DPH
	
C	CALL SW_PT_H(PWE,TWE,HWE)
	CALL SW_PT_V(PWE,TWE,VWE)
	CALL SW_PT_C(PWL,TWL,WCO)
c	CALL SW_PT_H(PWL,TWL,HWL)
	CALL T_GC(TGE,GCI)
	CALL T_GC(TGL,GCO)

	ROLWE = 1.0/VWE

	IF(WWL.GT.0.1) THEN
C	    DTWL=(WWL*(HWE-HWL)+WMQH)/(WWL*WCO+0.8*EMM*EMCH)
C	    TWL=TWL+DTWL*STEP
	    XWWL=WWL-WLK                                                    !2006.12.07
c	    DTWL=(WWL*HWE-XWWL*HWL-WLK*0.2*HWL+WMQH)/(XWWL*WCO+0.8*EMM*EMCH)! 泄漏会导致出口温度升高
c	    TWL=TWL+DTWL*STEP
	  DHWL=(WWL*HWE-XWWL*HWL-WLK*0.2*HWL+WMQH)/(XWWL+0.8*EMM*EMCH/WCO)
          HWL=HWL+DHWL*STEP
C	    CALL SW_PH_T(PWL,HWL,TWL)
	ELSE
C	    TWL=TWE
          HWL=HWE
	ENDIF
	
C	IF(TWL.LT.TWE) TWL=TWE
C      IF(HWL.LT.HWE) HWL=HWE    !2009.09.01

	CALL SW_PH_T(PWL,HWL,TWL)

C----------------------------------------------
C       Calculates gas temperature in outlet
C----------------------------------------------
	
	IF(WGL.GT.0.1) THEN
	    XTGL=(WGL*GCI*TGE-GMQC/GKQ)/(WGL*GCO)
	ELSE
	    XTGL=TGL
	ENDIF
	TGL=TGL+coef*(XTGL-TGL)
	
c-------------------------------------------------------------        
c       The effects of water leakage
c-------------------------------------------------------------
	
	CALL SW_PT_H(PWE,TWE,HWE)
	IF(XE1.GT.0.005) THEN
		IF(EC1.LT.0.5) THEN
		    WLK=XE1*0.2*PWE
		    EC1=1.0
		ELSE
		    WLK=WLK+XE1*1.0E-2*PWE
C		    X=0.2*WWL
		    X=0.3*WWL  !2006.8.29
		    IF(WLK.GT.X) WLK=X
		ENDIF
	ELSE
		WLK=0.0
		EC1=0.0
	ENDIF
			       
	IF(WGL.GT.0.5.AND.WLK.GT.0.1) THEN
C           SWE = WWE*(HWE-4.1868*102.9)/(4.1868*539)
	   TGL=WGL*TGL/(WGL+WLK)   
	ENDIF

c-------------------------------------------------------
c       the effect of ash blowing
c-------------------------------------------------------

	IF (WGL.gt.0.5.and.Wsbl.gt.0.1) THEN
	    TGL=(WGL*GCO*TGL+Wsbl*Hsbl)/(WGL+Wsbl)/GCO
	ENDIF
	IF (TGL.LT.Tatma)  TGL = Tatma

C----------------------------------------------------------------
C      Secondary Combustion zfb
C----------------------------------------------------------------
	IF(E3.GT.100) E3 = 100
	XXE3 = E3 * 0.01
      IF(E3.GT.0.5) THEN
		TADD = TADD + XXE3 * STEP
		IF(WGL.GT.10.0) THEN
			IF(WSBL.GT.0.5) TADD = TADD - 0.42 * STEP
		ELSE
			IF(WSBL.GT.0.5) THEN
				TADD = TADD - 0.75 * STEP
			ELSE
				TADD = TADD - 0.52 * STEP
			ENDIF
		ENDIF
		IF(TADD.GT.100.0) TADD = 100.0
		IF(TADD.LT.0.01) THEN
			TADD = 0.0
			E3 = 0.0
		ENDIF
	ELSE
		TADD = TADD - 0.5 * STEP
		IF(TADD.LT.0.01) TADD = 0.0
	ENDIF
	TMH = TMH + TADD * STEP
	TMC = TMC + TADD * STEP
	IF (TMH.GT.500.0) TMH=500.0
	IF (TMC.GT.450.0) TMC=450.0
	TGL = TGL + TADD * STEP * 2.5
C----------------------------------------------
C       Calculates RB1,RB2,CB
C----------------------------------------------

	CALL TPPCND (RB1,RB2,CB,CVMAX,WWL,ROLWE)

	END
	
