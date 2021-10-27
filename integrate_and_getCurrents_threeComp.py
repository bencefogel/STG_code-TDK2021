from pylab import * 



def variables(v,t,p,temp,onlyDerivate = True):	
  
    if (len(v.shape) == 1): v.shape = (1, 46)					
    V_AB = v[:,0]
    NaM_AB = v[:,1]
    NaH_AB = v[:,2]
    CaTM_AB = v[:,3]
    CaTH_AB = v[:,4]
    CaSM_AB = v[:,5]
    CaSH_AB = v[:,6]
    HM_AB = v[:,7]
    KdM_AB = v[:,8]
    KCaM_AB = v[:,9]
    AM_AB = v[:,10]
    AH_AB = v[:,11]
    IntCa_AB = v[:,12]
    
    V_LP = v[:,13]
    NaM_LP = v[:,14]
    NaH_LP = v[:,15]
    CaTM_LP = v[:,16]
    CaTH_LP = v[:,17]
    CaSM_LP = v[:,18]
    CaSH_LP = v[:,19]
    HM_LP = v[:,20]
    KdM_LP = v[:,21]
    KCaM_LP = v[:,22]
    AM_LP = v[:,23]
    AH_LP = v[:,24]
    IntCa_LP = v[:,25]
    
    V_PY = v[:,26]
    NaM_PY = v[:,27]
    NaH_PY = v[:,28]
    CaTM_PY = v[:,29]
    CaTH_PY = v[:,30]
    CaSM_PY = v[:,31]
    CaSH_PY = v[:,32]
    HM_PY = v[:,33]
    KdM_PY = v[:,34]
    KCaM_PY = v[:,35]
    AM_PY = v[:,36]
    AH_PY = v[:,37]
    IntCa_PY = v[:,38]
    
    
    s_syn_ABPYglut = v[:,39]
    s_syn_ABPYchol = v[:,40]
    s_syn_ABLPglut = v[:,41]
    s_syn_ABLPchol = v[:,42]
    s_syn_LPPYglut = v[:,43]
    s_syn_PYLPglut = v[:,44]
    s_syn_LPABglut = v[:,45]
    
    
    
    CaReV_AB = CaNernst(IntCa_AB, temp)  
    
    CaRev_LP = CaNernst(IntCa_LP, temp)
    
    CaRev_PY = CaNernst(IntCa_PY, temp)
	
    C = 0.628#  // Capacitance (uF / cm^2)
    
    #A
    # gsABPYglut = 30.0
    # gsABPYchol = 30.0
    # gsABLPglut = 100.0
    # gsABLPchol = 0.0
    # gsLPPYglut = 3.0
    # gsPYLPglut = 30.0
    # gsLPABglut = 30.0
    
    
    #B
    gsABPYglut = 1.0
    gsABPYchol = 100.0
    gsABLPglut = 10.0
    gsABLPchol = 0.0
    gsLPPYglut = 1.0
    gsPYLPglut = 100.0
    gsLPABglut = 10.0
    

 #    // Ionic Currents (mV / ms)	    
 #    // double caF = p.get(17);  // Current (nA) to Concentration (uM) Conversion Factor (uM / nA)
 #    // double Ca0 = p.get(18);  // Background Intracellular Calcium Concentration (uM)
 #    // these numbers below convert calcium current to calcium concentration and have not been measured so people change them. 

    caF = 14.96		
    Ca0 = 0.05
    
#     //activation timescale of imi appears to be constant (golowash92) 
		
    tauIntCa = 200   #// Calcium buffer time constant (ms)p[35]

#     // Equilibrium Points of Calcium Sensors
#     // p_g=[gNa, gCaT,gCaS,gA,gKCa,gKd,gH,g_leak]

