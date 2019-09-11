C************************************************************************
C   Module code: DEAEMI01                                          
C   Module  Chinese  Name: ������
C   Execution Rate:    
C   Version :1.0
C   Updated:   D/M/Y     Engineer:          
C   General Description /Purpose:
C************************************************************************ 
        SUBROUTINE  DEAEMI01(STEP,
C  Inlet Mass Port 1:
     \    PSE1,  !  R*4,  MPa,  #1�������ѹ��
     \    WSE1,  !  R*4,  kg/s,  #1��������
     \    HSE1,  !  R*4,  kJ/kg,  #1������
C  Inlet Mass Port 2:
     \    PSE2,  !  R*4,  MPa,  #2�������ѹ��
     \    WSE2,  !  R*4,  kg/s,  #2��������
     \    HSE2,  !  R*4,  kJ/kg,  #2������
C  Inlet Mass Port 3:
     \    PSE3,  !  R*4,  MPa,  #3�������ѹ��
     \    WSE3,  !  R*4,  kg/s,  #3��������
     \    HSE3,  !  R*4,  kJ/kg,  #3������
C  Inlet Mass Port 4:
     \    PWE1,  !  R*4,  MPa,  ����ˮѹ��
     \    WWE1,  !  R*4,  kg/s,  ����ˮ����
     \    HWE1,  !  R*4,  kJ/kg,  ����ˮ��
C  Inlet Mass Port 5:
     \    PWE2,  !  R*4,  MPa,  ��������ˮѹ��
     \    WWE2,  !  R*4,  kg/s,  ��������ˮ����
     \    HWE2,  !  R*4,  kJ/kg,  ��������ˮ��
C  Inlet Mass Port 6:
     \    PWE3,  !  R*4,  MPa,  #1��ѭ��ˮѹ��
     \    WWE3,  !  R*4,  kg/s,  #1��ѭ��ˮ����
     \    HWE3,  !  R*4,  kJ/kg,  #1��ѭ��ˮ��
C  Inlet Mass Port 7:
     \    PWE4,  !  R*4,  MPa,  #2��ѭ��ˮѹ��
     \    WWE4,  !  R*4,  kg/s,  #2��ѭ��ˮ����
     \    HWE4,  !  R*4,  kJ/kg,  #2��ѭ��ˮ��
C  Inlet Mass Port 8:
     \    PWE5,  !  R*4,  MPa,  #3��ѭ��ˮѹ��
     \    WWE5,  !  R*4,  kg/s,  #3��ѭ��ˮ����
     \    HWE5,  !  R*4,  kJ/kg,  #3��ѭ��ˮ��
C  Inlet Mass Port 9:
     \    PWE6,  !  R*4,  MPa,  ����������������ѹ��
     \    WWE6,  !  R*4,  kg/s,  ��������������������
     \    HWE6,  !  R*4,  kJ/kg,  ������������������
C  Inlet Mass Port 10:
     \    PWE7,  !  R*4,  MPa,  ���������ˮ��������ѹ��
     \    WWE7,  !  R*4,  kg/s,  ���������ˮ������������
     \    HWE7,  !  R*4,  kJ/kg,  ���������ˮ����������
C  Outlet Mass Port 1:
     \    PWL1,  !  R*4,  MPa,  #1����ˮѹ��
     \    WWL1,  !  R*4,  kg/s,  #1����ˮ����
     \    HWL1,  !  R*4,  kJ/kg,  #1����ˮ��
     \    TWL1,  !  R*4,  C,  #1����ˮ��
C  Outlet Mass Port 2:
     \    PWL2,  !  R*4,  MPa,  #2����ˮѹ��
     \    WWL2,  !  R*4,  kg/s,  #2����ˮ����
     \    HWL2,  !  R*4,  kJ/kg,  #2����ˮ��
     \    TWL2,  !  R*4,  C,  #2����ˮ��
C  Outlet Mass Port 3:
     \    PWL3,  !  R*4,  MPa,  #3����ˮѹ��
     \    WWL3,  !  R*4,  kg/s,  #3����ˮ����
     \    HWL3,  !  R*4,  kJ/kg,  #3����ˮ��
     \    TWL3,  !  R*4,  C,  #3����ˮ��
C  Outlet Mass Port 4:
     \    PSL,  !  R*4,  MPa,  ��������ѹ��
     \    WSL,  !  R*4,  kg/s,  ����������
     \    HSL,  !  R*4,  kJ/kg,  ����������
     \    TSL,  !  R*4,  C,  ��������
C  Input Information Port 1:
     \    AV10,  !  R*4,  --,  #1����������
C  Input Information Port 2:
     \    AV20,  !  R*4,  --,  #2����������
C  Input Information Port 1:
     \    AV30,  !  R*4,  --,  ����������
C  Output Information Port 1:
     \    LEVEL,  !  R*4,  mm,  ˮλָʾֵ
C  Output Information Port 2:
     \    AV4,  !  R*4,  --,  ��ȫ�ſ���
C  Internal:
     \    LS,  !  R*4,  m,  ˮλ
     \    HF,  !  R*4,  kg/m^3,  ���౥��ˮ��
     \    TSM,  !  R*4,  C,  �����¶�
     \    PS,  !  R*4,  MPa,  ѹ��
     \    TW,  !  R*4,  C,  ˮ��ˮ��
     \    HW,  !  R*4,  kJ/kg,  ˮ��ˮ��
C  Constant:
     \    KLTOP,  !  R*4,  m,  �����߶�
     \    KSAM,  !  R*4,  kW/C,  �������ɢ��ϵ��
     \    KAT,  !  R*4,  kW/C,  ˮ�����ɢ��ϵ��
     \    KV,  !  R*4,  --,  �ſ�ϵ��
     \    KSR,  !  R*4,  --,  ����������ϵ��
     \    KSF,  !  R*4,  --,  ��ȫ������ϵ��
     \    KMS,  !  R*4,  kg,  ��������������
     \    UCD,  !  R*4,  kW/C,  Һ���������ϵ��
     \    UEV,  !  R*4,  kW/C,  Һ����������ϵ��
     \    KLTK,  !  R*4,  m,  ˮ�������ڸ߶�
     \    KOF,  !  R*4,  --,  ��������ϵ��
     \    KDIA,  !  R*4,  m,  ˮ��԰Ͳֱ��
     \    KLEN,  !  R*4,  m,  ˮ�䳤��
     \    KLMIN,  !  R*4,  m,  ˮ�����ˮλ
     \    KLGAIN,  !  R*4,  --,  ˮλָʾ��λ����ϵ��
     \    KLBIAS,  !  R*4,  m,  ˮλָʾ���߶�
     \    KAR,  !  R*4,  m^2,  ��������������
     \    DS,  !  R*4,  m,  ����ͷֱ��
     \    LENS,  !  R*4,  m,  ����ͷ����
     \    CPMA,  !  R*4,  MPa,  ��ȫ�Ŷ���ֵ
     \    CPMI,  !  R*4,  MPa,  ��ȫ�Ż���ֵ
     \    MODE,   !  R*4,  --,  ˮ����ʽѡ��
     \    PA,  !  R*4,  MPa,  ����ѹ��
     \    TA , !  R*4,  C,  �����¶�
C    Atmosphere
     &    Tatmw,   !  R*4,  C,  ˮ�����¶�
     &    Patmw,   !  R*4,  C,  ˮ����ѹ��	
     &    Tatma,   !  R*4,  C,  �绷���¶�
     &    Patma,   !  R*4,  C,  �绷��ѹ��	
     &    Tatmo,   !  R*4,  C,  �ͻ����¶�
     &    Patmo   !  R*4,  C,  �ͻ���ѹ��
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
