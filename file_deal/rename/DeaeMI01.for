C************************************************************************
C   Module code: DEAEMI01                                          
C   Module  Chinese  Name: 除氧器
C   Execution Rate:    
C   Version :1.0
C   Updated:   D/M/Y     Engineer:          
C   General Description /Purpose:
C************************************************************************ 
        SUBROUTINE  DEAEMI01(STEP,
C  Inlet Mass Port 1:
     \    PSE1,  !  R*4,  MPa,  #1蒸汽入口压力
     \    WSE1,  !  R*4,  kg/s,  #1蒸汽流量
     \    HSE1,  !  R*4,  kJ/kg,  #1蒸汽焓
C  Inlet Mass Port 2:
     \    PSE2,  !  R*4,  MPa,  #2蒸汽入口压力
     \    WSE2,  !  R*4,  kg/s,  #2蒸汽流量
     \    HSE2,  !  R*4,  kJ/kg,  #2蒸汽焓
C  Inlet Mass Port 3:
     \    PSE3,  !  R*4,  MPa,  #3蒸汽入口压力
     \    WSE3,  !  R*4,  kg/s,  #3蒸汽流量
     \    HSE3,  !  R*4,  kJ/kg,  #3蒸汽焓
C  Inlet Mass Port 4:
     \    PWE1,  !  R*4,  MPa,  凝结水压力
     \    WWE1,  !  R*4,  kg/s,  凝结水流量
     \    HWE1,  !  R*4,  kJ/kg,  凝结水焓
C  Inlet Mass Port 5:
     \    PWE2,  !  R*4,  MPa,  加热器疏水压力
     \    WWE2,  !  R*4,  kg/s,  加热器疏水流量
     \    HWE2,  !  R*4,  kJ/kg,  加热器疏水焓
C  Inlet Mass Port 6:
     \    PWE3,  !  R*4,  MPa,  #1再循环水压力
     \    WWE3,  !  R*4,  kg/s,  #1再循环水流量
     \    HWE3,  !  R*4,  kJ/kg,  #1再循环水焓
C  Inlet Mass Port 7:
     \    PWE4,  !  R*4,  MPa,  #2再循环水压力
     \    WWE4,  !  R*4,  kg/s,  #2再循环水流量
     \    HWE4,  !  R*4,  kJ/kg,  #2再循环水焓
C  Inlet Mass Port 8:
     \    PWE5,  !  R*4,  MPa,  #3再循环水压力
     \    WWE5,  !  R*4,  kg/s,  #3再循环水流量
     \    HWE5,  !  R*4,  kJ/kg,  #3再循环水焓
C  Inlet Mass Port 9:
     \    PWE6,  !  R*4,  MPa,  进入除氧器混合流体压力
     \    WWE6,  !  R*4,  kg/s,  进入除氧器混合流体流量
     \    HWE6,  !  R*4,  kJ/kg,  进入除氧器混合流体焓
C  Inlet Mass Port 10:
     \    PWE7,  !  R*4,  MPa,  进入除氧器水箱混合流体压力
     \    WWE7,  !  R*4,  kg/s,  进入除氧器水箱混合流体流量
     \    HWE7,  !  R*4,  kJ/kg,  进入除氧器水箱混合流体焓
C  Outlet Mass Port 1:
     \    PWL1,  !  R*4,  MPa,  #1出口水压力
     \    WWL1,  !  R*4,  kg/s,  #1出口水流量
     \    HWL1,  !  R*4,  kJ/kg,  #1出口水焓
     \    TWL1,  !  R*4,  C,  #1出口水温
C  Outlet Mass Port 2:
     \    PWL2,  !  R*4,  MPa,  #2出口水压力
     \    WWL2,  !  R*4,  kg/s,  #2出口水流量
     \    HWL2,  !  R*4,  kJ/kg,  #2出口水焓
     \    TWL2,  !  R*4,  C,  #2出口水温
C  Outlet Mass Port 3:
     \    PWL3,  !  R*4,  MPa,  #3出口水压力
     \    WWL3,  !  R*4,  kg/s,  #3出口水流量
     \    HWL3,  !  R*4,  kJ/kg,  #3出口水焓
     \    TWL3,  !  R*4,  C,  #3出口水温
C  Outlet Mass Port 4:
     \    PSL,  !  R*4,  MPa,  出口蒸汽压力
     \    WSL,  !  R*4,  kg/s,  出口蒸汽量
     \    HSL,  !  R*4,  kJ/kg,  出口蒸汽焓
     \    TSL,  !  R*4,  C,  出口汽温
C  Input Information Port 1:
     \    AV10,  !  R*4,  --,  #1放汽阀开度
C  Input Information Port 2:
     \    AV20,  !  R*4,  --,  #2放汽阀开度
C  Input Information Port 1:
     \    AV30,  !  R*4,  --,  溢流阀开度
C  Output Information Port 1:
     \    LEVEL,  !  R*4,  mm,  水位指示值
C  Output Information Port 2:
     \    AV4,  !  R*4,  --,  安全门开度
C  Internal:
     \    LS,  !  R*4,  m,  水位
     \    HF,  !  R*4,  kg/m^3,  汽侧饱和水焓
     \    TSM,  !  R*4,  C,  蒸汽温度
     \    PS,  !  R*4,  MPa,  压力
     \    TW,  !  R*4,  C,  水箱水温
     \    HW,  !  R*4,  kJ/kg,  水箱水焓
C  Constant:
     \    KLTOP,  !  R*4,  m,  顶部高度
     \    KSAM,  !  R*4,  kW/C,  汽侧外壳散热系数
     \    KAT,  !  R*4,  kW/C,  水箱外壳散热系数
     \    KV,  !  R*4,  --,  排空系数
     \    KSR,  !  R*4,  --,  放汽门流量系数
     \    KSF,  !  R*4,  --,  安全门流量系数
     \    KMS,  !  R*4,  kg,  汽侧混和流体质量
     \    UCD,  !  R*4,  kW/C,  液面凝结放热系数
     \    UEV,  !  R*4,  kW/C,  液面蒸发吸热系数
     \    KLTK,  !  R*4,  m,  水箱溢流口高度
     \    KOF,  !  R*4,  --,  溢流流量系数
     \    KDIA,  !  R*4,  m,  水箱园筒直径
     \    KLEN,  !  R*4,  m,  水箱长度
     \    KLMIN,  !  R*4,  m,  水箱最低水位
     \    KLGAIN,  !  R*4,  --,  水位指示单位换算系数
     \    KLBIAS,  !  R*4,  m,  水位指示零点高度
     \    KAR,  !  R*4,  m^2,  汽侧容器横截面积
     \    DS,  !  R*4,  m,  除氧头直径
     \    LENS,  !  R*4,  m,  除氧头长度
     \    CPMA,  !  R*4,  MPa,  安全门动作值
     \    CPMI,  !  R*4,  MPa,  安全门回座值
     \    MODE,   !  R*4,  --,  水箱型式选项
     \    PA,  !  R*4,  MPa,  大气压力
     \    TA , !  R*4,  C,  大气温度
C    Atmosphere
     &    Tatmw,   !  R*4,  C,  水环境温度
     &    Patmw,   !  R*4,  C,  水环境压力	
     &    Tatma,   !  R*4,  C,  风环境温度
     &    Patma,   !  R*4,  C,  风环境压力	
     &    Tatmo,   !  R*4,  C,  油环境温度
     &    Patmo   !  R*4,  C,  油环境压力
     \  )
       REAL *4
     \  LEVEL     , LS        , KLTOP     , KSAM      , KAT       , 
     \  KV        , KSR       , KSF       , KMS       , KLTK      , 
     \  KOF       , KDIA      , KLEN      , KLMIN     , KLGAIN    , 
     \  KLBIAS    , KAR       , LENS      , MODE  ,
     &	Tatmw  , Patmw,   Tatma	, Patma  ,Tatmo	, Patmo                                                         

	 CALL SW_PT_H(Patmw,Tatmw,XXH)
        IF(XXH.LT.0.001)XXH = 0.001
        IF ( LS .LT. KLTOP ) THEN
           XFULL = 0.0
        ELSE
           XFULL = 1.0
        END IF

        XWSHE = WSE1 + WSE2 + WSE3 + WWE1 + WWE2 + WWE6

        CALL SATW_H_T( HF, TSM)
        CALL SAT_T_P( TSM, XPV )

        PS = XPV
        IF ( PS .LT. PA ) PS = PA

        CALL SAT_P_VVHH( XPV, XROLF, XROLG, X, XHG )
        XROLF = 1.0/XROLF
        XROLG = 1.0/XROLG

        XWSAM = KSAM * ( TSM-TA ) / ( XHG-HF )

        IF ( PS .GT. PA ) THEN
           XPSD = SQRT( PS-PA )
        ELSE
           XPSD = 0.0
        END IF

        IF ( XFULL .GT. 0.5 ) THEN
           XWWV = KV * XPSD
        ELSE
           XWWV = 0.0
        END IF

        IF ( PS .GT. CPMA ) THEN
           AV4 = 1.0
        ELSE IF ( PS .LT. CPMI ) THEN
           AV4 = 0.0
        END IF

        IF ( XFULL .LT. 0.5 ) THEN
           XWSR = ( KSR * ( AV10 + AV20 ) + KSF * AV4 ) * XPSD
           XWWR = 0.0
        ELSE
           XWSR = 0.0
           XWWR = ( XROLF/XROLG ) * (KSR*(AV10+AV20) + KSF*AV4) * XPSD
        END IF

        IF ( TSM.GT. TW ) THEN
           XCD = 1.0
           XEV = 0.0
        ELSE
           XCD = 0.0
           XEV = 1.0
        END IF

        XNU =  WSE1*(HSE1-HF) + WSE2*(HSE2-HF) + WSE3*(HSE3-HF)
     \       + WWE1*(HWE1-HF) + WWE6*(HWE6-HF) + WWE2 *(HWE2 -HF)
     \       - XWSR*(XHG -HF) - WSL *(XHG -HF) - KSAM*(TSM -TA)
     \       + (1.0-XFULL)*(UCD*XCD+UEV*XEV)*(TW-TSM)
        XDM =  KMS + STEP * ( XWSHE - XWSR - WSL
     \       + (KSAM+(1.0-XFULL)*(UCD*XCD+UEV*XEV))*TSM/HF )

        HF  =  HF + STEP * XNU / XDM
        IF ( HF .LT. XXH ) THEN
           HF = XXH
        ELSE IF ( HF .GT. 961.8 ) THEN
           HF = 961.8
        END IF

        IF ( LS .GT. KLTK ) THEN
           XWOF = KOF * AV30 * XPSD
        ELSE
           XWOF = 0.0
        END IF

        IF ( TSM.GT. TW ) THEN
           XWCD = ( 1.0-XFULL ) * UCD * ( TSM-TW ) / ( XHG-HF )
           XWEV = 0.0
        ELSE
           XWCD = 0.0
           XWEV = ( 1.0-XFULL ) * UEV * ( TW-TSM) / ( XHG-HF )
        END IF

        XWTKE = XWSHE + WWE3 + WWE4 + WWE5 + WWE7 + XWCD + XWSAM
        XWTKL = WWL1 + WWL2 + WWL3 + XWEV + XWWV + XWWR + XWOF

        CALL SATW_H_T( HW, TW )

        CALL SATW_T_V( TW, XROLW )
        XROLW = 1.0/XROLW

        IF ( LS .LT. KLTK ) THEN
           IF ( MODE .LT. 0.5 ) THEN
               IF ( KDIA .GT. LS ) THEN
			    XA = 2.0 * KLEN * SQRT( LS * ( KDIA-LS ) )
                  X  = 0.05 * KDIA * KLEN
			   ELSE
	            X  = 0.05 * KDIA * KLEN
			    XA = X
               END IF
			IF ( XA .LT. X ) XA = X
           ELSE
              XA = 0.785398 * KDIA * KDIA
           END IF
        ELSE
           XA = KAR
        END IF

        LS = LS + ( XWTKE-XWTKL ) / ( XROLW*XA ) * STEP
        IF ( LS .GT. KLTOP )  THEN
           LS = KLTOP
        ELSE IF ( LS .LT. 0.0 ) THEN
           LS = 0.0
        END IF
        LEVEL = KLGAIN * ( LS - KLBIAS )
        IF ( MODE .LT. 0.5 ) THEN
           XATK = 0.85 * KDIA * KLEN
        ELSE
           XATK = 0.785398 * KDIA * KDIA
        END IF
        IF ( LS .LT. KLMIN ) THEN
           XLLIMIT = KLMIN
        ELSE IF ( LS .GT. KLTK ) THEN
           XLLIMIT = KLTK
        ELSE                                    ! 2006.07.10
	     XLLIMIT = LS
        END IF
        XMW = XATK * XLLIMIT * XROLW
        IF ( LS .GE. KLTK ) THEN
           XMWS = ( LS - KLTK ) * KAR * XROLW
        ELSE
           XMWS = 0.0
        END IF
        XMW = XMW + XMWS
        XNU =  XWSHE*(HF  -HW) + WWE3*(HWE3-HW) + WWE4*(HWE4-HW)
     \       + WWE5 *(HWE5-HW) + WWE7*(HWE7-HW) + XWSAM*(HF -HW)
     \       + (1.0-XFULL)*( UEV*XEV + UCD*XCD ) * (TSM-TW)
     \       - KAT * (TW-TA)
        XDM =  XMW + STEP * ( XWSHE + WWE2 + WWE3 + WWE4 + WWE5 + WWE7
     \       + XWSAM + (KAT + (1.0-XFULL)*(UEV*XEV+UCD*XCD))*TW/HW )

        HW  = HW + STEP * XNU / XDM
        IF ( HW .LT. XXH ) THEN
           HW = XXH
        ELSE IF ( HW .GT. 961.8 ) THEN
           HW = 961.8
        END IF

        PSE1 = PS
        PSE2 = PS
        PSE3 = PS
        PWE1 = PS
        PSL  = PS
        PWE2  = PS
        PWE3 = PS
        PWE4 = PS
        PWE5 = PS
        PWE6 = PS
        PWE7 = PS
        PWL1 = PS + 9.80665E-06 * LS * XROLW
        PWL2 = PWL1
        PWL3 = PWL1
        HWL1 = HW
        HWL2 = HW
        HWL3 = HW
        TWL1 = TW
        TWL2 = TW
        TWL3 = TW
        HSL  = XHG
        TSL  = TSM

        RETURN
        END