#     // Fixed Maximal Conductances of AB neurons

    gNa_AB = p[0]    #// Transient Sodium Maximal Conductance
    gCaT_AB = p[1]    #// Low Threshold Calcium Maximal Conductance
    gCaS_AB = p[2]    #// Slow Calcium Maximal Conductance
    gA_AB   = p[3]    #// Transient Potassium Maximal Conductance
    gKCa_AB = p[4]  	#// Calcium Dependent Potassium Maximal Conductance
    gKd_AB  = p[5]    #// Potassium Maximal Conductance
    gH_AB   = p[6]    #// Hyperpolarization Activated Cation Maximal Conductance
    gL_AB   = p[7]    #// Leak Maximal Conductance
    
#    // Fixed Maximal Conductances of LP neurons
    gNa_LP = p[8]    #// Transient Sodium Maximal Conductance
    gCaT_LP = p[9]    #// Low Threshold Calcium Maximal Conductance
    gCaS_LP = p[10]    #// Slow Calcium Maximal Conductance
    gA_LP   = p[11]    #// Transient Potassium Maximal Conductance
    gKCa_LP = p[12]  	#// Calcium Dependent Potassium Maximal Conductance
    gKd_LP  = p[13]    #// Potassium Maximal Conductance
    gH_LP   = p[14]    #// Hyperpolarization Activated Cation Maximal Conductance
    gL_LP   = p[15]    #// Leak Maximal Conductance
    
#    // Fixed Maximal Conductances of LP neurons
    gNa_PY = p[16]    #// Transient Sodium Maximal Conductance
    gCaT_PY = p[17]    #// Low Threshold Calcium Maximal Conductance
    gCaS_PY = p[18]    #// Slow Calcium Maximal Conductance
    gA_PY   = p[19]    #// Transient Potassium Maximal Conductance
    gKCa_PY = p[20]  	#// Calcium Dependent Potassium Maximal Conductance
    gKd_PY  = p[21]    #// Potassium Maximal Conductance
    gH_PY   = p[22]    #// Hyperpolarization Activated Cation Maximal Conductance
    gL_PY   = p[23]    #// Leak Maximal Conductance
    

# // p_Erev = [e_leak,e_na,e_k,e_h]
    EL = -50 #   // Leak Reversal Potential  
    ENa = 50#  // Sodium Reversal Potential  
    ECaT_AB = CaReV_AB #    // Low Threshold Calcium Reversal Potential
    ECaS_AB = CaReV_AB #   // Slow Calcium Reversal Potential
    
    ECaT_LP = CaRev_LP #    // Low Threshold Calcium Reversal Potential
    ECaS_LP = CaRev_LP #   // Slow Calcium Reversal Potential
    
    ECaT_PY= CaRev_PY#    // Low Threshold Calcium Reversal Potential
    ECaS_PY= CaRev_PY#   // Slow Calcium Reversal Potential

    EKd  = -80 #   // Potassium Reversal PotentialEKd  
    EKCa = -80#  // Calcium Dependent Potassium Reversal Potential 
    EA   = -80 #    // Transient Potassium Reversal Potential 
    EH   = -20 #    // Hyperpolarization Activated Cation Reversal Potential EH   

    Es_glut = -70  # Glutamatergic synaptic reversal potential   
    Es_chol = -80  # Cholinergic synaptic reversal potential
    
    k_glut = 1/40
    k_chol = 1/100


#     Applied Current    
    Iapp = 0

#     Steady State Gating Variables of ABPD3 neuron
    NaMinf_AB  = boltzSS(V_AB, 25.5, -5.29)	#;  // m^3  
    NaHinf_AB  = boltzSS(V_AB, 48.9, 5.18)		#;  // h
    CaTMinf_AB = boltzSS(V_AB, 27.1, -7.20)	#;  // m^3
    CaTHinf_AB = boltzSS(V_AB, 32.1, 5.50)		#;  // h
    CaSMinf_AB = boltzSS(V_AB, 33.0, -8.1)		#;  // m^3
    CaSHinf_AB = boltzSS(V_AB, 60.0, 6.20)		#;  // h
    HMinf_AB   = boltzSS(V_AB, 75.0, 5.5)		#;  // m (V, 70.0, 6.0)
    KdMinf_AB  = boltzSS(V_AB, 12.3, -11.8)	#;  // m^4
    KCaMinf_AB = (IntCa_AB/(IntCa_AB + 3.0))*boltzSS(V_AB, 28.3, -12.6)#;  // m^4
    AMinf_AB   = boltzSS(V_AB, 27.2, -8.70)	#;  // m^3
    AHinf_AB   = boltzSS(V_AB, 56.9, 4.90)		#;  // h
   
    #Steady state gating variables of LP neuron
    NaMinf_LP  = boltzSS(V_LP, 25.5, -5.29)	#;  // m^3
    NaHinf_LP = boltzSS(V_LP, 48.9, 5.18)		#;  // h
    CaTMinf_LP = boltzSS(V_LP, 27.1, -7.20)	#;  // m^3
    CaTHinf_LP = boltzSS(V_LP, 32.1, 5.50)		#;  // h
    CaSMinf_LP = boltzSS(V_LP, 33.0, -8.1)		#;  // m^3
    CaSHinf_LP = boltzSS(V_LP, 60.0, 6.20)		#;  // h
    HMinf_LP   = boltzSS(V_LP, 75.0, 5.5)		#;  // m (V, 70.0, 6.0)
    KdMinf_LP  = boltzSS(V_LP, 12.3, -11.8)	#;  // m^4
    KCaMinf_LP = (IntCa_LP/(IntCa_LP + 3.0))*boltzSS(V_LP, 28.3, -12.6)#;  // m^4
    AMinf_LP   = boltzSS(V_LP, 27.2, -8.70)	#;  // m^3
    AHinf_LP   = boltzSS(V_LP, 56.9, 4.90)		#;  // h
    
    #Steady state gating variables of PY neuron
    NaMinf_PY  = boltzSS(V_PY, 25.5, -5.29)	#;  // m^3
    NaHinf_PY = boltzSS(V_PY, 48.9, 5.18)		#;  // h
    CaTMinf_PY = boltzSS(V_PY, 27.1, -7.20)	#;  // m^3
    CaTHinf_PY = boltzSS(V_PY, 32.1, 5.50)		#;  // h
    CaSMinf_PY = boltzSS(V_PY, 33.0, -8.1)		#;  // m^3
    CaSHinf_PY = boltzSS(V_PY, 60.0, 6.20)		#;  // h
    HMinf_PY   = boltzSS(V_PY, 75.0, 5.5)		#;  // m (V, 70.0, 6.0)
    KdMinf_PY  = boltzSS(V_PY, 12.3, -11.8)	#;  // m^4
    KCaMinf_PY = (IntCa_PY/(IntCa_PY + 3.0))*boltzSS(V_PY, 28.3, -12.6)#;  // m^4
    AMinf_PY   = boltzSS(V_PY, 27.2, -8.70)	#;  // m^3
    AHinf_PY   = boltzSS(V_PY, 56.9, 4.90)		#;  // h
    
    
    
    # // Time Constants (ms) of ABPD3 neuron
    tauNaM_AB  = tauX(V_AB, 2.64, 2.52, 120.0, -25.0) 
    tauNaH_AB  = tauX(V_AB, 0.0, -1.34, 62.9, -10.0)*tauX(V_AB, 1.5, -1.00, 34.9, 3.60) 
    tauCaTM_AB = tauX(V_AB, 43.4, 42.6, 68.1, -20.5)															
    tauCaTH_AB = tauX(V_AB, 210.0, 179.6, 55.0, -16.9)															
    tauCaSM_AB = spectau(V_AB, 2.80, 14.00, 27.0, 10.0, 70.0, -13.0)										
    tauCaSH_AB = spectau(V_AB, 120.0, 300.0, 55.0, 9.00, 65.0, -16.0) 
    tauHM_AB   = spectau(V_AB,0.0,2.0,169.7,-11.6,-26.7,14.3)                                              															
    tauKdM_AB = tauX(V_AB, 14.4, 12.8, 28.3, -19.2)	 														
    tauKCaM_AB = tauX(V_AB, 180.6, 150.2, 46.0, -22.7) 															
    tauAM_AB   = tauX(V_AB, 23.2, 20.8, 32.9, -15.2)	 															
    tauAH_AB   = tauX(V_AB, 77.2, 58.4, 38.9, -26.5)		

    # // Time Constants (ms) of LP neuron
    tauNaM_LP  = tauX(V_LP, 2.64, 2.52, 120.0, -25.0) 
    tauNaH_LP  = tauX(V_LP, 0.0, -1.34, 62.9, -10.0)*tauX(V_LP, 1.5, -1.00, 34.9, 3.60) 
    tauCaTM_LP= tauX(V_LP, 43.4, 42.6, 68.1, -20.5)															
    tauCaTH_LP = tauX(V_LP, 210.0, 179.6, 55.0, -16.9)															
    tauCaSM_LP= spectau(V_LP, 2.80, 14.00, 27.0, 10.0, 70.0, -13.0)										
    tauCaSH_LP = spectau(V_LP, 120.0, 300.0, 55.0, 9.00, 65.0, -16.0) 
    tauHM_LP  = spectau(V_LP,0.0,2.0,169.7,-11.6,-26.7,14.3)                                              															
    tauKdM_LP = tauX(V_LP, 14.4, 12.8, 28.3, -19.2)	 														
    tauKCaM_LP= tauX(V_LP, 180.6, 150.2, 46.0, -22.7) 															
    tauAM_LP   = tauX(V_LP, 23.2, 20.8, 32.9, -15.2)	 															
    tauAH_LP   = tauX(V_LP, 77.2, 58.4, 38.9, -26.5)	
    
    # // Time Constants (ms) of PY neuron
    tauNaM_PY  = tauX(V_PY, 2.64, 2.52, 120.0, -25.0) 
    tauNaH_PY  = tauX(V_PY, 0.0, -1.34, 62.9, -10.0)*tauX(V_PY, 1.5, -1.00, 34.9, 3.60) 
    tauCaTM_PY= tauX(V_PY, 43.4, 42.6, 68.1, -20.5)															
    tauCaTH_PY = tauX(V_PY, 210.0, 179.6, 55.0, -16.9)															
    tauCaSM_PY= spectau(V_PY, 2.80, 14.00, 27.0, 10.0, 70.0, -13.0)										
    tauCaSH_PY = spectau(V_PY, 120.0, 300.0, 55.0, 9.00, 65.0, -16.0) 
    tauHM_PY  = spectau(V_PY,0.0,2.0,169.7,-11.6,-26.7,14.3)                                              															
    tauKdM_PY = tauX(V_PY, 14.4, 12.8, 28.3, -19.2)	 														
    tauKCaM_PY= tauX(V_PY, 180.6, 150.2, 46.0, -22.7) 															
    tauAM_PY   = tauX(V_PY, 23.2, 20.8, 32.9, -15.2)	 															
    tauAH_PY   = tauX(V_PY, 77.2, 58.4, 38.9, -26.5)	
    
    										  
  
    # Currents of ABPD3 neuron
    iNa_AB  = 	iIonic(gNa_AB	, NaM_AB	, NaH_AB	, 3	, V_AB, ENa)
    iCaT_AB = 	iIonic(gCaT_AB	, CaTM_AB  , CaTH_AB  , 3	, V_AB, ECaT_AB)
    iCaS_AB = 	iIonic(gCaS_AB	, CaSM_AB  , CaSH_AB  , 3	, V_AB, ECaS_AB)
    iH_AB   = 	iIonic(gH_AB   , HM_AB	, 1	, 1	, V_AB, EH)
    iKd_AB  = 	iIonic(gKd_AB	, KdM_AB	, 1	, 4	, V_AB, EKd)
    iKCa_AB = 	iIonic(gKCa_AB	, KCaM_AB  , 1	, 4	, V_AB, EKCa)
    iA_AB   = 	iIonic(gA_AB	, AM_AB	, AH_AB	, 3	, V_AB, EA)
    iL_AB   = 	iIonic(gL_AB	, 1	, 1	, 1	, V_AB, EL)
    
    # Currents of LP neuron
    iNa_LP  = 	iIonic(gNa_LP	, NaM_LP	, NaH_LP	, 3	, V_LP, ENa)
    iCaT_LP = 	iIonic(gCaT_LP	, CaTM_LP  , CaTH_LP  , 3	, V_LP, ECaT_LP)
    iCaS_LP = 	iIonic(gCaS_LP	, CaSM_LP  , CaSH_LP  , 3	, V_LP, ECaS_LP)
    iH_LP   = 	iIonic(gH_LP	, HM_LP	, 1	, 1	, V_LP, EH)
    iKd_LP  = 	iIonic(gKd_LP	, KdM_LP	, 1	, 4	, V_LP, EKd)
    iKCa_LP = 	iIonic(gKCa_LP	, KCaM_LP  , 1	, 4	, V_LP, EKCa)
    iA_LP   = 	iIonic(gA_LP	, AM_LP	, AH_LP	, 3	, V_LP, EA)
    iL_LP   = 	iIonic(gL_LP	, 1	, 1	, 1	, V_LP, EL)
    
     # Currents of PY neuron
    iNa_PY  = 	iIonic(gNa_PY	, NaM_PY	, NaH_PY	, 3	, V_PY, ENa)
    iCaT_PY = 	iIonic(gCaT_PY	, CaTM_PY  , CaTH_PY  , 3	, V_PY, ECaT_PY)
    iCaS_PY = 	iIonic(gCaS_PY	, CaSM_PY  , CaSH_PY  , 3	, V_PY, ECaS_PY)
    iH_PY   = 	iIonic(gH_PY	, HM_PY	, 1	, 1	, V_PY, EH)
    iKd_PY  = 	iIonic(gKd_PY	, KdM_PY	, 1	, 4	, V_PY, EKd)
    iKCa_PY = 	iIonic(gKCa_PY	, KCaM_PY  , 1	, 4	, V_PY, EKCa)
    iA_PY   = 	iIonic(gA_PY	, AM_PY	, AH_PY	, 3	, V_PY, EA)
    iL_PY   = 	iIonic(gL_PY	, 1	, 1	, 1	, V_PY, EL)
    
    #Synaptic current calculations
    A = 0.628*1e-3             # Membrane area (cm2)
    
        #conversion the synaptic conductivity to mS/cm2 from nS
    gsABPYglut_unit = (gsABPYglut/1e6)/A
    gsABPYchol_unit = (gsABPYchol/1e6)/A
    gsABLPglut_unit = (gsABLPglut/1e6)/A
    gsABLPchol_unit = (gsABLPchol/1e6)/A
    gsLPPYglut_unit = (gsLPPYglut/1e6)/A
    gsPYLPglut_unit = (gsPYLPglut/1e6)/A
    gsLPABglut_unit = (gsLPABglut/1e6)/A
   
    
    iABPYglut = iIonic(gsABPYglut_unit,s_syn_ABPYglut,1,1,V_PY,Es_glut)  
    iABPYchol = iIonic(gsABPYchol_unit,s_syn_ABPYchol,1,1,V_PY,Es_chol)
    iABLPglut = iIonic(gsABLPglut_unit,s_syn_ABLPglut,1,1,V_LP,Es_glut) 
    iABLPchol = iIonic(gsABLPchol_unit,s_syn_ABLPchol,1,1,V_LP,Es_chol)
    iLPPYglut = iIonic(gsLPPYglut_unit,s_syn_LPPYglut,1,1,V_PY,Es_glut)
    iPYLPglut = iIonic(gsPYLPglut_unit,s_syn_PYLPglut,1,1,V_LP,Es_glut)
    iLPABglut = iIonic(gsLPABglut_unit,s_syn_LPABglut,1,1,V_AB,Es_glut)
    
    
    #Steady state garing variable of the synapse     Sinf    = boltzSS(-V_AB,-35.0,5.0) 

    Sinf_ABPYglut = boltzSS(-V_AB,-35.0,5.0) 
    Sinf_ABPYchol = boltzSS(-V_AB,-35.0,5.0)
    Sinf_ABLPglut = boltzSS(-V_AB,-35.0,5.0)
    Sinf_ABLPchol = boltzSS(-V_AB,-35.0,5.0)
    Sinf_LPPYglut = boltzSS(-V_LP,-35.0,5.0)
    Sinf_PYLPglut = boltzSS(-V_PY,-35.0,5.0)
    Sinf_LPABglut = boltzSS(-V_LP,-35.0,5.0)
    
    # synaptic tau    tauS = (1- Sinf) / (1/40)

    tau_ABPYglut = (1 - Sinf_ABPYglut) / k_glut
    tau_ABPYchol = (1 - Sinf_ABPYchol) / k_chol
    tau_ABLPglut = (1 - Sinf_ABLPglut) / k_glut
    tau_ABLPchol = (1 - Sinf_ABLPchol) / k_chol
    tau_LPPYglut = (1 - Sinf_LPPYglut) / k_glut
    tau_PYLPglut = (1 - Sinf_PYLPglut) / k_glut
    tau_LPABglut =(1 - Sinf_LPABglut) / k_glut

    if onlyDerivate:
 #    // State Equations
 #    // Voltage Time Evolution: C*dV/dt = -I_ionic + I_applied; I_ionic = sum(g_i*m^q*h*(V - E_i))
 # // double dV = (-(iNa + iCaT + iCaS + iH + iKd + iKCa + iA + iL) + iSyns + Iapp)/C;
 # // double intrinsic_currents = iNa + iCaT + iCaS + iH + iKd + iKCa + iA + iL;
 # // cout << intrinsic_currents <<endl;
        dV_AB = (-(iNa_AB + iCaT_AB+ iCaS_AB + iH_AB + iKd_AB + iKCa_AB + iA_AB + iL_AB ) - (iLPABglut) + Iapp)/C 
       
        # // Gating Variable Time Evolution: dX/dt = (X_inf - X)/tau_X of ABPD3
        dNaM_AB   = (NaMinf_AB - NaM_AB)/tauNaM_AB
        dNaH_AB   = (NaHinf_AB - NaH_AB)/tauNaH_AB
        dCaTM_AB  = (CaTMinf_AB - CaTM_AB)/tauCaTM_AB
        dCaTH_AB  = (CaTHinf_AB - CaTH_AB)/tauCaTH_AB
        dCaSM_AB  = (CaSMinf_AB - CaSM_AB)/tauCaSM_AB
        dCaSH_AB	= (CaSHinf_AB - CaSH_AB)/tauCaSH_AB
        dHM_AB 		= (HMinf_AB - HM_AB)/tauHM_AB
        dKdM_AB 	= (KdMinf_AB - KdM_AB)/tauKdM_AB
        dKCaM_AB	= (KCaMinf_AB - KCaM_AB)/tauKCaM_AB
        dAM_AB 		= (AMinf_AB - AM_AB)/tauAM_AB
        dAH_AB 		= (AHinf_AB - AH_AB)/tauAH_AB
        
        dIntCa_AB = (-caF*(iCaT_AB + iCaS_AB) - IntCa_AB + Ca0)/tauIntCa
        
        
        
        
        #dV of LP
        
        dV_LP = (-(iNa_LP + iCaT_LP + iCaS_LP + iH_LP + iKd_LP + iKCa_LP + iA_LP + iL_LP )- (iABLPglut + iABLPchol + iPYLPglut) + Iapp)/C 
       
        # // Gating Variable Time Evolution: dX/dt = (X_inf - X)/tau_X of LP2
        dNaM_LP   = (NaMinf_LP - NaM_LP)/tauNaM_LP
        dNaH_LP   = (NaHinf_LP - NaH_LP)/tauNaH_LP
        dCaTM_LP  = (CaTMinf_LP - CaTM_LP)/tauCaTM_LP
        dCaTH_LP  = (CaTHinf_LP - CaTH_LP)/tauCaTH_LP
        dCaSM_LP  = (CaSMinf_LP - CaSM_LP)/tauCaSM_LP
        dCaSH_LP	= (CaSHinf_LP - CaSH_LP)/tauCaSH_LP
        dHM_LP 		= (HMinf_LP - HM_LP)/tauHM_LP
        dKdM_LP 	= (KdMinf_LP - KdM_LP)/tauKdM_LP
        dKCaM_LP	= (KCaMinf_LP - KCaM_LP)/tauKCaM_LP
        dAM_LP 		= (AMinf_LP - AM_LP)/tauAM_LP
        dAH_LP 		= (AHinf_LP - AH_LP)/tauAH_LP
        
        dIntCa_LP = (-caF*(iCaT_LP + iCaS_LP) - IntCa_LP + Ca0)/tauIntCa
        
        
        
        #dV of PY
        
        dV_PY = (-(iNa_PY + iCaT_PY + iCaS_PY + iH_PY + iKd_PY + iKCa_PY + iA_PY + iL_PY )- (iABPYchol + iABPYglut + iLPPYglut) + Iapp)/C 
       
        #// Gating Variable Time Evolution: dX/dt = (X_inf - X)/tau_X of LP2
        dNaM_PY   = (NaMinf_PY - NaM_PY)/tauNaM_PY
        dNaH_PY   = (NaHinf_PY - NaH_PY)/tauNaH_PY
        dCaTM_PY  = (CaTMinf_PY - CaTM_PY)/tauCaTM_PY
        dCaTH_PY  = (CaTHinf_PY - CaTH_PY)/tauCaTH_PY
        dCaSM_PY  = (CaSMinf_PY - CaSM_PY)/tauCaSM_PY
        dCaSH_PY	= (CaSHinf_PY - CaSH_PY)/tauCaSH_PY
        dHM_PY 		= (HMinf_PY - HM_PY)/tauHM_PY
        dKdM_PY 	= (KdMinf_PY - KdM_PY)/tauKdM_PY
        dKCaM_PY	= (KCaMinf_PY - KCaM_PY)/tauKCaM_PY
        dAM_PY 		= (AMinf_PY - AM_PY)/tauAM_PY
        dAH_PY 		= (AHinf_PY - AH_PY)/tauAH_PY
        
        dIntCa_PY = (-caF*(iCaT_PY + iCaS_PY) - IntCa_PY + Ca0)/tauIntCa
        
        
        #dS      =(Sinf - s_syn)/tauS
        
        dS_ABPYglut =  (Sinf_ABPYglut - s_syn_ABPYglut) / tau_ABPYglut
        dS_ABPYchol =  (Sinf_ABPYchol - s_syn_ABPYchol) / tau_ABPYchol
        dS_ABLPglut =  (Sinf_ABLPglut - s_syn_ABLPglut) / tau_ABLPglut
        dS_ABLPchol = (Sinf_ABLPchol - s_syn_ABLPchol) / tau_ABLPchol
        dS_LPPYglut =  (Sinf_LPPYglut - s_syn_LPPYglut) / tau_LPPYglut
        dS_PYLPglut = (Sinf_PYLPglut - s_syn_PYLPglut) / tau_PYLPglut
        dS_LPABglut = (Sinf_LPABglut - s_syn_LPABglut) / tau_LPABglut
        
        
        
        
        
        y_dot= zeros(46)
        y_dot[0]=dV_AB
        y_dot[1]=dNaM_AB
        y_dot[2]=dNaH_AB
        y_dot[3]=dCaTM_AB
        y_dot[4]=dCaTH_AB
        y_dot[5]=dCaSM_AB
        y_dot[6]=dCaSH_AB
        y_dot[7]=dHM_AB
        y_dot[8]=dKdM_AB
        y_dot[9]=dKCaM_AB
        y_dot[10]=dAM_AB
        y_dot[11]=dAH_AB
        y_dot[12]=dIntCa_AB
        
        y_dot[13]=dV_LP
        y_dot[14]=dNaM_LP
        y_dot[15]=dNaH_LP
        y_dot[16]=dCaTM_LP
        y_dot[17]=dCaTH_LP
        y_dot[18]=dCaSM_LP
        y_dot[19]=dCaSH_LP
        y_dot[20]=dHM_LP
        y_dot[21]=dKdM_LP
        y_dot[22]=dKCaM_LP
        y_dot[23]=dAM_LP
        y_dot[24]=dAH_LP
        y_dot[25]=dIntCa_LP
        
        y_dot[26]=dV_PY
        y_dot[27]=dNaM_PY
        y_dot[28]=dNaH_PY
        y_dot[29]=dCaTM_PY
        y_dot[30]=dCaTH_PY
        y_dot[31]=dCaSM_PY
        y_dot[32]=dCaSH_PY
        y_dot[33]=dHM_PY
        y_dot[34]=dKdM_PY
        y_dot[35]=dKCaM_PY
        y_dot[36]=dAM_PY
        y_dot[37]=dAH_PY
        y_dot[38]=dIntCa_PY
        
        y_dot[39]=dS_ABPYglut                
        y_dot[40]=dS_ABPYchol
        y_dot[41]=dS_ABLPglut
        y_dot[42]=dS_ABLPchol
        y_dot[43] =dS_LPPYglut
        y_dot[44]=dS_PYLPglut
        y_dot[45] =dS_LPABglut
        return y_dot
    
    
    else:
        iABglut = iLPABglut
        iLPglut = iABLPglut + iPYLPglut
        iPYglut = iLPPYglut + iABPYglut
        iABchol = np.zeros_like(iABglut)
        
        r = [iNa_AB, iCaT_AB,iCaS_AB,iA_AB,iKCa_AB,iKd_AB,iH_AB,iL_AB,iABglut,iABchol,
             iNa_LP, iCaT_LP,iCaS_LP,iA_LP,iKCa_LP,iKd_LP,iH_LP,iL_LP,iLPglut,iABLPchol,
             iNa_PY, iCaT_PY,iCaS_PY,iA_PY,iKCa_PY,iKd_PY,iH_PY,iL_PY,iPYglut,iABPYchol
             ]
        return r
        
    
	
def boltzSS(Volt,A, B):
    act = 1./(1. + exp((Volt + A)/B))
    return act



	
# // Time constants of activation-inactivation   tauX(s_syn,0,-(1/40),35,5)
def tauX( Volt,  CT,  DT,  AT,  BT):   	
    timeconst = CT - DT/(1. + exp((Volt + AT)/BT))
    return timeconst

# // Some currents require a special time constant function
def spectau( Volt,  CT,  DT,  AT,  BT,  AT2,  BT2):
    spec = CT + DT/(exp((Volt + AT)/BT) + exp((Volt + AT2)/BT2))
    return spec
	
def iIonic( g,  m,  h,  q,  Volt,  Erev):
    flux = g*pow(m, q)*h*(Volt - Erev)
    return flux

def CaNernst(CaIn,temp):      
            R = 8.314*pow(10, 3)	 # Ideal Gas Constant (*10^3 to put into mV)
            T = 273.15 + temp 	 # Temperature in Kelvin
            z = 2.0   			 # Valence of Calcium Ions
            Far = 96485.33		 # Faraday's Constant
            CaOut = 3000.0 		 # Outer Ca Concentration (uM)
            CalRev = ((R*T)/(z*Far))*(np.log(CaOut/CaIn))	    
            return CalRev


