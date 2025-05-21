danush@danush mcSampleProdScriptsNewVOMS % ssh dshekar@lxplus8.cern.ch -XY
(dshekar@lxplus8.cern.ch) Password: 
* ********************************************************************
* Welcome to lxplus807.cern.ch, Red Hat Enterprise Linux release 8.10 (Ootpa)
* Archive of news is available in /etc/motd-archive
* Reminder: you have agreed to the CERN
*   computing rules, in particular OC5. CERN implements
*   the measures necessary to ensure compliance.
*   https://cern.ch/ComputingRules
* Puppet environment: qa, Roger state: production
* Foreman hostgroup: lxplus/nodes/login
* Availability zone: cern-geneva-c
* LXPLUS Public Login Service - http://lxplusdoc.web.cern.ch/
* Please read LXPLUS Privacy Notice in http://cern.ch/go/TpV7
* ********************************************************************
* October 10th: LxPlus will switch to requiring 2fa during 2025
*  Test your access from now https://cern.ch/otg0152605

cd pr	[dshekar@lxplus807 ~]$ cd private/mcSamples/powheg/mcSampleProdScripts_newx509/step2/
[dshekar@lxplus807 step2]$ ls
bash_template.py  cmsdriver_commands.py  condor_logs_mc_production  condor_MC.jdl  __pycache__  README.md  run_MC_2023.sh  submit.py  temp_debug
[dshekar@lxplus807 step2]$ cd temp_debug/
[dshekar@lxplus807 temp_debug]$ ls
CMSSW_13_0_13
[dshekar@lxplus807 temp_debug]$ export SCRAM_ARCH=el8_amd64_gcc11
[dshekar@lxplus807 temp_debug]$ scram p CMSSW_13_0_13
WARNING: There already exists /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/mcSampleProdScripts_newx509/step2/temp_debug/CMSSW_13_0_13 area for SCRAM_ARCH el8_amd64_gcc11.
[dshekar@lxplus807 temp_debug]$ cd CMSSW_13_0_13/src
[dshekar@lxplus807 src]$ eval `scram runtime -sh`
[dshekar@lxplus807 src]$ 
[dshekar@lxplus807 src]$ mkdir -p Configuration/GenProduction/python/
[dshekar@lxplus807 src]$ cp /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/CMSSW_13_0_13/src/Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py ./Configuration/GenProduction/python/
[dshekar@lxplus807 src]$ scram b
>> Local Products Rules ..... started
>> Local Products Rules ..... done
>> Entering Package Configuration/GenProduction
>> Leaving Package Configuration/GenProduction
>> Package Configuration/GenProduction built
>> Subsystem Configuration built
>> Subsystem BigProducts built
>> Building CMSSW version CMSSW_13_0_13 ----
gmake[1]: Entering directory '/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/mcSampleProdScripts_newx509/step2/temp_debug/CMSSW_13_0_13'
>> Local Products Rules ..... started
>> Local Products Rules ..... done
>> Creating project symlinks
>> Done python_symlink
>> Compiling python3 modules cfipython/el8_amd64_gcc11
>> Compiling python3 modules python
>> Compiling python3 modules src/Configuration/GenProduction/python
>> All python modules compiled
>> Plugins of all types refreshed.
>> Done generating edm plugin poisoned information
gmake[1]: Leaving directory '/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/mcSampleProdScripts_newx509/step2/temp_debug/CMSSW_13_0_13'
[dshekar@lxplus807 src]$ cmsDriver.py Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --python_filename wmLHEGS_cfg.py --mc --eventcontent RAWSIM, LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM, LHE --conditions 130X_mcRun3_2023_realistic_v14 --beamspot Realistic25ns13p6TeVEarly2023Collision --customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --step LHE,GEN,SIM --geometry DB:Extended --era Run3_2023  --fileout file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
LHE,GEN,SIM,ENDJOB
with DB:
Step: LHE Spec: 
Loading lhe fragment from Configuration.GenProduction.vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment
Step: GEN Spec: 
Loading generator fragment from Configuration.GenProduction.vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment
Step: SIM Spec: 
Step: ENDJOB Spec: 
customising the process with addMonitoring from Configuration/DataProcessing/Utils
Config file wmLHEGS_cfg.py created
[dshekar@lxplus807 src]$ cmsRun wmLHEGS_cfg.py

**************************************************************
 Geant4 version Name: geant4-10-07-patch-02 [MT]   (11-June-2021)
  << in Multi-threaded mode >> 
                       Copyright : Geant4 Collaboration
                      References : NIM A 506 (2003), 250-303
                                 : IEEE-TNS 53 (2006), 270-278
                                 : NIM A 835 (2016), 186-225
                             WWW : http://geant4.org/
**************************************************************

   ______________________________________     
         Running Generic Tarball/Gridpack     
   ______________________________________     
gridpack tarball path = /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/vbfhToWW2L2Nu/CMSSW_13_0_13/src/genproductions_scripts/bin/Powheg/VBF_H_el8_amd64_gcc11_CMSSW_13_0_13_VBFHToWW2L2Nu.tgz
%MSG-MG5 number of events requested = 10
%MSG-MG5 random seed used for the run = 234567
%MSG-MG5 thread count requested = 1
%MSG-MG5 residual/optional arguments = 
   ______________________________________     
         Running Powheg                       
   ______________________________________     
%MSG-POWHEG number of events requested = 10
%MSG-POWHEG random seed used for the run = 234567
%MSG-POWHEG number of cputs for the run = 1
%MSG-POWHEG SCRAM_ARCH version = el8_amd64_gcc11
%MSG-POWHEG CMSSW version = CMSSW_13_0_13
numevts 10
ih1   1           ! hadron 1 (1 for protons, -1 for antiprotons)
ih2   1           ! hadron 2 (1 for protons, -1 for antiprotons)
ebeam1 6800d0     ! energy of beam 1
ebeam2 6800d0     ! energy of beam 2

lhans1  325300         ! pdf set for hadron 1 (LHA numbering)
lhans2  325300         ! pdf set for hadron 2 (LHA numbering)	

! Parameters to allow or not the use of stored data
use-old-grid    1 ! if 1 use old grid if file pwggrids.dat is present (<> 1 regenerate)
use-old-ubound  1 ! if 1 use norm of upper bounding function stored in pwgubound.dat, if present; <> 1 regenerate

ncall1 100000   ! number of calls for initializing the integration grid
itmx1  1    ! number of iterations for initializing the integration grid
ncall2 100000   ! number of calls for computing the integral and finding upper bound
itmx2  5    ! number of iterations for computing the integral and finding upper bound
foldcsi 2    ! number of folds on csi integration
foldy   5      ! number of folds on  y  integration
foldphi 2    ! number of folds on phi integration
nubound 200000 ! number of bbarra calls to setup norm of upper bounding function
icsimax  1     ! <= 100, number of csi subdivision when computing the upper bounds
iymax    1     ! <= 100, number of y subdivision when computing the upper bounds
xupbound 2d0   ! increase upper bound for radiation generation

! OPTIONAL PARAMETERS

renscfact  1d0   ! (default 1d0) ren scale factor: muren  = muref * renscfact
facscfact  1d0   ! (default 1d0) fac scale factor: mufact = muref * facscfact
withdamp    1      ! (default 0, do not use) use Born-zero damping factor
testplots  1      ! (default 0, do not) do NLO and PWHG distributions
#pdfreweight 0       ! PDF reweighting
#storeinfo_rwgt 0    ! store weight information
#withnegweights 1 ! default 0,

iseed 234567

hmass    125d0       ! Higgs boson mass
hwidth   0.00407d0    ! Higgs boson width
hdecaymode -1   ! -1 no decay
                ! 0 all decay channels open
                ! 1-6 d dbar, u ubar,..., t tbar
                ! 7-9 e+ e-, mu+ mu-, tau+ tau-
                ! 10  W+W-
                ! 11  ZZ
                ! 12  gamma gamma

masswindow 999d0
complexpolescheme 1 ! switch on Complex Pole scheme


#manyseeds 1

#parallelstage 4

#xgriditeration 1 1
#rwl_group_events 2000
#lhapdf6maxsets 50
#rwl_file '-'
#rwl_format_rwgt 1

pdfreweight 0
storeinfo_rwgt 0

rwl_group_events 2000
lhapdf6maxsets 50
rwl_file 'pwg-rwl.dat'
rwl_format_rwgt 1
SVN status Begin
/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/vbfhToWW2L2Nu/CMSSW_13_0_13/src/genproductions_scripts/bin/Powheg/VBFHToWW2L2Nu/POWHEG-BOX/VBF_H
no svn repository found
/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/vbfhToWW2L2Nu/CMSSW_13_0_13/src/genproductions_scripts/bin/Powheg/VBFHToWW2L2Nu/POWHEG-BOX
URL: svn://powhegbox.mib.infn.it/trunk/POWHEG-BOX-V2
Rev.4091
Warning: not a clean version:
M       include/pwhg_rwl.h
SVN status End
  found input file powheg.input
  opened powheg.input
  powheginput keyword compress_lhe         absent; set to   -1000000.0000000000     
  powheginput keyword compress_upb         absent; set to   -1000000.0000000000     
  powheginput keyword testplots            set to    1.0000000000000000     
  powheginput keyword numevts              set to    10.000000000000000     
  powheginput keyword storemintupb         absent; set to   -1000000.0000000000     
  powheginput keyword fastbtlbound         absent; set to   -1000000.0000000000     
  powheginput keyword mintupbratlim        absent; set to   -1000000.0000000000     
  powheginput keyword StoredubNoOutliers   absent; set to   -1000000.0000000000     
  powheginput keyword maxseeds             absent; set to   -1000000.0000000000     
  powheginput keyword manyseeds            absent; set to   -1000000.0000000000     
  powheginput keyword rwl_add              absent; set to   -1000000.0000000000     
  powheginput keyword rwl_format_rwgt      set to    1.0000000000000000     
  powheginput keyword flg_debug            absent; set to   -1000000.0000000000     
  powheginput keyword withnegweights       absent; set to   -1000000.0000000000     
  powheginput keyword bornsuppfact         absent; set to   -1000000.0000000000     
  powheginput keyword ptsupp               absent; set to   -1000000.0000000000     
  powheginput keyword doublefsr            absent; set to   -1000000.0000000000     
  powheginput keyword smartsig             absent; set to   -1000000.0000000000     
  powheginput keyword withsubtr            absent; set to   -1000000.0000000000     
  powheginput keyword hfact                absent; set to   -1000000.0000000000     
  powheginput keyword withdamp             set to    1.0000000000000000     
  powheginput keyword bornzerodamp         absent; set to   -1000000.0000000000     
  powheginput keyword hdamp                absent; set to   -1000000.0000000000     
  powheginput keyword bornonly             absent; set to   -1000000.0000000000     
  powheginput keyword LOevents             absent; set to   -1000000.0000000000     
  powheginput keyword novirtual            absent; set to   -1000000.0000000000     
  powheginput keyword iseed                set to    234567.00000000000     
  powheginput keyword rand1                absent; set to   -1000000.0000000000     
  powheginput keyword rand2                absent; set to   -1000000.0000000000     
  powheginput keyword iupperisr            absent; set to   -1000000.0000000000     
  powheginput keyword iupperfsr            absent; set to   -1000000.0000000000     
  powheginput keyword pdfreweight          set to    0.0000000000000000     
  powheginput keyword storeinfo_rwgt       set to    0.0000000000000000     
  powheginput keyword compute_rwgt         absent; set to   -1000000.0000000000     
  powheginput keyword minlo                absent; set to   -1000000.0000000000     
  powheginput keyword nnlops               absent; set to   -1000000.0000000000     
  powheginput keyword alphas_from_pdf      absent; set to   -1000000.0000000000     
  powheginput keyword alphas_from_lhapdf   absent; set to   -1000000.0000000000     
  powheginput keyword ubexcess_correct     absent; set to   -1000000.0000000000     
 RM48 INITIALIZED:    234567           0         0
  powheginput keyword par_diexp            absent; set to   -1000000.0000000000     
  powheginput keyword par_dijexp           absent; set to   -1000000.0000000000     
  powheginput keyword par_2gsupp           absent; set to   -1000000.0000000000     
  powheginput keyword ih1                  set to    1.0000000000000000     
  powheginput keyword ih2                  set to    1.0000000000000000     
  powheginput keyword lhans1               set to    325300.00000000000     
  powheginput keyword lhans2               set to    325300.00000000000     
  powheginput keyword lhapdf6maxsets       set to    50.000000000000000     
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0000.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #0, version 1; LHAPDF ID = 325300
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
  powheginput keyword ebeam1               set to    6800.0000000000000     
  powheginput keyword ebeam2               set to    6800.0000000000000     
  powheginput keyword bornktmin            absent; set to   -1000000.0000000000     
  powheginput keyword ptsqmin              absent; set to   -1000000.0000000000     
  powheginput keyword charmthr             absent; set to   -1000000.0000000000     
  powheginput keyword bottomthr            absent; set to   -1000000.0000000000     
  powheginput keyword renscfact            set to    1.0000000000000000     
  powheginput keyword facscfact            set to    1.0000000000000000     
  powheginput keyword evenmaxrat           absent; set to   -1000000.0000000000     
  powheginput keyword hdecaymode           set to   -1.0000000000000000     
  powheginput keyword hmass                set to    125.00000000000000     
  powheginput keyword hwidth               set to    4.0699999999999998E-003
 **************************************
 **************************************
 Higgs boson mass  =    125.00000000000000     
 Higgs boson width =    4.0699999999999998E-003
 **************************************
 **************************************
  **** Minimum maxalr allowed:          660  *********
  **** Number of born graphs:           132
  **** Number of real graphs:           264
  **** Number of regular regions:           0
  powheginput keyword softtest             absent; set to   -1000000.0000000000     
  powheginput keyword colltest             absent; set to   -1000000.0000000000     
  powheginput keyword chklimseed           absent; set to   -1000000.0000000000     
  powheginput keyword tinyForLims          absent; set to   -1000000.0000000000     
  powheginput keyword higgsfixedwidth      absent; set to   -1000000.0000000000     
  powheginput keyword complexpolescheme    set to    1.0000000000000000     
 *******************************************
 *******************************************
 ****        COMPLEX-POLE SCHEME        ****
 ****          Passarino et al          ****
 *******************************************
 *******************************************
    
 *
  *
   * --- cpHTO v 1.1 (May 2012) by Giampiero 
  *
 *
    
    
 ******* OUTPUT **************************************
     
 top mass [GeV]          0.17250E+03
 muh      [GeV]          0.12500E+03
 GH OS    [GeV] =       0.4030000E-02
    
 *****************************************************
    
    
 gH Total [GeV] =        0.4029644E-02
    
 *** Bar scheme **************************************
    
 MHB      [GeV] =          0.12500E+03
 GHB      [GeV] =          0.40296E-02
    
 *****************************************************
    
    
  powheginput keyword charmthrpdf          absent; set to   -1000000.0000000000     
  powheginput keyword bottomthrpdf         absent; set to   -1000000.0000000000     
 ===============================
 LHAPDF called in POWHEG
 pdf cutoff factor =    1.0000000000000000     
 pdf cutoff [GeV] =    1.6499999999999999     
 ===============================
 **********************************
 RENORMALIZATION SCALE =    80.397999999999996     
 FACTORIZATION   SCALE =    80.397999999999996     
 **********************************
  powheginput keyword compare_vecsb_ep     absent; set to   -1000000.0000000000     
 RM48 INITIALIZED:    234567         210         0
 RM48IN SKIPPING OVER             210
 Writing bornequiv file...
 Done
  powheginput keyword writeequivfile       absent; set to   -1000000.0000000000     
  powheginput keyword compare_vecsr_ep     absent; set to   -1000000.0000000000     
 RM48 INITIALIZED:    234567         486         0
 RM48IN SKIPPING OVER             486
 Writing realequivregions-btl file...
 Done
  powheginput keyword olddij               absent; set to   -1000000.0000000000     
 RM48 INITIALIZED:    234567           0         0
  POWHEG:  
  Check of soft/collinear limits performed
  Results in file pwhg_checklimits
  powheginput keyword parallelstage        absent; set to   -1000000.0000000000     
  powheginput keyword use-old-grid         set to    1.0000000000000000     
  powheginput keyword foldcsi              set to    2.0000000000000000     
  powheginput keyword foldy                set to    5.0000000000000000     
  powheginput keyword foldphi              set to    2.0000000000000000     
  powheginput keyword ncallfrominput       absent; set to   -1000000.0000000000     
 upper bound grids successfully loaded
 btilde pos.   weights:   4.1420305721177400       +-   1.7096915839017460E-002
 btilde |neg.| weights:   2.6667075915827927E-003  +-   2.7146200507369497E-004
 btilde total (pos.-|neg.|):   4.1393638645261657       +-   1.7095391660452732E-002
  powheginput keyword nubound              set to    200000.00000000000     
  powheginput keyword iymax                set to    1.0000000000000000     
  powheginput keyword icsimax              set to    1.0000000000000000     
  powheginput keyword xupbound             set to    2.0000000000000000     
  powheginput keyword use-old-ubound       set to    1.0000000000000000     
  normalization of upper bounding function for radiation successfully loaded
  powheginput keyword skipextratests       absent; set to   -1000000.0000000000     
  powheginput keyword btlscalereal         absent; set to   -1000000.0000000000     
 RM48 INITIALIZED:    234567           0         0
 POWHEG: efficiency in the generation of the remnant variables =   1.5105740181268883E-002
  powheginput keyword clobberlhe           absent; set to   -1000000.0000000000     
  powheginput keyword lhrwgt_group_name    set to ""
  powheginput keyword lhrwgt_group_combine set to ""
  powheginput keyword lhrwgt_id            set to ""
  powheginput keyword lhrwgt_descr         set to ""

  POWHEG: generating events
  powheginput keyword fullrwgt             absent; set to   -1000000.0000000000     
  powheginput keyword rwl_file             set to "pwg-rwl.dat"
  powheginput keyword max_io_bufsize       absent; set to   -1000000.0000000000     
Weight    1
   id=1001,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.10000D+01
      facscfact=0.10000D+01
Weight    2
   id=1002,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.10000D+01
      facscfact=0.20000D+01
Weight    3
   id=1003,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.10000D+01
      facscfact=0.50000D+00
Weight    4
   id=1004,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.20000D+01
      facscfact=0.10000D+01
Weight    5
   id=1005,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.20000D+01
      facscfact=0.20000D+01
Weight    6
   id=1006,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.20000D+01
      facscfact=0.50000D+00
Weight    7
   id=1007,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.50000D+00
      facscfact=0.10000D+01
Weight    8
   id=1008,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.50000D+00
      facscfact=0.20000D+01
Weight    9
   id=1009,
   group=1,
   key value pairs:
      lhapdf=0.32530D+06
      renscfact=0.50000D+00
      facscfact=0.50000D+00
Weight   10
   id=2000,
   group=2,
   key value pairs:
      lhapdf=0.32530D+06
Weight   11
   id=2001,
   group=2,
   key value pairs:
      lhapdf=0.32530D+06
Weight   12
   id=2002,
   group=2,
   key value pairs:
      lhapdf=0.32530D+06
Weight   13
   id=2003,
   group=2,
   key value pairs:
      lhapdf=0.32530D+06
Weight   14
   id=2004,
   group=2,
   key value pairs:
      lhapdf=0.32530D+06
Weight   15
   id=2005,
   group=2,
   key value pairs:
      lhapdf=0.32530D+06
Weight   16
   id=2006,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   17
   id=2007,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   18
   id=2008,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   19
   id=2009,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   20
   id=2010,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   21
   id=2011,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   22
   id=2012,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   23
   id=2013,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   24
   id=2014,
   group=2,
   key value pairs:
      lhapdf=0.32531D+06
Weight   25
   id=2015,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   26
   id=2016,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   27
   id=2017,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   28
   id=2018,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   29
   id=2019,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   30
   id=2020,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   31
   id=2021,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   32
   id=2022,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   33
   id=2023,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   34
   id=2024,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   35
   id=2025,
   group=2,
   key value pairs:
      lhapdf=0.32532D+06
Weight   36
   id=2026,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   37
   id=2027,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   38
   id=2028,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   39
   id=2029,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   40
   id=2030,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   41
   id=2031,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   42
   id=2032,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   43
   id=2033,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   44
   id=2034,
   group=2,
   key value pairs:
      lhapdf=0.32533D+06
Weight   45
   id=2035,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   46
   id=2036,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   47
   id=2037,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   48
   id=2038,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   49
   id=2039,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   50
   id=2040,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   51
   id=2041,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   52
   id=2042,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   53
   id=2043,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   54
   id=2044,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   55
   id=2045,
   group=2,
   key value pairs:
      lhapdf=0.32534D+06
Weight   56
   id=2046,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   57
   id=2047,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   58
   id=2048,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   59
   id=2049,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   60
   id=2050,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   61
   id=2051,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   62
   id=2052,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   63
   id=2053,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   64
   id=2054,
   group=2,
   key value pairs:
      lhapdf=0.32535D+06
Weight   65
   id=2055,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   66
   id=2056,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   67
   id=2057,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   68
   id=2058,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   69
   id=2059,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   70
   id=2060,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   71
   id=2061,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   72
   id=2062,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   73
   id=2063,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   74
   id=2064,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   75
   id=2065,
   group=2,
   key value pairs:
      lhapdf=0.32536D+06
Weight   76
   id=2066,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   77
   id=2067,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   78
   id=2068,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   79
   id=2069,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   80
   id=2070,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   81
   id=2071,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   82
   id=2072,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   83
   id=2073,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   84
   id=2074,
   group=2,
   key value pairs:
      lhapdf=0.32537D+06
Weight   85
   id=2075,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   86
   id=2076,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   87
   id=2077,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   88
   id=2078,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   89
   id=2079,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   90
   id=2080,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   91
   id=2081,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   92
   id=2082,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   93
   id=2083,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   94
   id=2084,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   95
   id=2085,
   group=2,
   key value pairs:
      lhapdf=0.32538D+06
Weight   96
   id=2086,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight   97
   id=2087,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight   98
   id=2088,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight   99
   id=2089,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight  100
   id=2090,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight  101
   id=2091,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight  102
   id=2092,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight  103
   id=2093,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight  104
   id=2094,
   group=2,
   key value pairs:
      lhapdf=0.32539D+06
Weight  105
   id=2095,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  106
   id=2096,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  107
   id=2097,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  108
   id=2098,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  109
   id=2099,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  110
   id=2100,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  111
   id=2101,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  112
   id=2102,
   group=2,
   key value pairs:
      lhapdf=0.32540D+06
Weight  113
   id=2200,
   group=2,
   key value pairs:
      lhapdf=0.30600D+06
Weight  114
   id=2201,
   group=2,
   key value pairs:
      lhapdf=0.32250D+06
Weight  115
   id=2202,
   group=2,
   key value pairs:
      lhapdf=0.32270D+06
Weight  116
   id=2203,
   group=2,
   key value pairs:
      lhapdf=0.32290D+06
Weight  117
   id=2204,
   group=2,
   key value pairs:
      lhapdf=0.32310D+06
Weight  118
   id=2205,
   group=2,
   key value pairs:
      lhapdf=0.32330D+06
Weight  119
   id=2206,
   group=2,
   key value pairs:
      lhapdf=0.32350D+06
Weight  120
   id=2207,
   group=2,
   key value pairs:
      lhapdf=0.32370D+06
Weight  121
   id=2208,
   group=2,
   key value pairs:
      lhapdf=0.32390D+06
Weight  122
   id=2300,
   group=2,
   key value pairs:
      lhapdf=0.30580D+06
Weight  123
   id=2301,
   group=2,
   key value pairs:
      lhapdf=0.30580D+06
Weight  124
   id=2302,
   group=2,
   key value pairs:
      lhapdf=0.30580D+06
Weight  125
   id=2303,
   group=2,
   key value pairs:
      lhapdf=0.30580D+06
Weight  126
   id=2304,
   group=2,
   key value pairs:
      lhapdf=0.30580D+06
Weight  127
   id=2305,
   group=2,
   key value pairs:
      lhapdf=0.30580D+06
Weight  128
   id=2306,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  129
   id=2307,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  130
   id=2308,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  131
   id=2309,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  132
   id=2310,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  133
   id=2311,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  134
   id=2312,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  135
   id=2313,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  136
   id=2314,
   group=2,
   key value pairs:
      lhapdf=0.30581D+06
Weight  137
   id=2315,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  138
   id=2316,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  139
   id=2317,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  140
   id=2318,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  141
   id=2319,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  142
   id=2320,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  143
   id=2321,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  144
   id=2322,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  145
   id=2323,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  146
   id=2324,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  147
   id=2325,
   group=2,
   key value pairs:
      lhapdf=0.30582D+06
Weight  148
   id=2326,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  149
   id=2327,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  150
   id=2328,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  151
   id=2329,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  152
   id=2330,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  153
   id=2331,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  154
   id=2332,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  155
   id=2333,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  156
   id=2334,
   group=2,
   key value pairs:
      lhapdf=0.30583D+06
Weight  157
   id=2335,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  158
   id=2336,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  159
   id=2337,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  160
   id=2338,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  161
   id=2339,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  162
   id=2340,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  163
   id=2341,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  164
   id=2342,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  165
   id=2343,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  166
   id=2344,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  167
   id=2345,
   group=2,
   key value pairs:
      lhapdf=0.30584D+06
Weight  168
   id=2346,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  169
   id=2347,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  170
   id=2348,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  171
   id=2349,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  172
   id=2350,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  173
   id=2351,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  174
   id=2352,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  175
   id=2353,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  176
   id=2354,
   group=2,
   key value pairs:
      lhapdf=0.30585D+06
Weight  177
   id=2355,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  178
   id=2356,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  179
   id=2357,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  180
   id=2358,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  181
   id=2359,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  182
   id=2360,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  183
   id=2361,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  184
   id=2362,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  185
   id=2363,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  186
   id=2364,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  187
   id=2365,
   group=2,
   key value pairs:
      lhapdf=0.30586D+06
Weight  188
   id=2366,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  189
   id=2367,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  190
   id=2368,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  191
   id=2369,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  192
   id=2370,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  193
   id=2371,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  194
   id=2372,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  195
   id=2373,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  196
   id=2374,
   group=2,
   key value pairs:
      lhapdf=0.30587D+06
Weight  197
   id=2375,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  198
   id=2376,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  199
   id=2377,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  200
   id=2378,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  201
   id=2379,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  202
   id=2380,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  203
   id=2381,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  204
   id=2382,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  205
   id=2383,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  206
   id=2384,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  207
   id=2385,
   group=2,
   key value pairs:
      lhapdf=0.30588D+06
Weight  208
   id=2386,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  209
   id=2387,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  210
   id=2388,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  211
   id=2389,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  212
   id=2390,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  213
   id=2391,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  214
   id=2392,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  215
   id=2393,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  216
   id=2394,
   group=2,
   key value pairs:
      lhapdf=0.30589D+06
Weight  217
   id=2395,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  218
   id=2396,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  219
   id=2397,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  220
   id=2398,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  221
   id=2399,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  222
   id=2400,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  223
   id=2401,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  224
   id=2402,
   group=2,
   key value pairs:
      lhapdf=0.30590D+06
Weight  225
   id=2500,
   group=2,
   key value pairs:
      lhapdf=0.30320D+06
Weight  226
   id=2501,
   group=2,
   key value pairs:
      lhapdf=0.29220D+06
Weight  227
   id=2600,
   group=2,
   key value pairs:
      lhapdf=0.33160D+06
Weight  228
   id=2601,
   group=2,
   key value pairs:
      lhapdf=0.33160D+06
Weight  229
   id=2602,
   group=2,
   key value pairs:
      lhapdf=0.33160D+06
Weight  230
   id=2603,
   group=2,
   key value pairs:
      lhapdf=0.33160D+06
Weight  231
   id=2604,
   group=2,
   key value pairs:
      lhapdf=0.33160D+06
Weight  232
   id=2605,
   group=2,
   key value pairs:
      lhapdf=0.33160D+06
Weight  233
   id=2606,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  234
   id=2607,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  235
   id=2608,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  236
   id=2609,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  237
   id=2610,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  238
   id=2611,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  239
   id=2612,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  240
   id=2613,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  241
   id=2614,
   group=2,
   key value pairs:
      lhapdf=0.33161D+06
Weight  242
   id=2615,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  243
   id=2616,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  244
   id=2617,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  245
   id=2618,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  246
   id=2619,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  247
   id=2620,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  248
   id=2621,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  249
   id=2622,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  250
   id=2623,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  251
   id=2624,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  252
   id=2625,
   group=2,
   key value pairs:
      lhapdf=0.33162D+06
Weight  253
   id=2626,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  254
   id=2627,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  255
   id=2628,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  256
   id=2629,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  257
   id=2630,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  258
   id=2631,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  259
   id=2632,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  260
   id=2633,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  261
   id=2634,
   group=2,
   key value pairs:
      lhapdf=0.33163D+06
Weight  262
   id=2635,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  263
   id=2636,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  264
   id=2637,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  265
   id=2638,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  266
   id=2639,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  267
   id=2640,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  268
   id=2641,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  269
   id=2642,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  270
   id=2643,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  271
   id=2644,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  272
   id=2645,
   group=2,
   key value pairs:
      lhapdf=0.33164D+06
Weight  273
   id=2646,
   group=2,
   key value pairs:
      lhapdf=0.33165D+06
Weight  274
   id=2647,
   group=2,
   key value pairs:
      lhapdf=0.33165D+06
Weight  275
   id=2648,
   group=2,
   key value pairs:
      lhapdf=0.33165D+06
Weight  276
   id=2649,
   group=2,
   key value pairs:
      lhapdf=0.33165D+06
Weight  277
   id=2650,
   group=2,
   key value pairs:
      lhapdf=0.33165D+06
Weight  278
   id=2651,
   group=2,
   key value pairs:
      lhapdf=0.33165D+06
Weight  279
   id=2652,
   group=2,
   key value pairs:
      lhapdf=0.33165D+06
Weight  280
   id=2700,
   group=2,
   key value pairs:
      lhapdf=0.33270D+06
Weight  281
   id=2701,
   group=2,
   key value pairs:
      lhapdf=0.33290D+06
Weight  282
   id=2702,
   group=2,
   key value pairs:
      lhapdf=0.33310D+06
Weight  283
   id=2703,
   group=2,
   key value pairs:
      lhapdf=0.33330D+06
Weight  284
   id=2704,
   group=2,
   key value pairs:
      lhapdf=0.33350D+06
Weight  285
   id=2705,
   group=2,
   key value pairs:
      lhapdf=0.33370D+06
Weight  286
   id=2800,
   group=2,
   key value pairs:
      lhapdf=0.33230D+06
Weight  287
   id=4000,
   group=2,
   key value pairs:
      lhapdf=0.14000D+05
Weight  288
   id=4001,
   group=2,
   key value pairs:
      lhapdf=0.14001D+05
Weight  289
   id=4002,
   group=2,
   key value pairs:
      lhapdf=0.14002D+05
Weight  290
   id=4003,
   group=2,
   key value pairs:
      lhapdf=0.14003D+05
Weight  291
   id=4004,
   group=2,
   key value pairs:
      lhapdf=0.14004D+05
Weight  292
   id=4005,
   group=2,
   key value pairs:
      lhapdf=0.14005D+05
Weight  293
   id=4006,
   group=2,
   key value pairs:
      lhapdf=0.14006D+05
Weight  294
   id=4007,
   group=2,
   key value pairs:
      lhapdf=0.14007D+05
Weight  295
   id=4008,
   group=2,
   key value pairs:
      lhapdf=0.14008D+05
Weight  296
   id=4009,
   group=2,
   key value pairs:
      lhapdf=0.14009D+05
Weight  297
   id=4010,
   group=2,
   key value pairs:
      lhapdf=0.14010D+05
Weight  298
   id=4011,
   group=2,
   key value pairs:
      lhapdf=0.14011D+05
Weight  299
   id=4012,
   group=2,
   key value pairs:
      lhapdf=0.14012D+05
Weight  300
   id=4013,
   group=2,
   key value pairs:
      lhapdf=0.14013D+05
Weight  301
   id=4014,
   group=2,
   key value pairs:
      lhapdf=0.14014D+05
Weight  302
   id=4015,
   group=2,
   key value pairs:
      lhapdf=0.14015D+05
Weight  303
   id=4016,
   group=2,
   key value pairs:
      lhapdf=0.14016D+05
Weight  304
   id=4017,
   group=2,
   key value pairs:
      lhapdf=0.14017D+05
Weight  305
   id=4018,
   group=2,
   key value pairs:
      lhapdf=0.14018D+05
Weight  306
   id=4019,
   group=2,
   key value pairs:
      lhapdf=0.14019D+05
Weight  307
   id=4020,
   group=2,
   key value pairs:
      lhapdf=0.14020D+05
Weight  308
   id=4021,
   group=2,
   key value pairs:
      lhapdf=0.14021D+05
Weight  309
   id=4022,
   group=2,
   key value pairs:
      lhapdf=0.14022D+05
Weight  310
   id=4023,
   group=2,
   key value pairs:
      lhapdf=0.14023D+05
Weight  311
   id=4024,
   group=2,
   key value pairs:
      lhapdf=0.14024D+05
Weight  312
   id=4025,
   group=2,
   key value pairs:
      lhapdf=0.14025D+05
Weight  313
   id=4026,
   group=2,
   key value pairs:
      lhapdf=0.14026D+05
Weight  314
   id=4027,
   group=2,
   key value pairs:
      lhapdf=0.14027D+05
Weight  315
   id=4028,
   group=2,
   key value pairs:
      lhapdf=0.14028D+05
Weight  316
   id=4029,
   group=2,
   key value pairs:
      lhapdf=0.14029D+05
Weight  317
   id=4030,
   group=2,
   key value pairs:
      lhapdf=0.14030D+05
Weight  318
   id=4031,
   group=2,
   key value pairs:
      lhapdf=0.14031D+05
Weight  319
   id=4032,
   group=2,
   key value pairs:
      lhapdf=0.14032D+05
Weight  320
   id=4033,
   group=2,
   key value pairs:
      lhapdf=0.14033D+05
Weight  321
   id=4034,
   group=2,
   key value pairs:
      lhapdf=0.14034D+05
Weight  322
   id=4035,
   group=2,
   key value pairs:
      lhapdf=0.14035D+05
Weight  323
   id=4036,
   group=2,
   key value pairs:
      lhapdf=0.14036D+05
Weight  324
   id=4037,
   group=2,
   key value pairs:
      lhapdf=0.14037D+05
Weight  325
   id=4038,
   group=2,
   key value pairs:
      lhapdf=0.14038D+05
Weight  326
   id=4039,
   group=2,
   key value pairs:
      lhapdf=0.14039D+05
Weight  327
   id=4040,
   group=2,
   key value pairs:
      lhapdf=0.14040D+05
Weight  328
   id=4041,
   group=2,
   key value pairs:
      lhapdf=0.14041D+05
Weight  329
   id=4042,
   group=2,
   key value pairs:
      lhapdf=0.14042D+05
Weight  330
   id=4043,
   group=2,
   key value pairs:
      lhapdf=0.14043D+05
Weight  331
   id=4044,
   group=2,
   key value pairs:
      lhapdf=0.14044D+05
Weight  332
   id=4045,
   group=2,
   key value pairs:
      lhapdf=0.14045D+05
Weight  333
   id=4046,
   group=2,
   key value pairs:
      lhapdf=0.14046D+05
Weight  334
   id=4047,
   group=2,
   key value pairs:
      lhapdf=0.14047D+05
Weight  335
   id=4048,
   group=2,
   key value pairs:
      lhapdf=0.14048D+05
Weight  336
   id=4049,
   group=2,
   key value pairs:
      lhapdf=0.14049D+05
Weight  337
   id=4050,
   group=2,
   key value pairs:
      lhapdf=0.14050D+05
Weight  338
   id=4051,
   group=2,
   key value pairs:
      lhapdf=0.14051D+05
Weight  339
   id=4052,
   group=2,
   key value pairs:
      lhapdf=0.14052D+05
Weight  340
   id=4053,
   group=2,
   key value pairs:
      lhapdf=0.14053D+05
Weight  341
   id=4054,
   group=2,
   key value pairs:
      lhapdf=0.14054D+05
Weight  342
   id=4055,
   group=2,
   key value pairs:
      lhapdf=0.14055D+05
Weight  343
   id=4056,
   group=2,
   key value pairs:
      lhapdf=0.14056D+05
Weight  344
   id=4057,
   group=2,
   key value pairs:
      lhapdf=0.14057D+05
Weight  345
   id=4058,
   group=2,
   key value pairs:
      lhapdf=0.14058D+05
Weight  346
   id=4100,
   group=2,
   key value pairs:
      lhapdf=0.14066D+05
Weight  347
   id=4101,
   group=2,
   key value pairs:
      lhapdf=0.14067D+05
Weight  348
   id=4102,
   group=2,
   key value pairs:
      lhapdf=0.14069D+05
Weight  349
   id=4103,
   group=2,
   key value pairs:
      lhapdf=0.14070D+05
Weight  350
   id=4200,
   group=2,
   key value pairs:
      lhapdf=0.14100D+05
Weight  351
   id=4201,
   group=2,
   key value pairs:
      lhapdf=0.14101D+05
Weight  352
   id=4202,
   group=2,
   key value pairs:
      lhapdf=0.14102D+05
Weight  353
   id=4203,
   group=2,
   key value pairs:
      lhapdf=0.14103D+05
Weight  354
   id=4204,
   group=2,
   key value pairs:
      lhapdf=0.14104D+05
Weight  355
   id=4205,
   group=2,
   key value pairs:
      lhapdf=0.14105D+05
Weight  356
   id=4206,
   group=2,
   key value pairs:
      lhapdf=0.14106D+05
Weight  357
   id=4207,
   group=2,
   key value pairs:
      lhapdf=0.14107D+05
Weight  358
   id=4208,
   group=2,
   key value pairs:
      lhapdf=0.14108D+05
Weight  359
   id=4209,
   group=2,
   key value pairs:
      lhapdf=0.14109D+05
Weight  360
   id=4210,
   group=2,
   key value pairs:
      lhapdf=0.14110D+05
Weight  361
   id=4211,
   group=2,
   key value pairs:
      lhapdf=0.14111D+05
Weight  362
   id=4212,
   group=2,
   key value pairs:
      lhapdf=0.14112D+05
Weight  363
   id=4213,
   group=2,
   key value pairs:
      lhapdf=0.14113D+05
Weight  364
   id=4214,
   group=2,
   key value pairs:
      lhapdf=0.14114D+05
Weight  365
   id=4215,
   group=2,
   key value pairs:
      lhapdf=0.14115D+05
Weight  366
   id=4216,
   group=2,
   key value pairs:
      lhapdf=0.14116D+05
Weight  367
   id=4217,
   group=2,
   key value pairs:
      lhapdf=0.14117D+05
Weight  368
   id=4218,
   group=2,
   key value pairs:
      lhapdf=0.14118D+05
Weight  369
   id=4219,
   group=2,
   key value pairs:
      lhapdf=0.14119D+05
Weight  370
   id=4220,
   group=2,
   key value pairs:
      lhapdf=0.14120D+05
Weight  371
   id=4221,
   group=2,
   key value pairs:
      lhapdf=0.14121D+05
Weight  372
   id=4222,
   group=2,
   key value pairs:
      lhapdf=0.14122D+05
Weight  373
   id=4223,
   group=2,
   key value pairs:
      lhapdf=0.14123D+05
Weight  374
   id=4224,
   group=2,
   key value pairs:
      lhapdf=0.14124D+05
Weight  375
   id=4225,
   group=2,
   key value pairs:
      lhapdf=0.14125D+05
Weight  376
   id=4226,
   group=2,
   key value pairs:
      lhapdf=0.14126D+05
Weight  377
   id=4227,
   group=2,
   key value pairs:
      lhapdf=0.14127D+05
Weight  378
   id=4228,
   group=2,
   key value pairs:
      lhapdf=0.14128D+05
Weight  379
   id=4229,
   group=2,
   key value pairs:
      lhapdf=0.14129D+05
Weight  380
   id=4230,
   group=2,
   key value pairs:
      lhapdf=0.14130D+05
Weight  381
   id=4231,
   group=2,
   key value pairs:
      lhapdf=0.14131D+05
Weight  382
   id=4232,
   group=2,
   key value pairs:
      lhapdf=0.14132D+05
Weight  383
   id=4233,
   group=2,
   key value pairs:
      lhapdf=0.14133D+05
Weight  384
   id=4234,
   group=2,
   key value pairs:
      lhapdf=0.14134D+05
Weight  385
   id=4235,
   group=2,
   key value pairs:
      lhapdf=0.14135D+05
Weight  386
   id=4236,
   group=2,
   key value pairs:
      lhapdf=0.14136D+05
Weight  387
   id=4237,
   group=2,
   key value pairs:
      lhapdf=0.14137D+05
Weight  388
   id=4238,
   group=2,
   key value pairs:
      lhapdf=0.14138D+05
Weight  389
   id=4239,
   group=2,
   key value pairs:
      lhapdf=0.14139D+05
Weight  390
   id=4240,
   group=2,
   key value pairs:
      lhapdf=0.14140D+05
Weight  391
   id=4241,
   group=2,
   key value pairs:
      lhapdf=0.14141D+05
Weight  392
   id=4242,
   group=2,
   key value pairs:
      lhapdf=0.14142D+05
Weight  393
   id=4243,
   group=2,
   key value pairs:
      lhapdf=0.14143D+05
Weight  394
   id=4244,
   group=2,
   key value pairs:
      lhapdf=0.14144D+05
Weight  395
   id=4245,
   group=2,
   key value pairs:
      lhapdf=0.14145D+05
Weight  396
   id=4246,
   group=2,
   key value pairs:
      lhapdf=0.14146D+05
Weight  397
   id=4247,
   group=2,
   key value pairs:
      lhapdf=0.14147D+05
Weight  398
   id=4248,
   group=2,
   key value pairs:
      lhapdf=0.14148D+05
Weight  399
   id=4249,
   group=2,
   key value pairs:
      lhapdf=0.14149D+05
Weight  400
   id=4250,
   group=2,
   key value pairs:
      lhapdf=0.14150D+05
Weight  401
   id=4251,
   group=2,
   key value pairs:
      lhapdf=0.14151D+05
Weight  402
   id=4252,
   group=2,
   key value pairs:
      lhapdf=0.14152D+05
Weight  403
   id=4253,
   group=2,
   key value pairs:
      lhapdf=0.14153D+05
Weight  404
   id=4254,
   group=2,
   key value pairs:
      lhapdf=0.14154D+05
Weight  405
   id=4255,
   group=2,
   key value pairs:
      lhapdf=0.14155D+05
Weight  406
   id=4256,
   group=2,
   key value pairs:
      lhapdf=0.14156D+05
Weight  407
   id=4257,
   group=2,
   key value pairs:
      lhapdf=0.14157D+05
Weight  408
   id=4258,
   group=2,
   key value pairs:
      lhapdf=0.14158D+05
Weight  409
   id=4300,
   group=2,
   key value pairs:
      lhapdf=0.14200D+05
Weight  410
   id=4301,
   group=2,
   key value pairs:
      lhapdf=0.14300D+05
Weight  411
   id=5000,
   group=2,
   key value pairs:
      lhapdf=0.27400D+05
Weight  412
   id=5001,
   group=2,
   key value pairs:
      lhapdf=0.27401D+05
Weight  413
   id=5002,
   group=2,
   key value pairs:
      lhapdf=0.27402D+05
Weight  414
   id=5003,
   group=2,
   key value pairs:
      lhapdf=0.27403D+05
Weight  415
   id=5004,
   group=2,
   key value pairs:
      lhapdf=0.27404D+05
Weight  416
   id=5005,
   group=2,
   key value pairs:
      lhapdf=0.27405D+05
Weight  417
   id=5006,
   group=2,
   key value pairs:
      lhapdf=0.27406D+05
Weight  418
   id=5007,
   group=2,
   key value pairs:
      lhapdf=0.27407D+05
Weight  419
   id=5008,
   group=2,
   key value pairs:
      lhapdf=0.27408D+05
Weight  420
   id=5009,
   group=2,
   key value pairs:
      lhapdf=0.27409D+05
Weight  421
   id=5010,
   group=2,
   key value pairs:
      lhapdf=0.27410D+05
Weight  422
   id=5011,
   group=2,
   key value pairs:
      lhapdf=0.27411D+05
Weight  423
   id=5012,
   group=2,
   key value pairs:
      lhapdf=0.27412D+05
Weight  424
   id=5013,
   group=2,
   key value pairs:
      lhapdf=0.27413D+05
Weight  425
   id=5014,
   group=2,
   key value pairs:
      lhapdf=0.27414D+05
Weight  426
   id=5015,
   group=2,
   key value pairs:
      lhapdf=0.27415D+05
Weight  427
   id=5016,
   group=2,
   key value pairs:
      lhapdf=0.27416D+05
Weight  428
   id=5017,
   group=2,
   key value pairs:
      lhapdf=0.27417D+05
Weight  429
   id=5018,
   group=2,
   key value pairs:
      lhapdf=0.27418D+05
Weight  430
   id=5019,
   group=2,
   key value pairs:
      lhapdf=0.27419D+05
Weight  431
   id=5020,
   group=2,
   key value pairs:
      lhapdf=0.27420D+05
Weight  432
   id=5021,
   group=2,
   key value pairs:
      lhapdf=0.27421D+05
Weight  433
   id=5022,
   group=2,
   key value pairs:
      lhapdf=0.27422D+05
Weight  434
   id=5023,
   group=2,
   key value pairs:
      lhapdf=0.27423D+05
Weight  435
   id=5024,
   group=2,
   key value pairs:
      lhapdf=0.27424D+05
Weight  436
   id=5025,
   group=2,
   key value pairs:
      lhapdf=0.27425D+05
Weight  437
   id=5026,
   group=2,
   key value pairs:
      lhapdf=0.27426D+05
Weight  438
   id=5027,
   group=2,
   key value pairs:
      lhapdf=0.27427D+05
Weight  439
   id=5028,
   group=2,
   key value pairs:
      lhapdf=0.27428D+05
Weight  440
   id=5029,
   group=2,
   key value pairs:
      lhapdf=0.27429D+05
Weight  441
   id=5030,
   group=2,
   key value pairs:
      lhapdf=0.27430D+05
Weight  442
   id=5031,
   group=2,
   key value pairs:
      lhapdf=0.27431D+05
Weight  443
   id=5032,
   group=2,
   key value pairs:
      lhapdf=0.27432D+05
Weight  444
   id=5033,
   group=2,
   key value pairs:
      lhapdf=0.27433D+05
Weight  445
   id=5034,
   group=2,
   key value pairs:
      lhapdf=0.27434D+05
Weight  446
   id=5035,
   group=2,
   key value pairs:
      lhapdf=0.27435D+05
Weight  447
   id=5036,
   group=2,
   key value pairs:
      lhapdf=0.27436D+05
Weight  448
   id=5037,
   group=2,
   key value pairs:
      lhapdf=0.27437D+05
Weight  449
   id=5038,
   group=2,
   key value pairs:
      lhapdf=0.27438D+05
Weight  450
   id=5039,
   group=2,
   key value pairs:
      lhapdf=0.27439D+05
Weight  451
   id=5040,
   group=2,
   key value pairs:
      lhapdf=0.27440D+05
Weight  452
   id=5041,
   group=2,
   key value pairs:
      lhapdf=0.27441D+05
Weight  453
   id=5042,
   group=2,
   key value pairs:
      lhapdf=0.27442D+05
Weight  454
   id=5043,
   group=2,
   key value pairs:
      lhapdf=0.27443D+05
Weight  455
   id=5044,
   group=2,
   key value pairs:
      lhapdf=0.27444D+05
Weight  456
   id=5045,
   group=2,
   key value pairs:
      lhapdf=0.27445D+05
Weight  457
   id=5046,
   group=2,
   key value pairs:
      lhapdf=0.27446D+05
Weight  458
   id=5047,
   group=2,
   key value pairs:
      lhapdf=0.27447D+05
Weight  459
   id=5048,
   group=2,
   key value pairs:
      lhapdf=0.27448D+05
Weight  460
   id=5049,
   group=2,
   key value pairs:
      lhapdf=0.27449D+05
Weight  461
   id=5050,
   group=2,
   key value pairs:
      lhapdf=0.27450D+05
Weight  462
   id=5051,
   group=2,
   key value pairs:
      lhapdf=0.27451D+05
Weight  463
   id=5052,
   group=2,
   key value pairs:
      lhapdf=0.27452D+05
Weight  464
   id=5053,
   group=2,
   key value pairs:
      lhapdf=0.27453D+05
Weight  465
   id=5054,
   group=2,
   key value pairs:
      lhapdf=0.27454D+05
Weight  466
   id=5055,
   group=2,
   key value pairs:
      lhapdf=0.27455D+05
Weight  467
   id=5056,
   group=2,
   key value pairs:
      lhapdf=0.27456D+05
Weight  468
   id=5057,
   group=2,
   key value pairs:
      lhapdf=0.27457D+05
Weight  469
   id=5058,
   group=2,
   key value pairs:
      lhapdf=0.27458D+05
Weight  470
   id=5059,
   group=2,
   key value pairs:
      lhapdf=0.27459D+05
Weight  471
   id=5060,
   group=2,
   key value pairs:
      lhapdf=0.27460D+05
Weight  472
   id=5061,
   group=2,
   key value pairs:
      lhapdf=0.27461D+05
Weight  473
   id=5062,
   group=2,
   key value pairs:
      lhapdf=0.27462D+05
Weight  474
   id=5063,
   group=2,
   key value pairs:
      lhapdf=0.27463D+05
Weight  475
   id=5064,
   group=2,
   key value pairs:
      lhapdf=0.27464D+05
Weight  476
   id=5100,
   group=2,
   key value pairs:
      lhapdf=0.27500D+05
Weight  477
   id=5101,
   group=2,
   key value pairs:
      lhapdf=0.27550D+05
Weight  478
   id=6000,
   group=2,
   key value pairs:
      lhapdf=0.93300D+05
Weight  479
   id=6001,
   group=2,
   key value pairs:
      lhapdf=0.93301D+05
Weight  480
   id=6002,
   group=2,
   key value pairs:
      lhapdf=0.93302D+05
Weight  481
   id=6003,
   group=2,
   key value pairs:
      lhapdf=0.93303D+05
Weight  482
   id=6004,
   group=2,
   key value pairs:
      lhapdf=0.93304D+05
Weight  483
   id=6005,
   group=2,
   key value pairs:
      lhapdf=0.93305D+05
Weight  484
   id=6006,
   group=2,
   key value pairs:
      lhapdf=0.93306D+05
Weight  485
   id=6007,
   group=2,
   key value pairs:
      lhapdf=0.93307D+05
Weight  486
   id=6008,
   group=2,
   key value pairs:
      lhapdf=0.93308D+05
Weight  487
   id=6009,
   group=2,
   key value pairs:
      lhapdf=0.93309D+05
Weight  488
   id=6010,
   group=2,
   key value pairs:
      lhapdf=0.93310D+05
Weight  489
   id=6011,
   group=2,
   key value pairs:
      lhapdf=0.93311D+05
Weight  490
   id=6012,
   group=2,
   key value pairs:
      lhapdf=0.93312D+05
Weight  491
   id=6013,
   group=2,
   key value pairs:
      lhapdf=0.93313D+05
Weight  492
   id=6014,
   group=2,
   key value pairs:
      lhapdf=0.93314D+05
Weight  493
   id=6015,
   group=2,
   key value pairs:
      lhapdf=0.93315D+05
Weight  494
   id=6016,
   group=2,
   key value pairs:
      lhapdf=0.93316D+05
Weight  495
   id=6017,
   group=2,
   key value pairs:
      lhapdf=0.93317D+05
Weight  496
   id=6018,
   group=2,
   key value pairs:
      lhapdf=0.93318D+05
Weight  497
   id=6019,
   group=2,
   key value pairs:
      lhapdf=0.93319D+05
Weight  498
   id=6020,
   group=2,
   key value pairs:
      lhapdf=0.93320D+05
Weight  499
   id=6021,
   group=2,
   key value pairs:
      lhapdf=0.93321D+05
Weight  500
   id=6022,
   group=2,
   key value pairs:
      lhapdf=0.93322D+05
Weight  501
   id=6023,
   group=2,
   key value pairs:
      lhapdf=0.93323D+05
Weight  502
   id=6024,
   group=2,
   key value pairs:
      lhapdf=0.93324D+05
Weight  503
   id=6025,
   group=2,
   key value pairs:
      lhapdf=0.93325D+05
Weight  504
   id=6026,
   group=2,
   key value pairs:
      lhapdf=0.93326D+05
Weight  505
   id=6027,
   group=2,
   key value pairs:
      lhapdf=0.93327D+05
Weight  506
   id=6028,
   group=2,
   key value pairs:
      lhapdf=0.93328D+05
Weight  507
   id=6029,
   group=2,
   key value pairs:
      lhapdf=0.93329D+05
Weight  508
   id=6030,
   group=2,
   key value pairs:
      lhapdf=0.93330D+05
Weight  509
   id=6031,
   group=2,
   key value pairs:
      lhapdf=0.93331D+05
Weight  510
   id=6032,
   group=2,
   key value pairs:
      lhapdf=0.93332D+05
Weight  511
   id=6033,
   group=2,
   key value pairs:
      lhapdf=0.93333D+05
Weight  512
   id=6034,
   group=2,
   key value pairs:
      lhapdf=0.93334D+05
Weight  513
   id=6035,
   group=2,
   key value pairs:
      lhapdf=0.93335D+05
Weight  514
   id=6036,
   group=2,
   key value pairs:
      lhapdf=0.93336D+05
Weight  515
   id=6037,
   group=2,
   key value pairs:
      lhapdf=0.93337D+05
Weight  516
   id=6038,
   group=2,
   key value pairs:
      lhapdf=0.93338D+05
Weight  517
   id=6039,
   group=2,
   key value pairs:
      lhapdf=0.93339D+05
Weight  518
   id=6040,
   group=2,
   key value pairs:
      lhapdf=0.93340D+05
Weight  519
   id=6041,
   group=2,
   key value pairs:
      lhapdf=0.93341D+05
Weight  520
   id=6042,
   group=2,
   key value pairs:
      lhapdf=0.93342D+05
Weight  521
   id=7000,
   group=2,
   key value pairs:
      lhapdf=0.61200D+05
Weight  522
   id=7001,
   group=2,
   key value pairs:
      lhapdf=0.61201D+05
Weight  523
   id=7002,
   group=2,
   key value pairs:
      lhapdf=0.61202D+05
Weight  524
   id=7003,
   group=2,
   key value pairs:
      lhapdf=0.61203D+05
Weight  525
   id=7004,
   group=2,
   key value pairs:
      lhapdf=0.61204D+05
Weight  526
   id=7005,
   group=2,
   key value pairs:
      lhapdf=0.61205D+05
Weight  527
   id=7006,
   group=2,
   key value pairs:
      lhapdf=0.61206D+05
Weight  528
   id=7007,
   group=2,
   key value pairs:
      lhapdf=0.61207D+05
Weight  529
   id=7008,
   group=2,
   key value pairs:
      lhapdf=0.61208D+05
Weight  530
   id=7009,
   group=2,
   key value pairs:
      lhapdf=0.61209D+05
Weight  531
   id=7010,
   group=2,
   key value pairs:
      lhapdf=0.61210D+05
Weight  532
   id=7011,
   group=2,
   key value pairs:
      lhapdf=0.61211D+05
Weight  533
   id=7012,
   group=2,
   key value pairs:
      lhapdf=0.61212D+05
Weight  534
   id=7013,
   group=2,
   key value pairs:
      lhapdf=0.61213D+05
Weight  535
   id=7014,
   group=2,
   key value pairs:
      lhapdf=0.61214D+05
Weight  536
   id=7015,
   group=2,
   key value pairs:
      lhapdf=0.61215D+05
Weight  537
   id=7016,
   group=2,
   key value pairs:
      lhapdf=0.61216D+05
Weight  538
   id=7017,
   group=2,
   key value pairs:
      lhapdf=0.61217D+05
Weight  539
   id=7018,
   group=2,
   key value pairs:
      lhapdf=0.61218D+05
Weight  540
   id=7019,
   group=2,
   key value pairs:
      lhapdf=0.61219D+05
Weight  541
   id=7020,
   group=2,
   key value pairs:
      lhapdf=0.61220D+05
Weight  542
   id=7021,
   group=2,
   key value pairs:
      lhapdf=0.61221D+05
Weight  543
   id=7022,
   group=2,
   key value pairs:
      lhapdf=0.61222D+05
Weight  544
   id=7023,
   group=2,
   key value pairs:
      lhapdf=0.61223D+05
Weight  545
   id=7024,
   group=2,
   key value pairs:
      lhapdf=0.61224D+05
Weight  546
   id=7025,
   group=2,
   key value pairs:
      lhapdf=0.61225D+05
Weight  547
   id=7026,
   group=2,
   key value pairs:
      lhapdf=0.61226D+05
Weight  548
   id=7027,
   group=2,
   key value pairs:
      lhapdf=0.61227D+05
Weight  549
   id=7028,
   group=2,
   key value pairs:
      lhapdf=0.61228D+05
Weight  550
   id=8000,
   group=2,
   key value pairs:
      lhapdf=0.42780D+05
Weight  551
   id=8001,
   group=2,
   key value pairs:
      lhapdf=0.42781D+05
Weight  552
   id=8002,
   group=2,
   key value pairs:
      lhapdf=0.42782D+05
Weight  553
   id=8003,
   group=2,
   key value pairs:
      lhapdf=0.42783D+05
Weight  554
   id=8004,
   group=2,
   key value pairs:
      lhapdf=0.42784D+05
Weight  555
   id=8005,
   group=2,
   key value pairs:
      lhapdf=0.42785D+05
Weight  556
   id=8006,
   group=2,
   key value pairs:
      lhapdf=0.42786D+05
Weight  557
   id=8007,
   group=2,
   key value pairs:
      lhapdf=0.42787D+05
Weight  558
   id=8008,
   group=2,
   key value pairs:
      lhapdf=0.42788D+05
Weight  559
   id=8009,
   group=2,
   key value pairs:
      lhapdf=0.42789D+05
Weight  560
   id=8010,
   group=2,
   key value pairs:
      lhapdf=0.42790D+05
Weight  561
   id=8011,
   group=2,
   key value pairs:
      lhapdf=0.42791D+05
Weight  562
   id=8012,
   group=2,
   key value pairs:
      lhapdf=0.42792D+05
Weight  563
   id=8013,
   group=2,
   key value pairs:
      lhapdf=0.42793D+05
Weight  564
   id=8014,
   group=2,
   key value pairs:
      lhapdf=0.42794D+05
Weight  565
   id=8015,
   group=2,
   key value pairs:
      lhapdf=0.42795D+05
Weight  566
   id=8016,
   group=2,
   key value pairs:
      lhapdf=0.42796D+05
Weight  567
   id=8017,
   group=2,
   key value pairs:
      lhapdf=0.42797D+05
Weight  568
   id=8018,
   group=2,
   key value pairs:
      lhapdf=0.42798D+05
Weight  569
   id=8019,
   group=2,
   key value pairs:
      lhapdf=0.42799D+05
Weight  570
   id=8020,
   group=2,
   key value pairs:
      lhapdf=0.42800D+05
Weight  571
   id=8021,
   group=2,
   key value pairs:
      lhapdf=0.42801D+05
Weight  572
   id=8022,
   group=2,
   key value pairs:
      lhapdf=0.42802D+05
Weight  573
   id=8023,
   group=2,
   key value pairs:
      lhapdf=0.42803D+05
Weight  574
   id=8024,
   group=2,
   key value pairs:
      lhapdf=0.42804D+05
Weight  575
   id=8025,
   group=2,
   key value pairs:
      lhapdf=0.42805D+05
Weight  576
   id=8026,
   group=2,
   key value pairs:
      lhapdf=0.42806D+05
Weight  577
   id=8027,
   group=2,
   key value pairs:
      lhapdf=0.42807D+05
Weight  578
   id=8028,
   group=2,
   key value pairs:
      lhapdf=0.42808D+05
Weight  579
   id=8029,
   group=2,
   key value pairs:
      lhapdf=0.42809D+05
Weight  580
   id=3000,
   group=3,
   key value pairs:
      lhapdf=0.31620D+06
Weight  581
   id=3001,
   group=3,
   key value pairs:
      lhapdf=0.31620D+06
Weight  582
   id=3002,
   group=3,
   key value pairs:
      lhapdf=0.31620D+06
Weight  583
   id=3003,
   group=3,
   key value pairs:
      lhapdf=0.31620D+06
Weight  584
   id=3004,
   group=3,
   key value pairs:
      lhapdf=0.31620D+06
Weight  585
   id=3005,
   group=3,
   key value pairs:
      lhapdf=0.31620D+06
Weight  586
   id=3006,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  587
   id=3007,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  588
   id=3008,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  589
   id=3009,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  590
   id=3010,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  591
   id=3011,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  592
   id=3012,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  593
   id=3013,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  594
   id=3014,
   group=3,
   key value pairs:
      lhapdf=0.31621D+06
Weight  595
   id=3015,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  596
   id=3016,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  597
   id=3017,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  598
   id=3018,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  599
   id=3019,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  600
   id=3020,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  601
   id=3021,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  602
   id=3022,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  603
   id=3023,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  604
   id=3024,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  605
   id=3025,
   group=3,
   key value pairs:
      lhapdf=0.31622D+06
Weight  606
   id=3026,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  607
   id=3027,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  608
   id=3028,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  609
   id=3029,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  610
   id=3030,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  611
   id=3031,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  612
   id=3032,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  613
   id=3033,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  614
   id=3034,
   group=3,
   key value pairs:
      lhapdf=0.31623D+06
Weight  615
   id=3035,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  616
   id=3036,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  617
   id=3037,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  618
   id=3038,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  619
   id=3039,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  620
   id=3040,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  621
   id=3041,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  622
   id=3042,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  623
   id=3043,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  624
   id=3044,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  625
   id=3045,
   group=3,
   key value pairs:
      lhapdf=0.31624D+06
Weight  626
   id=3046,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  627
   id=3047,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  628
   id=3048,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  629
   id=3049,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  630
   id=3050,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  631
   id=3051,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  632
   id=3052,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  633
   id=3053,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  634
   id=3054,
   group=3,
   key value pairs:
      lhapdf=0.31625D+06
Weight  635
   id=3055,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  636
   id=3056,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  637
   id=3057,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  638
   id=3058,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  639
   id=3059,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  640
   id=3060,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  641
   id=3061,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  642
   id=3062,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  643
   id=3063,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  644
   id=3064,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  645
   id=3065,
   group=3,
   key value pairs:
      lhapdf=0.31626D+06
Weight  646
   id=3066,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  647
   id=3067,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  648
   id=3068,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  649
   id=3069,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  650
   id=3070,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  651
   id=3071,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  652
   id=3072,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  653
   id=3073,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  654
   id=3074,
   group=3,
   key value pairs:
      lhapdf=0.31627D+06
Weight  655
   id=3075,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  656
   id=3076,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  657
   id=3077,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  658
   id=3078,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  659
   id=3079,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  660
   id=3080,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  661
   id=3081,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  662
   id=3082,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  663
   id=3083,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  664
   id=3084,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  665
   id=3085,
   group=3,
   key value pairs:
      lhapdf=0.31628D+06
Weight  666
   id=3086,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  667
   id=3087,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  668
   id=3088,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  669
   id=3089,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  670
   id=3090,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  671
   id=3091,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  672
   id=3092,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  673
   id=3093,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  674
   id=3094,
   group=3,
   key value pairs:
      lhapdf=0.31629D+06
Weight  675
   id=3095,
   group=3,
   key value pairs:
      lhapdf=0.31630D+06
Weight  676
   id=3096,
   group=3,
   key value pairs:
      lhapdf=0.31630D+06
Weight  677
   id=3097,
   group=3,
   key value pairs:
      lhapdf=0.31630D+06
Weight  678
   id=3098,
   group=3,
   key value pairs:
      lhapdf=0.31630D+06
Weight  679
   id=3099,
   group=3,
   key value pairs:
      lhapdf=0.31630D+06
Weight  680
   id=3100,
   group=3,
   key value pairs:
      lhapdf=0.31630D+06
Weight  681
   id=3200,
   group=3,
   key value pairs:
      lhapdf=0.33130D+06
Weight  682
   id=3201,
   group=3,
   key value pairs:
      lhapdf=0.33130D+06
Weight  683
   id=3202,
   group=3,
   key value pairs:
      lhapdf=0.33130D+06
Weight  684
   id=3203,
   group=3,
   key value pairs:
      lhapdf=0.33130D+06
Weight  685
   id=3204,
   group=3,
   key value pairs:
      lhapdf=0.33130D+06
Weight  686
   id=3205,
   group=3,
   key value pairs:
      lhapdf=0.33130D+06
Weight  687
   id=3206,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  688
   id=3207,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  689
   id=3208,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  690
   id=3209,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  691
   id=3210,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  692
   id=3211,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  693
   id=3212,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  694
   id=3213,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  695
   id=3214,
   group=3,
   key value pairs:
      lhapdf=0.33131D+06
Weight  696
   id=3215,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  697
   id=3216,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  698
   id=3217,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  699
   id=3218,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  700
   id=3219,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  701
   id=3220,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  702
   id=3221,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  703
   id=3222,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  704
   id=3223,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  705
   id=3224,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  706
   id=3225,
   group=3,
   key value pairs:
      lhapdf=0.33132D+06
Weight  707
   id=3226,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  708
   id=3227,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  709
   id=3228,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  710
   id=3229,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  711
   id=3230,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  712
   id=3231,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  713
   id=3232,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  714
   id=3233,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  715
   id=3234,
   group=3,
   key value pairs:
      lhapdf=0.33133D+06
Weight  716
   id=3235,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  717
   id=3236,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  718
   id=3237,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  719
   id=3238,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  720
   id=3239,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  721
   id=3240,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  722
   id=3241,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  723
   id=3242,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  724
   id=3243,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  725
   id=3244,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  726
   id=3245,
   group=3,
   key value pairs:
      lhapdf=0.33134D+06
Weight  727
   id=3246,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  728
   id=3247,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  729
   id=3248,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  730
   id=3249,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  731
   id=3250,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  732
   id=3251,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  733
   id=3252,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  734
   id=3253,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  735
   id=3254,
   group=3,
   key value pairs:
      lhapdf=0.33135D+06
Weight  736
   id=3255,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  737
   id=3256,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  738
   id=3257,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  739
   id=3258,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  740
   id=3259,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  741
   id=3260,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  742
   id=3261,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  743
   id=3262,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  744
   id=3263,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  745
   id=3264,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  746
   id=3265,
   group=3,
   key value pairs:
      lhapdf=0.33136D+06
Weight  747
   id=3266,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  748
   id=3267,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  749
   id=3268,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  750
   id=3269,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  751
   id=3270,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  752
   id=3271,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  753
   id=3272,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  754
   id=3273,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  755
   id=3274,
   group=3,
   key value pairs:
      lhapdf=0.33137D+06
Weight  756
   id=3275,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  757
   id=3276,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  758
   id=3277,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  759
   id=3278,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  760
   id=3279,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  761
   id=3280,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  762
   id=3281,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  763
   id=3282,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  764
   id=3283,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  765
   id=3284,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  766
   id=3285,
   group=3,
   key value pairs:
      lhapdf=0.33138D+06
Weight  767
   id=3286,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  768
   id=3287,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  769
   id=3288,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  770
   id=3289,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  771
   id=3290,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  772
   id=3291,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  773
   id=3292,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  774
   id=3293,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  775
   id=3294,
   group=3,
   key value pairs:
      lhapdf=0.33139D+06
Weight  776
   id=3295,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  777
   id=3296,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  778
   id=3297,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  779
   id=3298,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  780
   id=3299,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  781
   id=3300,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  782
   id=3301,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  783
   id=3302,
   group=3,
   key value pairs:
      lhapdf=0.33140D+06
Weight  784
   id=3400,
   group=3,
   key value pairs:
      lhapdf=0.33210D+06
Weight  785
   id=3401,
   group=3,
   key value pairs:
      lhapdf=0.33210D+06
Weight  786
   id=3402,
   group=3,
   key value pairs:
      lhapdf=0.33210D+06
Weight  787
   id=3403,
   group=3,
   key value pairs:
      lhapdf=0.33210D+06
Weight  788
   id=3404,
   group=3,
   key value pairs:
      lhapdf=0.33210D+06
Weight  789
   id=3405,
   group=3,
   key value pairs:
      lhapdf=0.33210D+06
Weight  790
   id=3406,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  791
   id=3407,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  792
   id=3408,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  793
   id=3409,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  794
   id=3410,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  795
   id=3411,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  796
   id=3412,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  797
   id=3413,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  798
   id=3414,
   group=3,
   key value pairs:
      lhapdf=0.33211D+06
Weight  799
   id=3415,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  800
   id=3416,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  801
   id=3417,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  802
   id=3418,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  803
   id=3419,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  804
   id=3420,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  805
   id=3421,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  806
   id=3422,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  807
   id=3423,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  808
   id=3424,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  809
   id=3425,
   group=3,
   key value pairs:
      lhapdf=0.33212D+06
Weight  810
   id=3426,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  811
   id=3427,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  812
   id=3428,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  813
   id=3429,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  814
   id=3430,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  815
   id=3431,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  816
   id=3432,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  817
   id=3433,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  818
   id=3434,
   group=3,
   key value pairs:
      lhapdf=0.33213D+06
Weight  819
   id=3435,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  820
   id=3436,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  821
   id=3437,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  822
   id=3438,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  823
   id=3439,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  824
   id=3440,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  825
   id=3441,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  826
   id=3442,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  827
   id=3443,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  828
   id=3444,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  829
   id=3445,
   group=3,
   key value pairs:
      lhapdf=0.33214D+06
Weight  830
   id=3446,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  831
   id=3447,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  832
   id=3448,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  833
   id=3449,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  834
   id=3450,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  835
   id=3451,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  836
   id=3452,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  837
   id=3453,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  838
   id=3454,
   group=3,
   key value pairs:
      lhapdf=0.33215D+06
Weight  839
   id=3455,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  840
   id=3456,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  841
   id=3457,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  842
   id=3458,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  843
   id=3459,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  844
   id=3460,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  845
   id=3461,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  846
   id=3462,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  847
   id=3463,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  848
   id=3464,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  849
   id=3465,
   group=3,
   key value pairs:
      lhapdf=0.33216D+06
Weight  850
   id=3466,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  851
   id=3467,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  852
   id=3468,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  853
   id=3469,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  854
   id=3470,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  855
   id=3471,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  856
   id=3472,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  857
   id=3473,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  858
   id=3474,
   group=3,
   key value pairs:
      lhapdf=0.33217D+06
Weight  859
   id=3475,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  860
   id=3476,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  861
   id=3477,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  862
   id=3478,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  863
   id=3479,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  864
   id=3480,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  865
   id=3481,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  866
   id=3482,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  867
   id=3483,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  868
   id=3484,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  869
   id=3485,
   group=3,
   key value pairs:
      lhapdf=0.33218D+06
Weight  870
   id=3486,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  871
   id=3487,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  872
   id=3488,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  873
   id=3489,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  874
   id=3490,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  875
   id=3491,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  876
   id=3492,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  877
   id=3493,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  878
   id=3494,
   group=3,
   key value pairs:
      lhapdf=0.33219D+06
Weight  879
   id=3495,
   group=3,
   key value pairs:
      lhapdf=0.33220D+06
Weight  880
   id=3496,
   group=3,
   key value pairs:
      lhapdf=0.33220D+06
Weight  881
   id=3497,
   group=3,
   key value pairs:
      lhapdf=0.33220D+06
Weight  882
   id=3498,
   group=3,
   key value pairs:
      lhapdf=0.33220D+06
Weight  883
   id=3499,
   group=3,
   key value pairs:
      lhapdf=0.33220D+06
Weight  884
   id=3500,
   group=3,
   key value pairs:
      lhapdf=0.33220D+06
  powheginput keyword noevents             absent; set to   -1000000.0000000000     
  powheginput keyword rwl_group_events     set to    2000.0000000000000     
  powheginput keyword btildeborn           absent; set to   -1000000.0000000000     
  powheginput keyword btildevirt           absent; set to   -1000000.0000000000     
  powheginput keyword btildecoll           absent; set to   -1000000.0000000000     
  powheginput keyword btildereal           absent; set to   -1000000.0000000000     
  powheginput keyword compare_vecsv_ep     absent; set to   -1000000.0000000000     
 RM48 INITIALIZED:    234567          22         0
 RM48IN SKIPPING OVER              22
 Writing virtequiv file...
 Done
  powheginput keyword btlscalect           absent; set to   -1000000.0000000000     
  powheginput keyword testsuda             absent; set to   -1000000.0000000000     
  powheginput keyword radregion            absent; set to   -1000000.0000000000     
 RM48 INITIALIZED:    234567         576         0
 RM48IN SKIPPING OVER             576
 Writing realequivregions-rad file...
 Done
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0001.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #1, version 1; LHAPDF ID = 325301
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0002.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #2, version 1; LHAPDF ID = 325302
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0003.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #3, version 1; LHAPDF ID = 325303
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0004.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #4, version 1; LHAPDF ID = 325304
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0005.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #5, version 1; LHAPDF ID = 325305
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0006.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #6, version 1; LHAPDF ID = 325306
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0007.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #7, version 1; LHAPDF ID = 325307
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0008.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #8, version 1; LHAPDF ID = 325308
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0009.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #9, version 1; LHAPDF ID = 325309
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0010.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #10, version 1; LHAPDF ID = 325310
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0011.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #11, version 1; LHAPDF ID = 325311
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0012.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #12, version 1; LHAPDF ID = 325312
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0013.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #13, version 1; LHAPDF ID = 325313
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0014.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #14, version 1; LHAPDF ID = 325314
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0015.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #15, version 1; LHAPDF ID = 325315
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0016.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #16, version 1; LHAPDF ID = 325316
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0017.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #17, version 1; LHAPDF ID = 325317
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0018.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #18, version 1; LHAPDF ID = 325318
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0019.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #19, version 1; LHAPDF ID = 325319
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0020.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #20, version 1; LHAPDF ID = 325320
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0021.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #21, version 1; LHAPDF ID = 325321
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0022.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #22, version 1; LHAPDF ID = 325322
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0023.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #23, version 1; LHAPDF ID = 325323
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0024.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #24, version 1; LHAPDF ID = 325324
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0025.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #25, version 1; LHAPDF ID = 325325
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0026.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #26, version 1; LHAPDF ID = 325326
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0027.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #27, version 1; LHAPDF ID = 325327
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0028.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #28, version 1; LHAPDF ID = 325328
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0029.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #29, version 1; LHAPDF ID = 325329
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0030.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #30, version 1; LHAPDF ID = 325330
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0031.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #31, version 1; LHAPDF ID = 325331
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0032.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #32, version 1; LHAPDF ID = 325332
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0033.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #33, version 1; LHAPDF ID = 325333
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0034.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #34, version 1; LHAPDF ID = 325334
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0035.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #35, version 1; LHAPDF ID = 325335
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0036.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #36, version 1; LHAPDF ID = 325336
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0037.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #37, version 1; LHAPDF ID = 325337
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0038.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #38, version 1; LHAPDF ID = 325338
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0039.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #39, version 1; LHAPDF ID = 325339
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0040.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #40, version 1; LHAPDF ID = 325340
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0041.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #41, version 1; LHAPDF ID = 325341
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0042.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #42, version 1; LHAPDF ID = 325342
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0043.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #43, version 1; LHAPDF ID = 325343
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0044.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #44, version 1; LHAPDF ID = 325344
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0045.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #45, version 1; LHAPDF ID = 325345
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0046.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #46, version 1; LHAPDF ID = 325346
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0047.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #47, version 1; LHAPDF ID = 325347
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0048.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #48, version 1; LHAPDF ID = 325348
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0049.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #49, version 1; LHAPDF ID = 325349
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0050.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #50, version 1; LHAPDF ID = 325350
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0051.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #51, version 1; LHAPDF ID = 325351
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0052.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #52, version 1; LHAPDF ID = 325352
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0053.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #53, version 1; LHAPDF ID = 325353
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0054.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #54, version 1; LHAPDF ID = 325354
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0055.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #55, version 1; LHAPDF ID = 325355
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0056.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #56, version 1; LHAPDF ID = 325356
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0057.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #57, version 1; LHAPDF ID = 325357
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0058.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #58, version 1; LHAPDF ID = 325358
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0059.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #59, version 1; LHAPDF ID = 325359
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0060.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #60, version 1; LHAPDF ID = 325360
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0061.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #61, version 1; LHAPDF ID = 325361
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0062.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #62, version 1; LHAPDF ID = 325362
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0063.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #63, version 1; LHAPDF ID = 325363
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0064.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #64, version 1; LHAPDF ID = 325364
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0065.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #65, version 1; LHAPDF ID = 325365
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0066.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #66, version 1; LHAPDF ID = 325366
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0067.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #67, version 1; LHAPDF ID = 325367
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0068.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #68, version 1; LHAPDF ID = 325368
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0069.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #69, version 1; LHAPDF ID = 325369
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0070.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #70, version 1; LHAPDF ID = 325370
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0071.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #71, version 1; LHAPDF ID = 325371
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0072.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #72, version 1; LHAPDF ID = 325372
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0073.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #73, version 1; LHAPDF ID = 325373
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0074.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #74, version 1; LHAPDF ID = 325374
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0075.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #75, version 1; LHAPDF ID = 325375
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0076.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #76, version 1; LHAPDF ID = 325376
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0077.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #77, version 1; LHAPDF ID = 325377
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0078.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #78, version 1; LHAPDF ID = 325378
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0079.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #79, version 1; LHAPDF ID = 325379
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0080.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #80, version 1; LHAPDF ID = 325380
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0081.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #81, version 1; LHAPDF ID = 325381
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0082.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #82, version 1; LHAPDF ID = 325382
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0083.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #83, version 1; LHAPDF ID = 325383
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0084.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #84, version 1; LHAPDF ID = 325384
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0085.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #85, version 1; LHAPDF ID = 325385
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0086.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #86, version 1; LHAPDF ID = 325386
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0087.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #87, version 1; LHAPDF ID = 325387
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0088.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #88, version 1; LHAPDF ID = 325388
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0089.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #89, version 1; LHAPDF ID = 325389
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0090.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #90, version 1; LHAPDF ID = 325390
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0091.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #91, version 1; LHAPDF ID = 325391
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0092.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #92, version 1; LHAPDF ID = 325392
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0093.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #93, version 1; LHAPDF ID = 325393
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0094.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #94, version 1; LHAPDF ID = 325394
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0095.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #95, version 1; LHAPDF ID = 325395
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0096.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #96, version 1; LHAPDF ID = 325396
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0097.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #97, version 1; LHAPDF ID = 325397
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0098.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #98, version 1; LHAPDF ID = 325398
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0099.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #99, version 1; LHAPDF ID = 325399
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0100.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #100, version 1; LHAPDF ID = 325400
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0101.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #101, version 1; LHAPDF ID = 325401
  check: alpha_s(Mz)=  0.11600210403341857     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.18590415209195268     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc_hessian_pdfas/NNPDF31_nnlo_as_0118_mc_hessian_pdfas_0102.dat
NNPDF31_nnlo_as_0118_mc_hessian_pdfas PDF set, member #102, version 1; LHAPDF ID = 325402
  check: alpha_s(Mz)=  0.12000221977880079     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.23268984164819539     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_hessian_pdfas/NNPDF31_nnlo_hessian_pdfas_0000.dat
NNPDF31_nnlo_hessian_pdfas PDF set, member #0, version 1; LHAPDF ID = 306000
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0108/NNPDF31_nnlo_as_0108_0000.dat
NNPDF31_nnlo_as_0108 PDF set, member #0, version 1; LHAPDF ID = 322500
  check: alpha_s(Mz)=  0.10800186760710467     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.11275134463951170     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0110/NNPDF31_nnlo_as_0110_0000.dat
NNPDF31_nnlo_as_0110 PDF set, member #0, version 1; LHAPDF ID = 322700
  check: alpha_s(Mz)=  0.11000192180756951     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.12865941775281300     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0112/NNPDF31_nnlo_as_0112_0000.dat
NNPDF31_nnlo_as_0112 PDF set, member #0, version 1; LHAPDF ID = 322900
  check: alpha_s(Mz)=  0.11200198707341759     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.14610675391738989     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0114/NNPDF31_nnlo_as_0114_0000.dat
NNPDF31_nnlo_as_0114 PDF set, member #0, version 1; LHAPDF ID = 323100
  check: alpha_s(Mz)=  0.11400204585444509     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.16516511223838429     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0117/NNPDF31_nnlo_as_0117_0000.dat
NNPDF31_nnlo_as_0117 PDF set, member #0, version 1; LHAPDF ID = 323300
  check: alpha_s(Mz)=  0.11700212910978669     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.19692495081382516     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0119/NNPDF31_nnlo_as_0119_0000.dat
NNPDF31_nnlo_as_0119 PDF set, member #0, version 1; LHAPDF ID = 323500
  check: alpha_s(Mz)=  0.11900219136857998     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.22030998348098008     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0122/NNPDF31_nnlo_as_0122_0000.dat
NNPDF31_nnlo_as_0122 PDF set, member #0, version 1; LHAPDF ID = 323700
  check: alpha_s(Mz)=  0.12200228249837269     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.25886228724144389     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0124/NNPDF31_nnlo_as_0124_0000.dat
NNPDF31_nnlo_as_0124 PDF set, member #0, version 1; LHAPDF ID = 323900
  check: alpha_s(Mz)=  0.12400233818334780     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.28696644315731307     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0000.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #0, version 1; LHAPDF ID = 305800
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0001.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #1, version 1; LHAPDF ID = 305801
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0002.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #2, version 1; LHAPDF ID = 305802
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0003.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #3, version 1; LHAPDF ID = 305803
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0004.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #4, version 1; LHAPDF ID = 305804
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0005.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #5, version 1; LHAPDF ID = 305805
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0006.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #6, version 1; LHAPDF ID = 305806
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0007.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #7, version 1; LHAPDF ID = 305807
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0008.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #8, version 1; LHAPDF ID = 305808
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0009.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #9, version 1; LHAPDF ID = 305809
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0010.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #10, version 1; LHAPDF ID = 305810
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0011.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #11, version 1; LHAPDF ID = 305811
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0012.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #12, version 1; LHAPDF ID = 305812
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0013.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #13, version 1; LHAPDF ID = 305813
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0014.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #14, version 1; LHAPDF ID = 305814
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0015.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #15, version 1; LHAPDF ID = 305815
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0016.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #16, version 1; LHAPDF ID = 305816
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0017.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #17, version 1; LHAPDF ID = 305817
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0018.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #18, version 1; LHAPDF ID = 305818
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0019.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #19, version 1; LHAPDF ID = 305819
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0020.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #20, version 1; LHAPDF ID = 305820
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0021.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #21, version 1; LHAPDF ID = 305821
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0022.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #22, version 1; LHAPDF ID = 305822
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0023.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #23, version 1; LHAPDF ID = 305823
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0024.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #24, version 1; LHAPDF ID = 305824
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0025.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #25, version 1; LHAPDF ID = 305825
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0026.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #26, version 1; LHAPDF ID = 305826
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0027.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #27, version 1; LHAPDF ID = 305827
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0028.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #28, version 1; LHAPDF ID = 305828
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0029.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #29, version 1; LHAPDF ID = 305829
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0030.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #30, version 1; LHAPDF ID = 305830
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0031.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #31, version 1; LHAPDF ID = 305831
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0032.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #32, version 1; LHAPDF ID = 305832
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0033.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #33, version 1; LHAPDF ID = 305833
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0034.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #34, version 1; LHAPDF ID = 305834
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0035.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #35, version 1; LHAPDF ID = 305835
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0036.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #36, version 1; LHAPDF ID = 305836
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0037.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #37, version 1; LHAPDF ID = 305837
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0038.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #38, version 1; LHAPDF ID = 305838
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0039.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #39, version 1; LHAPDF ID = 305839
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0040.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #40, version 1; LHAPDF ID = 305840
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0041.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #41, version 1; LHAPDF ID = 305841
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0042.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #42, version 1; LHAPDF ID = 305842
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0043.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #43, version 1; LHAPDF ID = 305843
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0044.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #44, version 1; LHAPDF ID = 305844
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0045.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #45, version 1; LHAPDF ID = 305845
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0046.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #46, version 1; LHAPDF ID = 305846
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0047.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #47, version 1; LHAPDF ID = 305847
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0048.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #48, version 1; LHAPDF ID = 305848
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0049.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #49, version 1; LHAPDF ID = 305849
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0050.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #50, version 1; LHAPDF ID = 305850
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0051.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #51, version 1; LHAPDF ID = 305851
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0052.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #52, version 1; LHAPDF ID = 305852
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0053.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #53, version 1; LHAPDF ID = 305853
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0054.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #54, version 1; LHAPDF ID = 305854
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0055.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #55, version 1; LHAPDF ID = 305855
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0056.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #56, version 1; LHAPDF ID = 305856
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0057.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #57, version 1; LHAPDF ID = 305857
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0058.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #58, version 1; LHAPDF ID = 305858
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0059.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #59, version 1; LHAPDF ID = 305859
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0060.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #60, version 1; LHAPDF ID = 305860
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0061.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #61, version 1; LHAPDF ID = 305861
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0062.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #62, version 1; LHAPDF ID = 305862
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0063.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #63, version 1; LHAPDF ID = 305863
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0064.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #64, version 1; LHAPDF ID = 305864
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0065.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #65, version 1; LHAPDF ID = 305865
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0066.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #66, version 1; LHAPDF ID = 305866
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0067.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #67, version 1; LHAPDF ID = 305867
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0068.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #68, version 1; LHAPDF ID = 305868
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0069.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #69, version 1; LHAPDF ID = 305869
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0070.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #70, version 1; LHAPDF ID = 305870
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0071.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #71, version 1; LHAPDF ID = 305871
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0072.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #72, version 1; LHAPDF ID = 305872
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0073.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #73, version 1; LHAPDF ID = 305873
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0074.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #74, version 1; LHAPDF ID = 305874
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0075.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #75, version 1; LHAPDF ID = 305875
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0076.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #76, version 1; LHAPDF ID = 305876
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0077.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #77, version 1; LHAPDF ID = 305877
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0078.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #78, version 1; LHAPDF ID = 305878
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0079.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #79, version 1; LHAPDF ID = 305879
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0080.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #80, version 1; LHAPDF ID = 305880
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0081.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #81, version 1; LHAPDF ID = 305881
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0082.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #82, version 1; LHAPDF ID = 305882
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0083.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #83, version 1; LHAPDF ID = 305883
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0084.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #84, version 1; LHAPDF ID = 305884
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0085.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #85, version 1; LHAPDF ID = 305885
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0086.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #86, version 1; LHAPDF ID = 305886
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0087.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #87, version 1; LHAPDF ID = 305887
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0088.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #88, version 1; LHAPDF ID = 305888
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0089.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #89, version 1; LHAPDF ID = 305889
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0090.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #90, version 1; LHAPDF ID = 305890
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0091.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #91, version 1; LHAPDF ID = 305891
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0092.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #92, version 1; LHAPDF ID = 305892
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0093.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #93, version 1; LHAPDF ID = 305893
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0094.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #94, version 1; LHAPDF ID = 305894
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0095.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #95, version 1; LHAPDF ID = 305895
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0096.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #96, version 1; LHAPDF ID = 305896
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0097.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #97, version 1; LHAPDF ID = 305897
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0098.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #98, version 1; LHAPDF ID = 305898
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0099.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #99, version 1; LHAPDF ID = 305899
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0100.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #100, version 1; LHAPDF ID = 305900
  check: alpha_s(Mz)=  0.11800216951342939     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626127452891817     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0101.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #101, version 1; LHAPDF ID = 305901
  check: alpha_s(Mz)=  0.11600210623570216     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.20183318533040315     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nlo_hessian_pdfas/NNPDF31_nlo_hessian_pdfas_0102.dat
NNPDF31_nlo_hessian_pdfas PDF set, member #102, version 1; LHAPDF ID = 305902
  check: alpha_s(Mz)=  0.12000223029127519     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.25265541079529102     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF30_nnlo_as_0118_hessian/NNPDF30_nnlo_as_0118_hessian_0000.dat
NNPDF30_nnlo_as_0118_hessian PDF set, member #0, version 1; LHAPDF ID = 303200
  check: alpha_s(Mz)=  0.11800230075848536     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839257465514974     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF30_nlo_nf_5_pdfas/NNPDF30_nlo_nf_5_pdfas_0000.dat
NNPDF30_nlo_nf_5_pdfas PDF set, member #0, version 2; LHAPDF ID = 292200
  check: alpha_s(Mz)=  0.11800230471993879     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626299159596305     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0000.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #0, version 1; LHAPDF ID = 331600
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0001.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #1, version 1; LHAPDF ID = 331601
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0002.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #2, version 1; LHAPDF ID = 331602
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0003.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #3, version 1; LHAPDF ID = 331603
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0004.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #4, version 1; LHAPDF ID = 331604
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0005.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #5, version 1; LHAPDF ID = 331605
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0006.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #6, version 1; LHAPDF ID = 331606
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0007.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #7, version 1; LHAPDF ID = 331607
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0008.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #8, version 1; LHAPDF ID = 331608
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0009.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #9, version 1; LHAPDF ID = 331609
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0010.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #10, version 1; LHAPDF ID = 331610
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0011.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #11, version 1; LHAPDF ID = 331611
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0012.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #12, version 1; LHAPDF ID = 331612
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0013.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #13, version 1; LHAPDF ID = 331613
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0014.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #14, version 1; LHAPDF ID = 331614
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0015.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #15, version 1; LHAPDF ID = 331615
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0016.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #16, version 1; LHAPDF ID = 331616
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0017.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #17, version 1; LHAPDF ID = 331617
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0018.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #18, version 1; LHAPDF ID = 331618
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0019.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #19, version 1; LHAPDF ID = 331619
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0020.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #20, version 1; LHAPDF ID = 331620
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0021.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #21, version 1; LHAPDF ID = 331621
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0022.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #22, version 1; LHAPDF ID = 331622
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0023.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #23, version 1; LHAPDF ID = 331623
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0024.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #24, version 1; LHAPDF ID = 331624
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0025.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #25, version 1; LHAPDF ID = 331625
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0026.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #26, version 1; LHAPDF ID = 331626
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0027.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #27, version 1; LHAPDF ID = 331627
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0028.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #28, version 1; LHAPDF ID = 331628
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0029.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #29, version 1; LHAPDF ID = 331629
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0030.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #30, version 1; LHAPDF ID = 331630
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0031.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #31, version 1; LHAPDF ID = 331631
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0032.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #32, version 1; LHAPDF ID = 331632
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0033.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #33, version 1; LHAPDF ID = 331633
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0034.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #34, version 1; LHAPDF ID = 331634
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0035.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #35, version 1; LHAPDF ID = 331635
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0036.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #36, version 1; LHAPDF ID = 331636
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0037.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #37, version 1; LHAPDF ID = 331637
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0038.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #38, version 1; LHAPDF ID = 331638
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0039.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #39, version 1; LHAPDF ID = 331639
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0040.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #40, version 1; LHAPDF ID = 331640
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0041.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #41, version 1; LHAPDF ID = 331641
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0042.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #42, version 1; LHAPDF ID = 331642
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0043.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #43, version 1; LHAPDF ID = 331643
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0044.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #44, version 1; LHAPDF ID = 331644
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0045.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #45, version 1; LHAPDF ID = 331645
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0046.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #46, version 1; LHAPDF ID = 331646
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0047.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #47, version 1; LHAPDF ID = 331647
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0048.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #48, version 1; LHAPDF ID = 331648
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0049.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #49, version 1; LHAPDF ID = 331649
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0050.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #50, version 1; LHAPDF ID = 331650
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0051.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #51, version 1; LHAPDF ID = 331651
  check: alpha_s(Mz)=  0.11700212910978669     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.19692495081382516     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_hessian_pdfas/NNPDF40_nnlo_hessian_pdfas_0052.dat
NNPDF40_nnlo_hessian_pdfas PDF set, member #52, version 1; LHAPDF ID = 331652
  check: alpha_s(Mz)=  0.11900219136857998     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.22030998348098008     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_as_01160/NNPDF40_nnlo_as_01160_0000.dat
NNPDF40_nnlo_as_01160 PDF set, member #0, version 1; LHAPDF ID = 332700
  check: alpha_s(Mz)=  0.11600210403341857     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.18590415209195268     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_as_01170/NNPDF40_nnlo_as_01170_0000.dat
NNPDF40_nnlo_as_01170 PDF set, member #0, version 1; LHAPDF ID = 332900
  check: alpha_s(Mz)=  0.11700212910978669     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.19692495081382516     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_as_01175/NNPDF40_nnlo_as_01175_0000.dat
NNPDF40_nnlo_as_01175 PDF set, member #0, version 1; LHAPDF ID = 333100
  check: alpha_s(Mz)=  0.11750214490617363     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20260180303898312     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_as_01185/NNPDF40_nnlo_as_01185_0000.dat
NNPDF40_nnlo_as_01185 PDF set, member #0, version 1; LHAPDF ID = 333300
  check: alpha_s(Mz)=  0.11850218042167245     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.21429338888587329     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_as_01190/NNPDF40_nnlo_as_01190_0000.dat
NNPDF40_nnlo_as_01190 PDF set, member #0, version 1; LHAPDF ID = 333500
  check: alpha_s(Mz)=  0.11900219136857998     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.22030998348098008     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_as_01200/NNPDF40_nnlo_as_01200_0000.dat
NNPDF40_nnlo_as_01200 PDF set, member #0, version 1; LHAPDF ID = 333700
  check: alpha_s(Mz)=  0.12000221977880079     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.23268984164819539     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nlo_pch_as_01180/NNPDF40_nlo_pch_as_01180_0000.dat
NNPDF40_nlo_pch_as_01180 PDF set, member #0, version 1; LHAPDF ID = 332300
  check: alpha_s(Mz)=  0.11800265731386438     
  alpha_s order (0,1,2):            1
  Lambda 5 is   0.22626746943603107     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0000.dat
CT18NNLO PDF set, member #0, version 1; LHAPDF ID = 14000
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0001.dat
CT18NNLO PDF set, member #1, version 1; LHAPDF ID = 14001
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0002.dat
CT18NNLO PDF set, member #2, version 1; LHAPDF ID = 14002
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0003.dat
CT18NNLO PDF set, member #3, version 1; LHAPDF ID = 14003
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0004.dat
CT18NNLO PDF set, member #4, version 1; LHAPDF ID = 14004
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0005.dat
CT18NNLO PDF set, member #5, version 1; LHAPDF ID = 14005
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0006.dat
CT18NNLO PDF set, member #6, version 1; LHAPDF ID = 14006
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0007.dat
CT18NNLO PDF set, member #7, version 1; LHAPDF ID = 14007
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0008.dat
CT18NNLO PDF set, member #8, version 1; LHAPDF ID = 14008
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0009.dat
CT18NNLO PDF set, member #9, version 1; LHAPDF ID = 14009
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0010.dat
CT18NNLO PDF set, member #10, version 1; LHAPDF ID = 14010
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0011.dat
CT18NNLO PDF set, member #11, version 1; LHAPDF ID = 14011
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0012.dat
CT18NNLO PDF set, member #12, version 1; LHAPDF ID = 14012
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0013.dat
CT18NNLO PDF set, member #13, version 1; LHAPDF ID = 14013
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0014.dat
CT18NNLO PDF set, member #14, version 1; LHAPDF ID = 14014
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0015.dat
CT18NNLO PDF set, member #15, version 1; LHAPDF ID = 14015
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0016.dat
CT18NNLO PDF set, member #16, version 1; LHAPDF ID = 14016
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0017.dat
CT18NNLO PDF set, member #17, version 1; LHAPDF ID = 14017
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0018.dat
CT18NNLO PDF set, member #18, version 1; LHAPDF ID = 14018
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0019.dat
CT18NNLO PDF set, member #19, version 1; LHAPDF ID = 14019
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0020.dat
CT18NNLO PDF set, member #20, version 1; LHAPDF ID = 14020
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0021.dat
CT18NNLO PDF set, member #21, version 1; LHAPDF ID = 14021
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0022.dat
CT18NNLO PDF set, member #22, version 1; LHAPDF ID = 14022
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0023.dat
CT18NNLO PDF set, member #23, version 1; LHAPDF ID = 14023
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0024.dat
CT18NNLO PDF set, member #24, version 1; LHAPDF ID = 14024
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0025.dat
CT18NNLO PDF set, member #25, version 1; LHAPDF ID = 14025
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0026.dat
CT18NNLO PDF set, member #26, version 1; LHAPDF ID = 14026
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0027.dat
CT18NNLO PDF set, member #27, version 1; LHAPDF ID = 14027
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0028.dat
CT18NNLO PDF set, member #28, version 1; LHAPDF ID = 14028
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0029.dat
CT18NNLO PDF set, member #29, version 1; LHAPDF ID = 14029
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0030.dat
CT18NNLO PDF set, member #30, version 1; LHAPDF ID = 14030
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0031.dat
CT18NNLO PDF set, member #31, version 1; LHAPDF ID = 14031
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0032.dat
CT18NNLO PDF set, member #32, version 1; LHAPDF ID = 14032
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0033.dat
CT18NNLO PDF set, member #33, version 1; LHAPDF ID = 14033
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0034.dat
CT18NNLO PDF set, member #34, version 1; LHAPDF ID = 14034
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0035.dat
CT18NNLO PDF set, member #35, version 1; LHAPDF ID = 14035
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0036.dat
CT18NNLO PDF set, member #36, version 1; LHAPDF ID = 14036
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0037.dat
CT18NNLO PDF set, member #37, version 1; LHAPDF ID = 14037
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0038.dat
CT18NNLO PDF set, member #38, version 1; LHAPDF ID = 14038
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0039.dat
CT18NNLO PDF set, member #39, version 1; LHAPDF ID = 14039
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0040.dat
CT18NNLO PDF set, member #40, version 1; LHAPDF ID = 14040
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0041.dat
CT18NNLO PDF set, member #41, version 1; LHAPDF ID = 14041
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0042.dat
CT18NNLO PDF set, member #42, version 1; LHAPDF ID = 14042
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0043.dat
CT18NNLO PDF set, member #43, version 1; LHAPDF ID = 14043
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0044.dat
CT18NNLO PDF set, member #44, version 1; LHAPDF ID = 14044
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0045.dat
CT18NNLO PDF set, member #45, version 1; LHAPDF ID = 14045
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0046.dat
CT18NNLO PDF set, member #46, version 1; LHAPDF ID = 14046
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0047.dat
CT18NNLO PDF set, member #47, version 1; LHAPDF ID = 14047
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0048.dat
CT18NNLO PDF set, member #48, version 1; LHAPDF ID = 14048
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0049.dat
CT18NNLO PDF set, member #49, version 1; LHAPDF ID = 14049
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0050.dat
CT18NNLO PDF set, member #50, version 1; LHAPDF ID = 14050
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0051.dat
CT18NNLO PDF set, member #51, version 1; LHAPDF ID = 14051
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0052.dat
CT18NNLO PDF set, member #52, version 1; LHAPDF ID = 14052
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0053.dat
CT18NNLO PDF set, member #53, version 1; LHAPDF ID = 14053
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0054.dat
CT18NNLO PDF set, member #54, version 1; LHAPDF ID = 14054
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0055.dat
CT18NNLO PDF set, member #55, version 1; LHAPDF ID = 14055
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0056.dat
CT18NNLO PDF set, member #56, version 1; LHAPDF ID = 14056
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0057.dat
CT18NNLO PDF set, member #57, version 1; LHAPDF ID = 14057
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO/CT18NNLO_0058.dat
CT18NNLO PDF set, member #58, version 1; LHAPDF ID = 14058
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO_as_0116/CT18NNLO_as_0116_0000.dat
CT18NNLO_as_0116 PDF set, member #0, version 1; LHAPDF ID = 14066
  check: alpha_s(Mz)=  0.11800071759569249     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837406661620839     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO_as_0117/CT18NNLO_as_0117_0000.dat
CT18NNLO_as_0117 PDF set, member #0, version 1; LHAPDF ID = 14067
  check: alpha_s(Mz)=  0.11800071759569249     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837406661620839     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO_as_0119/CT18NNLO_as_0119_0000.dat
CT18NNLO_as_0119 PDF set, member #0, version 1; LHAPDF ID = 14069
  check: alpha_s(Mz)=  0.11800071759569249     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837406661620839     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18NNLO_as_0120/CT18NNLO_as_0120_0000.dat
CT18NNLO_as_0120 PDF set, member #0, version 1; LHAPDF ID = 14070
  check: alpha_s(Mz)=  0.11800071759569249     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837406661620839     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0000.dat
CT18ZNNLO PDF set, member #0, version 1; LHAPDF ID = 14100
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0001.dat
CT18ZNNLO PDF set, member #1, version 1; LHAPDF ID = 14101
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0002.dat
CT18ZNNLO PDF set, member #2, version 1; LHAPDF ID = 14102
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0003.dat
CT18ZNNLO PDF set, member #3, version 1; LHAPDF ID = 14103
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0004.dat
CT18ZNNLO PDF set, member #4, version 1; LHAPDF ID = 14104
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0005.dat
CT18ZNNLO PDF set, member #5, version 1; LHAPDF ID = 14105
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0006.dat
CT18ZNNLO PDF set, member #6, version 1; LHAPDF ID = 14106
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0007.dat
CT18ZNNLO PDF set, member #7, version 1; LHAPDF ID = 14107
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0008.dat
CT18ZNNLO PDF set, member #8, version 1; LHAPDF ID = 14108
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0009.dat
CT18ZNNLO PDF set, member #9, version 1; LHAPDF ID = 14109
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0010.dat
CT18ZNNLO PDF set, member #10, version 1; LHAPDF ID = 14110
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0011.dat
CT18ZNNLO PDF set, member #11, version 1; LHAPDF ID = 14111
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0012.dat
CT18ZNNLO PDF set, member #12, version 1; LHAPDF ID = 14112
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0013.dat
CT18ZNNLO PDF set, member #13, version 1; LHAPDF ID = 14113
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0014.dat
CT18ZNNLO PDF set, member #14, version 1; LHAPDF ID = 14114
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0015.dat
CT18ZNNLO PDF set, member #15, version 1; LHAPDF ID = 14115
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0016.dat
CT18ZNNLO PDF set, member #16, version 1; LHAPDF ID = 14116
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0017.dat
CT18ZNNLO PDF set, member #17, version 1; LHAPDF ID = 14117
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0018.dat
CT18ZNNLO PDF set, member #18, version 1; LHAPDF ID = 14118
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0019.dat
CT18ZNNLO PDF set, member #19, version 1; LHAPDF ID = 14119
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0020.dat
CT18ZNNLO PDF set, member #20, version 1; LHAPDF ID = 14120
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0021.dat
CT18ZNNLO PDF set, member #21, version 1; LHAPDF ID = 14121
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0022.dat
CT18ZNNLO PDF set, member #22, version 1; LHAPDF ID = 14122
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0023.dat
CT18ZNNLO PDF set, member #23, version 1; LHAPDF ID = 14123
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0024.dat
CT18ZNNLO PDF set, member #24, version 1; LHAPDF ID = 14124
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0025.dat
CT18ZNNLO PDF set, member #25, version 1; LHAPDF ID = 14125
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0026.dat
CT18ZNNLO PDF set, member #26, version 1; LHAPDF ID = 14126
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0027.dat
CT18ZNNLO PDF set, member #27, version 1; LHAPDF ID = 14127
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0028.dat
CT18ZNNLO PDF set, member #28, version 1; LHAPDF ID = 14128
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0029.dat
CT18ZNNLO PDF set, member #29, version 1; LHAPDF ID = 14129
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0030.dat
CT18ZNNLO PDF set, member #30, version 1; LHAPDF ID = 14130
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0031.dat
CT18ZNNLO PDF set, member #31, version 1; LHAPDF ID = 14131
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0032.dat
CT18ZNNLO PDF set, member #32, version 1; LHAPDF ID = 14132
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0033.dat
CT18ZNNLO PDF set, member #33, version 1; LHAPDF ID = 14133
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0034.dat
CT18ZNNLO PDF set, member #34, version 1; LHAPDF ID = 14134
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0035.dat
CT18ZNNLO PDF set, member #35, version 1; LHAPDF ID = 14135
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0036.dat
CT18ZNNLO PDF set, member #36, version 1; LHAPDF ID = 14136
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0037.dat
CT18ZNNLO PDF set, member #37, version 1; LHAPDF ID = 14137
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0038.dat
CT18ZNNLO PDF set, member #38, version 1; LHAPDF ID = 14138
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0039.dat
CT18ZNNLO PDF set, member #39, version 1; LHAPDF ID = 14139
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0040.dat
CT18ZNNLO PDF set, member #40, version 1; LHAPDF ID = 14140
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0041.dat
CT18ZNNLO PDF set, member #41, version 1; LHAPDF ID = 14141
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0042.dat
CT18ZNNLO PDF set, member #42, version 1; LHAPDF ID = 14142
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0043.dat
CT18ZNNLO PDF set, member #43, version 1; LHAPDF ID = 14143
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0044.dat
CT18ZNNLO PDF set, member #44, version 1; LHAPDF ID = 14144
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0045.dat
CT18ZNNLO PDF set, member #45, version 1; LHAPDF ID = 14145
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0046.dat
CT18ZNNLO PDF set, member #46, version 1; LHAPDF ID = 14146
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0047.dat
CT18ZNNLO PDF set, member #47, version 1; LHAPDF ID = 14147
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0048.dat
CT18ZNNLO PDF set, member #48, version 1; LHAPDF ID = 14148
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0049.dat
CT18ZNNLO PDF set, member #49, version 1; LHAPDF ID = 14149
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0050.dat
CT18ZNNLO PDF set, member #50, version 1; LHAPDF ID = 14150
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0051.dat
CT18ZNNLO PDF set, member #51, version 1; LHAPDF ID = 14151
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0052.dat
CT18ZNNLO PDF set, member #52, version 1; LHAPDF ID = 14152
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0053.dat
CT18ZNNLO PDF set, member #53, version 1; LHAPDF ID = 14153
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0054.dat
CT18ZNNLO PDF set, member #54, version 1; LHAPDF ID = 14154
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0055.dat
CT18ZNNLO PDF set, member #55, version 1; LHAPDF ID = 14155
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0056.dat
CT18ZNNLO PDF set, member #56, version 1; LHAPDF ID = 14156
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0057.dat
CT18ZNNLO PDF set, member #57, version 1; LHAPDF ID = 14157
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ZNNLO/CT18ZNNLO_0058.dat
CT18ZNNLO PDF set, member #58, version 1; LHAPDF ID = 14158
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18ANNLO/CT18ANNLO_0000.dat
CT18ANNLO PDF set, member #0, version 1; LHAPDF ID = 14200
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/CT18XNNLO/CT18XNNLO_0000.dat
CT18XNNLO PDF set, member #0, version 1; LHAPDF ID = 14300
  check: alpha_s(Mz)=  0.11800021884307436     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836823616052982     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0000.dat
MSHT20nnlo_as118 PDF set, member #0, version 3; LHAPDF ID = 27400
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0001.dat
MSHT20nnlo_as118 PDF set, member #1, version 3; LHAPDF ID = 27401
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0002.dat
MSHT20nnlo_as118 PDF set, member #2, version 3; LHAPDF ID = 27402
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0003.dat
MSHT20nnlo_as118 PDF set, member #3, version 3; LHAPDF ID = 27403
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0004.dat
MSHT20nnlo_as118 PDF set, member #4, version 3; LHAPDF ID = 27404
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0005.dat
MSHT20nnlo_as118 PDF set, member #5, version 3; LHAPDF ID = 27405
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0006.dat
MSHT20nnlo_as118 PDF set, member #6, version 3; LHAPDF ID = 27406
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0007.dat
MSHT20nnlo_as118 PDF set, member #7, version 3; LHAPDF ID = 27407
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0008.dat
MSHT20nnlo_as118 PDF set, member #8, version 3; LHAPDF ID = 27408
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0009.dat
MSHT20nnlo_as118 PDF set, member #9, version 3; LHAPDF ID = 27409
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0010.dat
MSHT20nnlo_as118 PDF set, member #10, version 3; LHAPDF ID = 27410
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0011.dat
MSHT20nnlo_as118 PDF set, member #11, version 3; LHAPDF ID = 27411
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0012.dat
MSHT20nnlo_as118 PDF set, member #12, version 3; LHAPDF ID = 27412
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0013.dat
MSHT20nnlo_as118 PDF set, member #13, version 3; LHAPDF ID = 27413
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0014.dat
MSHT20nnlo_as118 PDF set, member #14, version 3; LHAPDF ID = 27414
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0015.dat
MSHT20nnlo_as118 PDF set, member #15, version 3; LHAPDF ID = 27415
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0016.dat
MSHT20nnlo_as118 PDF set, member #16, version 3; LHAPDF ID = 27416
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0017.dat
MSHT20nnlo_as118 PDF set, member #17, version 3; LHAPDF ID = 27417
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0018.dat
MSHT20nnlo_as118 PDF set, member #18, version 3; LHAPDF ID = 27418
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0019.dat
MSHT20nnlo_as118 PDF set, member #19, version 3; LHAPDF ID = 27419
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0020.dat
MSHT20nnlo_as118 PDF set, member #20, version 3; LHAPDF ID = 27420
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0021.dat
MSHT20nnlo_as118 PDF set, member #21, version 3; LHAPDF ID = 27421
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0022.dat
MSHT20nnlo_as118 PDF set, member #22, version 3; LHAPDF ID = 27422
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0023.dat
MSHT20nnlo_as118 PDF set, member #23, version 3; LHAPDF ID = 27423
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0024.dat
MSHT20nnlo_as118 PDF set, member #24, version 3; LHAPDF ID = 27424
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0025.dat
MSHT20nnlo_as118 PDF set, member #25, version 3; LHAPDF ID = 27425
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0026.dat
MSHT20nnlo_as118 PDF set, member #26, version 3; LHAPDF ID = 27426
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0027.dat
MSHT20nnlo_as118 PDF set, member #27, version 3; LHAPDF ID = 27427
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0028.dat
MSHT20nnlo_as118 PDF set, member #28, version 3; LHAPDF ID = 27428
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0029.dat
MSHT20nnlo_as118 PDF set, member #29, version 3; LHAPDF ID = 27429
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0030.dat
MSHT20nnlo_as118 PDF set, member #30, version 3; LHAPDF ID = 27430
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0031.dat
MSHT20nnlo_as118 PDF set, member #31, version 3; LHAPDF ID = 27431
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0032.dat
MSHT20nnlo_as118 PDF set, member #32, version 3; LHAPDF ID = 27432
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0033.dat
MSHT20nnlo_as118 PDF set, member #33, version 3; LHAPDF ID = 27433
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0034.dat
MSHT20nnlo_as118 PDF set, member #34, version 3; LHAPDF ID = 27434
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0035.dat
MSHT20nnlo_as118 PDF set, member #35, version 3; LHAPDF ID = 27435
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0036.dat
MSHT20nnlo_as118 PDF set, member #36, version 3; LHAPDF ID = 27436
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0037.dat
MSHT20nnlo_as118 PDF set, member #37, version 3; LHAPDF ID = 27437
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0038.dat
MSHT20nnlo_as118 PDF set, member #38, version 3; LHAPDF ID = 27438
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0039.dat
MSHT20nnlo_as118 PDF set, member #39, version 3; LHAPDF ID = 27439
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0040.dat
MSHT20nnlo_as118 PDF set, member #40, version 3; LHAPDF ID = 27440
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0041.dat
MSHT20nnlo_as118 PDF set, member #41, version 3; LHAPDF ID = 27441
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0042.dat
MSHT20nnlo_as118 PDF set, member #42, version 3; LHAPDF ID = 27442
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0043.dat
MSHT20nnlo_as118 PDF set, member #43, version 3; LHAPDF ID = 27443
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0044.dat
MSHT20nnlo_as118 PDF set, member #44, version 3; LHAPDF ID = 27444
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0045.dat
MSHT20nnlo_as118 PDF set, member #45, version 3; LHAPDF ID = 27445
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0046.dat
MSHT20nnlo_as118 PDF set, member #46, version 3; LHAPDF ID = 27446
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0047.dat
MSHT20nnlo_as118 PDF set, member #47, version 3; LHAPDF ID = 27447
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0048.dat
MSHT20nnlo_as118 PDF set, member #48, version 3; LHAPDF ID = 27448
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0049.dat
MSHT20nnlo_as118 PDF set, member #49, version 3; LHAPDF ID = 27449
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0050.dat
MSHT20nnlo_as118 PDF set, member #50, version 3; LHAPDF ID = 27450
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0051.dat
MSHT20nnlo_as118 PDF set, member #51, version 3; LHAPDF ID = 27451
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0052.dat
MSHT20nnlo_as118 PDF set, member #52, version 3; LHAPDF ID = 27452
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0053.dat
MSHT20nnlo_as118 PDF set, member #53, version 3; LHAPDF ID = 27453
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0054.dat
MSHT20nnlo_as118 PDF set, member #54, version 3; LHAPDF ID = 27454
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0055.dat
MSHT20nnlo_as118 PDF set, member #55, version 3; LHAPDF ID = 27455
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0056.dat
MSHT20nnlo_as118 PDF set, member #56, version 3; LHAPDF ID = 27456
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0057.dat
MSHT20nnlo_as118 PDF set, member #57, version 3; LHAPDF ID = 27457
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0058.dat
MSHT20nnlo_as118 PDF set, member #58, version 3; LHAPDF ID = 27458
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0059.dat
MSHT20nnlo_as118 PDF set, member #59, version 3; LHAPDF ID = 27459
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0060.dat
MSHT20nnlo_as118 PDF set, member #60, version 3; LHAPDF ID = 27460
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0061.dat
MSHT20nnlo_as118 PDF set, member #61, version 3; LHAPDF ID = 27461
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0062.dat
MSHT20nnlo_as118 PDF set, member #62, version 3; LHAPDF ID = 27462
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0063.dat
MSHT20nnlo_as118 PDF set, member #63, version 3; LHAPDF ID = 27463
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as118/MSHT20nnlo_as118_0064.dat
MSHT20nnlo_as118 PDF set, member #64, version 3; LHAPDF ID = 27464
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as_smallrange/MSHT20nnlo_as_smallrange_0000.dat
MSHT20nnlo_as_smallrange PDF set, member #0, version 3; LHAPDF ID = 27500
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/MSHT20nnlo_as_largerange/MSHT20nnlo_as_largerange_0000.dat
MSHT20nnlo_as_largerange PDF set, member #0, version 1; LHAPDF ID = 27550
  check: alpha_s(Mz)=  0.11800072760577117     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20837418363593610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0000.dat
PDF4LHC21_40_pdfas PDF set, member #0, version 1; LHAPDF ID = 93300
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0001.dat
PDF4LHC21_40_pdfas PDF set, member #1, version 1; LHAPDF ID = 93301
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0002.dat
PDF4LHC21_40_pdfas PDF set, member #2, version 1; LHAPDF ID = 93302
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0003.dat
PDF4LHC21_40_pdfas PDF set, member #3, version 1; LHAPDF ID = 93303
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0004.dat
PDF4LHC21_40_pdfas PDF set, member #4, version 1; LHAPDF ID = 93304
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0005.dat
PDF4LHC21_40_pdfas PDF set, member #5, version 1; LHAPDF ID = 93305
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0006.dat
PDF4LHC21_40_pdfas PDF set, member #6, version 1; LHAPDF ID = 93306
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0007.dat
PDF4LHC21_40_pdfas PDF set, member #7, version 1; LHAPDF ID = 93307
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0008.dat
PDF4LHC21_40_pdfas PDF set, member #8, version 1; LHAPDF ID = 93308
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0009.dat
PDF4LHC21_40_pdfas PDF set, member #9, version 1; LHAPDF ID = 93309
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0010.dat
PDF4LHC21_40_pdfas PDF set, member #10, version 1; LHAPDF ID = 93310
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0011.dat
PDF4LHC21_40_pdfas PDF set, member #11, version 1; LHAPDF ID = 93311
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0012.dat
PDF4LHC21_40_pdfas PDF set, member #12, version 1; LHAPDF ID = 93312
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0013.dat
PDF4LHC21_40_pdfas PDF set, member #13, version 1; LHAPDF ID = 93313
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0014.dat
PDF4LHC21_40_pdfas PDF set, member #14, version 1; LHAPDF ID = 93314
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0015.dat
PDF4LHC21_40_pdfas PDF set, member #15, version 1; LHAPDF ID = 93315
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0016.dat
PDF4LHC21_40_pdfas PDF set, member #16, version 1; LHAPDF ID = 93316
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0017.dat
PDF4LHC21_40_pdfas PDF set, member #17, version 1; LHAPDF ID = 93317
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0018.dat
PDF4LHC21_40_pdfas PDF set, member #18, version 1; LHAPDF ID = 93318
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0019.dat
PDF4LHC21_40_pdfas PDF set, member #19, version 1; LHAPDF ID = 93319
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0020.dat
PDF4LHC21_40_pdfas PDF set, member #20, version 1; LHAPDF ID = 93320
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0021.dat
PDF4LHC21_40_pdfas PDF set, member #21, version 1; LHAPDF ID = 93321
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0022.dat
PDF4LHC21_40_pdfas PDF set, member #22, version 1; LHAPDF ID = 93322
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0023.dat
PDF4LHC21_40_pdfas PDF set, member #23, version 1; LHAPDF ID = 93323
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0024.dat
PDF4LHC21_40_pdfas PDF set, member #24, version 1; LHAPDF ID = 93324
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0025.dat
PDF4LHC21_40_pdfas PDF set, member #25, version 1; LHAPDF ID = 93325
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0026.dat
PDF4LHC21_40_pdfas PDF set, member #26, version 1; LHAPDF ID = 93326
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0027.dat
PDF4LHC21_40_pdfas PDF set, member #27, version 1; LHAPDF ID = 93327
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0028.dat
PDF4LHC21_40_pdfas PDF set, member #28, version 1; LHAPDF ID = 93328
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0029.dat
PDF4LHC21_40_pdfas PDF set, member #29, version 1; LHAPDF ID = 93329
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0030.dat
PDF4LHC21_40_pdfas PDF set, member #30, version 1; LHAPDF ID = 93330
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0031.dat
PDF4LHC21_40_pdfas PDF set, member #31, version 1; LHAPDF ID = 93331
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0032.dat
PDF4LHC21_40_pdfas PDF set, member #32, version 1; LHAPDF ID = 93332
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0033.dat
PDF4LHC21_40_pdfas PDF set, member #33, version 1; LHAPDF ID = 93333
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0034.dat
PDF4LHC21_40_pdfas PDF set, member #34, version 1; LHAPDF ID = 93334
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0035.dat
PDF4LHC21_40_pdfas PDF set, member #35, version 1; LHAPDF ID = 93335
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0036.dat
PDF4LHC21_40_pdfas PDF set, member #36, version 1; LHAPDF ID = 93336
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0037.dat
PDF4LHC21_40_pdfas PDF set, member #37, version 1; LHAPDF ID = 93337
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0038.dat
PDF4LHC21_40_pdfas PDF set, member #38, version 1; LHAPDF ID = 93338
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0039.dat
PDF4LHC21_40_pdfas PDF set, member #39, version 1; LHAPDF ID = 93339
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0040.dat
PDF4LHC21_40_pdfas PDF set, member #40, version 1; LHAPDF ID = 93340
  check: alpha_s(Mz)=  0.11800030173809385     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836920520174346     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0041.dat
PDF4LHC21_40_pdfas PDF set, member #41, version 1; LHAPDF ID = 93341
  check: alpha_s(Mz)=  0.11699999145854194     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.19690092092835307     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/PDF4LHC21_40_pdfas/PDF4LHC21_40_pdfas_0042.dat
PDF4LHC21_40_pdfas PDF set, member #42, version 1; LHAPDF ID = 93342
  check: alpha_s(Mz)=  0.11899990125307931     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.22028216479138857     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0000.dat
HERAPDF20_NNLO_EIG PDF set, member #0, version 1; LHAPDF ID = 61200
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0001.dat
HERAPDF20_NNLO_EIG PDF set, member #1, version 1; LHAPDF ID = 61201
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0002.dat
HERAPDF20_NNLO_EIG PDF set, member #2, version 1; LHAPDF ID = 61202
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0003.dat
HERAPDF20_NNLO_EIG PDF set, member #3, version 1; LHAPDF ID = 61203
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0004.dat
HERAPDF20_NNLO_EIG PDF set, member #4, version 1; LHAPDF ID = 61204
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0005.dat
HERAPDF20_NNLO_EIG PDF set, member #5, version 1; LHAPDF ID = 61205
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0006.dat
HERAPDF20_NNLO_EIG PDF set, member #6, version 1; LHAPDF ID = 61206
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0007.dat
HERAPDF20_NNLO_EIG PDF set, member #7, version 1; LHAPDF ID = 61207
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0008.dat
HERAPDF20_NNLO_EIG PDF set, member #8, version 1; LHAPDF ID = 61208
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0009.dat
HERAPDF20_NNLO_EIG PDF set, member #9, version 1; LHAPDF ID = 61209
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0010.dat
HERAPDF20_NNLO_EIG PDF set, member #10, version 1; LHAPDF ID = 61210
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0011.dat
HERAPDF20_NNLO_EIG PDF set, member #11, version 1; LHAPDF ID = 61211
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0012.dat
HERAPDF20_NNLO_EIG PDF set, member #12, version 1; LHAPDF ID = 61212
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0013.dat
HERAPDF20_NNLO_EIG PDF set, member #13, version 1; LHAPDF ID = 61213
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0014.dat
HERAPDF20_NNLO_EIG PDF set, member #14, version 1; LHAPDF ID = 61214
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0015.dat
HERAPDF20_NNLO_EIG PDF set, member #15, version 1; LHAPDF ID = 61215
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0016.dat
HERAPDF20_NNLO_EIG PDF set, member #16, version 1; LHAPDF ID = 61216
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0017.dat
HERAPDF20_NNLO_EIG PDF set, member #17, version 1; LHAPDF ID = 61217
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0018.dat
HERAPDF20_NNLO_EIG PDF set, member #18, version 1; LHAPDF ID = 61218
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0019.dat
HERAPDF20_NNLO_EIG PDF set, member #19, version 1; LHAPDF ID = 61219
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0020.dat
HERAPDF20_NNLO_EIG PDF set, member #20, version 1; LHAPDF ID = 61220
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0021.dat
HERAPDF20_NNLO_EIG PDF set, member #21, version 1; LHAPDF ID = 61221
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0022.dat
HERAPDF20_NNLO_EIG PDF set, member #22, version 1; LHAPDF ID = 61222
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0023.dat
HERAPDF20_NNLO_EIG PDF set, member #23, version 1; LHAPDF ID = 61223
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0024.dat
HERAPDF20_NNLO_EIG PDF set, member #24, version 1; LHAPDF ID = 61224
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0025.dat
HERAPDF20_NNLO_EIG PDF set, member #25, version 1; LHAPDF ID = 61225
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0026.dat
HERAPDF20_NNLO_EIG PDF set, member #26, version 1; LHAPDF ID = 61226
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0027.dat
HERAPDF20_NNLO_EIG PDF set, member #27, version 1; LHAPDF ID = 61227
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/HERAPDF20_NNLO_EIG/HERAPDF20_NNLO_EIG_0028.dat
HERAPDF20_NNLO_EIG PDF set, member #28, version 1; LHAPDF ID = 61228
  check: alpha_s(Mz)=  0.11799964494802981     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20836152742366901     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0000.dat
ABMP16als118_5_nnlo PDF set, member #0, version 1; LHAPDF ID = 42780
  check: alpha_s(Mz)=  0.11798450000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818453944094900     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0001.dat
ABMP16als118_5_nnlo PDF set, member #1, version 1; LHAPDF ID = 42781
  check: alpha_s(Mz)=  0.11797380000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20805955895701533     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0002.dat
ABMP16als118_5_nnlo PDF set, member #2, version 1; LHAPDF ID = 42782
  check: alpha_s(Mz)=  0.11798450000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818453944094900     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0003.dat
ABMP16als118_5_nnlo PDF set, member #3, version 1; LHAPDF ID = 42783
  check: alpha_s(Mz)=  0.11798430000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818220288160250     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0004.dat
ABMP16als118_5_nnlo PDF set, member #4, version 1; LHAPDF ID = 42784
  check: alpha_s(Mz)=  0.11798450000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818453944094900     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0005.dat
ABMP16als118_5_nnlo PDF set, member #5, version 1; LHAPDF ID = 42785
  check: alpha_s(Mz)=  0.11798450000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818453944094900     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0006.dat
ABMP16als118_5_nnlo PDF set, member #6, version 1; LHAPDF ID = 42786
  check: alpha_s(Mz)=  0.11798480000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818804431393792     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0007.dat
ABMP16als118_5_nnlo PDF set, member #7, version 1; LHAPDF ID = 42787
  check: alpha_s(Mz)=  0.11798470000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818687601841232     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0008.dat
ABMP16als118_5_nnlo PDF set, member #8, version 1; LHAPDF ID = 42788
  check: alpha_s(Mz)=  0.11798440000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818337115901087     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0009.dat
ABMP16als118_5_nnlo PDF set, member #9, version 1; LHAPDF ID = 42789
  check: alpha_s(Mz)=  0.11798450000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20818453944094900     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0010.dat
ABMP16als118_5_nnlo PDF set, member #10, version 1; LHAPDF ID = 42790
  check: alpha_s(Mz)=  0.11798390000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20817752981725932     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0011.dat
ABMP16als118_5_nnlo PDF set, member #11, version 1; LHAPDF ID = 42791
  check: alpha_s(Mz)=  0.11798699999999999     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20821374796140199     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0012.dat
ABMP16als118_5_nnlo PDF set, member #12, version 1; LHAPDF ID = 42792
  check: alpha_s(Mz)=  0.11798640000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20820673765832315     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0013.dat
ABMP16als118_5_nnlo PDF set, member #13, version 1; LHAPDF ID = 42793
  check: alpha_s(Mz)=  0.11795410000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20782959029126916     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0014.dat
ABMP16als118_5_nnlo PDF set, member #14, version 1; LHAPDF ID = 42794
  check: alpha_s(Mz)=  0.11798119999999999     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20814598852836361     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0015.dat
ABMP16als118_5_nnlo PDF set, member #15, version 1; LHAPDF ID = 42795
  check: alpha_s(Mz)=  0.11798030000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20813547549909217     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0016.dat
ABMP16als118_5_nnlo PDF set, member #16, version 1; LHAPDF ID = 42796
  check: alpha_s(Mz)=  0.11798530000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20819388585950338     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0017.dat
ABMP16als118_5_nnlo PDF set, member #17, version 1; LHAPDF ID = 42797
  check: alpha_s(Mz)=  0.11792200000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20745524610120386     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0018.dat
ABMP16als118_5_nnlo PDF set, member #18, version 1; LHAPDF ID = 42798
  check: alpha_s(Mz)=  0.11799809999999999     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20834346798170741     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0019.dat
ABMP16als118_5_nnlo PDF set, member #19, version 1; LHAPDF ID = 42799
  check: alpha_s(Mz)=  0.11797070000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20802335934449018     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0020.dat
ABMP16als118_5_nnlo PDF set, member #20, version 1; LHAPDF ID = 42800
  check: alpha_s(Mz)=  0.11799179999999999     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20826983625625878     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0021.dat
ABMP16als118_5_nnlo PDF set, member #21, version 1; LHAPDF ID = 42801
  check: alpha_s(Mz)=  0.11798220000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20815767010224692     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0022.dat
ABMP16als118_5_nnlo PDF set, member #22, version 1; LHAPDF ID = 42802
  check: alpha_s(Mz)=  0.11798800000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20822543216221862     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0023.dat
ABMP16als118_5_nnlo PDF set, member #23, version 1; LHAPDF ID = 42803
  check: alpha_s(Mz)=  0.11798560000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20819739084119368     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0024.dat
ABMP16als118_5_nnlo PDF set, member #24, version 1; LHAPDF ID = 42804
  check: alpha_s(Mz)=  0.11797420000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20806423019173989     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0025.dat
ABMP16als118_5_nnlo PDF set, member #25, version 1; LHAPDF ID = 42805
  check: alpha_s(Mz)=  0.11798090000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20814248414451342     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0026.dat
ABMP16als118_5_nnlo PDF set, member #26, version 1; LHAPDF ID = 42806
  check: alpha_s(Mz)=  0.11798570000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20819855917748220     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0027.dat
ABMP16als118_5_nnlo PDF set, member #27, version 1; LHAPDF ID = 42807
  check: alpha_s(Mz)=  0.11798880000000000     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20823477984899302     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0028.dat
ABMP16als118_5_nnlo PDF set, member #28, version 1; LHAPDF ID = 42808
  check: alpha_s(Mz)=  0.11798260000000001     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20816234285861179     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/ABMP16als118_5_nnlo/ABMP16als118_5_nnlo_0029.dat
ABMP16als118_5_nnlo PDF set, member #29, version 1; LHAPDF ID = 42809
  check: alpha_s(Mz)=  0.11799759999999999     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20833762353711188     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0000.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #0, version 1; LHAPDF ID = 316200
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0001.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #1, version 1; LHAPDF ID = 316201
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0002.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #2, version 1; LHAPDF ID = 316202
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0003.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #3, version 1; LHAPDF ID = 316203
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0004.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #4, version 1; LHAPDF ID = 316204
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0005.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #5, version 1; LHAPDF ID = 316205
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0006.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #6, version 1; LHAPDF ID = 316206
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0007.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #7, version 1; LHAPDF ID = 316207
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0008.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #8, version 1; LHAPDF ID = 316208
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0009.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #9, version 1; LHAPDF ID = 316209
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0010.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #10, version 1; LHAPDF ID = 316210
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0011.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #11, version 1; LHAPDF ID = 316211
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0012.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #12, version 1; LHAPDF ID = 316212
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0013.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #13, version 1; LHAPDF ID = 316213
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0014.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #14, version 1; LHAPDF ID = 316214
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0015.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #15, version 1; LHAPDF ID = 316215
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0016.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #16, version 1; LHAPDF ID = 316216
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0017.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #17, version 1; LHAPDF ID = 316217
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0018.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #18, version 1; LHAPDF ID = 316218
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0019.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #19, version 1; LHAPDF ID = 316219
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0020.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #20, version 1; LHAPDF ID = 316220
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0021.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #21, version 1; LHAPDF ID = 316221
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0022.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #22, version 1; LHAPDF ID = 316222
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0023.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #23, version 1; LHAPDF ID = 316223
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0024.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #24, version 1; LHAPDF ID = 316224
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0025.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #25, version 1; LHAPDF ID = 316225
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0026.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #26, version 1; LHAPDF ID = 316226
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0027.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #27, version 1; LHAPDF ID = 316227
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0028.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #28, version 1; LHAPDF ID = 316228
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0029.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #29, version 1; LHAPDF ID = 316229
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0030.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #30, version 1; LHAPDF ID = 316230
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0031.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #31, version 1; LHAPDF ID = 316231
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0032.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #32, version 1; LHAPDF ID = 316232
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0033.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #33, version 1; LHAPDF ID = 316233
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0034.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #34, version 1; LHAPDF ID = 316234
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0035.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #35, version 1; LHAPDF ID = 316235
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0036.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #36, version 1; LHAPDF ID = 316236
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0037.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #37, version 1; LHAPDF ID = 316237
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0038.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #38, version 1; LHAPDF ID = 316238
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0039.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #39, version 1; LHAPDF ID = 316239
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0040.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #40, version 1; LHAPDF ID = 316240
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0041.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #41, version 1; LHAPDF ID = 316241
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0042.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #42, version 1; LHAPDF ID = 316242
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0043.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #43, version 1; LHAPDF ID = 316243
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0044.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #44, version 1; LHAPDF ID = 316244
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0045.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #45, version 1; LHAPDF ID = 316245
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0046.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #46, version 1; LHAPDF ID = 316246
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0047.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #47, version 1; LHAPDF ID = 316247
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0048.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #48, version 1; LHAPDF ID = 316248
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0049.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #49, version 1; LHAPDF ID = 316249
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0050.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #50, version 1; LHAPDF ID = 316250
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0051.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #51, version 1; LHAPDF ID = 316251
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0052.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #52, version 1; LHAPDF ID = 316252
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0053.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #53, version 1; LHAPDF ID = 316253
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0054.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #54, version 1; LHAPDF ID = 316254
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0055.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #55, version 1; LHAPDF ID = 316255
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0056.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #56, version 1; LHAPDF ID = 316256
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0057.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #57, version 1; LHAPDF ID = 316257
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0058.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #58, version 1; LHAPDF ID = 316258
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0059.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #59, version 1; LHAPDF ID = 316259
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0060.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #60, version 1; LHAPDF ID = 316260
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0061.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #61, version 1; LHAPDF ID = 316261
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0062.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #62, version 1; LHAPDF ID = 316262
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0063.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #63, version 1; LHAPDF ID = 316263
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0064.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #64, version 1; LHAPDF ID = 316264
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0065.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #65, version 1; LHAPDF ID = 316265
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0066.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #66, version 1; LHAPDF ID = 316266
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0067.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #67, version 1; LHAPDF ID = 316267
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0068.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #68, version 1; LHAPDF ID = 316268
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0069.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #69, version 1; LHAPDF ID = 316269
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0070.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #70, version 1; LHAPDF ID = 316270
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0071.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #71, version 1; LHAPDF ID = 316271
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0072.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #72, version 1; LHAPDF ID = 316272
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0073.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #73, version 1; LHAPDF ID = 316273
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0074.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #74, version 1; LHAPDF ID = 316274
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0075.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #75, version 1; LHAPDF ID = 316275
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0076.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #76, version 1; LHAPDF ID = 316276
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0077.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #77, version 1; LHAPDF ID = 316277
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0078.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #78, version 1; LHAPDF ID = 316278
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0079.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #79, version 1; LHAPDF ID = 316279
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0080.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #80, version 1; LHAPDF ID = 316280
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0081.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #81, version 1; LHAPDF ID = 316281
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0082.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #82, version 1; LHAPDF ID = 316282
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0083.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #83, version 1; LHAPDF ID = 316283
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0084.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #84, version 1; LHAPDF ID = 316284
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0085.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #85, version 1; LHAPDF ID = 316285
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0086.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #86, version 1; LHAPDF ID = 316286
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0087.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #87, version 1; LHAPDF ID = 316287
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0088.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #88, version 1; LHAPDF ID = 316288
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0089.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #89, version 1; LHAPDF ID = 316289
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0090.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #90, version 1; LHAPDF ID = 316290
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0091.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #91, version 1; LHAPDF ID = 316291
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0092.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #92, version 1; LHAPDF ID = 316292
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0093.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #93, version 1; LHAPDF ID = 316293
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0094.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #94, version 1; LHAPDF ID = 316294
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0095.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #95, version 1; LHAPDF ID = 316295
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0096.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #96, version 1; LHAPDF ID = 316296
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0097.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #97, version 1; LHAPDF ID = 316297
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0098.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #98, version 1; LHAPDF ID = 316298
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0099.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #99, version 1; LHAPDF ID = 316299
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118_mc/NNPDF31_nnlo_as_0118_mc_0100.dat
NNPDF31_nnlo_as_0118_mc PDF set, member #100, version 1; LHAPDF ID = 316300
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0000.dat
NNPDF40_nnlo_pdfas PDF set, member #0, version 1; LHAPDF ID = 331300
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0001.dat
NNPDF40_nnlo_pdfas PDF set, member #1, version 1; LHAPDF ID = 331301
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0002.dat
NNPDF40_nnlo_pdfas PDF set, member #2, version 1; LHAPDF ID = 331302
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0003.dat
NNPDF40_nnlo_pdfas PDF set, member #3, version 1; LHAPDF ID = 331303
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0004.dat
NNPDF40_nnlo_pdfas PDF set, member #4, version 1; LHAPDF ID = 331304
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0005.dat
NNPDF40_nnlo_pdfas PDF set, member #5, version 1; LHAPDF ID = 331305
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0006.dat
NNPDF40_nnlo_pdfas PDF set, member #6, version 1; LHAPDF ID = 331306
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0007.dat
NNPDF40_nnlo_pdfas PDF set, member #7, version 1; LHAPDF ID = 331307
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0008.dat
NNPDF40_nnlo_pdfas PDF set, member #8, version 1; LHAPDF ID = 331308
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0009.dat
NNPDF40_nnlo_pdfas PDF set, member #9, version 1; LHAPDF ID = 331309
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0010.dat
NNPDF40_nnlo_pdfas PDF set, member #10, version 1; LHAPDF ID = 331310
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0011.dat
NNPDF40_nnlo_pdfas PDF set, member #11, version 1; LHAPDF ID = 331311
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0012.dat
NNPDF40_nnlo_pdfas PDF set, member #12, version 1; LHAPDF ID = 331312
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0013.dat
NNPDF40_nnlo_pdfas PDF set, member #13, version 1; LHAPDF ID = 331313
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0014.dat
NNPDF40_nnlo_pdfas PDF set, member #14, version 1; LHAPDF ID = 331314
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0015.dat
NNPDF40_nnlo_pdfas PDF set, member #15, version 1; LHAPDF ID = 331315
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0016.dat
NNPDF40_nnlo_pdfas PDF set, member #16, version 1; LHAPDF ID = 331316
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0017.dat
NNPDF40_nnlo_pdfas PDF set, member #17, version 1; LHAPDF ID = 331317
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0018.dat
NNPDF40_nnlo_pdfas PDF set, member #18, version 1; LHAPDF ID = 331318
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0019.dat
NNPDF40_nnlo_pdfas PDF set, member #19, version 1; LHAPDF ID = 331319
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0020.dat
NNPDF40_nnlo_pdfas PDF set, member #20, version 1; LHAPDF ID = 331320
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0021.dat
NNPDF40_nnlo_pdfas PDF set, member #21, version 1; LHAPDF ID = 331321
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0022.dat
NNPDF40_nnlo_pdfas PDF set, member #22, version 1; LHAPDF ID = 331322
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0023.dat
NNPDF40_nnlo_pdfas PDF set, member #23, version 1; LHAPDF ID = 331323
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0024.dat
NNPDF40_nnlo_pdfas PDF set, member #24, version 1; LHAPDF ID = 331324
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0025.dat
NNPDF40_nnlo_pdfas PDF set, member #25, version 1; LHAPDF ID = 331325
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0026.dat
NNPDF40_nnlo_pdfas PDF set, member #26, version 1; LHAPDF ID = 331326
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0027.dat
NNPDF40_nnlo_pdfas PDF set, member #27, version 1; LHAPDF ID = 331327
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0028.dat
NNPDF40_nnlo_pdfas PDF set, member #28, version 1; LHAPDF ID = 331328
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0029.dat
NNPDF40_nnlo_pdfas PDF set, member #29, version 1; LHAPDF ID = 331329
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0030.dat
NNPDF40_nnlo_pdfas PDF set, member #30, version 1; LHAPDF ID = 331330
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0031.dat
NNPDF40_nnlo_pdfas PDF set, member #31, version 1; LHAPDF ID = 331331
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0032.dat
NNPDF40_nnlo_pdfas PDF set, member #32, version 1; LHAPDF ID = 331332
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0033.dat
NNPDF40_nnlo_pdfas PDF set, member #33, version 1; LHAPDF ID = 331333
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0034.dat
NNPDF40_nnlo_pdfas PDF set, member #34, version 1; LHAPDF ID = 331334
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0035.dat
NNPDF40_nnlo_pdfas PDF set, member #35, version 1; LHAPDF ID = 331335
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0036.dat
NNPDF40_nnlo_pdfas PDF set, member #36, version 1; LHAPDF ID = 331336
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0037.dat
NNPDF40_nnlo_pdfas PDF set, member #37, version 1; LHAPDF ID = 331337
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0038.dat
NNPDF40_nnlo_pdfas PDF set, member #38, version 1; LHAPDF ID = 331338
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0039.dat
NNPDF40_nnlo_pdfas PDF set, member #39, version 1; LHAPDF ID = 331339
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0040.dat
NNPDF40_nnlo_pdfas PDF set, member #40, version 1; LHAPDF ID = 331340
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0041.dat
NNPDF40_nnlo_pdfas PDF set, member #41, version 1; LHAPDF ID = 331341
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0042.dat
NNPDF40_nnlo_pdfas PDF set, member #42, version 1; LHAPDF ID = 331342
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0043.dat
NNPDF40_nnlo_pdfas PDF set, member #43, version 1; LHAPDF ID = 331343
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0044.dat
NNPDF40_nnlo_pdfas PDF set, member #44, version 1; LHAPDF ID = 331344
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0045.dat
NNPDF40_nnlo_pdfas PDF set, member #45, version 1; LHAPDF ID = 331345
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0046.dat
NNPDF40_nnlo_pdfas PDF set, member #46, version 1; LHAPDF ID = 331346
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0047.dat
NNPDF40_nnlo_pdfas PDF set, member #47, version 1; LHAPDF ID = 331347
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0048.dat
NNPDF40_nnlo_pdfas PDF set, member #48, version 1; LHAPDF ID = 331348
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0049.dat
NNPDF40_nnlo_pdfas PDF set, member #49, version 1; LHAPDF ID = 331349
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0050.dat
NNPDF40_nnlo_pdfas PDF set, member #50, version 1; LHAPDF ID = 331350
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0051.dat
NNPDF40_nnlo_pdfas PDF set, member #51, version 1; LHAPDF ID = 331351
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0052.dat
NNPDF40_nnlo_pdfas PDF set, member #52, version 1; LHAPDF ID = 331352
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0053.dat
NNPDF40_nnlo_pdfas PDF set, member #53, version 1; LHAPDF ID = 331353
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0054.dat
NNPDF40_nnlo_pdfas PDF set, member #54, version 1; LHAPDF ID = 331354
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0055.dat
NNPDF40_nnlo_pdfas PDF set, member #55, version 1; LHAPDF ID = 331355
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0056.dat
NNPDF40_nnlo_pdfas PDF set, member #56, version 1; LHAPDF ID = 331356
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0057.dat
NNPDF40_nnlo_pdfas PDF set, member #57, version 1; LHAPDF ID = 331357
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0058.dat
NNPDF40_nnlo_pdfas PDF set, member #58, version 1; LHAPDF ID = 331358
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0059.dat
NNPDF40_nnlo_pdfas PDF set, member #59, version 1; LHAPDF ID = 331359
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0060.dat
NNPDF40_nnlo_pdfas PDF set, member #60, version 1; LHAPDF ID = 331360
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0061.dat
NNPDF40_nnlo_pdfas PDF set, member #61, version 1; LHAPDF ID = 331361
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0062.dat
NNPDF40_nnlo_pdfas PDF set, member #62, version 1; LHAPDF ID = 331362
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0063.dat
NNPDF40_nnlo_pdfas PDF set, member #63, version 1; LHAPDF ID = 331363
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0064.dat
NNPDF40_nnlo_pdfas PDF set, member #64, version 1; LHAPDF ID = 331364
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0065.dat
NNPDF40_nnlo_pdfas PDF set, member #65, version 1; LHAPDF ID = 331365
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0066.dat
NNPDF40_nnlo_pdfas PDF set, member #66, version 1; LHAPDF ID = 331366
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0067.dat
NNPDF40_nnlo_pdfas PDF set, member #67, version 1; LHAPDF ID = 331367
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0068.dat
NNPDF40_nnlo_pdfas PDF set, member #68, version 1; LHAPDF ID = 331368
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0069.dat
NNPDF40_nnlo_pdfas PDF set, member #69, version 1; LHAPDF ID = 331369
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0070.dat
NNPDF40_nnlo_pdfas PDF set, member #70, version 1; LHAPDF ID = 331370
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0071.dat
NNPDF40_nnlo_pdfas PDF set, member #71, version 1; LHAPDF ID = 331371
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0072.dat
NNPDF40_nnlo_pdfas PDF set, member #72, version 1; LHAPDF ID = 331372
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0073.dat
NNPDF40_nnlo_pdfas PDF set, member #73, version 1; LHAPDF ID = 331373
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0074.dat
NNPDF40_nnlo_pdfas PDF set, member #74, version 1; LHAPDF ID = 331374
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0075.dat
NNPDF40_nnlo_pdfas PDF set, member #75, version 1; LHAPDF ID = 331375
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0076.dat
NNPDF40_nnlo_pdfas PDF set, member #76, version 1; LHAPDF ID = 331376
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0077.dat
NNPDF40_nnlo_pdfas PDF set, member #77, version 1; LHAPDF ID = 331377
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0078.dat
NNPDF40_nnlo_pdfas PDF set, member #78, version 1; LHAPDF ID = 331378
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0079.dat
NNPDF40_nnlo_pdfas PDF set, member #79, version 1; LHAPDF ID = 331379
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0080.dat
NNPDF40_nnlo_pdfas PDF set, member #80, version 1; LHAPDF ID = 331380
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0081.dat
NNPDF40_nnlo_pdfas PDF set, member #81, version 1; LHAPDF ID = 331381
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0082.dat
NNPDF40_nnlo_pdfas PDF set, member #82, version 1; LHAPDF ID = 331382
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0083.dat
NNPDF40_nnlo_pdfas PDF set, member #83, version 1; LHAPDF ID = 331383
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0084.dat
NNPDF40_nnlo_pdfas PDF set, member #84, version 1; LHAPDF ID = 331384
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0085.dat
NNPDF40_nnlo_pdfas PDF set, member #85, version 1; LHAPDF ID = 331385
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0086.dat
NNPDF40_nnlo_pdfas PDF set, member #86, version 1; LHAPDF ID = 331386
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0087.dat
NNPDF40_nnlo_pdfas PDF set, member #87, version 1; LHAPDF ID = 331387
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0088.dat
NNPDF40_nnlo_pdfas PDF set, member #88, version 1; LHAPDF ID = 331388
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0089.dat
NNPDF40_nnlo_pdfas PDF set, member #89, version 1; LHAPDF ID = 331389
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0090.dat
NNPDF40_nnlo_pdfas PDF set, member #90, version 1; LHAPDF ID = 331390
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0091.dat
NNPDF40_nnlo_pdfas PDF set, member #91, version 1; LHAPDF ID = 331391
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0092.dat
NNPDF40_nnlo_pdfas PDF set, member #92, version 1; LHAPDF ID = 331392
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0093.dat
NNPDF40_nnlo_pdfas PDF set, member #93, version 1; LHAPDF ID = 331393
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0094.dat
NNPDF40_nnlo_pdfas PDF set, member #94, version 1; LHAPDF ID = 331394
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0095.dat
NNPDF40_nnlo_pdfas PDF set, member #95, version 1; LHAPDF ID = 331395
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0096.dat
NNPDF40_nnlo_pdfas PDF set, member #96, version 1; LHAPDF ID = 331396
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0097.dat
NNPDF40_nnlo_pdfas PDF set, member #97, version 1; LHAPDF ID = 331397
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0098.dat
NNPDF40_nnlo_pdfas PDF set, member #98, version 1; LHAPDF ID = 331398
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0099.dat
NNPDF40_nnlo_pdfas PDF set, member #99, version 1; LHAPDF ID = 331399
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0100.dat
NNPDF40_nnlo_pdfas PDF set, member #100, version 1; LHAPDF ID = 331400
  check: alpha_s(Mz)=  0.11800215829284905     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839090910744684     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0101.dat
NNPDF40_nnlo_pdfas PDF set, member #101, version 1; LHAPDF ID = 331401
  check: alpha_s(Mz)=  0.11700212910978669     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.19692495081382516     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pdfas/NNPDF40_nnlo_pdfas_0102.dat
NNPDF40_nnlo_pdfas PDF set, member #102, version 1; LHAPDF ID = 331402
  check: alpha_s(Mz)=  0.11900219136857998     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.22030998348098008     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0000.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #0, version 1; LHAPDF ID = 332100
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0001.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #1, version 1; LHAPDF ID = 332101
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0002.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #2, version 1; LHAPDF ID = 332102
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0003.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #3, version 1; LHAPDF ID = 332103
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0004.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #4, version 1; LHAPDF ID = 332104
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0005.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #5, version 1; LHAPDF ID = 332105
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0006.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #6, version 1; LHAPDF ID = 332106
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0007.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #7, version 1; LHAPDF ID = 332107
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0008.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #8, version 1; LHAPDF ID = 332108
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0009.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #9, version 1; LHAPDF ID = 332109
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0010.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #10, version 1; LHAPDF ID = 332110
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0011.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #11, version 1; LHAPDF ID = 332111
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0012.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #12, version 1; LHAPDF ID = 332112
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0013.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #13, version 1; LHAPDF ID = 332113
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0014.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #14, version 1; LHAPDF ID = 332114
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0015.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #15, version 1; LHAPDF ID = 332115
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0016.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #16, version 1; LHAPDF ID = 332116
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0017.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #17, version 1; LHAPDF ID = 332117
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0018.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #18, version 1; LHAPDF ID = 332118
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0019.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #19, version 1; LHAPDF ID = 332119
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0020.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #20, version 1; LHAPDF ID = 332120
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0021.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #21, version 1; LHAPDF ID = 332121
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0022.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #22, version 1; LHAPDF ID = 332122
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0023.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #23, version 1; LHAPDF ID = 332123
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0024.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #24, version 1; LHAPDF ID = 332124
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0025.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #25, version 1; LHAPDF ID = 332125
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0026.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #26, version 1; LHAPDF ID = 332126
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0027.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #27, version 1; LHAPDF ID = 332127
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0028.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #28, version 1; LHAPDF ID = 332128
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0029.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #29, version 1; LHAPDF ID = 332129
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0030.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #30, version 1; LHAPDF ID = 332130
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0031.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #31, version 1; LHAPDF ID = 332131
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0032.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #32, version 1; LHAPDF ID = 332132
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0033.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #33, version 1; LHAPDF ID = 332133
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0034.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #34, version 1; LHAPDF ID = 332134
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0035.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #35, version 1; LHAPDF ID = 332135
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0036.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #36, version 1; LHAPDF ID = 332136
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0037.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #37, version 1; LHAPDF ID = 332137
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0038.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #38, version 1; LHAPDF ID = 332138
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0039.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #39, version 1; LHAPDF ID = 332139
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0040.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #40, version 1; LHAPDF ID = 332140
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0041.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #41, version 1; LHAPDF ID = 332141
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0042.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #42, version 1; LHAPDF ID = 332142
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0043.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #43, version 1; LHAPDF ID = 332143
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0044.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #44, version 1; LHAPDF ID = 332144
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0045.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #45, version 1; LHAPDF ID = 332145
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0046.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #46, version 1; LHAPDF ID = 332146
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0047.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #47, version 1; LHAPDF ID = 332147
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0048.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #48, version 1; LHAPDF ID = 332148
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0049.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #49, version 1; LHAPDF ID = 332149
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0050.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #50, version 1; LHAPDF ID = 332150
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0051.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #51, version 1; LHAPDF ID = 332151
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0052.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #52, version 1; LHAPDF ID = 332152
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0053.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #53, version 1; LHAPDF ID = 332153
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0054.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #54, version 1; LHAPDF ID = 332154
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0055.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #55, version 1; LHAPDF ID = 332155
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0056.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #56, version 1; LHAPDF ID = 332156
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0057.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #57, version 1; LHAPDF ID = 332157
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0058.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #58, version 1; LHAPDF ID = 332158
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0059.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #59, version 1; LHAPDF ID = 332159
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0060.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #60, version 1; LHAPDF ID = 332160
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0061.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #61, version 1; LHAPDF ID = 332161
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0062.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #62, version 1; LHAPDF ID = 332162
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0063.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #63, version 1; LHAPDF ID = 332163
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0064.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #64, version 1; LHAPDF ID = 332164
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0065.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #65, version 1; LHAPDF ID = 332165
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0066.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #66, version 1; LHAPDF ID = 332166
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0067.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #67, version 1; LHAPDF ID = 332167
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0068.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #68, version 1; LHAPDF ID = 332168
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0069.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #69, version 1; LHAPDF ID = 332169
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0070.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #70, version 1; LHAPDF ID = 332170
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0071.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #71, version 1; LHAPDF ID = 332171
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0072.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #72, version 1; LHAPDF ID = 332172
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0073.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #73, version 1; LHAPDF ID = 332173
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0074.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #74, version 1; LHAPDF ID = 332174
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0075.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #75, version 1; LHAPDF ID = 332175
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0076.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #76, version 1; LHAPDF ID = 332176
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0077.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #77, version 1; LHAPDF ID = 332177
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0078.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #78, version 1; LHAPDF ID = 332178
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0079.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #79, version 1; LHAPDF ID = 332179
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0080.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #80, version 1; LHAPDF ID = 332180
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0081.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #81, version 1; LHAPDF ID = 332181
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0082.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #82, version 1; LHAPDF ID = 332182
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0083.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #83, version 1; LHAPDF ID = 332183
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0084.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #84, version 1; LHAPDF ID = 332184
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0085.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #85, version 1; LHAPDF ID = 332185
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0086.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #86, version 1; LHAPDF ID = 332186
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0087.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #87, version 1; LHAPDF ID = 332187
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0088.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #88, version 1; LHAPDF ID = 332188
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0089.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #89, version 1; LHAPDF ID = 332189
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0090.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #90, version 1; LHAPDF ID = 332190
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0091.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #91, version 1; LHAPDF ID = 332191
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0092.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #92, version 1; LHAPDF ID = 332192
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0093.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #93, version 1; LHAPDF ID = 332193
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0094.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #94, version 1; LHAPDF ID = 332194
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0095.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #95, version 1; LHAPDF ID = 332195
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0096.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #96, version 1; LHAPDF ID = 332196
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0097.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #97, version 1; LHAPDF ID = 332197
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0098.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #98, version 1; LHAPDF ID = 332198
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0099.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #99, version 1; LHAPDF ID = 332199
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF40_nnlo_pch_as_01180/NNPDF40_nnlo_pch_as_01180_0100.dat
NNPDF40_nnlo_pch_as_01180 PDF set, member #100, version 1; LHAPDF ID = 332200
  check: alpha_s(Mz)=  0.11800267099667515     
  alpha_s order (0,1,2):            2
  Lambda 5 is   0.20839690310591610     
 RM48 INITIALIZED:    234567         547         0
 RM48IN SKIPPING OVER             547
 powheginput WARNING: unused variable ncall1              
 powheginput WARNING: unused variable itmx1               
 powheginput WARNING: unused variable ncall2              
 powheginput WARNING: unused variable itmx2               
 powheginput WARNING: unused variable masswindow          
Thanks for using LHAPDF 6.4.0. Please make sure to cite the paper:
  Eur.Phys.J. C75 (2015) 3, 132  (http://arxiv.org/abs/1412.7420)

 finished computing weights ..

-rw-r--r--. 1 dshekar zh 344988 May 21 03:32 cmsgrid_final.lhe
/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/mcSampleProdScripts_newx509/step2/temp_debug/CMSSW_13_0_13/src/thread0/lheevent/powhegbox_VBF_H
Output ready with cmsgrid_final.lhe at /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/mcSampleProdScripts_newx509/step2/temp_debug/CMSSW_13_0_13/src/thread0/lheevent
End of job on  Wed May 21 03:32:05 CEST 2025
21-May-2025 03:32:06 CEST  Initiating request to open LHE file thread0/cmsgrid_final.lhe
21-May-2025 03:32:06 CEST  Successfully opened LHE file thread0/cmsgrid_final.lhe
21-May-2025 03:32:06 CEST  Initiating request to open LHE file thread0/cmsgrid_final.lhe
21-May-2025 03:32:06 CEST  Successfully opened LHE file thread0/cmsgrid_final.lhe
%MSG-w LogicError:  Pythia8ConcurrentHadronizerFilter:generator@beginLumi  21-May-2025 03:32:06 CEST Run: 1 Lumi: 1
::getByLabel: An attempt was made to read a Run product before endRun() was called.
The product is of type 'LHERunInfoProduct'.
The specified ModuleLabel was 'externalLHEProducer'.
The specified productInstanceName was ''.

%MSG

 *------------------------------------------------------------------------------------* 
 |                                                                                    | 
 |  *------------------------------------------------------------------------------*  | 
 |  |                                                                              |  | 
 |  |                                                                              |  | 
 |  |   PPP   Y   Y  TTTTT  H   H  III    A      Welcome to the Lund Monte Carlo!  |  | 
 |  |   P  P   Y Y     T    H   H   I    A A     This is PYTHIA version 8.306      |  | 
 |  |   PPP     Y      T    HHHHH   I   AAAAA    Last date of change: 28 Jun 2021  |  | 
 |  |   P       Y      T    H   H   I   A   A                                      |  | 
 |  |   P       Y      T    H   H  III  A   A    Now is 21 May 2025 at 03:32:06    |  | 
 |  |                                                                              |  | 
 |  |   Program documentation and an archive of historic versions is found on:     |  | 
 |  |                                                                              |  | 
 |  |                               https://pythia.org/                            |  | 
 |  |                                                                              |  | 
 |  |   PYTHIA is authored by a collaboration consisting of:                       |  | 
 |  |                                                                              |  | 
 |  |   Christian Bierlich, Nishita Desai, Leif Gellersen, Ilkka Helenius, Philip  |  | 
 |  |   Ilten, Leif Lönnblad, Stephen Mrenna, Stefan Prestel, Christian Preuss,    |  | 
 |  |   Torbjörn Sjöstrand, Peter Skands, Marius Utheim and Rob Verheyen.          |  | 
 |  |                                                                              |  | 
 |  |   The complete list of authors, including contact information and            |  | 
 |  |   affiliations, can be found on https://pythia.org/.                         |  | 
 |  |   Problems or bugs should be reported on email at authors@pythia.org.        |  | 
 |  |                                                                              |  | 
 |  |   The main program reference is 'An Introduction to PYTHIA 8.2',             |  | 
 |  |   T. Sjöstrand et al, Comput. Phys. Commun. 191 (2015) 159                   |  | 
 |  |   [arXiv:1410.3012 [hep-ph]]                                                 |  | 
 |  |                                                                              |  | 
 |  |   The main physics reference is the 'PYTHIA 6.4 Physics and Manual',         |  | 
 |  |   T. Sjöstrand, S. Mrenna and P. Skands, JHEP05 (2006) 026 [hep-ph/0603175]  |  | 
 |  |                                                                              |  | 
 |  |   PYTHIA is released under the GNU General Public Licence version 2 or later.|  | 
 |  |   Please respect the MCnet Guidelines for Event Generator Authors and Users. |  | 
 |  |                                                                              |  | 
 |  |   Disclaimer: this program comes without any guarantees.                     |  | 
 |  |   Beware of errors and use common sense when interpreting results.           |  | 
 |  |                                                                              |  | 
 |  |   Copyright (C) 2021 Torbjörn Sjöstrand                                      |  | 
 |  |                                                                              |  | 
 |  |                                                                              |  | 
 |  *------------------------------------------------------------------------------*  | 
 |                                                                                    | 
 *------------------------------------------------------------------------------------* 


 *------------------------------------------------------------------------------------* 
 |                                                                                    | 
 |  *------------------------------------------------------------------------------*  | 
 |  |                                                                              |  | 
 |  |                                                                              |  | 
 |  |   PPP   Y   Y  TTTTT  H   H  III    A      Welcome to the Lund Monte Carlo!  |  | 
 |  |   P  P   Y Y     T    H   H   I    A A     This is PYTHIA version 8.306      |  | 
 |  |   PPP     Y      T    HHHHH   I   AAAAA    Last date of change: 28 Jun 2021  |  | 
 |  |   P       Y      T    H   H   I   A   A                                      |  | 
 |  |   P       Y      T    H   H  III  A   A    Now is 21 May 2025 at 03:32:07    |  | 
 |  |                                                                              |  | 
 |  |   Program documentation and an archive of historic versions is found on:     |  | 
 |  |                                                                              |  | 
 |  |                               https://pythia.org/                            |  | 
 |  |                                                                              |  | 
 |  |   PYTHIA is authored by a collaboration consisting of:                       |  | 
 |  |                                                                              |  | 
 |  |   Christian Bierlich, Nishita Desai, Leif Gellersen, Ilkka Helenius, Philip  |  | 
 |  |   Ilten, Leif Lönnblad, Stephen Mrenna, Stefan Prestel, Christian Preuss,    |  | 
 |  |   Torbjörn Sjöstrand, Peter Skands, Marius Utheim and Rob Verheyen.          |  | 
 |  |                                                                              |  | 
 |  |   The complete list of authors, including contact information and            |  | 
 |  |   affiliations, can be found on https://pythia.org/.                         |  | 
 |  |   Problems or bugs should be reported on email at authors@pythia.org.        |  | 
 |  |                                                                              |  | 
 |  |   The main program reference is 'An Introduction to PYTHIA 8.2',             |  | 
 |  |   T. Sjöstrand et al, Comput. Phys. Commun. 191 (2015) 159                   |  | 
 |  |   [arXiv:1410.3012 [hep-ph]]                                                 |  | 
 |  |                                                                              |  | 
 |  |   The main physics reference is the 'PYTHIA 6.4 Physics and Manual',         |  | 
 |  |   T. Sjöstrand, S. Mrenna and P. Skands, JHEP05 (2006) 026 [hep-ph/0603175]  |  | 
 |  |                                                                              |  | 
 |  |   PYTHIA is released under the GNU General Public Licence version 2 or later.|  | 
 |  |   Please respect the MCnet Guidelines for Event Generator Authors and Users. |  | 
 |  |                                                                              |  | 
 |  |   Disclaimer: this program comes without any guarantees.                     |  | 
 |  |   Beware of errors and use common sense when interpreting results.           |  | 
 |  |                                                                              |  | 
 |  |   Copyright (C) 2021 Torbjörn Sjöstrand                                      |  | 
 |  |                                                                              |  | 
 |  |                                                                              |  | 
 |  *------------------------------------------------------------------------------*  | 
 |                                                                                    | 
 *------------------------------------------------------------------------------------* 

LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118/NNPDF31_nnlo_as_0118_0000.dat
NNPDF31_nnlo_as_0118 PDF set, member #0, version 1; LHAPDF ID = 303600
LHAPDF 6.4.0 loading /cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/share/LHAPDF/NNPDF31_nnlo_as_0118/NNPDF31_nnlo_as_0118_0000.dat
NNPDF31_nnlo_as_0118 PDF set, member #0, version 1; LHAPDF ID = 303600

 *-------  PYTHIA Process Initialization  --------------------------*
 |                                                                  |
 | We collide p+ with p+ at a CM energy of 1.360e+04 GeV            |
 |                                                                  |
 |------------------------------------------------------------------|
 |                                                    |             |
 | Subprocess                                    Code |   Estimated |
 |                                                    |    max (mb) |
 |                                                    |             |
 |------------------------------------------------------------------|
 |                                                    |             |
 | Les Houches User Process(es)                  9999 |   1.000e-09 |
 |                                                                  |
 *-------  End PYTHIA Process Initialization -----------------------*

 *-------  PYTHIA Multiparton Interactions Initialization  ---------* 
 |                                                                  | 
 |                   sigmaNonDiffractive =    55.96 mb              | 
 |                                                                  | 
 |    pT0 =  1.44 gives sigmaInteraction =   479.45 mb: accepted    | 
 |                                                                  | 
 *-------  End PYTHIA Multiparton Interactions Initialization  -----* 
 PYTHIA Warning in MultipartonInteractions::init: maximum increased by factor 1.087

 *-------  PYTHIA Flag + Mode + Parm + Word + FVec + MVec + PVec + WVec Settings (changes only)  ------------------* 
 |                                                                                                                 | 
 | Name                                          |                      Now |      Default         Min         Max | 
 |                                               |                          |                                      | 
 | Beams:frameType                               |                        5 |            1           1           5 | 
 | Check:epTolErr                                |                0.0100000 |   1.0000e-04                         | 
 | ColourReconnection:range                      |                  5.17600 |      1.80000         0.0    10.00000 | 
 | Main:timesAllowErrors                         |                    10000 |           10           0             | 
 | MultipartonInteractions:alphaSorder           |                        2 |            1           0           2 | 
 | MultipartonInteractions:alphaSvalue           |                  0.11800 |      0.13000   0.0600000     0.25000 | 
 | MultipartonInteractions:bProfile              |                        2 |            3           0           4 | 
 | MultipartonInteractions:coreFraction          |                  0.63000 |      0.50000         0.0     1.00000 | 
 | MultipartonInteractions:coreRadius            |                  0.76340 |      0.40000     0.10000     1.00000 | 
 | MultipartonInteractions:ecmPow                |                0.0334400 |      0.21500         0.0     0.50000 | 
 | MultipartonInteractions:pT0Ref                |                  1.41000 |      2.28000     0.50000    10.00000 | 
 | Next:numberShowEvent                          |                        0 |            1           0             | 
 | ParticleDecays:allowPhotonRadiation           |                       on |          off                         | 
 | ParticleDecays:limitTau0                      |                       on |          off                         | 
 | PDF:pSet                                      | LHAPDF6:NNPDF31_nnlo_as_0118 |           13                     | 
 | POWHEG:nFinal                                 |                        3 |            2           1             | 
 | POWHEG:pTdef                                  |                        1 |            0           0           2 | 
 | POWHEG:veto                                   |                        1 |            0           0           1 | 
 | POWHEG:vetoCount                              |                      100 |            3           0             | 
 | SigmaProcess:alphaSorder                      |                        2 |            1           0           2 | 
 | SigmaProcess:alphaSvalue                      |                  0.11800 |      0.13000   0.0600000     0.25000 | 
 | SigmaTotal:mode                               |                        0 |            1           0           4 | 
 | SigmaTotal:sigmaEl                            |                 22.08000 |     25.00000         0.0             | 
 | SigmaTotal:sigmaTot                           |                101.03700 |    100.00000         0.0             | 
 | SigmaTotal:zeroAXB                            |                      off |           on                         | 
 | SLHA:minMassSM                                |                 1000.000 |    100.00000                         | 
 | SpaceShower:alphaSorder                       |                        2 |            1           0           2 | 
 | SpaceShower:alphaSvalue                       |                  0.11800 |      0.13650   0.0600000     0.25000 | 
 | SpaceShower:pTmaxMatch                        |                        2 |            0           0           2 | 
 | TimeShower:alphaSorder                        |                        2 |            1           0           2 | 
 | TimeShower:alphaSvalue                        |                  0.11800 |      0.13650   0.0600000     0.25000 | 
 | TimeShower:pTmaxMatch                         |                        2 |            1           0           2 | 
 | Tune:preferLHAPDF                             |                        2 |            1           0           2 | 
 | UncertaintyBands:doVariations                 |                       on |          off                         | 
 | UncertaintyBands:FSRpTmin2Fac                 |                 20.00000 |      4.00000         0.0   100.00000 | 
 | UncertaintyBands:ISRpTmin2Fac                 |                 20.00000 |      4.00000         0.0   100.00000 | 
 | UncertaintyBands:List                         | isrRedHi isr:muRfac=0.707 | alphaShi fsr:muRfac=0.5 isr:muRfac=0.5 | 
 |                                               | fsrRedHi fsr:muRfac=0.707 |   alphaSlo fsr:muRfac=2.0 isr:muRfac=2.0 | 
 |                                               | isrRedLo isr:muRfac=1.414 |   hardHi fsr:cNS=2.0 isr:cNS=2.0    | 
 |                                               | fsrRedLo fsr:muRfac=1.414 |  hardLo fsr:cNS=-2.0 isr:cNS=-2.0   | 
 |                                               |  isrDefHi isr:muRfac=0.5 |                                      | 
 |                                               |  fsrDefHi fsr:muRfac=0.5 |                                      | 
 |                                               |  isrDefLo isr:muRfac=2.0 |                                      | 
 |                                               |  fsrDefLo fsr:muRfac=2.0 |                                      | 
 |                                               | isrConHi isr:muRfac=0.25 |                                      | 
 |                                               | fsrConHi fsr:muRfac=0.25 |                                      | 
 |                                               |  isrConLo isr:muRfac=4.0 |                                      | 
 |                                               |  fsrConLo fsr:muRfac=4.0 |                                      | 
 |                                               | fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5 |                           | 
 |                                               | fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0 |                           | 
 |                                               | fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5 |                           | 
 |                                               | fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0 |                           | 
 |                                               | fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5 |                           | 
 |                                               | fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0 |                           | 
 |                                               | fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5 |                           | 
 |                                               | fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0 |                           | 
 |                                               | fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0 |                             | 
 |                                               | fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0 |                              | 
 |                                               | fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0 |                             | 
 |                                               | fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0 |                              | 
 |                                               | fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0 |                             | 
 |                                               | fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0 |                              | 
 |                                               | fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0 |                             | 
 |                                               | fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0 |                              | 
 |                                               | isr_G2GG_muR_dn isr:G2GG:muRfac=0.5 |                           | 
 |                                               | isr_G2GG_muR_up isr:G2GG:muRfac=2.0 |                           | 
 |                                               | isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5 |                           | 
 |                                               | isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0 |                           | 
 |                                               | isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5 |                           | 
 |                                               | isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0 |                           | 
 |                                               | isr_X2XG_muR_dn isr:X2XG:muRfac=0.5 |                           | 
 |                                               | isr_X2XG_muR_up isr:X2XG:muRfac=2.0 |                           | 
 |                                               | isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0 |                             | 
 |                                               | isr_G2GG_cNS_up isr:G2GG:cNS=2.0 |                              | 
 |                                               | isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0 |                             | 
 |                                               | isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0 |                              | 
 |                                               | isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0 |                             | 
 |                                               | isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0 |                              | 
 |                                               | isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0 |                             | 
 |                                               | isr_X2XG_cNS_up isr:X2XG:cNS=2.0 |                              | 
 | UncertaintyBands:MPIshowers                   |                       on |          off                         | 
 | UncertaintyBands:nFlavQ                       |                        4 |            6           2           6 | 
 | UncertaintyBands:overSampleFSR                |                 10.00000 |      3.00000     1.00000    10.00000 | 
 | UncertaintyBands:overSampleISR                |                 10.00000 |      2.00000     1.00000    10.00000 | 
 |                                                                                                                 | 
 *-------  End PYTHIA Flag + Mode + Parm + Word + FVec + MVec + PVec + WVec Settings  -----------------------------* 

 --------  PYTHIA Particle Data Table (changed only)  ------------------------------------------------------------------------------
 
      id   name            antiName         spn chg col      m0        mWidth      mMin       mMax       tau0    res dec ext vis wid
             no onMode   bRatio   meMode     products 

 no particle data has been changed from its default value 

 --------  End PYTHIA Particle Data Table  -----------------------------------------------------------------------------------------


 *-------  PYTHIA Flag + Mode + Parm + Word + FVec + MVec + PVec + WVec Settings (changes only)  ------------------* 
 |                                                                                                                 | 
 | Name                                          |                      Now |      Default         Min         Max | 
 |                                               |                          |                                      | 
 | Next:numberShowEvent                          |                        0 |            1           0             | 
 | ParticleDecays:allowPhotonRadiation           |                       on |          off                         | 
 | ParticleDecays:limitTau0                      |                       on |          off                         | 
 | ProcessLevel:all                              |                      off |           on                         | 
 |                                                                                                                 | 
 *-------  End PYTHIA Flag + Mode + Parm + Word + FVec + MVec + PVec + WVec Settings  -----------------------------* 

 --------  PYTHIA Particle Data Table (changed only)  ------------------------------------------------------------------------------
 
      id   name            antiName         spn chg col      m0        mWidth      mMin       mMax       tau0    res dec ext vis wid
             no onMode   bRatio   meMode     products 

 no particle data has been changed from its default value 

 --------  End PYTHIA Particle Data Table  -----------------------------------------------------------------------------------------

Begin processing the 1st record. Run 1, Event 1, LumiSection 1 on stream 0 at 21-May-2025 03:32:07.569 CEST

 --------  LHA event information and listing  ---------------------------------------------------------------------- 

    process =     9999    weight =   4.1637e+00     scale =   2.1833e+00 (GeV) 
                        alpha_em =  -1.0000e+00    alpha_strong =   3.3298e-01

    Participating Particles 
    no        id stat     mothers     colours      p_x        p_y        p_z         e          m        tau    spin 
     1         1   -1     0     0   501     0      0.000      0.000   1847.698   1847.698      0.000   0.000   9.000
     2        -3   -1     0     0     0   502      0.000      0.000   -276.015    276.015      0.000   0.000   9.000
     3        25    1     1     2     0     0    -52.072    -73.698    242.739    287.559    125.001   0.000   9.000
     4         2    1     1     2   511     0     14.427     49.939    846.355    847.949      0.330   0.000   9.000
     5        -4    1     1     2     0   502     23.227    -18.479   -251.254    253.005      1.500   0.000   9.000
     6        21    1     1     2   501   511     14.417     42.238    733.843    735.199      0.000   0.000   9.000

 --------  End LHA event information and listing  ------------------------------------------------------------------ 

 --------  PYTHIA Info Listing  ---------------------------------------- 
 
 Beam A: id =   2212, pz =  6.800e+03, e =  6.800e+03, m =  9.383e-01.
 Beam B: id =   2212, pz = -6.800e+03, e =  6.800e+03, m =  9.383e-01.

 In 1: id =    1, x =  2.717e-01, pdf =  0.000e+00 at Q2 =  4.767e+00.
 In 2: id =   -3, x =  4.059e-02, pdf =  0.000e+00 at same Q2.

 Process Les Houches User Process(es) with code 9999 is 2 -> 4.
 Subprocess user process 9999 with code 9999 is 2 -> 4.
     alphaEM =  7.504e-03,  alphaS =  3.330e-01    at Q2 =  4.767e+00.

 Impact parameter b =  1.761e-01 gives enhancement factor =  4.243e+00.
 Max pT scale for MPI =  1.360e+04, ISR =  1.360e+04, FSR =  1.360e+04.
 Number of MPI =    30, ISR =    36, FSRproc =    94, FSRreson =     3.

 --------  End PYTHIA Info Listing  ------------------------------------

 --------  PYTHIA Event Listing  (hard process)  -----------------------------------------------------------------------------------
 
    no         id  name            status     mothers   daughters     colours      p_x        p_y        p_z         e          m 
     0         90  (system)           -11     0     0     0     0     0     0      0.000      0.000      0.000  13600.000  13600.000
     1       2212  (p+)               -12     0     0     3     0     0     0      0.000      0.000   6800.000   6800.000      0.938
     2       2212  (p+)               -12     0     0     4     0     0     0      0.000      0.000  -6800.000   6800.000      0.938
     3          1  (d)                -21     1     0     5     8   501     0      0.000      0.000   1847.698   1847.698      0.000
     4         -3  (sbar)             -21     2     0     5     8     0   502      0.000      0.000   -276.015    276.015      0.000
     5         25  (h0)               -22     3     4     9    10     0     0    -52.072    -73.698    242.739    287.559    125.001
     6          2  u                   23     3     4     0     0   511     0     14.427     49.939    846.355    847.949      0.330
     7         -4  cbar                23     3     4     0     0     0   502     23.227    -18.479   -251.254    253.005      1.500
     8         21  g                   23     3     4     0     0   501   511     14.417     42.238    733.843    735.199      0.000
     9          5  b                   23     5     0     0     0   512     0    -33.536   -108.838    173.770    207.821      4.800
    10         -5  bbar                23     5     0     0     0     0   512    -18.536     35.141     68.969     79.738      4.800
                                   Charge sum:  0.000           Momentum sum:      0.000      0.000   1571.683   2123.713   1428.275

 --------  End PYTHIA Event Listing  -----------------------------------------------------------------------------------------------

 --------  PYTHIA Info Listing  ---------------------------------------- 
 
 Beam A: id =   2212, pz =  6.800e+03, e =  6.800e+03, m =  9.383e-01.
 Beam B: id =   2212, pz = -6.800e+03, e =  6.800e+03, m =  9.383e-01.

 In 1: id =    1, x =  2.717e-01, pdf =  0.000e+00 at Q2 =  4.767e+00.
 In 2: id =   -3, x =  4.059e-02, pdf =  0.000e+00 at same Q2.

 Process Les Houches User Process(es) with code 9999 is 2 -> 4.
 Subprocess user process 9999 with code 9999 is 2 -> 4.
     alphaEM =  7.504e-03,  alphaS =  3.330e-01    at Q2 =  4.767e+00.

 Impact parameter b =  1.761e-01 gives enhancement factor =  4.243e+00.
 Max pT scale for MPI =  1.360e+04, ISR =  1.360e+04, FSR =  1.360e+04.
 Number of MPI =    30, ISR =    36, FSRproc =    94, FSRreson =     3.

 --------  End PYTHIA Info Listing  ------------------------------------

 --------  PYTHIA Event Listing  (complete event)  ---------------------------------------------------------------------------------
 
    no         id  name            status     mothers   daughters     colours      p_x        p_y        p_z         e          m 
     0         90  (system)           -11     0     0     0     0     0     0      0.000      0.000      0.000  13600.000  13600.000
     1       2212  (p+)               -12     0     0   658     0     0     0      0.000      0.000   6800.000   6800.000      0.938
     2       2212  (p+)               -12     0     0   659     0     0     0      0.000      0.000  -6800.000   6800.000      0.938
     3          1  (d)                -21   180   180     5     8   501     0      0.000      0.000   1847.698   1847.698      0.000
     4         -3  (sbar)             -21   162   162     5     8     0   502      0.000      0.000   -276.015    276.015      0.000
     5         25  (h0)               -22     3     4   182   182     0     0    -52.072    -73.698    242.739    287.559    125.001
     6          2  (u)                -23     3     4   183   183   511     0     14.427     49.939    846.355    847.949      0.330
     7         -4  (cbar)             -23     3     4   160   161     0   502     23.227    -18.479   -251.254    253.005      1.500
     8         21  (g)                -23     3     4   185   185   501   511     14.417     42.238    733.843    735.199      0.000
     9         21  (g)                -31    17     0    11    12   604   603      0.000      0.000      2.901      2.901      0.000
    10         21  (g)                -31    18    18    11    12   606   605      0.000      0.000    -27.795     27.795      0.000
    11         21  (g)                -33     9    10    19    19   606   603      3.069      2.636    -26.149     26.460      0.000
    12         21  (g)                -33     9    10    20    20   604   605     -3.069     -2.636      1.255      4.235      0.000
    13         21  (g)                -31    54     0    15    16   611   610      0.000      0.000      3.327      3.327      0.000
    14         21  (g)                -31    55    55    15    16   613   612      0.000      0.000   -149.285    149.285      0.000
    15         21  (g)                -33    13    14    56    56   613   610      3.872      0.853   -148.068    148.121      0.000
    16         21  (g)                -33    13    14    57    57   611   612     -3.872     -0.853      2.109      4.491      0.000
    17         21  (g)                -41   673   673    21     9   604   659     -0.000     -0.000      4.316      4.316      0.000
    18         21  (g)                -42    92    92    10    10   606   605      0.000      0.000    -27.795     27.795      0.000
    19         21  (g)                -44    11    11    90    91   606   603      2.938      2.559    -22.148     22.488      0.000
    20         21  (g)                -44    12    12   317   318   604   605     -5.372     -3.994     -0.731      6.734      0.000
    21         21  (g)                -43    17     0   376   376   603   659      2.434      1.436     -0.600      2.889      0.000
    22         21  (g)                -31    30     0    24    25   683   684      0.000      0.000      1.809      1.809      0.000
    23         21  (g)                -31    31    31    24    25   685   686      0.000      0.000   -105.149    105.149      0.000
    24         21  (g)                -33    22    23    32    32   683   686     -1.285      2.568      0.636      2.942      0.000
    25         21  (g)                -33    22    23    33    33   685   684      1.285     -2.568   -103.976    104.016      0.000
    26         21  (g)                -31    93    93    28    29   692   691      0.000      0.000     85.991     85.991      0.000
    27         -2  (ubar)             -31    94     0    28    29     0   690      0.000      0.000     -0.733      0.733      0.000
    28         21  (g)                -33    26    27    95    95   692   690     -1.768      2.185     83.146     83.193      0.000
    29         -2  (ubar)             -33    26    27    96    96     0   691      1.768     -2.185      2.112      3.531      0.330
    30         21  (g)                -41    44    44    34    22   683   694      0.000     -0.000     22.044     22.044      0.000
    31         21  (g)                -42    45     0    23    23   685   686     -0.000      0.000   -105.149    105.149      0.000
    32         21  (g)                -44    24    24    46    46   683   686     -3.307      4.446     -2.434      6.052      0.000
    33         21  (g)                -44    25    25    47    47   685   684      1.263     -2.548   -100.789    100.829      0.000
    34         21  (g)                -43    30     0    48    48   684   694      2.045     -1.898     20.119     20.311      0.000
    35         21  (g)                -31    39     0    37    38   699   698      0.000      0.000    244.383    244.383      0.000
    36         21  (g)                -31    40    40    37    38   698   700      0.000      0.000     -0.038      0.038      0.000
    37         21  (g)                -33    35    36    41    41   701   700     -2.625     -0.827     69.127     69.181      0.000
    38         21  (g)                -33    35    36    42    42   699   701      2.625      0.827    175.218    175.240      0.000
    39         21  (g)                -41    70    70    43    35   699   721     -0.000     -0.000    760.723    760.723      0.000
    40         21  (g)                -42    71     0    36    36   698   700      0.000     -0.000     -0.038      0.038      0.000
    41         21  (g)                -44    37    37    72    72   701   700     -2.180     -1.342     87.135     87.173      0.000
    42         21  (g)                -44    38    38    73    73   699   701      3.753     -0.477    220.822    220.855      0.000
    43         21  (g)                -43    39     0    74    74   698   721     -1.573      1.819    452.727    452.734      0.000
    44         21  (g)                -42    62    62    30    30   683   694     -0.000     -0.000     22.044     22.044      0.000
    45         21  (g)                -41    63     0    49    31   685   729      0.000      0.000   -116.167    116.167      0.000
    46         21  (g)                -44    32    32    64    64   683   686     -3.359      4.363     -2.500      6.047      0.000
    47         21  (g)                -44    33    33    59    60   685   684      0.047     -4.508   -101.471    101.571      0.000
    48         21  (g)                -44    34    34    61    61   684   694      2.043     -1.900     19.982     20.176      0.000
    49         21  (g)                -43    45     0    67    67   686   729      1.268      2.045    -10.136     10.417      0.000
    50         21  (g)                -31   626   626    52    53   732   733      0.000      0.000     10.463     10.463      0.000
    51         21  (g)                -31   627     0    52    53   734   732      0.000      0.000    -28.636     28.636      0.000
    52         21  (g)                -33    50    51    98    99   734   735     -2.161     -1.216    -28.434     28.542      0.000
    53         21  (g)                -33    50    51   100   100   735   733      2.161      1.216     10.261     10.557      0.000
    54         21  (g)                -41    76    76    58    13   611   744      0.000     -0.000      4.167      4.167      0.000
    55         21  (g)                -42    77     0    14    14   613   612      0.000     -0.000   -149.285    149.285      0.000
    56         21  (g)                -44    15    15    78    78   613   610      3.876      0.835   -145.850    145.904      0.000
    57         21  (g)                -44    16    16    79    79   611   612     -3.444     -3.164      1.717      4.982      0.000
    58         21  (g)                -43    54     0    80    80   610   744     -0.431      2.329     -0.985      2.566      0.000
    59         21  (g)                -51    47     0    65    65   685   749     -0.840     -1.032    -73.663     73.675      0.000
    60         21  (g)                -51    47     0    68    68   749   684      0.894     -3.483    -27.736     27.968      0.000
    61         21  (g)                -52    48    48    66    66   684   694      2.036     -1.893     19.911     20.104      0.000
    62         21  (g)                -42   133     0    44    44   683   694     -0.000      0.000     22.044     22.044      0.000
    63         21  (g)                -41   134   134    69    45   765   729      0.000     -0.000   -213.323    213.323      0.000
    64         21  (g)                -44    46    46   135   135   683   686     -3.380      4.446     -2.456      6.101      0.000
    65         21  (g)                -44    59    59   136   136   685   749     -1.205      0.401    -73.749     73.760      0.000
    66         21  (g)                -44    61    61   137   137   684   694      2.036     -1.891     19.864     20.057      0.000
    67         21  (g)                -44    49    49   138   138   686   729      1.218      2.245    -10.130     10.447      0.000
    68         21  (g)                -44    60    60   139   139   749   684      0.756     -2.942    -27.802     27.967      0.000
    69         21  (g)                -43    63     0   140   140   765   685      0.575     -2.259    -97.007     97.035      0.000
    70         21  (g)                -42   101   101    39    39   699   721     -0.000     -0.000    760.723    760.723      0.000
    71         21  (g)                -41   102     0    75    40   698   788      0.000      0.000     -1.356      1.356      0.000
    72         21  (g)                -44    41    41   103   103   701   700     -1.663     -0.384     37.090     37.129      0.000
    73         21  (g)                -44    42    42   104   104   699   701      4.199      0.349    262.485    262.518      0.000
    74         21  (g)                -44    43    43   105   105   698   721     -1.485      1.982    460.178    460.185      0.000
    75         21  (g)                -43    71     0   106   106   700   788     -1.051     -1.948     -0.386      2.247      0.000
    76         21  (g)                -42   606     0    54    54   611   744      0.000      0.000      4.167      4.167      0.000
    77         -1  (dbar)             -41   433   433    81    55     0   612     -0.000     -0.000   -233.200    233.200      0.000
    78         21  (g)                -44    56    56   419   419   613   610      3.273     -1.168   -146.622    146.663      0.000
    79         21  (g)                -44    57    57   431   432   611   612     -3.451     -3.187      1.719      5.002      0.000
    80         21  (g)                -44    58    58   464   465   610   744     -0.439      2.305     -1.013      2.556      0.000
    81         -1  (dbar)             -43    77     0   417   418     0   613      0.617      2.049    -83.118     83.146      0.330
    82         -1  (dbar)             -31   748   748    84    85     0   810      0.000      0.000      0.790      0.790      0.000
    83         21  (g)                -31   749   749    84    85   810   811      0.000      0.000   -189.950    189.950      0.000
    84         -1  (dbar)             -33    82    83   263   264     0   812      1.127     -1.748     -0.628      2.198      0.330
    85         21  (g)                -33    82    83   265   265   812   811     -1.127      1.748   -188.531    188.543      0.000
    86         21  (g)                -31   116     0    88    89   814   815      0.000      0.000      0.150      0.150      0.000
    87          2  (u)                -31   117   117    88    89   813     0      0.000      0.000   -542.937    542.937      0.000
    88         21  (g)                -33    86    87   118   118   813   815      0.289      2.057     -7.140      7.436      0.000
    89          2  (u)                -33    86    87   119   119   814     0     -0.289     -2.057   -535.647    535.651      0.330
    90         21  (g)                -51    19     0   374   375   841   603     -0.276      0.638     -1.247      1.427      0.000
    91         21  (g)                -51    19     0   485   486   606   841      3.215      1.921    -43.888     44.047      0.000
    92         21  (g)                -53   319   319    18    18   606   605     -0.000      0.000    -50.782     50.782      0.000
    93         21  (g)                -42   635     0    26    26   692   691      0.000      0.000     85.991     85.991      0.000
    94         -2  (ubar)             -41   358   358    97    27     0   843     -0.000     -0.000     -0.845      0.845      0.000
    95         21  (g)                -44    28    28   282   282   692   690     -1.788      2.161     74.203     74.255      0.000
    96         -2  (ubar)             -44    29    29   638   638     0   691      1.178     -2.902      2.341      3.924      0.330
    97         21  (g)                -43    94     0   280   281   690   843      0.610      0.741      8.603      8.656      0.000
    98         21  (g)                -51    52     0   628   628   734   851     -3.302     -1.565    -20.046     20.376      0.000
    99         21  (g)                -51    52     0   210   211   851   735      1.173      0.367     -8.234      8.325      0.000
   100         21  (g)                -52    53    53   212   212   735   733      2.129      1.198     10.107     10.398      0.000
   101         21  (g)                -42   339   339    70    70   699   721     -0.000      0.000    760.723    760.723      0.000
   102         21  (g)                -41   340     0   107    71   915   788      0.000     -0.000     -8.166      8.166      0.000
   103         21  (g)                -44    72    72   195   196   701   700     -1.686     -0.378     38.001     38.040      0.000
   104         21  (g)                -44    73    73   342   342   699   701      4.179      0.354    259.835    259.869      0.000
   105         21  (g)                -44    74    74   209   209   698   721     -1.489      1.983    460.977    460.983      0.000
   106         21  (g)                -44    75    75   197   197   700   788     -2.617     -1.572      0.452      3.086      0.000
   107         21  (g)                -43   102     0   207   208   915   698      1.613     -0.387     -6.708      6.910      0.000
   108          2  (u)                -31   359   359   110   111   928     0      0.000      0.000      7.624      7.624      0.000
   109         21  (g)                -31   360     0   110   111   929   928      0.000      0.000     -2.286      2.286      0.000
   110          2  (u)                -33   108   109   235   236   930     0     -1.592      0.356      7.225      7.415      0.330
   111         21  (g)                -33   108   109   237   237   929   930      1.592     -0.356     -1.888      2.495      0.000
   112         21  (g)                -31   147   147   114   115   971   972      0.000      0.000      8.241      8.241      0.000
   113          2  (u)                -31   148     0   114   115   970     0      0.000      0.000     -0.286      0.286      0.000
   114         21  (g)                -33   112   113   149   149   970   972      0.843     -1.262      3.834      4.123      0.000
   115          2  (u)                -33   112   113   150   150   971     0     -0.843      1.262      4.121      4.404      0.330
   116         21  (g)                -41   757   757   120    86   975   815      0.000     -0.000     99.851     99.851      0.000
   117          2  (u)                -42   758   758    87    87   813     0     -0.000      0.000   -542.937    542.937      0.000
   118         21  (g)                -44    88    88   759   759   813   815     -0.547      3.303    -18.650     18.948      0.000
   119          2  (u)                -44    89    89   216   217   814     0     -0.300     -2.040   -524.130    524.134      0.330
   120         21  (g)                -43   116     0   218   218   975   814      0.848     -1.263     99.694     99.705      0.000
   121         21  (g)                -31   142   142   123   124   978   977      0.000      0.000      2.791      2.791      0.000
   122         21  (g)                -31   143     0   123   124   980   979      0.000      0.000     -1.079      1.079      0.000
   123         21  (g)                -33   121   122   144   144   980   977     -1.468      0.389      1.793      2.350      0.000
   124         21  (g)                -33   121   122   145   145   978   979      1.468     -0.389     -0.081      1.521      0.000
   125         21  (g)                -31   243     0   127   128   987   988      0.000      0.000      0.137      0.137      0.000
   126         21  (g)                -31   200   200   127   128   989   990      0.000      0.000   -112.917    112.917      0.000
   127         21  (g)                -33   125   126   245   245   987   990     -0.714     -1.320   -108.636    108.647      0.000
   128         21  (g)                -33   125   126   198   199   989   988      0.714      1.320     -4.144      4.407      0.000
   129         -2  (ubar)             -31   805   805   131   132     0   996      0.000      0.000      0.016      0.016      0.000
   130          1  (d)                -31   806   806   131   132   996     0      0.000      0.000  -1482.515   1482.515      0.000
   131         -2  (ubar)             -33   129   130   206   206     0   997      1.487     -0.033    -36.139     36.171      0.330
   132          1  (d)                -33   129   130   204   205   997     0     -1.487      0.033  -1446.359   1446.360      0.330
   133         21  (g)                -41   167   167   141    62   683  1004     -0.000      0.000     58.109     58.109      0.000
   134         21  (g)                -42   168     0    63    63   765   729     -0.000     -0.000   -213.323    213.323      0.000
   135         21  (g)                -44    64    64   169   169   683   686     -3.480      4.516     -2.634      6.280      0.000
   136         21  (g)                -44    65    65   170   170   685   749     -1.205      0.401    -73.776     73.787      0.000
   137         21  (g)                -44    66    66   171   171   684   694      0.937     -1.132     19.937     19.991      0.000
   138         21  (g)                -44    67    67   172   172   686   729      1.209      2.251    -10.137     10.454      0.000
   139         21  (g)                -44    68    68   173   173   749   684      0.752     -2.939    -27.720     27.885      0.000
   140         21  (g)                -44    69    69   174   174   765   685      0.574     -2.258    -96.930     96.958      0.000
   141         21  (g)                -43   133     0   175   175   694  1004      1.213     -0.839     36.046     36.076      0.000
   142         21  (g)                -42   338   338   121   121   978   977      0.000     -0.000      2.791      2.791      0.000
   143         21  (g)                -41   421   421   146   122   980  1053     -0.000      0.000    -36.766     36.766      0.000
   144         21  (g)                -44   123   123   422   422   980   977     -1.489      0.746      1.813      2.461      0.000
   145         21  (g)                -44   124   124   201   202   978   979      1.408      0.638     -0.293      1.574      0.000
   146         21  (g)                -43   143     0   203   203   979  1053      0.080     -1.384    -35.495     35.522      0.000
   147         21  (g)                -42   778   778   112   112   971   972      0.000      0.000      8.241      8.241      0.000
   148         21  (g)                -41   325   325   151   113   970  1061      0.000      0.000    -17.232     17.232      0.000
   149         21  (g)                -44   114   114   323   324   970   972      0.804     -1.956      6.237      6.585      0.000
   150          2  (u)                -44   115   115   781   781   971     0     -0.881      0.585      1.630      1.971      0.330
   151         -2  (ubar)             -43   148     0   782   782     0  1061      0.077      1.371    -16.857     16.916      0.330
   152         21  (g)                -31   648     0   154   155  1079  1078      0.000      0.000     53.767     53.767      0.000
   153          2  (u)                -31   649   649   154   155  1078     0      0.000      0.000   -187.345    187.345      0.000
   154         21  (g)                -33   152   153   192   193  1079  1080      0.924      0.977     53.756     53.773      0.000
   155          2  (u)                -33   152   153   194   194  1080     0     -0.924     -0.977   -187.334    187.340      0.330
   156         21  (g)                -31   238     0   158   159  1083  1082      0.000      0.000      1.261      1.261      0.000
   157         -3  (sbar)             -31   239   239   158   159     0  1081      0.000      0.000     -2.198      2.198      0.000
   158         21  (g)                -33   156   157   240   240  1083  1081      1.239     -0.438      0.538      1.420      0.000
   159         -3  (sbar)             -33   156   157   241   241     0  1082     -1.239      0.438     -1.475      2.038      0.500
   160         -4  (cbar)             -51     7     0   184   184     0  1118     13.836    -12.198   -162.147    163.200      1.500
   161         21  (g)                -51     7     0   186   186  1118   502      9.391     -6.281    -90.971     91.669      0.000
   162         -3  (sbar)             -53   181     0     4     4     0   502      0.000     -0.000   -277.879    277.879      0.000
   163         -2  (ubar)             -31   222   222   165   166     0  1121      0.000      0.000    653.431    653.431      0.000
   164         21  (g)                -31   223     0   165   166  1121  1122      0.000      0.000     -3.489      3.489      0.000
   165         -2  (ubar)             -33   163   164   179   179     0  1123     -0.183     -1.259    653.314    653.316      0.330
   166         21  (g)                -33   163   164   177   178  1123  1122      0.183      1.259     -3.372      3.604      0.000
   167         21  (g)                -42   322   322   133   133   683  1004     -0.000      0.000     58.109     58.109      0.000
   168         21  (g)                -41   472   472   176   134  1133   729      0.000     -0.000   -327.647    327.647      0.000
   169         21  (g)                -44   135   135   320   321   683   686     -3.500      4.533     -2.618      6.297      0.000
   170         21  (g)                -44   136   136   530   531   685   749     -1.531      0.687    -73.779     73.798      0.000
   171         21  (g)                -44   137   137   493   493   684   694      0.937     -1.132     19.931     19.985      0.000
   172         21  (g)                -44   138   138   398   398   686   729      1.163      2.291    -10.137     10.457      0.000
   173         21  (g)                -44   139   139   491   492   749   684      0.629     -2.831    -27.730     27.881      0.000
   174         21  (g)                -44   140   140   550   550   765   685      0.146     -1.883    -96.943     96.962      0.000
   175         21  (g)                -44   141   141   701   701   694  1004      1.213     -0.839     36.038     36.068      0.000
   176         21  (g)                -43   168     0   524   525  1133   765      0.943     -0.827   -114.300    114.307      0.000
   177         21  (g)                -51   166     0   225   225  1153  1122      0.791      1.264     -3.316      3.636      0.000
   178         21  (g)                -51   166     0   226   226  1123  1153     -0.611     -0.019      7.399      7.424      0.000
   179         -2  (ubar)             -52   165   165   224   224     0  1123     -0.180     -1.245    645.859    645.861      0.330
   180          1  (d)                -42   379   379     3     3   501     0      0.000      0.000   1847.698   1847.698      0.000
   181         -3  (sbar)             -41   659   659   187   162     0  1177     -0.000     -0.000   -477.400    477.400      0.000
   182         25  (h0)               -44     5     5   660   660     0     0    -52.053    -73.603    242.561    287.381    125.001
   183          2  (u)                -44     6     6   249   250   511     0     14.428     49.942    846.464    848.059      0.330
   184         -4  (cbar)             -44   160   160   662   662     0  1118     13.972    -11.512   -162.167    163.181      1.500
   185         21  (g)                -44     8     8   251   251   501   511     14.418     42.241    733.937    735.293      0.000
   186         21  (g)                -44   161   161   213   214  1118   502      9.467     -5.896    -90.980     91.661      0.000
   187         21  (g)                -43   181     0   215   215   502  1177     -0.232     -1.172   -199.519    199.522      0.000
   188         21  (g)                -31   283     0   190   191  1188  1189      0.000      0.000      0.668      0.668      0.000
   189         21  (g)                -31   284   284   190   191  1189  1190      0.000      0.000     -5.358      5.358      0.000
   190         21  (g)                -33   188   189   285   285  1188  1191      1.162      0.195      0.013      1.178      0.000
   191         21  (g)                -33   188   189   286   286  1191  1190     -1.162     -0.195     -4.703      4.848      0.000
   192         21  (g)                -51   154     0   408   409  1079  1202      1.898      0.945     53.341     53.383      0.000
   193         21  (g)                -51   154     0   228   229  1202  1080     -0.977      0.029     -0.190      0.996      0.000
   194          2  (u)                -52   155   155   230   230  1080     0     -0.921     -0.974   -186.729    186.734      0.330
   195         21  (g)                -51   103     0   341   341   701  1233     -0.508     -0.779     32.211     32.224      0.000
   196         21  (g)                -51   103     0   346   346  1233   700     -1.305      0.325      5.812      5.966      0.000
   197         21  (g)                -52   106   106   344   344   700   788     -2.490     -1.496      0.430      2.937      0.000
   198         -1  (dbar)             -51   128     0   246   246     0   988      1.250      0.116     -6.316      6.448      0.330
   199          1  (d)                -51   128     0   247   247   989     0     -0.536      1.205     -6.954      7.086      0.330
   200         21  (g)                -53   244   244   126   126   989   990      0.000      0.000   -122.044    122.044      0.000
   201         21  (g)                -51   145     0   336   337   978  1261      2.037      0.964     -1.878      2.934      0.000
   202         21  (g)                -51   145     0   425   425  1261   979     -0.623     -0.433     -1.154      1.381      0.000
   203         21  (g)                -52   146   146   424   424   979  1053      0.074     -1.277    -32.756     32.781      0.000
   204          1  (d)                -51   132     0   808   808  1264     0     -1.329      0.069  -1450.089   1450.090      0.330
   205         21  (g)                -51   132     0   809   809   997  1264      0.024     -0.041     -0.273      0.277      0.000
   206         -2  (ubar)             -52   131   131   807   807     0   997      1.305     -0.029    -32.137     32.165      0.330
   207         21  (g)                -51   107     0   326   327   915  1289      2.525     -0.654     -6.108      6.642      0.000
   208         21  (g)                -51   107     0   221   221  1289   698     -0.914      0.270      0.090      0.957      0.000
   209         21  (g)                -52   105   105   219   220   698   721     -1.487      1.980    460.287    460.294      0.000
   210         21  (g)                -51    99     0   630   630   851  1295      1.815     -0.285     -6.635      6.885      0.000
   211         21  (g)                -51    99     0   473   474  1295   735     -0.597      0.677     -1.389      1.657      0.000
   212         21  (g)                -52   100   100   475   475   735   733      2.084      1.173      9.897     10.182      0.000
   213         21  (g)                -51   186     0   551   552  1118  1309      9.701     -6.167    -98.048     98.720      0.000
   214         21  (g)                -51   186     0   401   401  1309   502     -0.248      0.199     -5.196      5.205      0.000
   215         21  (g)                -52   187   187   399   400   502  1177     -0.218     -1.100   -187.255    187.258      0.000
   216          2  (u)                -51   119     0   760   760  1310     0      0.042     -1.647   -160.889    160.898      0.330
   217         21  (g)                -51   119     0   270   271   814  1310     -0.342     -0.393   -363.238    363.239      0.000
   218         21  (g)                -52   120   120   272   272   975   814      0.848     -1.263     99.691     99.703      0.000
   219         21  (g)                -51   209     0   343   343  1317   721     -1.475      1.437    455.368    455.372      0.000
   220         21  (g)                -51   209     0   348   348   698  1317     -0.042      0.552      4.923      4.954      0.000
   221         21  (g)                -52   208   208   328   328  1289   698     -0.884      0.261      0.087      0.925      0.000
   222         -2  (ubar)             -42   252   252   163   163     0  1121     -0.000      0.000    653.431    653.431      0.000
   223         21  (g)                -41   253     0   227   164  1121  1318      0.000     -0.000     -3.585      3.585      0.000
   224         -2  (ubar)             -44   179   179   254   254     0  1123     -0.180     -1.245    643.077    643.078      0.330
   225         21  (g)                -44   177   177   255   255  1153  1122      1.689      0.962     -3.220      3.762      0.000
   226         21  (g)                -44   178   178   256   256  1123  1153     -0.607     -0.020      7.289      7.314      0.000
   227         21  (g)                -43   223     0   257   257  1122  1318     -0.901      0.303      2.700      2.863      0.000
   228         21  (g)                -51   193     0   410   410  1202  1342     -1.112     -0.842     -0.934      1.679      0.000
   229         21  (g)                -51   193     0   288   289  1342  1080      0.103      0.837     -5.827      5.888      0.000
   230          2  (u)                -52   194   194   290   290  1080     0     -0.889     -0.940   -180.158    180.163      0.330
   231         21  (g)                -31   846   846   233   234  1355  1356      0.000      0.000    333.424    333.424      0.000
   232         -2  (ubar)             -31   847   847   233   234     0  1355      0.000      0.000     -0.315      0.315      0.000
   233         21  (g)                -33   231   232   380   381  1357  1356     -0.282     -0.956    332.545    332.546      0.000
   234         -2  (ubar)             -33   231   232   382   382     0  1357      0.282      0.956      0.565      1.193      0.330
   235          2  (u)                -51   110     0   361   361  1358     0     -0.479      0.139      6.365      6.393      0.330
   236         21  (g)                -51   110     0   363   363   930  1358     -0.983      0.188      0.706      1.225      0.000
   237         21  (g)                -52   111   111   362   362   929   930      1.462     -0.327     -1.734      2.291      0.000
   238         21  (g)                -41   820   820   242   156  1083  1368      0.000     -0.000      1.780      1.780      0.000
   239         -3  (sbar)             -42   821   821   157   157     0  1081     -0.000     -0.000     -2.198      2.198      0.000
   240         21  (g)                -44   158   158   822   822  1083  1081      0.857     -0.538      1.075      1.477      0.000
   241         -3  (sbar)             -44   159   159   823   823     0  1082     -1.349      0.409     -1.158      1.892      0.500
   242         21  (g)                -43   238     0   824   824  1082  1368      0.492      0.129     -0.334      0.609      0.000
   243         21  (g)                -41   291     0   248   125  1401   988     -0.000     -0.000      0.162      0.162      0.000
   244         21  (g)                -42   292   292   200   200   989   990      0.000      0.000   -122.044    122.044      0.000
   245         21  (g)                -44   127   127   293   293   987   990     -0.718     -1.295    -97.033     97.045      0.000
   246         -1  (dbar)             -44   198   198   294   294     0   988      1.193      0.443     -5.944      6.088      0.330
   247          1  (d)                -44   199   199   295   295   989     0     -0.592      1.531     -9.707      9.851      0.330
   248         21  (g)                -43   243     0   296   296  1401   987      0.117     -0.679     -9.197      9.222      0.000
   249          2  (u)                -51   183     0   661   661  1403     0      2.575      8.452    136.227    136.513      0.330
   250         21  (g)                -51   183     0   667   667   511  1403     21.355     69.329   1193.951   1196.153      0.000
   251         21  (g)                -52   185   185   377   378   501   511      4.916     14.401    250.224    250.687      0.000
   252         -2  (ubar)             -42   305   305   222   222     0  1121      0.000      0.000    653.431    653.431      0.000
   253         21  (g)                -41   306     0   258   223  1121  1405     -0.000     -0.000    -16.275     16.275      0.000
   254         -2  (ubar)             -44   224   224   307   307     0  1123     -0.180     -1.245    642.853    642.855      0.330
   255         21  (g)                -44   225   225   308   308  1153  1122      2.296      1.673     -2.914      4.069      0.000
   256         21  (g)                -44   226   226   309   309  1123  1153     -0.605     -0.017      7.233      7.259      0.000
   257         21  (g)                -44   227   227   310   310  1122  1318     -0.887      0.319      2.654      2.816      0.000
   258         21  (g)                -43   253     0   311   311  1318  1405     -0.623     -0.729    -12.671     12.707      0.000
   259         21  (g)                -31   853   853   261   262  1407  1406      0.000      0.000    113.648    113.648      0.000
   260         21  (g)                -31   854   854   261   262  1409  1408      0.000      0.000    -15.716     15.716      0.000
   261         21  (g)                -33   259   260   855   855  1409  1406      0.941     -0.175    113.632    113.636      0.000
   262         21  (g)                -33   259   260   856   856  1407  1408     -0.941      0.175    -15.699     15.729      0.000
   263         -1  (dbar)             -51    84     0   496   496     0  1415      1.637     -1.408     -1.799      2.830      0.330
   264         21  (g)                -51    84     0   458   459  1415   812     -0.518     -0.329     -0.080      0.618      0.000
   265         21  (g)                -52    85    85   460   460   812   811     -1.120      1.737   -187.281    187.293      0.000
   266         21  (g)                -31   351     0   268   269  1420  1419      0.000      0.000      0.106      0.106      0.000
   267         21  (g)                -31   352   352   268   269  1422  1421      0.000      0.000   -103.111    103.111      0.000
   268         21  (g)                -33   266   267   353   353  1422  1419      0.597     -0.730   -100.954    100.959      0.000
   269         21  (g)                -33   266   267   354   354  1420  1421     -0.597      0.730     -2.051      2.258      0.000
   270         21  (g)                -51   217     0   304   304  1437  1310     -0.938      0.343   -308.055    308.057      0.000
   271         21  (g)                -51   217     0   273   274   814  1437      0.596     -0.735    -55.178     55.186      0.000
   272         21  (g)                -52   218   218   275   275   975   814      0.847     -1.263     99.687     99.698      0.000
   273         21  (g)                -51   271     0   302   303  1449  1437      0.462     -1.613    -52.969     52.996      0.000
   274         21  (g)                -51   271     0   407   407   814  1449      0.134      0.877     -2.111      2.289      0.000
   275         21  (g)                -52   272   272   515   516   975   814      0.847     -1.262     99.588     99.600      0.000
   276         21  (g)                -31   866   866   278   279  1461  1462      0.000      0.000     77.635     77.635      0.000
   277         21  (g)                -31   867   867   278   279  1463  1464      0.000      0.000     -0.038      0.038      0.000
   278         21  (g)                -33   276   277   868   868  1461  1464      0.909      0.092     71.690     71.696      0.000
   279         21  (g)                -33   276   277   869   869  1463  1462     -0.909     -0.092      5.907      5.978      0.000
   280         21  (g)                -51    97     0   356   357  1512   843     -0.079      1.792     21.827     21.901      0.000
   281         21  (g)                -51    97     0   539   540   690  1512     -0.029     -0.183     16.568     16.569      0.000
   282         21  (g)                -52    95    95   541   541   692   690     -1.070      1.293     44.410     44.442      0.000
   283         21  (g)                -41   584     0   287   188  1188  1522     -0.000      0.000      3.034      3.034      0.000
   284         21  (g)                -42   585   585   189   189  1189  1190      0.000      0.000     -5.358      5.358      0.000
   285         21  (g)                -44   190   190   545   546  1188  1191      1.218     -0.571     -0.075      1.347      0.000
   286         21  (g)                -44   191   191   547   547  1191  1190     -1.155     -0.289     -4.490      4.645      0.000
   287         21  (g)                -43   283     0   588   588  1189  1522     -0.062      0.860      2.241      2.401      0.000
   288          2  (u)                -51   229     0   559   559  1342     0      0.518     -0.322    -10.769     10.792      0.330
   289         -2  (ubar)             -51   229     0   654   654     0  1080     -0.532      1.034    -18.742     18.781      0.330
   290          2  (u)                -52   230   230   651   651  1080     0     -0.772     -0.815   -156.474    156.479      0.330
   291         21  (g)                -41   795   795   297   243  1571   988      0.000     -0.000    179.093    179.093      0.000
   292         21  (g)                -42   796   796   244   244   989   990     -0.000      0.000   -122.044    122.044      0.000
   293         21  (g)                -44   245   245   797   797   987   990     -0.692     -1.308    -96.011     96.023      0.000
   294         -1  (dbar)             -44   246   246   798   798     0   988      1.529      0.278     -8.635      8.780      0.330
   295          1  (d)                -44   247   247   799   799   989     0     -0.257      1.367     -6.991      7.135      0.330
   296         21  (g)                -44   248   248   442   442  1401   987      0.177     -0.709    -10.243     10.269      0.000
   297         21  (g)                -43   291     0   440   441  1571  1401     -0.758      0.371    178.929    178.931      0.000
   298         -3  (sbar)             -31   870   870   300   301     0  1580      0.000      0.000      4.607      4.607      0.000
   299         -3  (sbar)             -31   430   430   300   301     0  1581      0.000      0.000     -4.303      4.303      0.000
   300         -3  (sbar)             -33   298   299   428   429     0  1581      0.319      0.770      4.500      4.603      0.500
   301         -3  (sbar)             -33   298   299   873   873     0  1580     -0.319     -0.770     -4.196      4.307      0.500
   302         21  (g)                -51   273     0   405   406  1449  1583     -0.028     -1.604    -95.036     95.050      0.000
   303         21  (g)                -51   273     0   571   571  1583  1437      0.348      0.043     -4.623      4.636      0.000
   304         21  (g)                -52   270   270   569   570  1437  1310     -0.795      0.291   -261.365    261.367      0.000
   305         -2  (ubar)             -42   446     0   252   252     0  1121      0.000      0.000    653.431    653.431      0.000
   306         21  (g)                -41   447   447   312   253  1121  1589     -0.000     -0.000    -94.894     94.894      0.000
   307         -2  (ubar)             -44   254   254   393   394     0  1123     -0.180     -1.245    642.871    642.872      0.330
   308         21  (g)                -44   255   255   414   415  1153  1122      2.207      1.517     -2.978      4.005      0.000
   309         21  (g)                -44   256   256   395   395  1123  1153     -0.605     -0.018      7.241      7.266      0.000
   310         21  (g)                -44   257   257   451   451  1122  1318     -0.889      0.315      2.658      2.821      0.000
   311         21  (g)                -44   258   258   373   373  1318  1405     -0.945     -1.294    -12.638     12.740      0.000
   312         21  (g)                -43   306     0   371   372  1405  1589      0.412      0.724    -78.617     78.621      0.000
   313         21  (g)                -31   599   599   315   316  1594  1593      0.000      0.000      0.046      0.046      0.000
   314         21  (g)                -31   600     0   315   316  1595  1594      0.000      0.000    -56.123     56.123      0.000
   315         21  (g)                -33   313   314   509   510  1596  1593     -0.786      0.269     -3.972      4.058      0.000
   316         21  (g)                -33   313   314   511   511  1595  1596      0.786     -0.269    -52.104     52.111      0.000
   317         21  (g)                -51    20     0   676   676   604  1628     -3.614     -2.140     -1.256      4.383      0.000
   318         21  (g)                -51    20     0   679   679  1628   605     -1.758     -1.855      0.302      2.574      0.000
   319         21  (g)                -53   674   674    92    92   606   605      0.000     -0.000    -51.004     51.004      0.000
   320         21  (g)                -51   169     0   396   397  1661   686     -2.475      3.412     -2.746      5.031      0.000
   321         21  (g)                -51   169     0   703   703   683  1661     -1.025      1.121      0.445      1.583      0.000
   322         21  (g)                -53   693   693   167   167   683  1004     -0.000      0.000     58.425     58.425      0.000
   323         21  (g)                -51   149     0   780   780  1679   972      0.316     -2.129      4.250      4.763      0.000
   324         21  (g)                -51   149     0   783   783   970  1679      0.488      0.173      1.869      1.940      0.000
   325         21  (g)                -53   779   779   148   148   970  1061     -0.000     -0.000    -17.349     17.349      0.000
   326          3  (s)                -51   207     0   345   345   915     0      1.678     -0.776     -5.327      5.661      0.500
   327         -3  (sbar)             -51   207     0   349   349     0  1289      0.683      0.171     -0.766      1.154      0.500
   328         21  (g)                -52   221   221   347   347  1289   698     -0.719      0.212      0.071      0.753      0.000
   329         -1  (dbar)             -31   883   883   331   332     0  1712      0.000      0.000      1.987      1.987      0.000
   330         21  (g)                -31   335   335   331   332  1714  1713      0.000      0.000    -12.878     12.878      0.000
   331         -1  (dbar)             -33   329   330   333   334     0  1713     -0.119      0.770      1.884      2.065      0.330
   332         21  (g)                -33   329   330   886   886  1714  1712      0.119     -0.770    -12.775     12.799      0.000
   333         -1  (dbar)             -51   331     0   499   499     0  1733     -0.587      0.944      1.715      2.070      0.330
   334         21  (g)                -51   331     0   497   498  1733  1713      0.468     -0.174     -0.671      0.836      0.000
   335         21  (g)                -53   884   884   330   330  1714  1713      0.000     -0.000    -13.718     13.718      0.000
   336         21  (g)                -51   201     0   423   423  1734  1261      0.993     -0.350     -0.735      1.284      0.000
   337         21  (g)                -51   201     0   426   426   978  1734      1.044      1.314     -0.892      1.901      0.000
   338         21  (g)                -53   420     0   142   142   978   977      0.000     -0.000      3.042      3.042      0.000
   339         21  (g)                -42   523   523   101   101   699   721      0.000      0.000    760.723    760.723      0.000
   340         21  (g)                -41   490   490   350   102  1816   788     -0.000     -0.000    -36.188     36.188      0.000
   341         21  (g)                -44   195   195   388   388   701  1233     -0.508     -0.779     32.167     32.181      0.000
   342         21  (g)                -44   104   104   481   481   699   701      4.180      0.355    259.937    259.971      0.000
   343         21  (g)                -44   219   219   521   522  1317   721     -1.475      1.437    455.377    455.382      0.000
   344         21  (g)                -44   197   197   488   489   700   788     -2.433     -1.398      0.317      2.824      0.000
   345          3  (s)                -44   326   326   445   445   915     0      1.929     -0.345     -5.308      5.680      0.500
   346         21  (g)                -44   196   196   386   387  1233   700     -1.302      0.331      5.795      5.949      0.000
   347         21  (g)                -44   328   328   728   728  1289   698     -0.704      0.239      0.063      0.746      0.000
   348         21  (g)                -44   220   220   729   729   698  1317     -0.042      0.554      4.943      4.974      0.000
   349         -3  (sbar)             -44   327   327   730   730     0  1289      0.726      0.247     -0.741      1.178      0.500
   350         21  (g)                -43   340     0   443   444  1816   915     -0.373     -0.641    -28.017     28.027      0.000
   351         21  (g)                -41   365   365   355   266  1866  1419      0.000      0.000    185.760    185.760      0.000
   352         21  (g)                -42   366     0   267   267  1422  1421     -0.000     -0.000   -103.111    103.111      0.000
   353         21  (g)                -44   268   268   367   367  1422  1419      0.610     -0.722   -100.108    100.113      0.000
   354         21  (g)                -44   269   269   368   368  1420  1421     -0.011      1.120     -2.895      3.104      0.000
   355         21  (g)                -43   351     0   369   369  1866  1420     -0.599     -0.398    185.653    185.654      0.000
   356          1  (d)                -51   280     0   639   639  1512     0      0.081      1.517     10.905     11.016      0.330
   357         -1  (dbar)             -51   280     0   641   641     0   843     -0.160      0.276     10.898     10.908      0.330
   358         -2  (ubar)             -53   636   636    94    94     0   843     -0.000     -0.000     -0.868      0.868      0.000
   359          2  (u)                -42   771   771   108   108   928     0     -0.000      0.000      7.624      7.624      0.000
   360         -3  (sbar)             -41   772   772   364   109     0   928      0.000     -0.000     -3.032      3.032      0.000
   361          2  (u)                -44   235   235   773   773  1358     0     -0.478      0.136      6.160      6.188      0.330
   362         21  (g)                -44   237   237   542   543   929   930      1.606     -0.741     -1.691      2.447      0.000
   363         21  (g)                -44   236   236   544   544   930  1358     -0.965      0.134      0.622      1.156      0.000
   364         -3  (sbar)             -43   360     0   776   776     0   929     -0.163      0.471     -0.499      0.865      0.500
   365         21  (g)                -42   857   857   351   351  1866  1419     -0.000     -0.000    185.760    185.760      0.000
   366         21  (g)                -41   858   858   370   352  1951  1421      0.000      0.000   -104.204    104.204      0.000
   367         21  (g)                -44   353   353   859   859  1422  1419      1.076     -0.269   -100.166    100.173      0.000
   368         21  (g)                -44   354   354   383   384  1420  1421      0.003      1.133     -2.895      3.109      0.000
   369         21  (g)                -44   355   355   385   385  1866  1420     -0.599     -0.398    185.541    185.542      0.000
   370         21  (g)                -43   366     0   862   862  1951  1422     -0.480     -0.466     -0.923      1.140      0.000
   371         21  (g)                -51   312     0   453   453  1956  1589      0.773      0.406    -31.438     31.451      0.000
   372         21  (g)                -51   312     0   454   454  1405  1956     -0.456      0.188    -48.453     48.456      0.000
   373         21  (g)                -52   311   311   452   452  1318  1405     -0.850     -1.164    -11.364     11.455      0.000
   374          3  (s)                -51    90     0   487   487   841     0      0.064      0.210     -0.028      0.547      0.500
   375         -3  (sbar)             -51    90     0   680   680     0   603      0.415      0.873     -1.405      1.777      0.500
   376         21  (g)                -52    21    21   677   677   603   659      1.678      0.990     -0.414      1.992      0.000
   377         21  (g)                -51   251     0   484   484  1987   511      4.132     13.619    227.651    228.096      0.000
   378         21  (g)                -51   251     0   482   483   501  1987      0.784      0.783     34.318     34.336      0.000
   379          1  (d)                -53   658   658   180   180   501     0      0.000      0.000   1859.442   1859.442      0.000
   380         21  (g)                -51   233     0   411   412  2016  1356      0.313     -1.149    306.348    306.350      0.000
   381         21  (g)                -51   233     0   413   413  1357  2016     -0.592      0.205     26.202     26.210      0.000
   382         -2  (ubar)             -52   234   234   580   580     0  1357      0.279      0.944      0.560      1.179      0.330
   383         21  (g)                -51   368     0   404   404  2023  1421     -0.437      0.610     -2.816      2.915      0.000
   384         21  (g)                -51   368     0   402   403  1420  2023      0.437      0.521      0.715      0.987      0.000
   385         21  (g)                -52   369   369   556   556  1866  1420     -0.596     -0.396    184.748    184.750      0.000
   386         21  (g)                -51   346     0   502   502  2047   700     -1.336     -0.374      8.713      8.822      0.000
   387         21  (g)                -51   346     0   732   732  1233  2047     -0.064      0.554      3.320      3.367      0.000
   388         21  (g)                -52   341   341   479   480   701  1233     -0.409     -0.628     25.930     25.941      0.000
   389         -1  (dbar)             -31   621   621   391   392     0  2049      0.000      0.000      0.192      0.192      0.000
   390         21  (g)                -31   622     0   391   392  2051  2050      0.000      0.000     -3.543      3.543      0.000
   391         -1  (dbar)             -33   389   390   623   623     0  2050     -0.614     -0.171     -0.678      0.988      0.330
   392         21  (g)                -33   389   390   624   624  2051  2049      0.614      0.171     -2.672      2.747      0.000
   393         -2  (ubar)             -51   307     0   448   448     0  2056     -0.020     -1.482    442.701    442.703      0.330
   394         21  (g)                -51   307     0   455   455  2056  1123     -0.197      0.236    200.606    200.606      0.000
   395         21  (g)                -52   309   309   416   416  1123  1153     -0.569     -0.017      6.805      6.829      0.000
   396         21  (g)                -51   320     0   695   695  1661  2107     -0.033     -0.105     -0.727      0.736      0.000
   397         21  (g)                -51   320     0   704   704  2107   686     -2.322      3.753     -3.063      5.372      0.000
   398         21  (g)                -52   172   172   470   471   686   729      1.044      2.055     -9.092      9.380      0.000
   399         21  (g)                -51   215     0   665   665  2152  1177      0.229      0.078    -82.488     82.488      0.000
   400         21  (g)                -51   215     0   669   669   502  2152     -0.550     -1.095   -106.915    106.922      0.000
   401         21  (g)                -52   214   214   553   553  1309   502     -0.146      0.117     -3.047      3.053      0.000
   402         21  (g)                -51   384     0   554   555  1420  2192     -0.106      0.482      0.697      0.854      0.000
   403         21  (g)                -51   384     0   864   864  2192  2023      0.449      0.171     -0.590      0.761      0.000
   404         21  (g)                -52   383   383   860   860  2023  1421     -0.342      0.479     -2.209      2.286      0.000
   405         21  (g)                -51   302     0   763   763  2200  1583     -0.432     -0.694    -69.152     69.157      0.000
   406         21  (g)                -51   302     0   437   438  1449  2200      0.411     -0.867    -25.990     26.008      0.000
   407         21  (g)                -52   274   274   439   439   814  1449      0.128      0.833     -2.005      2.174      0.000
   408         21  (g)                -51   192     0   650   650  1079  2202      1.589      1.421     45.468     45.518      0.000
   409         21  (g)                -51   192     0   655   655  2202  1202      0.297     -0.485      7.862      7.883      0.000
   410         21  (g)                -52   228   228   557   558  1202  1342     -1.100     -0.833     -0.924      1.660      0.000
   411         21  (g)                -51   380     0   848   848  2211  1356     -0.035     -1.358    230.941    230.945      0.000
   412         21  (g)                -51   380     0   851   851  2016  2211      0.167      0.272     83.424     83.425      0.000
   413         21  (g)                -52   381   381   578   579  1357  2016     -0.411      0.142     18.184     18.190      0.000
   414         21  (g)                -51   308     0   449   449  2219  1122      1.449      1.671     -2.645      3.447      0.000
   415         21  (g)                -51   308     0   456   456  1153  2219      0.741     -0.154     -0.125      0.767      0.000
   416         21  (g)                -52   395   395   450   450  1123  1153     -0.551     -0.016      6.596      6.619      0.000
   417         -1  (dbar)             -51    81     0   611   611     0  2240      0.317      1.122    -74.237     74.247      0.330
   418         21  (g)                -51    81     0   612   612  2240   613      0.625      0.811    -23.404     23.426      0.000
   419         21  (g)                -52    78    78   466   466   613   610      2.948     -1.052   -132.099    132.136      0.000
   420         21  (g)                -41   784   784   427   338   978  2247      0.000      0.000    200.299    200.299      0.000
   421         21  (g)                -42   505   505   143   143   980  1053     -0.000     -0.000    -36.766     36.766      0.000
   422         21  (g)                -44   144   144   436   436   980   977     -1.279      1.129      1.799      2.479      0.000
   423         21  (g)                -44   336   336   527   528  1734  1261      1.020     -0.301     -0.754      1.304      0.000
   424         21  (g)                -44   203   203   788   788   979  1053      0.075     -1.275    -32.617     32.642      0.000
   425         21  (g)                -44   202   202   789   789  1261   979     -0.612     -0.413     -1.085      1.312      0.000
   426         21  (g)                -44   337   337   529   529   978  1734      1.094      1.405     -1.064      2.074      0.000
   427         21  (g)                -43   420     0   434   435   977  2247     -0.298     -0.545    197.254    197.255      0.000
   428         -3  (sbar)             -51   300     0   478   478     0  2262      0.789      0.650      4.141      4.294      0.500
   429         21  (g)                -51   300     0   476   477  2262  1581     -0.470      0.120      0.158      0.510      0.000
   430         -3  (sbar)             -53   871   871   299   299     0  1581      0.000     -0.000     -4.505      4.505      0.000
   431         21  (g)                -51    79     0   609   609   611  2300     -2.849     -3.440      1.639      4.758      0.000
   432         21  (g)                -51    79     0   613   613  2300   612     -0.602      0.253     -0.495      0.819      0.000
   433         -1  (dbar)             -53   607   607    77    77     0   612     -0.000     -0.000   -233.776    233.776      0.000
   434         21  (g)                -51   427     0   791   791  2303  2247     -0.430      0.080    175.881    175.881      0.000
   435         21  (g)                -51   427     0   792   792   977  2303      0.116     -0.611     21.396     21.405      0.000
   436         21  (g)                -52   422   422   503   504   980   977     -1.263      1.115      1.776      2.448      0.000
   437         21  (g)                -51   406     0   766   766  2312  2200      0.855     -0.363    -17.361     17.386      0.000
   438         21  (g)                -51   406     0   767   767  1449  2312     -0.425     -0.379     -8.927      8.946      0.000
   439         21  (g)                -52   407   407   517   517   814  1449      0.109      0.708     -1.706      1.850      0.000
   440         21  (g)                -51   297     0   801   801  1571  2344     -0.617     -0.228    171.474    171.476      0.000
   441         21  (g)                -51   297     0   520   520  2344  1401     -0.140      0.598      7.442      7.467      0.000
   442         21  (g)                -52   296   296   518   519  1401   987      0.177     -0.708    -10.230     10.256      0.000
   443         21  (g)                -51   350     0   731   731  1816  2351     -0.569     -0.099    -22.420     22.427      0.000
   444         21  (g)                -51   350     0   733   733  2351   915      0.391     -0.575     -6.063      6.103      0.000
   445          3  (s)                -52   345   345   726   726   915     0      1.734     -0.312     -4.842      5.177      0.500
   446         -2  (ubar)             -41   825   825   457   305     0  2354      0.000      0.000    851.152    851.152      0.000
   447         21  (g)                -42   826   826   306   306  1121  1589     -0.000      0.000    -94.894     94.894      0.000
   448         -2  (ubar)             -44   393   393   467   468     0  2056      0.294     -1.739    442.703    442.707      0.330
   449         21  (g)                -44   414   414   572   573  2219  1122      1.449      1.670     -2.645      3.447      0.000
   450         21  (g)                -44   416   416   829   829  1123  1153     -0.547     -0.020      6.597      6.619      0.000
   451         21  (g)                -44   310   310   574   574  1122  1318     -0.887      0.314      2.658      2.820      0.000
   452         21  (g)                -44   373   373   831   831  1318  1405     -0.850     -1.164    -11.364     11.455      0.000
   453         21  (g)                -44   371   371   832   832  1956  1589      0.773      0.406    -31.438     31.451      0.000
   454         21  (g)                -44   372   372   833   833  1405  1956     -0.456      0.188    -48.453     48.455      0.000
   455         21  (g)                -44   394   394   469   469  2056  1123     -0.055      0.119    200.608    200.608      0.000
   456         21  (g)                -44   415   415   835   835  1153  2219      0.741     -0.154     -0.125      0.767      0.000
   457         21  (g)                -43   446     0   836   836  1121  2354     -0.463      0.379    197.716    197.717      0.000
   458         21  (g)                -51   264     0   494   495  1415  2355     -0.967     -0.122     -1.004      1.399      0.000
   459         21  (g)                -51   264     0   463   463  2355   812      0.440     -0.191     -0.733      0.876      0.000
   460         21  (g)                -52   265   265   461   462   812   811     -1.110      1.721   -185.625    185.636      0.000
   461         21  (g)                -51   460     0   751   751  2372   811     -1.148      0.995    -95.119     95.131      0.000
   462         21  (g)                -51   460     0   512   513   812  2372      0.050      0.722    -90.525     90.528      0.000
   463         21  (g)                -52   459   459   514   514  2355   812      0.428     -0.186     -0.713      0.853      0.000
   464         21  (g)                -51    80     0   610   610  2373   744     -0.702      1.620     -0.402      1.810      0.000
   465         21  (g)                -51    80     0   566   567   610  2373      0.293      0.675     -1.945      2.080      0.000
   466         21  (g)                -52   419   419   568   568   613   610      2.919     -1.042   -130.765    130.802      0.000
   467         -2  (ubar)             -51   448     0   827   827     0  2437     -0.385     -0.338    165.066    165.067      0.330
   468         21  (g)                -51   448     0   837   837  2437  2056      0.640     -1.315    420.876    420.879      0.000
   469         21  (g)                -52   455   455   834   834  2056  1123     -0.016      0.034     57.368     57.368      0.000
   470         21  (g)                -51   398     0   698   698   686  2449      0.073      1.358     -7.040      7.170      0.000
   471         21  (g)                -51   398     0   705   705  2449   729      0.970      0.696     -4.455      4.612      0.000
   472         21  (g)                -53   526   526   168   168  1133   729      0.000     -0.000   -330.049    330.049      0.000
   473         21  (g)                -51   211     0   562   562  1295  2464     -0.249      0.672     -1.431      1.600      0.000
   474         21  (g)                -51   211     0   560   561  2464   735     -0.207      0.085      0.713      0.747      0.000
   475         21  (g)                -52   212   212   629   629   735   733      1.943      1.093      9.225      9.491      0.000
   476         21  (g)                -51   429     0   874   874  2477  1581     -0.421     -0.045      1.529      1.587      0.000
   477         21  (g)                -51   429     0   875   875  2262  2477      0.286      0.407      0.210      0.540      0.000
   478         -3  (sbar)             -52   428   428   872   872     0  2262      0.453      0.408      2.559      2.678      0.500
   479         21  (g)                -51   388     0   506   507  2485  1233     -0.388     -0.280      9.476      9.488      0.000
   480         21  (g)                -51   388     0   508   508   701  2485      0.734     -0.283     63.460     63.465      0.000
   481         21  (g)                -52   342   342   723   723   699   701      3.424      0.291    212.931    212.958      0.000
   482         21  (g)                -51   378     0   583   583   501  2495     -0.136      0.472     16.583     16.590      0.000
   483         21  (g)                -51   378     0   581   582  2495  1987      1.437      2.014     46.203     46.270      0.000
   484         21  (g)                -52   377   377   663   663  1987   511      3.615     11.916    199.183    199.572      0.000
   485         21  (g)                -51    91     0   678   678   606  2500      2.628      2.041    -34.115     34.277      0.000
   486         21  (g)                -51    91     0   681   681  2500   841      0.588     -0.113     -9.753      9.772      0.000
   487          3  (s)                -52   374   374   675   675   841     0      0.063      0.203     -0.047      0.545      0.500
   488         21  (g)                -51   344     0   500   501   700  2509     -2.244     -1.744      0.213      2.850      0.000
   489         21  (g)                -51   344     0   735   735  2509   788     -0.189      0.346     -0.968      1.046      0.000
   490         21  (g)                -53   721   721   340   340  1816   788     -0.000     -0.000    -37.260     37.260      0.000
   491         21  (g)                -51   173     0   532   532   749  2541      0.389     -2.693    -27.644     27.778      0.000
   492         21  (g)                -51   173     0   577   577  2541   684      0.250     -0.150      0.131      0.320      0.000
   493         21  (g)                -52   171   171   575   576   684   694      0.927     -1.120     19.715     19.769      0.000
   494         21  (g)                -51   458     0   752   752  2546  2355     -0.135      0.366     -0.148      0.417      0.000
   495         21  (g)                -51   458     0   755   755  1415  2546     -0.528     -0.745     -1.178      1.490      0.000
   496         -1  (dbar)             -52   263   263   750   750     0  1415      1.333     -1.152     -1.477      2.322      0.330
   497         21  (g)                -51   334     0   887   887  2549  1713     -0.384     -0.204     -0.179      0.470      0.000
   498         21  (g)                -51   334     0   888   888  1733  2549      0.730      0.220     -0.142      0.776      0.000
   499         -1  (dbar)             -52   333   333   885   885     0  1733     -0.465      0.753      1.365      1.660      0.330
   500         -1  (dbar)             -51   488     0   725   725     0  2509     -0.679      0.049      0.584      0.956      0.330
   501          1  (d)                -51   488     0   736   736   700     0     -1.655     -1.818      0.218      2.490      0.330
   502         21  (g)                -52   386   386   727   727  2047   700     -1.246     -0.348      8.124      8.226      0.000
   503         21  (g)                -51   436     0   786   786  2578   977      0.016      0.702      0.044      0.704      0.000
   504         21  (g)                -51   436     0   793   793   980  2578     -1.279      0.413      1.478      1.998      0.000
   505         21  (g)                -53   785   785   421   421   980  1053     -0.000     -0.000    -37.020     37.020      0.000
   506         21  (g)                -51   479     0   722   722  2583  1233     -0.142     -0.332      4.496      4.510      0.000
   507         21  (g)                -51   479     0   737   737  2485  2583      0.230     -0.132     46.047     46.048      0.000
   508         21  (g)                -52   480   480   734   734   701  2485      0.259     -0.100     22.393     22.395      0.000
   509         21  (g)                -51   315     0   601   601  2627  1593      0.034     -0.441     -6.073      6.090      0.000
   510         21  (g)                -51   315     0   533   534  1596  2627     -0.691      0.666     -6.454      6.524      0.000
   511         21  (g)                -52   316   316   535   535  1595  1596      0.657     -0.225    -43.549     43.555      0.000
   512         21  (g)                -51   462     0   754   754  2669  2372      0.246     -0.152    -45.776     45.777      0.000
   513         21  (g)                -51   462     0   756   756   812  2669     -0.176      0.864    -44.783     44.791      0.000
   514         21  (g)                -52   463   463   753   753  2355   812      0.408     -0.177     -0.679      0.812      0.000
   515          2  (u)                -51   275     0   761   761   975     0      1.152     -1.382     86.526     86.546      0.330
   516         -2  (ubar)             -51   275     0   538   538     0   814     -0.305      0.123     13.054     13.062      0.330
   517         21  (g)                -52   439   439   536   537   814  1449      0.108      0.705     -1.698      1.842      0.000
   518         -2  (ubar)             -51   442     0   800   800     0   987      0.469     -0.138     -4.920      4.955      0.330
   519          2  (u)                -51   442     0   565   565  1401     0     -0.293     -0.568     -5.282      5.330      0.330
   520         21  (g)                -52   441   441   563   564  2344  1401     -0.140      0.596      7.413      7.438      0.000
   521         21  (g)                -51   343     0   724   724  1317  2726     -1.683      1.167    498.149    498.153      0.000
   522         21  (g)                -51   343     0   738   738  2726   721      0.208      0.271    129.412    129.413      0.000
   523         21  (g)                -53   720   720   339   339   699   721      0.000      0.000    932.906    932.906      0.000
   524         21  (g)                -51   176     0   702   702  2761   765      1.090     -0.986   -167.707    167.713      0.000
   525         21  (g)                -51   176     0   707   707  1133  2761     -0.147      0.159    -52.950     52.950      0.000
   526         21  (g)                -53   694   694   472   472  1133   729      0.000     -0.000   -436.405    436.405      0.000
   527         21  (g)                -51   423     0   787   787  2782  1261      0.605      0.330     -1.169      1.357      0.000
   528         21  (g)                -51   423     0   794   794  1734  2782      0.944      0.049     -0.100      0.951      0.000
   529         21  (g)                -52   426   426   790   790   978  1734      0.564      0.725     -0.549      1.070      0.000
   530         21  (g)                -51   170     0   548   549   685  2806     -1.219      0.905    -50.545     50.568      0.000
   531         21  (g)                -51   170     0   708   708  2806   749     -0.288     -0.386    -24.961     24.966      0.000
   532         21  (g)                -52   491   491   699   699   749  2541      0.364     -2.525    -25.917     26.042      0.000
   533         21  (g)                -51   510     0   603   603  2818  2627     -0.739      0.046     -5.390      5.441      0.000
   534         21  (g)                -51   510     0   604   604  1596  2818      0.161      0.581     -8.549      8.570      0.000
   535         21  (g)                -52   511   511   602   602  1595  1596      0.544     -0.186    -36.064     36.068      0.000
   536         21  (g)                -51   517     0   764   764  2821  1449      0.478     -0.106     -0.201      0.529      0.000
   537         21  (g)                -51   517     0   769   769   814  2821     -0.375      0.813     -1.262      1.548      0.000
   538         -2  (ubar)             -52   516   516   768   768     0   814     -0.300      0.121     12.819     12.827      0.330
   539         21  (g)                -51   281     0   640   640  2823  1512      0.009     -0.240      6.187      6.192      0.000
   540         21  (g)                -51   281     0   642   642   690  2823     -0.835      1.020     43.449     43.469      0.000
   541         21  (g)                -52   282   282   637   637   692   690     -0.273      0.330     11.342     11.350      0.000
   542         21  (g)                -51   362     0   774   774   929  2841      1.633     -0.890     -1.450      2.358      0.000
   543         21  (g)                -51   362     0   777   777  2841   930     -0.197      0.172     -0.131      0.293      0.000
   544         21  (g)                -52   363   363   775   775   930  1358     -0.795      0.111      0.513      0.952      0.000
   545         21  (g)                -51   285     0   586   586  1188  2882      1.237     -0.864     -0.433      1.570      0.000
   546         21  (g)                -51   285     0   589   589  2882  1191     -0.170      0.255     -0.224      0.380      0.000
   547         21  (g)                -52   286   286   587   587  1191  1190     -1.005     -0.251     -3.907      4.042      0.000
   548         21  (g)                -51   530     0   696   696  2892  2806     -1.362      0.765    -62.549     62.568      0.000
   549         21  (g)                -51   530     0   709   709   685  2892      0.169     -0.189     -4.944      4.950      0.000
   550         21  (g)                -52   174   174   700   700   765   685      0.120     -1.553    -79.996     80.011      0.000
   551         21  (g)                -51   213     0   664   664  1118  2905      0.394     -0.527     -4.189      4.240      0.000
   552         21  (g)                -51   213     0   671   671  2905  1309      9.281     -5.619    -94.417     95.038      0.000
   553         21  (g)                -52   401   401   666   666  1309   502     -0.119      0.095     -2.490      2.494      0.000
   554         21  (g)                -51   402     0   863   863  2919  2192      0.060      0.067     -0.046      0.101      0.000
   555         21  (g)                -51   402     0   865   865  1420  2919     -0.197      0.395      9.985      9.995      0.000
   556         21  (g)                -52   385   385   861   861  1866  1420     -0.567     -0.376    175.506    175.508      0.000
   557         21  (g)                -51   410     0   652   652  1202  2938     -0.892     -0.223     -0.399      1.002      0.000
   558         21  (g)                -51   410     0   656   656  2938  1342     -0.158     -0.640     -1.544      1.679      0.000
   559          2  (u)                -52   288   288   653   653  1342     0      0.467     -0.293     -9.750      9.771      0.330
   560         21  (g)                -51   474     0   632   632  2941   735     -0.392     -0.327      0.223      0.557      0.000
   561         21  (g)                -51   474     0   633   633  2464  2941      0.119      0.589      0.113      0.612      0.000
   562         21  (g)                -52   473   473   631   631  1295  2464     -0.183      0.495     -1.054      1.178      0.000
   563         21  (g)                -51   520     0   802   802  2344  2946      0.073      0.866      4.613      4.694      0.000
   564         21  (g)                -51   520     0   804   804  2946  1401     -0.215     -0.274      2.761      2.783      0.000
   565          2  (u)                -52   519   519   803   803  1401     0     -0.291     -0.563     -5.243      5.291      0.330
   566         21  (g)                -51   465     0   614   614  2958  2373     -0.014      0.916     -4.047      4.149      0.000
   567         21  (g)                -51   465     0   615   615   610  2958      0.447     -0.291     -4.172      4.206      0.000
   568         21  (g)                -52   466   466   608   608   613   610      2.779     -0.992   -124.492    124.527      0.000
   569         21  (g)                -51   304     0   762   762  3064  1310     -0.484      0.612   -114.197    114.199      0.000
   570         21  (g)                -51   304     0   770   770  1437  3064     -0.263     -0.315   -147.816    147.817      0.000
   571         21  (g)                -52   303   303   765   765  1583  1437      0.299      0.037     -3.975      3.987      0.000
   572         21  (g)                -51   449     0   828   828  2219  3106      0.947      1.552     -2.573      3.150      0.000
   573         21  (g)                -51   449     0   838   838  3106  1122      0.446      0.139      0.099      0.477      0.000
   574         21  (g)                -52   451   451   830   830  1122  1318     -0.831      0.294      2.489      2.640      0.000
   575         21  (g)                -51   493     0   697   697  3114   694      0.507     -0.139     11.132     11.145      0.000
   576         21  (g)                -51   493     0   710   710   684  3114      0.458     -1.004      8.603      8.674      0.000
   577         21  (g)                -52   492   492   706   706  2541   684      0.211     -0.126      0.110      0.270      0.000
   578         21  (g)                -51   413     0   850   850  3120  2016      0.312      0.254      1.636      1.685      0.000
   579         21  (g)                -51   413     0   852   852  1357  3120     -0.696     -0.023     16.583     16.598      0.000
   580         -2  (ubar)             -52   382   382   849   849     0  1357      0.252      0.855      0.524      1.086      0.330
   581         21  (g)                -51   483     0   670   670  3139  1987      0.726      1.039     17.584     17.630      0.000
   582         21  (g)                -51   483     0   672   672  2495  3139      0.609      1.328     41.002     41.028      0.000
   583         21  (g)                -52   482   482   668   668   501  2495     -0.034      0.119      4.200      4.202      0.000
   584         21  (g)                -41   839   839   590   283  3168  1522      0.000      0.000     16.246     16.246      0.000
   585         21  (g)                -42   840   840   284   284  1189  1190      0.000      0.000     -5.358      5.358      0.000
   586         21  (g)                -44   545   545   841   841  1188  2882      1.312     -0.912     -0.548      1.689      0.000
   587         21  (g)                -44   547   547   842   842  1191  1190     -0.996     -0.257     -3.835      3.970      0.000
   588         21  (g)                -44   287   287   843   843  1189  1522      0.244      0.664      2.277      2.384      0.000
   589         21  (g)                -44   546   546   844   844  2882  1191     -0.159      0.249     -0.201      0.357      0.000
   590         21  (g)                -43   584     0   845   845  3168  1188     -0.401      0.256     13.195     13.204      0.000
   591          3  (s)                -31   894   894   593   594  3171     0      0.000      0.000      0.051      0.051      0.000
   592          1  (d)                -31   895   895   593   594  3172     0      0.000      0.000   -140.130    140.130      0.000
   593          3  (s)                -33   591   592   896   896  3172     0     -0.321     -0.338     -2.256      2.357      0.500
   594          1  (d)                -33   591   592   897   897  3171     0      0.321      0.338   -137.824    137.825      0.330
   595         21  (g)                -31   898   898   597   598  3175  3176      0.000      0.000      0.030      0.030      0.000
   596         21  (g)                -31   899   899   597   598  3177  3178      0.000      0.000    -72.481     72.481      0.000
   597         21  (g)                -33   595   596   900   900  3175  3178      0.364      0.294    -70.612     70.614      0.000
   598         21  (g)                -33   595   596   901   901  3177  3176     -0.364     -0.294     -1.839      1.898      0.000
   599         21  (g)                -42   876   876   313   313  1594  1593      0.000      0.000      0.046      0.046      0.000
   600         21  (g)                -41   877   877   605   314  1595  3191     -0.000     -0.000   -171.662    171.662      0.000
   601         21  (g)                -44   509   509   878   878  2627  1593      0.076     -0.426     -6.222      6.237      0.000
   602         21  (g)                -44   535   535   879   879  1595  1596      0.791     -0.095    -36.937     36.946      0.000
   603         21  (g)                -44   533   533   880   880  2818  2627     -0.702      0.060     -5.524      5.569      0.000
   604         21  (g)                -44   534   534   881   881  1596  2818      0.220      0.603     -8.756      8.779      0.000
   605         21  (g)                -43   600     0   882   882  1594  3191     -0.384     -0.141   -114.176    114.177      0.000
   606         21  (g)                -41   682   682   616    76  3193   744      0.000      0.000     44.055     44.055      0.000
   607         -1  (dbar)             -42   683   683   433   433     0   612     -0.000     -0.000   -233.776    233.776      0.000
   608         21  (g)                -44   568   568   684   684   613   610      2.780     -0.990   -124.528    124.563      0.000
   609         21  (g)                -44   431   431   685   685   611  2300     -2.664     -3.193      1.847      4.550      0.000
   610         21  (g)                -44   464   464   686   686  2373   744     -0.661      1.674     -0.445      1.854      0.000
   611         -1  (dbar)             -44   417   417   687   687     0  2240      0.317      1.123    -74.286     74.296      0.330
   612         21  (g)                -44   418   418   688   688  2240   613      0.625      0.812    -23.452     23.474      0.000
   613         21  (g)                -44   432   432   689   689  2300   612     -0.593      0.266     -0.487      0.812      0.000
   614         21  (g)                -44   566   566   690   690  2958  2373     -0.011      0.920     -4.082      4.184      0.000
   615         21  (g)                -44   567   567   691   691   610  2958      0.448     -0.290     -4.173      4.207      0.000
   616         21  (g)                -43   606     0   692   692  3193   611     -0.240     -0.321     39.887     39.889      0.000
   617         21  (g)                -31   902   902   619   620  3201  3200      0.000      0.000      0.011      0.011      0.000
   618         21  (g)                -31   903   903   619   620  3203  3202      0.000      0.000    -23.640     23.640      0.000
   619         21  (g)                -33   617   618   904   904  3203  3200     -0.017     -0.367    -19.977     19.980      0.000
   620         21  (g)                -33   617   618   905   905  3201  3202      0.017      0.367     -3.652      3.671      0.000
   621         -1  (dbar)             -42   889   889   389   389     0  2049      0.000      0.000      0.192      0.192      0.000
   622          2  (u)                -41   890   890   625   390  2051     0     -0.000     -0.000     -7.116      7.116      0.000
   623         -1  (dbar)             -44   391   391   891   891     0  2050     -0.628     -0.224     -0.756      1.061      0.330
   624         21  (g)                -44   392   392   892   892  2051  2049      0.571     -0.001     -2.928      2.983      0.000
   625          2  (u)                -43   622     0   893   893  2050     0      0.057      0.225     -3.240      3.265      0.330
   626         21  (g)                -42   739   739    50    50   732   733      0.000      0.000     10.463     10.463      0.000
   627         21  (g)                -41   740   740   634    51  3216   732      0.000      0.000    -29.271     29.271      0.000
   628         21  (g)                -44    98    98   741   741   734   851     -3.262     -1.381    -20.121     20.430      0.000
   629         21  (g)                -44   475   475   742   742   735   733      1.943      1.095      9.202      9.469      0.000
   630         21  (g)                -44   210   210   743   743   851  1295      1.828     -0.224     -6.656      6.906      0.000
   631         21  (g)                -44   562   562   744   744  1295  2464     -0.181      0.505     -1.055      1.184      0.000
   632         21  (g)                -44   560   560   745   745  2941   735     -0.391     -0.326      0.219      0.554      0.000
   633         21  (g)                -44   561   561   746   746  2464  2941      0.120      0.592      0.114      0.614      0.000
   634         21  (g)                -43   627     0   747   747  3216   734     -0.057     -0.261     -0.511      0.577      0.000
   635         21  (g)                -41   711   711   643    93   692  3220     -0.000      0.000    121.567    121.567      0.000
   636         -2  (ubar)             -42   712   712   358   358     0   843      0.000      0.000     -0.868      0.868      0.000
   637         21  (g)                -44   541   541   713   713   692   690     -0.238      0.338     11.352     11.359      0.000
   638         -2  (ubar)             -44    96    96   714   714     0   691      1.188     -2.900      2.344      3.927      0.330
   639          1  (d)                -44   356   356   715   715  1512     0      0.115      1.524     10.914     11.026      0.330
   640         21  (g)                -44   539   539   716   716  2823  1512      0.029     -0.236      6.193      6.197      0.000
   641         -1  (dbar)             -44   357   357   717   717     0   843     -0.126      0.283     10.908     10.917      0.330
   642         21  (g)                -44   540   540   718   718   690  2823     -0.699      1.049     43.488     43.506      0.000
   643         21  (g)                -43   635     0   719   719   691  3220     -0.269     -0.059     35.500     35.501      0.000
   644         -2  (ubar)             -31   906   906   646   647     0  3232      0.000      0.000      0.049      0.049      0.000
   645         21  (g)                -31   907   907   646   647  3234  3233      0.000      0.000     -2.812      2.812      0.000
   646         -2  (ubar)             -33   644   645   908   908     0  3233     -0.006      0.178     -0.732      0.823      0.330
   647         21  (g)                -33   644   645   909   909  3234  3232      0.006     -0.178     -2.030      2.038      0.000
   648         21  (g)                -41   810   810   657   152  3236  1078     -0.000     -0.000    192.974    192.974      0.000
   649          2  (u)                -42   811   811   153   153  1078     0     -0.000      0.000   -187.345    187.345      0.000
   650         21  (g)                -44   408   408   812   812  1079  2202      1.771      1.434     45.465     45.522      0.000
   651          2  (u)                -44   290   290   813   813  1080     0     -0.772     -0.815   -156.472    156.477      0.330
   652         21  (g)                -44   557   557   814   814  1202  2938     -0.891     -0.223     -0.397      1.000      0.000
   653          2  (u)                -44   559   559   815   815  1342     0      0.467     -0.293     -9.751      9.772      0.330
   654         -2  (ubar)             -44   289   289   816   816     0  1080     -0.532      1.034    -18.741     18.780      0.330
   655         21  (g)                -44   409   409   817   817  2202  1202      0.329     -0.482      7.862      7.883      0.000
   656         21  (g)                -44   558   558   818   818  2938  1342     -0.157     -0.640     -1.544      1.678      0.000
   657         21  (g)                -43   648     0   819   819  3236  1079     -0.215     -0.016    139.207    139.207      0.000
   658          1  (d)                -61     1     0   379   379  2056     0      1.362     -4.993   1859.448   1859.455      0.000
   659         -3  (sbar)             -61     2     0   181   181     0   612      0.989     -0.810   -477.398    477.400      0.000
   660         25  (h0)               -62   182   182   928   929     0     0    -51.812    -74.353    242.491    287.471    125.001
   661          2  (u)                -62   249   249  1177  1177  1403     0      2.675      8.086    136.233    136.499      0.330
   662         -4  (cbar)             -62   184   184  1214  1214     0  1118     14.310    -11.789   -162.163    163.226      1.500
   663         21  (g)                -62   484   484  1179  1179  1987   511      3.761     11.380    199.192    199.552      0.000
   664         21  (g)                -62   551   551   969     0  1118  2351      0.403     -0.534     -4.189      4.242      0.000
   665         21  (g)                -62   399   399  1283  1283  2152   612      0.400     -0.062    -82.487     82.488      0.000
   666         21  (g)                -62   553   553   949     0  1309  2892     -0.114      0.091     -2.490      2.494      0.000
   667         21  (g)                -62   250   250  1178  1178   511  1403     22.233     66.119   1194.003   1196.039      0.000
   668         21  (g)                -62   583   583  1009     0   501  3193     -0.031      0.108      4.200      4.202      0.000
   669         21  (g)                -62   400   400  1286  1286   502  2200     -0.328     -1.277   -106.916    106.924      0.000
   670         21  (g)                -62   581   581  1180  1180  3139  1987      0.739      0.992     17.585     17.629      0.000
   671         21  (g)                -62   552   552  1212  1212  2905  1583      9.478     -5.780    -94.413     95.063      0.000
   672         21  (g)                -62   582   582  1182  1182  2495  1079      0.639      1.217     41.003     41.026      0.000
   673         21  (g)                -61     1     0    17    17   605   605     -0.361      3.402      3.675      5.021      0.000
   674         21  (g)                -61     2     0   319   319   659   659     -1.286      0.375    -50.812     50.830      0.000
   675          3  (s)                -62   487   487  1146  1146   841     0      0.033      0.402     -0.160      0.662      0.500
   676         21  (g)                -62   317   317  1127  1127   604  1628     -3.802     -0.884     -0.747      3.974      0.000
   677         21  (g)                -62   376   376  1006     0   603  2919      1.576      1.619     -0.864      2.419      0.000
   678         21  (g)                -62   485   485   960     0   606  2051      1.746      2.356    -34.718     34.841      0.000
   679         21  (g)                -62   318   318   981     0  1628  2941     -1.895     -0.714      0.764      2.164      0.000
   680         -3  (sbar)             -62   375   375   989     0     0  2219      0.353      1.033     -1.754      2.126      0.500
   681         21  (g)                -62   486   486   952     0  2500  1407      0.343     -0.035     -9.658      9.664      0.000
   682         21  (g)                -61     1     0   606   606   612   744     -0.158      1.809     44.032     44.070      0.000
   683         -1  (dbar)             -61     2     0   607   607     0   612     -0.833     -1.971   -233.755    233.765      0.000
   684         21  (g)                -62   608   608  1289  1289   613   987      2.336     -2.039   -124.493    124.531      0.000
   685         21  (g)                -62   609   609  1125  1125   611   700     -2.681     -3.073      1.924      4.509      0.000
   686         21  (g)                -62   610   610  1149  1149  2373  2578     -0.668      1.693     -0.487      1.884      0.000
   687         -1  (dbar)             -62   611   611  1227  1227     0   744      0.052      0.497    -74.307     74.310      0.330
   688         21  (g)                -62   612   612   948     0  2240  1956      0.542      0.615    -23.470     23.484      0.000
   689         21  (g)                -62   613   613   980     0  2300  2546     -0.596      0.267     -0.494      0.819      0.000
   690         21  (g)                -62   614   614   959     0  2958   686     -0.026      0.887     -4.104      4.199      0.000
   691         21  (g)                -62   615   615   967     0   610  2905      0.433     -0.324     -4.166      4.201      0.000
   692         21  (g)                -62   616   616  1011     0  3193   690     -0.383      1.317     39.874     39.898      0.000
   693         21  (g)                -61     1     0   322   322   729   729      1.427     -1.697     58.406     58.448      0.000
   694         21  (g)                -61     2     0   526   526  1004  1004     -0.293     -0.642   -436.398    436.398      0.000
   695         21  (g)                -62   396   396   968     0  1661  1714     -0.034     -0.107     -0.728      0.737      0.000
   696         21  (g)                -62   548   548   955     0  2892  2372     -1.404      0.673    -62.520     62.539      0.000
   697         21  (g)                -62   575   575   998     0  3114   694      0.779     -0.463     11.120     11.157      0.000
   698         21  (g)                -62   470   470   959     0   686   813      0.070      1.346     -7.022      7.150      0.000
   699         21  (g)                -62   532   532   966     0   749  2627      0.348     -2.565    -25.956     26.084      0.000
   700         21  (g)                -62   550   550   956     0   765  3203      0.067     -1.671    -80.018     80.035      0.000
   701         21  (g)                -62   175   175   998     0   694  2202      2.094     -1.886     35.999     36.109      0.000
   702         21  (g)                -62   524   524   951     0  2761  1816      0.977     -1.232   -167.732    167.739      0.000
   703         21  (g)                -62   321   321  1152  1152   683  1289     -1.001      1.091      0.473      1.554      0.000
   704         21  (g)                -62   397   397  1150  1150  2107  2373     -2.296      3.714     -2.982      5.287      0.000
   705         21  (g)                -62   471   471  1029  1029  2449   989      0.969      0.688     -4.457      4.613      0.000
   706         21  (g)                -62   577   577  1007     0  2541  1083      0.216     -0.132      0.106      0.274      0.000
   707         21  (g)                -62   525   525   946     0  1133  1437     -0.183      0.081    -52.945     52.945      0.000
   708         21  (g)                -62   531   531   945     0  2806   502     -0.305     -0.423    -24.963     24.968      0.000
   709         21  (g)                -62   549   549   965     0   685   997      0.165     -0.197     -4.948      4.955      0.000
   710         21  (g)                -62   576   576   999     0   684  1679      0.669     -1.255      8.581      8.698      0.000
   711         21  (g)                -61     1     0   635   635   843  3220      0.095      0.841    121.376    121.379      0.000
   712         -2  (ubar)             -61     2     0   636   636     0   843     -0.006     -0.813     -0.676      1.057      0.000
   713         21  (g)                -62   637   637  1010     0   692  1420     -0.229      0.412     11.177     11.186      0.000
   714         -2  (ubar)             -62   638   638  1198  1198     0  3220      1.186     -3.610      3.877      5.439      0.330
   715          1  (d)                -62   639   639   995     0  1512     0      0.123      1.543     10.190     10.312      0.330
   716         21  (g)                -62   640   640   991     0  2823  2583      0.034     -0.194      6.295      6.298      0.000
   717         -1  (dbar)             -62   641   641  1009     0     0   501     -0.117      0.353     10.759     10.770      0.330
   718         21  (g)                -62   642   642  1011     0   690   692     -0.666      1.338     42.930     42.956      0.000
   719         21  (g)                -62   643   643   943     0   691  2303     -0.241      0.187     35.473     35.475      0.000
   720         21  (g)                -61     1     0   523   523   788   788      0.417     -1.472    932.913    932.914      0.000
   721         21  (g)                -61     2     0   490   490   721   721      1.292     -0.137    -37.249     37.272      0.000
   722         21  (g)                -62   506   506   992     0  2583  2946     -0.140     -0.339      4.494      4.509      0.000
   723         21  (g)                -62   481   481  1409  1409   699  1409      3.519     -0.045    212.991    213.020      0.000
   724         21  (g)                -62   521   521  1404  1404  1317   691     -1.460      0.380    498.123    498.125      0.000
   725         -1  (dbar)             -62   500   500  1004     0     0   930     -0.672      0.047      0.573      0.944      0.330
   726          3  (s)                -62   445   445   988     0   915     0      1.908     -0.331     -4.810      5.210      0.500
   727         21  (g)                -62   502   502  1000     0  2047  1122     -1.240     -0.361      8.103      8.205      0.000
   728         21  (g)                -62   347   347  1003     0  1289  2841     -0.691      0.237      0.051      0.733      0.000
   729         21  (g)                -62   348   348   997     0   698  1233     -0.039      0.546      4.942      4.972      0.000
   730         -3  (sbar)             -62   349   349   976     0     0  2192      0.760      0.243     -0.729      1.191      0.500
   731         21  (g)                -62   443   443   951     0  1816  2152      0.209     -0.182    -22.423     22.424      0.000
   732         21  (g)                -62   387   387   993     0  1233  2344     -0.062      0.548      3.319      3.364      0.000
   733         21  (g)                -62   444   444   967     0  2351   610      0.602     -0.597     -6.054      6.113      0.000
   734         21  (g)                -62   508   508   942     0   701   699      0.269     -0.135     22.398     22.400      0.000
   735         21  (g)                -62   489   489   957     0  2509  2958     -0.154      0.342     -0.972      1.042      0.000
   736          1  (d)                -62   501   501  1124  1124   700     0     -1.615     -1.824      0.191      2.466      0.330
   737         21  (g)                -62   507   507   940     0  2485  1461      0.250     -0.205     46.051     46.052      0.000
   738         21  (g)                -62   522   522   941     0  2726  1571      0.265      0.066    129.416    129.417      0.000
   739         21  (g)                -61     1     0   626   626   732   732     -3.458      1.780     10.094     10.818      0.000
   740         21  (g)                -61     2     0   627   627   733   733      1.608     -0.686    -28.938     28.991      0.000
   741         21  (g)                -62   628   628   971     0   734  1318     -2.175     -1.840    -20.389     20.587      0.000
   742         21  (g)                -62   629   629  1249  1249   735  3168     -1.148      2.685      9.143      9.598      0.000
   743         21  (g)                -62   630   630   988     0   851   915      2.141     -0.353     -6.211      6.579      0.000
   744         21  (g)                -62   631   631   957     0  1295  2509     -0.137      0.488     -1.128      1.237      0.000
   745         21  (g)                -62   632   632   981     0  2941   611     -0.508     -0.265      0.164      0.596      0.000
   746         21  (g)                -62   633   633  1001     0  2464   603      0.014      0.647      0.070      0.651      0.000
   747         21  (g)                -62   634   634   979     0  3216  2938     -0.038     -0.268     -0.492      0.561      0.000
   748         -1  (dbar)             -61     1     0    82    82     0   612     -1.664     -1.249     -0.566      2.156      0.000
   749         21  (g)                -61     2     0    83    83   612   811     -0.848     -0.289   -189.955    189.957      0.000
   750         -1  (dbar)             -62   496   496  1106  1106     0   811      0.437     -1.821     -1.714      2.560      0.330
   751         21  (g)                -62   461   461   955     0  2372   812     -1.588      0.839    -95.550     95.567      0.000
   752         21  (g)                -62   494   494   980     0  2546  2549     -0.418      0.153     -0.231      0.502      0.000
   753         21  (g)                -62   514   514   987     0  2355   929      0.266     -0.282     -0.505      0.637      0.000
   754         21  (g)                -62   512   512   953     0  2669  2761      0.042     -0.222    -45.640     45.640      0.000
   755         21  (g)                -62   495   495   983     0  1415  1951     -0.868     -0.995     -2.584      2.902      0.000
   756         21  (g)                -62   513   513   950     0   812  1405     -0.383      0.790    -44.295     44.303      0.000
   757         21  (g)                -61     1     0   116   116  1310   815      0.018      0.134     99.850     99.850      0.000
   758          2  (u)                -61     2     0   117   117   815     0      0.145      1.860   -542.940    542.943      0.000
   759         21  (g)                -62   118   118  1089  1089   813  3201     -0.542      3.368    -18.647     18.956      0.000
   760          2  (u)                -62   216   216  1413  1413  1310     0      0.085     -1.096   -160.892    160.896      0.330
   761          2  (u)                -62   515   515  1411  1411   975     0      1.168     -1.266     86.524     86.542      0.330
   762         21  (g)                -62   569   569  1295  1295  3064  1594     -0.453      1.003   -114.197    114.202      0.000
   763         21  (g)                -62   405   405   953     0  2200  2669     -0.414     -0.457    -69.153     69.156      0.000
   764         21  (g)                -62   536   536   984     0  2821  1188      0.478     -0.104     -0.201      0.529      0.000
   765         21  (g)                -62   571   571   970     0  1583  2312      0.300      0.051     -3.975      3.987      0.000
   766         21  (g)                -62   437   437   970     0  2312   685      0.860     -0.304    -17.362     17.386      0.000
   767         21  (g)                -62   438   438   973     0  1449  1401     -0.423     -0.349     -8.928      8.945      0.000
   768         -2  (ubar)             -62   538   538   994     0     0  1357     -0.298      0.138     12.819     12.827      0.330
   769         21  (g)                -62   537   537   958     0   814  1295     -0.375      0.818     -1.262      1.550      0.000
   770         21  (g)                -62   570   570   947     0  1437  3175     -0.223      0.192   -147.817    147.818      0.000
   771          2  (u)                -61     1     0   359   359   928     0      0.675     -1.513      7.379      7.563      0.000
   772         -3  (sbar)             -61     2     0   360   360     0   928     -1.232      0.817     -2.768      3.139      0.000
   773          2  (u)                -62   361   361  1022  1022  1358     0      0.075     -1.104      6.113      6.221      0.330
   774         21  (g)                -62   542   542   987     0   929   851      0.848     -0.393     -1.912      2.128      0.000
   775         21  (g)                -62   544   544  1004     0   930   980     -0.802     -0.002      0.731      1.085      0.000
   776         -3  (sbar)             -62   364   364  1023  1023     0  1358     -0.410      0.601     -0.295      0.930      0.500
   777         21  (g)                -62   543   543  1003     0  2841  2107     -0.269      0.202     -0.026      0.337      0.000
   778         21  (g)                -61     1     0   147   147  1061  1061      1.151      1.517      8.119      8.339      0.000
   779         21  (g)                -61     2     0   325   325   972   972     -1.831      1.585    -17.307     17.476      0.000
   780         21  (g)                -62   323   323  1253  1253  1679  1123      0.923     -1.294      4.243      4.531      0.000
   781          2  (u)                -62   150   150  1056  1056   971     0     -0.643      0.937      1.685      2.059      0.330
   782         -2  (ubar)             -62   151   151   961     0     0  2023     -1.706      2.931    -16.890     17.230      0.330
   783         21  (g)                -62   324   324  1154  1154   970  2262      0.746      0.528      1.773      1.995      0.000
   784         21  (g)                -61     1     0   420   420  1053  1053     -1.646     -0.033    200.287    200.293      0.000
   785         21  (g)                -61     2     0   505   505  2247  2247      0.777      1.451    -37.000     37.037      0.000
   786         21  (g)                -62   503   503  1001     0  2578  2464      0.020      0.715      0.058      0.718      0.000
   787         21  (g)                -62   527   527   975     0  2782  2449      0.631      0.379     -1.153      1.368      0.000
   788         21  (g)                -62   424   424   944     0   979  2500      0.760      0.004    -32.623     32.632      0.000
   789         21  (g)                -62   425   425   982     0  1261  2300     -0.587     -0.366     -1.101      1.300      0.000
   790         21  (g)                -62   529   529  1002     0   978   841      0.579      0.756     -0.526      1.088      0.000
   791         21  (g)                -62   434   434   943     0  2303  2211     -1.876      0.052    175.865    175.875      0.000
   792         21  (g)                -62   435   435   991     0   977  2823     -0.060     -0.615     21.384     21.393      0.000
   793         21  (g)                -62   504   504  1008     0   980  1463     -1.288      0.423      1.468      1.998      0.000
   794         21  (g)                -62   528   528   986     0  1734  1153      0.952      0.070     -0.085      0.958      0.000
   795         21  (g)                -61     1     0   291   291   990   990      1.319      0.591    179.089    179.095      0.000
   796         21  (g)                -61     2     0   292   292   988   988      0.995     -1.703   -122.037    122.053      0.000
   797         21  (g)                -62   293   293   956     0   987   765      0.091     -2.648    -95.995     96.032      0.000
   798         -1  (dbar)             -62   294   294  1057  1057     0   971      1.601      0.157     -8.636      8.791      0.330
   799          1  (d)                -62   295   295  1028  1028   989     0     -0.199      1.268     -7.002      7.126      0.330
   800         -2  (ubar)             -62   518   518  1132  1132     0  3216      0.510     -0.207     -4.918      4.960      0.330
   801         21  (g)                -62   440   440  1401  1401  1571  1866      0.646      0.338    171.472    171.474      0.000
   802         21  (g)                -62   563   563   993     0  2344  3120      0.107      0.881      4.606      4.690      0.000
   803          2  (u)                -62   565   565   973     0  1401     0     -0.247     -0.637     -5.238      5.293      0.330
   804         21  (g)                -62   564   564   992     0  2946  3114     -0.194     -0.265      2.763      2.783      0.000
   805         -2  (ubar)             -61     1     0   129   129     0   811      0.440     -0.593     -8.246      8.279      0.000
   806          1  (d)                -61     2     0   130   130   811     0      0.133      0.211  -1477.847   1477.847      0.000
   807         -2  (ubar)             -62   206   206  1064  1064     0  1264      1.686     -0.529    -56.982     57.010      0.330
   808          1  (d)                -62   204   204  1063  1063  1264     0     -1.192      0.262  -1426.759   1426.760      0.330
   809         21  (g)                -62   205   205   965     0   997   749      0.079     -0.114     -2.352      2.356      0.000
   810         21  (g)                -61     1     0   648   648   811  1078      1.368     -3.918    192.966    193.010      0.000
   811          2  (u)                -61     2     0   649   649  1078     0      0.999     -0.283   -187.337    187.340      0.000
   812         21  (g)                -62   650   650  1181  1181  1079  3139      2.093      0.510     45.475     45.526      0.000
   813          2  (u)                -62   651   651  1105  1105   811     0      0.063     -1.052   -156.472    156.476      0.330
   814         21  (g)                -62   652   652   978     0  1202   604     -0.885     -0.230     -0.398      0.997      0.000
   815          2  (u)                -62   653   653  1086  1086  1342     0      0.519     -0.308     -9.754      9.778      0.330
   816         -2  (ubar)             -62   654   654  1299  1299     0  2818     -0.432      1.006    -18.730     18.764      0.330
   817         21  (g)                -62   655   655   999     0  2202   684      0.384     -0.642      7.857      7.892      0.000
   818         21  (g)                -62   656   656   979     0  2938  1415     -0.148     -0.643     -1.549      1.684      0.000
   819         21  (g)                -62   657   657  1258  1258  3236   977      0.772     -2.842    139.201    139.232      0.000
   820         21  (g)                -61     1     0   238   238  1355  1368      1.238      0.645      1.543      2.081      0.000
   821         -3  (sbar)             -61     2     0   239   239     0  1355      1.270     -1.128     -2.039      2.654      0.000
   822         21  (g)                -62   240   240  1007     0  1083   970      2.031     -0.163      1.094      2.313      0.000
   823         -3  (sbar)             -62   241   241  1351  1351     0  1368     -0.471     -0.223     -1.181      1.384      0.500
   824         21  (g)                -62   242   242   984     0  1082  2821      0.948     -0.097     -0.410      1.038      0.000
   825         -2  (ubar)             -61     1     0   446   446     0  1713      1.244     -1.171    851.149    851.151      0.000
   826         21  (g)                -61     2     0   447   447  1713  1589      0.502      1.356    -94.888     94.899      0.000
   827         -2  (ubar)             -62   467   467  1372  1372     0  1589     -0.143     -0.565    165.062    165.063      0.330
   828         21  (g)                -62   572   572   989     0  2219  1733      0.962      1.592     -2.559      3.164      0.000
   829         21  (g)                -62   450   450  1000     0  1123  2047     -0.537     -0.029      6.595      6.617      0.000
   830         21  (g)                -62   574   574  1251  1251  1122  1189     -0.826      0.291      2.489      2.639      0.000
   831         21  (g)                -62   452   452   974     0  1318  1449     -0.789     -1.001    -11.374     11.445      0.000
   832         21  (g)                -62   453   453   948     0  1956  1422      0.939      0.855    -31.432     31.457      0.000
   833         21  (g)                -62   454   454   950     0  1405  3064     -0.199      0.881    -48.449     48.458      0.000
   834         21  (g)                -62   469   469   939     0  2056  2016      0.068     -0.045     57.369     57.369      0.000
   835         21  (g)                -62   456   456   986     0  1153  1082      0.744     -0.148     -0.125      0.769      0.000
   836         21  (g)                -62   457   457  1403  1403  1121  1317     -0.174      0.107    197.718    197.718      0.000
   837         21  (g)                -62   468   468  1407  1407  2437  2485      1.255     -1.894    420.866    420.872      0.000
   838         21  (g)                -62   573   573   985     0  3106  1734      0.447      0.141      0.101      0.480      0.000
   839         21  (g)                -61     1     0   584   584  1190  1190     -1.598      1.313     16.095     16.227      0.000
   840         21  (g)                -61     2     0   585   585  1522  1522      1.160     -0.822     -5.200      5.391      0.000
   841         21  (g)                -62   586   586  1071  1071  1188  2355      1.477     -1.021     -0.207      1.807      0.000
   842         21  (g)                -62   587   587   968     0  1191  1661     -0.150     -0.857     -3.847      3.944      0.000
   843         21  (g)                -62   588   588  1250  1250  1189   735      0.029      0.842      2.217      2.372      0.000
   844         21  (g)                -62   589   589   958     0  2882   814     -0.103      0.209     -0.248      0.340      0.000
   845         21  (g)                -62   590   590  1248  1248  3168   698     -1.692      1.317     12.979     13.155      0.000
   846         21  (g)                -61     1     0   231   231  1355  1355     -0.009     -1.411    330.361    330.364      0.000
   847         -2  (ubar)             -61     2     0   232   232     0  1355     -0.691      1.934      3.051      3.678      0.000
   848         21  (g)                -62   411   411  1406  1406  2211  2437     -0.045     -2.306    224.710    224.722      0.000
   849         -2  (ubar)             -62   580   580  1328  1328     0  1355     -0.364      2.567      5.871      6.426      0.330
   850         21  (g)                -62   578   578   995     0  3120  1512      0.258      0.395      2.322      2.370      0.000
   851         21  (g)                -62   412   412   939     0  2016  2726      0.164     -0.082     83.314     83.315      0.000
   852         21  (g)                -62   579   579   994     0  1357  3236     -0.713     -0.051     17.195     17.210      0.000
   853         21  (g)                -61     1     0   259   259  1408  1408      1.175      0.811    113.661    113.670      0.000
   854         21  (g)                -61     2     0   260   260  1406  1406      1.388     -0.548    -15.683     15.754      0.000
   855         21  (g)                -62   261   261  1410  1410  1409   975      2.116      0.636    113.685    113.706      0.000
   856         21  (g)                -62   262   262   952     0  1407   613      0.447     -0.373    -15.707     15.718      0.000
   857         21  (g)                -61     1     0   365   365  1421  1421      0.655      1.311    185.761    185.767      0.000
   858         21  (g)                -61     2     0   366   366  1419  1419      1.487      0.702   -104.200    104.213      0.000
   859         21  (g)                -62   367   367   954     0  1422  1595      2.505      0.406   -100.157    100.189      0.000
   860         21  (g)                -62   404   404   961     0  2023  2882     -0.310      0.494     -2.211      2.286      0.000
   861         21  (g)                -62   556   556  1402  1402  1866  1121      0.052      0.862    175.504    175.506      0.000
   862         21  (g)                -62   370   370   982     0  1951  1261     -0.465     -0.459     -0.926      1.133      0.000
   863         21  (g)                -62   554   554  1002     0  2919   978      0.062      0.068     -0.046      0.102      0.000
   864         21  (g)                -62   403   403   975     0  2192  2782      0.459      0.176     -0.588      0.766      0.000
   865         21  (g)                -62   555   555  1010     0  1420  2495     -0.161      0.466      9.984      9.996      0.000
   866         21  (g)                -61     1     0   276   276  1464  1464     -0.441     -0.586     75.600     75.604      0.000
   867         21  (g)                -61     2     0   277   277  1462  1462      0.673      0.062      3.071      3.144      0.000
   868         21  (g)                -62   278   278   940     0  1461   701      0.505     -0.506     78.200     78.203      0.000
   869         21  (g)                -62   279   279  1005     0  1463  2477     -0.273     -0.018      0.471      0.545      0.000
   870         -3  (sbar)             -61     1     0   298   298     0   843     -0.306     -0.610      4.541      4.592      0.000
   871         -3  (sbar)             -61     2     0   430   430     0  1581     -0.393      0.927     -4.439      4.551      0.000
   872         -3  (sbar)             -62   478   478  1035  1035     0  1581      0.275      0.068      2.587      2.650      0.500
   873         -3  (sbar)             -62   301   301  1051  1051     0   843     -0.693      0.108     -4.261      4.348      0.500
   874         21  (g)                -62   476   476  1005     0  2477  2541     -0.528     -0.245      1.504      1.613      0.000
   875         21  (g)                -62   477   477  1153  1153  2262   683      0.247      0.385      0.273      0.533      0.000
   876         21  (g)                -61     1     0   599   599  3191  3191     -0.141      0.952     -4.843      4.937      0.000
   877         21  (g)                -61     2     0   600   600  1593  1593     -0.368      0.409   -172.385    172.386      0.000
   878         21  (g)                -62   601   601   964     0  2627  3234      0.049     -0.267     -2.591      2.605      0.000
   879         21  (g)                -62   602   602   944     0  1595   979      0.703      0.076    -35.453     35.460      0.000
   880         21  (g)                -62   603   603   949     0  2818  1309     -0.785      0.537     -9.516      9.563      0.000
   881         21  (g)                -62   604   604   962     0  1596   606      0.153      0.879    -15.870     15.895      0.000
   882         21  (g)                -62   605   605   946     0  1594  1133     -0.628      0.137   -113.799    113.801      0.000
   883         -1  (dbar)             -61     1     0   329   329     0  1712     -0.908      0.118      1.892      2.102      0.000
   884         21  (g)                -61     2     0   335   335  1712  1713     -1.684     -0.045    -13.979     14.080      0.000
   885         -1  (dbar)             -62   499   499  1018  1018     0  1713     -1.190      0.843      1.187      1.908      0.330
   886         21  (g)                -62   332   332   971     0  1714   734     -1.451     -0.811    -12.975     13.081      0.000
   887         21  (g)                -62   497   497   978     0  2549  1202     -0.500     -0.196     -0.251      0.593      0.000
   888         21  (g)                -62   498   498   985     0  1733  3106      0.549      0.237     -0.049      0.600      0.000
   889         -1  (dbar)             -61     1     0   621   621     0  1355      0.588     -1.199     -2.849      3.147      0.000
   890          2  (u)                -61     2     0   622   622  1355     0     -0.710      0.604     -4.304      4.404      0.000
   891         -1  (dbar)             -62   623   623  1014  1014     0  2050     -0.175     -1.180     -2.360      2.664      0.330
   892         21  (g)                -62   624   624   960     0  2051  1342      0.210      0.229     -3.150      3.165      0.000
   893          2  (u)                -62   625   625  1013  1013  2050     0     -0.157      0.355     -1.644      1.721      0.330
   894          3  (s)                -61     1     0   591   591  1355     0      0.129      0.278     -0.407      0.509      0.000
   895          1  (d)                -61     2     0   592   592  3172     0     -0.092      0.438   -140.920    140.920      0.000
   896          3  (s)                -62   593   593  1384  1384  3172     0     -0.193     -0.060     -1.396      1.497      0.500
   897          1  (d)                -62   594   594  1327  1327  1355     0      0.230      0.775   -139.930    139.933      0.330
   898         21  (g)                -61     1     0   595   595  3178  3178      0.357     -0.606     -4.050      4.111      0.000
   899         21  (g)                -61     2     0   596   596  3176  3176     -0.442     -0.094    -70.429     70.430      0.000
   900         21  (g)                -62   597   597   947     0  3175  2240     -0.054      0.189    -68.108     68.109      0.000
   901         21  (g)                -62   598   598   972     0  3177  1191     -0.032     -0.888     -6.371      6.432      0.000
   902         21  (g)                -61     1     0   617   617  3202  3202     -0.016     -0.052     -0.065      0.085      0.000
   903         21  (g)                -61     2     0   618   618  3200  3200     -0.472     -0.052    -26.261     26.266      0.000
   904         21  (g)                -62   619   619   945     0  3203  2806     -0.435     -0.421    -23.194     23.202      0.000
   905         21  (g)                -62   620   620   962     0  3201  1596     -0.053      0.317     -3.133      3.149      0.000
   906         -2  (ubar)             -61     1     0   644   644     0  1355     -0.538      0.077     -1.245      1.359      0.000
   907         21  (g)                -61     2     0   645   645  1355  3233      0.090      0.027     -2.004      2.006      0.000
   908         -2  (ubar)             -62   646   646  1043  1043     0  3233     -0.474      0.258     -1.813      1.920      0.330
   909         21  (g)                -62   647   647   964     0  3234  3177      0.025     -0.154     -1.436      1.444      0.000
   910          2  (u)                -63     1     0  1197  1197  3220     0      0.160      0.335    201.624    201.625      0.330
   911          1  (d)                -63     1     0  1114  1114  1712     0     -0.226      0.244      1.383      1.460      0.330
   912          2  (u)                -63     1     0  1017  1017  1713     0     -0.165      0.599      7.855      7.886      0.330
   913          2  (u)                -63     1     0  1350  1350  1368     0     -0.488      0.620    736.491    736.491      0.330
   914          3  (s)                -63     1     0  1338  1338  1078     0     -1.014      0.400     36.578     36.597      0.500
   915          1  (d)                -63     1     0  1236  1236  3245     0     -0.139      0.952    324.648    324.650      0.330
   916          1  (d)                -63     1     0  1383  1383   815     0     -0.193      0.502    178.569    178.570      0.330
   917         -3  (sbar)             -63     1     0  1237  1237     0  3245     -0.099      1.823      0.584      1.981      0.500
   918          2  (u)                -63     1     0  1226  1226   744     0     -0.251      0.050      2.637      2.670      0.330
   919          3  (s)                -63     2     0  1042  1042  3233     0      0.099     -0.028   -173.444    173.445      0.500
   920          1  (d)                -63     2     0  1050  1050   843     0     -0.354      0.155   -249.406    249.407      0.330
   921          2  (u)                -63     2     0  1371  1371  1589     0     -0.438     -0.626   -118.936    118.939      0.330
   922          3  (s)                -63     2     0  1382  1382  3252     0     -0.331     -0.096   -988.747    988.747      0.500
   923         -1  (dbar)             -63     2     0  1339  1339     0  1078     -0.371     -0.496    -24.840     24.850      0.330
   924          3  (s)                -63     2     0  1282  1282   612     0     -0.139     -0.548    -10.966     10.992      0.500
   925          2  (u)                -63     2     0  1034  1034  1581     0     -0.156     -0.100     -1.790      1.830      0.330
   926          3  (s)                -63     2     0  1412  1412   928     0     -0.312     -0.625   -649.419    649.419      0.500
   927         -2  (ubar)             -63     2     0  1115  1115     0  1712     -0.327     -0.373    -55.758     55.761      0.330
   928          5  (b)                -23   660     0   930   931   512     0    -33.348   -109.312    173.591    207.889      4.800
   929         -5  (bbar)             -23   660     0   932   932     0   512    -18.464     34.959     68.900     79.582      4.800
   930          5  (b)                -51   928     0   935   935  3297     0    -32.597   -108.598    171.344    205.519      4.800
   931         21  (g)                -51   928     0   933   934   512  3297     -0.854     -0.517      2.628      2.812      0.000
   932         -5  (bbar)             -52   929   929  1364  1364     0   512    -18.361     34.762     68.518     79.141      4.800
   933         21  (g)                -51   931     0   936   937   512  3321     -0.355      0.076      0.858      0.931      0.000
   934         21  (g)                -51   931     0   938   938  3321  3297     -2.254     -6.506     11.048     13.018      0.000
   935          5  (b)                -52   930   930   977     0  3297     0    -30.843   -102.684    162.067    194.381      4.800
   936         21  (g)                -51   933     0  1363  1363   512  3325     -0.108     -0.257      1.815      1.837      0.000
   937         21  (g)                -51   933     0  1362  1362  3325  3321     -0.997     -1.834      2.722      3.430      0.000
   938         21  (g)                -52   934   934   977     0  3321  3297     -1.503     -4.339      7.368      8.682      0.000
   939         21  (g)                -73   834   851   941     0  2056  2726      0.232     -0.127    140.683    140.683      0.055
   940         21  (g)                -73   737   868   942     0  2485   701      0.756     -0.711    124.251    124.255      0.137
   941         21  (g)                -73   738   939  1400  1400  2056  1571      0.497     -0.061    270.099    270.100      0.213
   942         21  (g)                -73   734   940  1408  1408  2485   699      1.025     -0.846    146.649    146.656      0.347
   943         21  (g)                -73   719   791  1405  1405   691  2211     -2.117      0.239    211.339    211.350      0.497
   944         21  (g)                -73   788   879   954     0  1595  2500      1.463      0.080    -68.076     68.092      0.137
   945         21  (g)                -73   708   904  1287  1287  3203   502     -0.740     -0.844    -48.157     48.170      0.161
   946         21  (g)                -73   707   882  1294  1294  1594  1437     -0.811      0.217   -166.744    166.746      0.163
   947         21  (g)                -73   770   900  1293  1293  1437  2240     -0.277      0.381   -215.926    215.926      0.165
   948         21  (g)                -73   688   832  1292  1292  2240  1422      1.481      1.470    -54.902     54.942      0.187
   949         21  (g)                -73   666   880  1298  1298  2818  2892     -0.899      0.628    -12.005     12.057      0.203
   950         21  (g)                -73   756   833  1296  1296   812  3064     -0.582      1.671    -92.744     92.761      0.210
   951         21  (g)                -73   702   731  1284  1284  2761  2152      1.186     -1.414   -190.154    190.163      0.218
   952         21  (g)                -73   681   856  1290  1290  2500   613      0.790     -0.409    -25.365     25.382      0.262
   953         21  (g)                -73   754   763  1285  1285  2200  2761     -0.372     -0.678   -114.793    114.797      0.400
   954         21  (g)                -73   859   944  1291  1291  1422  2500      3.968      0.486   -168.233    168.281      0.432
   955         21  (g)                -73   696   751  1297  1297  2892   812     -2.991      1.512   -158.070    158.107      0.476
   956         21  (g)                -73   700   797  1288  1288   987  3203      0.158     -4.319   -176.013    176.067      0.587
   957         21  (g)                -73   735   744   963     0  1295  2958     -0.291      0.830     -2.100      2.279      0.089
   958         21  (g)                -73   769   844   963     0  2882  1295     -0.478      1.028     -1.510      1.890      0.099
   959         21  (g)                -73   690   698  1090  1090  2958   813      0.045      2.233    -11.126     11.349      0.155
   960         21  (g)                -73   678   892  1087  1087   606  1342      1.956      2.585    -37.868     38.007      0.179
   961         -2  (ubar)             -73   782   860  1092  1092     0  2882     -2.016      3.425    -19.100     19.516      0.516
   962         21  (g)                -73   881   905  1088  1088  3201   606      0.100      1.195    -19.002     19.044      0.371
   963         21  (g)                -73   957   958  1091  1091  2882  2958     -0.768      1.858     -3.610      4.169      0.554
   964         21  (g)                -73   878   909   966     0  2627  3177      0.074     -0.421     -4.027      4.049      0.009
   965         21  (g)                -73   709   809  1210  1210   685   749      0.244     -0.311     -7.300      7.311      0.030
   966         21  (g)                -73   699   964  1209  1209   749  3177      0.423     -2.986    -29.982     30.134      0.082
   967         21  (g)                -73   691   733   969     0  2351  2905      1.035     -0.921    -10.219     10.313      0.107
   968         21  (g)                -73   695   842   972     0  1191  1714     -0.183     -0.963     -4.575      4.681      0.126
   969         21  (g)                -73   664   967  1213  1213  1118  2905      1.438     -1.456    -14.408     14.555      0.277
   970         21  (g)                -73   765   766  1211  1211  1583   685      1.160     -0.253    -21.337     21.373      0.331
   971         21  (g)                -73   741   886  1207  1207  1714  1318     -3.626     -2.651    -33.364     33.668      0.458
   972         21  (g)                -73   901   968  1208  1208  3177  1714     -0.215     -1.851    -10.946     11.113      0.465
   973          2  (u)                -73   803   767   974     0  1449     0     -0.670     -0.985    -14.166     14.237      0.781
   974          2  (u)                -73   973   831  1206  1206  1318     0     -1.459     -1.986    -25.539     25.682      1.110
   975         21  (g)                -73   787   864   976     0  2192  2449      1.090      0.556     -1.741      2.135      0.168
   976         -3  (sbar)             -73   730   975  1030  1030     0  2449      1.850      0.798     -2.470      3.325      0.947
   977          5  (b)                -73   935   938  1361  1361  3321     0    -32.346   -107.024    169.435    203.063      5.115
   978         21  (g)                -73   814   887  1128  1128  2549   604     -1.385     -0.426     -0.649      1.590      0.086
   979         21  (g)                -73   747   818  1131  1131  3216  1415     -0.186     -0.911     -2.041      2.246      0.103
   980         21  (g)                -73   689   752  1129  1129  2300  2549     -1.014      0.420     -0.725      1.321      0.115
   981         21  (g)                -73   679   745  1126  1126  1628   611     -2.402     -0.979      0.928      2.760      0.160
   982         21  (g)                -73   789   862   983     0  1951  2300     -1.052     -0.824     -2.027      2.433      0.162
   983         21  (g)                -73   755   982  1130  1130  1415  2300     -1.920     -1.819     -4.611      5.335      0.455
   984         21  (g)                -73   764   824   990     0  1082  1188      1.426     -0.202     -0.611      1.566      0.078
   985         21  (g)                -73   838   888  1073  1073  1733  1734      0.996      0.379      0.051      1.080      0.166
   986         21  (g)                -73   794   835   990     0  1734  1082      1.696     -0.078     -0.210      1.727      0.237
   987         21  (g)                -73   753   774  1070  1070  2355   851      1.114     -0.676     -2.417      2.765      0.326
   988          3  (s)                -73   726   743  1069  1069   851     0      4.049     -0.684    -11.021     11.789      0.800
   989         -3  (sbar)             -73   680   828  1074  1074     0  1733      1.315      2.625     -4.313      5.290      0.868
   990         21  (g)                -73   984   986  1072  1072  1734  1188      3.122     -0.280     -0.821      3.293      0.590
   991         21  (g)                -73   716   792  1257  1257   977  2583     -0.026     -0.809     27.679     27.691      0.097
   992         21  (g)                -73   722   804  1256  1256  2583  3114     -0.334     -0.604      7.257      7.291      0.155
   993         21  (g)                -73   732   802   996     0  1233  3120      0.046      1.429      7.924      8.054      0.192
   994         -2  (ubar)             -73   768   852  1259  1259     0  3236     -1.010      0.087     30.014     30.037      0.608
   995          1  (d)                -73   715   850   996     0  3120     0      0.381      1.938     12.513     12.682      0.611
   996          1  (d)                -73   995   993   997     0  1233     0      0.427      3.367     20.437     20.737      0.910
   997          1  (d)                -73   996   729  1247  1247   698     0      0.388      3.913     25.379     25.709      1.184
   998         21  (g)                -73   697   701  1255  1255  3114  2202      2.873     -2.349     47.120     47.267      0.322
   999         21  (g)                -73   710   817  1254  1254  2202  1679      1.054     -1.897     16.437     16.590      0.576
  1000         21  (g)                -73   727   829  1252  1252  1123  1122     -1.777     -0.390     14.698     14.822      0.597
  1001         21  (g)                -73   746   786  1148  1148  2578   603      0.034      1.362      0.128      1.369      0.019
  1002         21  (g)                -73   790   863  1006     0  2919   841      0.640      0.824     -0.572      1.190      0.029
  1003         21  (g)                -73   728   777  1151  1151  1289  2107     -0.960      0.439      0.025      1.070      0.172
  1004         -1  (dbar)             -73   725   775  1008     0     0   980     -1.474      0.045      1.304      2.029      0.492
  1005         21  (g)                -73   869   874  1156  1156  1463  2541     -0.801     -0.263      1.975      2.158      0.208
  1006         21  (g)                -73   677  1002  1147  1147   603   841      2.216      2.443     -1.436      3.609      0.291
  1007         21  (g)                -73   706   822  1155  1155  2541   970      2.247     -0.295      1.200      2.587      0.342
  1008         -1  (dbar)             -73  1004   793  1157  1157     0  1463     -2.762      0.467      2.771      4.027      0.829
  1009         -1  (dbar)             -73   717   668  1184  1184     0  3193     -0.149      0.462     14.959     14.972      0.393
  1010         21  (g)                -73   713   865  1012     0   692  2495     -0.390      0.878     21.161     21.183      0.113
  1011         21  (g)                -73   692   718  1012     0  3193   692     -1.049      2.655     82.804     82.853      0.256
  1012         21  (g)                -73  1010  1011  1183  1183  3193  2495     -1.440      3.532    103.965    104.036      0.598
  1013          2  (u)                -71   893   893  1015  1016  2050     0     -0.157      0.355     -1.644      1.721      0.330
  1014         -1  (dbar)             -71   891   891  1015  1016     0  2050     -0.175     -1.180     -2.360      2.664      0.330
  1015        111  (pi0)              -82  1013  1014  1650  1651     0     0     -0.493      0.065     -2.931      2.975      0.135
  1016        211  pi+                 82  1013  1014     0     0     0     0      0.161     -0.890     -1.073      1.410      0.140
  1017          2  (u)                -71   912   912  1019  1021  1713     0     -0.165      0.599      7.855      7.886      0.330
  1018         -1  (dbar)             -71   885   885  1019  1021     0  1713     -1.190      0.843      1.187      1.908      0.330
  1019        213  (rho+)             -83  1017  1018  1447  1448     0     0      0.003      0.727      4.746      4.865      0.783
  1020        311  (K0)               -83  1017  1018  1449  1449     0     0     -0.887      0.575      0.932      1.494      0.498
  1021       -311  (Kbar0)            -84  1017  1018  1450  1450     0     0     -0.471      0.139      3.363      3.435      0.498
  1022          2  (u)                -71   773   773  1024  1027  1358     0      0.075     -1.104      6.113      6.221      0.330
  1023         -3  (sbar)             -71   776   776  1024  1027     0  1358     -0.410      0.601     -0.295      0.930      0.500
  1024        113  (rho0)             -83  1022  1023  1451  1452     0     0     -0.049     -0.938      4.766      4.900      0.642
  1025        211  pi+                 84  1022  1023     0     0     0     0      0.037      0.117     -0.157      0.243      0.140
  1026       -213  (rho-)             -84  1022  1023  1453  1454     0     0     -0.550      0.192      0.614      1.193      0.840
  1027        321  K+                  84  1022  1023     0     0     0     0      0.227      0.126      0.595      0.815      0.494
  1028          1  (d)                -71   799   799  1031  1033   989     0     -0.199      1.268     -7.002      7.126      0.330
  1029         21  (g)                -71   705   705  1031  1033  2449   989      0.969      0.688     -4.457      4.613      0.000
  1030         -3  (sbar)             -71   976   976  1031  1033     0  2449      1.850      0.798     -2.470      3.325      0.947
  1031       2112  n0                  83  1028  1030     0     0     0     0      0.028      1.671     -9.271      9.467      0.940
  1032        111  (pi0)              -84  1028  1030  1652  1653     0     0      0.555      0.120     -1.005      1.162      0.135
  1033      -3122  Lambdabar0          84  1028  1030     0     0     0     0      2.038      0.963     -3.653      4.435      1.116
  1034          2  (u)                -71   925   925  1036  1041  1581     0     -0.156     -0.100     -1.790      1.830      0.330
  1035         -3  (sbar)             -71   872   872  1036  1041     0  1581      0.275      0.068      2.587      2.650      0.500
  1036        211  pi+                 83  1034  1035     0     0     0     0     -0.161     -0.080     -0.065      0.236      0.140
  1037       -211  pi-                 83  1034  1035     0     0     0     0      0.339      0.116     -0.258      0.463      0.140
  1038        113  (rho0)             -83  1034  1035  1455  1456     0     0     -0.190      0.224      0.095      0.820      0.760
  1039        211  pi+                 83  1034  1035     0     0     0     0      0.073     -0.207     -0.714      0.760      0.140
  1040       -211  pi-                 84  1034  1035     0     0     0     0      0.052     -0.377      0.670      0.783      0.140
  1041        323  (K*+)              -84  1034  1035  1457  1458     0     0      0.005      0.291      1.069      1.418      0.884
  1042          3  (s)                -71   919   919  1044  1049  3233     0      0.099     -0.028   -173.444    173.445      0.500
  1043         -2  (ubar)             -71   908   908  1044  1049     0  3233     -0.474      0.258     -1.813      1.920      0.330
  1044       -323  (K*-)              -83  1042  1043  1459  1460     0     0      0.103     -0.171    -66.805     66.811      0.891
  1045        223  (omega)            -83  1042  1043  1654  1656     0     0     -0.035      0.182    -28.915     28.926      0.781
  1046        213  (rho+)             -83  1042  1043  1461  1462     0     0     -0.246      0.471    -54.360     54.368      0.805
  1047       -213  (rho-)             -84  1042  1043  1463  1464     0     0     -0.153      0.032     -9.946      9.978      0.784
  1048        211  pi+                 84  1042  1043     0     0     0     0     -0.433     -0.376     -4.159      4.201      0.140
  1049       -211  pi-                 84  1042  1043     0     0     0     0      0.389      0.092    -11.073     11.081      0.140
  1050          1  (d)                -71   920   920  1052  1055   843     0     -0.354      0.155   -249.406    249.407      0.330
  1051         -3  (sbar)             -71   873   873  1052  1055     0   843     -0.693      0.108     -4.261      4.348      0.500
  1052       -213  (rho-)             -83  1050  1051  1465  1466     0     0     -0.375      0.155   -196.140    196.142      0.912
  1053        321  K+                  83  1050  1051     0     0     0     0      0.010      0.307    -44.794     44.798      0.494
  1054       -311  (Kbar0)            -84  1050  1051  1467  1467     0     0     -0.615     -0.329     -6.047      6.107      0.498
  1055        311  (K0)               -84  1050  1051  1468  1468     0     0     -0.067      0.129     -6.687      6.707      0.498
  1056          2  (u)                -71   781   781  1058  1062   971     0     -0.643      0.937      1.685      2.059      0.330
  1057         -1  (dbar)             -71   798   798  1058  1062     0   971      1.601      0.157     -8.636      8.791      0.330
  1058        211  pi+                 83  1056  1057     0     0     0     0     -0.343      0.881      1.554      1.825      0.140
  1059        111  (pi0)              -84  1056  1057  1657  1658     0     0     -0.241      0.306     -0.399      0.574      0.135
  1060        113  (rho0)             -84  1056  1057  1469  1470     0     0      0.599     -0.182     -3.263      3.412      0.777
  1061        111  (pi0)              -84  1056  1057  1659  1660     0     0     -0.007     -0.119     -1.602      1.612      0.135
  1062        113  (rho0)             -84  1056  1057  1471  1472     0     0      0.950      0.207     -3.241      3.427      0.542
  1063          1  (d)                -71   808   808  1065  1068  1264     0     -1.192      0.262  -1426.759   1426.760      0.330
  1064         -2  (ubar)             -71   807   807  1065  1068     0  1264      1.686     -0.529    -56.982     57.010      0.330
  1065        111  (pi0)              -83  1063  1064  1661  1662     0     0     -1.111     -0.153  -1261.130   1261.130      0.135
  1066       -211  pi-                 84  1063  1064     0     0     0     0     -0.286      0.571   -119.250    119.252      0.140
  1067        213  (rho+)             -84  1063  1064  1473  1474     0     0      0.539     -0.443    -48.218     48.228      0.643
  1068       -211  pi-                 84  1063  1064     0     0     0     0      1.351     -0.242    -55.143     55.160      0.140
  1069          3  (s)                -71   988   988  1075  1085   851     0      4.049     -0.684    -11.021     11.789      0.800
  1070         21  (g)                -71   987   987  1075  1085  2355   851      1.114     -0.676     -2.417      2.765      0.326
  1071         21  (g)                -71   841   841  1075  1085  1188  2355      1.477     -1.021     -0.207      1.807      0.000
  1072         21  (g)                -71   990   990  1075  1085  1734  1188      3.122     -0.280     -0.821      3.293      0.590
  1073         21  (g)                -71   985   985  1075  1085  1733  1734      0.996      0.379      0.051      1.080      0.166
  1074         -3  (sbar)             -71   989   989  1075  1085     0  1733      1.315      2.625     -4.313      5.290      0.868
  1075       -321  K-                  83  1069  1074     0     0     0     0      1.571     -0.332     -3.979      4.320      0.494
  1076        211  pi+                 83  1069  1074     0     0     0     0      2.195     -0.611     -4.768      5.286      0.140
  1077       -211  pi-                 83  1069  1074     0     0     0     0     -0.085     -0.751     -1.365      1.567      0.140
  1078        113  (rho0)             -83  1069  1074  1475  1476     0     0      1.251      0.106     -1.842      2.345      0.727
  1079        111  (pi0)              -83  1069  1074  1663  1664     0     0      0.903     -0.744     -1.557      1.952      0.135
  1080        321  K+                  84  1069  1074     0     0     0     0      2.028      0.398     -0.207      2.135      0.494
  1081       -323  (K*-)              -84  1069  1074  1477  1478     0     0      1.362      0.125     -1.071      1.971      0.931
  1082        211  pi+                 84  1069  1074     0     0     0     0      0.302     -0.069     -0.200      0.395      0.140
  1083       -211  pi-                 84  1069  1074     0     0     0     0      0.175     -0.090     -0.079      0.254      0.140
  1084        113  (rho0)             -84  1069  1074  1479  1480     0     0      1.072      0.218     -0.346      1.555      1.049
  1085        323  (K*+)              -84  1069  1074  1481  1482     0     0      1.299      2.094     -3.312      4.245      0.989
  1086          2  (u)                -71   815   815  1093  1104  1342     0      0.519     -0.308     -9.754      9.778      0.330
  1087         21  (g)                -71   960   960  1093  1104   606  1342      1.956      2.585    -37.868     38.007      0.179
  1088         21  (g)                -71   962   962  1093  1104  3201   606      0.100      1.195    -19.002     19.044      0.371
  1089         21  (g)                -71   759   759  1093  1104   813  3201     -0.542      3.368    -18.647     18.956      0.000
  1090         21  (g)                -71   959   959  1093  1104  2958   813      0.045      2.233    -11.126     11.349      0.155
  1091         21  (g)                -71   963   963  1093  1104  2882  2958     -0.768      1.858     -3.610      4.169      0.554
  1092         -2  (ubar)             -71   961   961  1093  1104     0  2882     -2.016      3.425    -19.100     19.516      0.516
  1093       3224  (Sigma*+)          -83  1086  1092  1483  1484     0     0      1.026      1.483    -30.130     30.221      1.508
  1094        111  (pi0)              -83  1086  1092  1665  1666     0     0      0.380      0.875     -7.552      7.613      0.135
  1095      -3322  Xibar0              83  1086  1092     0     0     0     0      0.379      1.018    -14.896     14.993      1.315
  1096       -321  K-                  83  1086  1092     0     0     0     0      0.021      0.741     -8.592      8.638      0.494
  1097        111  (pi0)              -83  1086  1092  1667  1668     0     0     -0.151      0.097     -2.608      2.618      0.135
  1098        213  (rho+)             -83  1086  1092  1485  1486     0     0      0.378      1.450    -12.178     12.301      0.880
  1099        111  (pi0)              -83  1086  1092  1669  1670     0     0      0.310      3.215    -19.839     20.101      0.135
  1100       -211  pi-                 84  1086  1092     0     0     0     0     -0.543      1.409     -3.073      3.426      0.140
  1101        213  (rho+)             -84  1086  1092  1487  1488     0     0     -1.024      1.055     -5.515      5.764      0.805
  1102       -211  pi-                 84  1086  1092     0     0     0     0     -0.199      1.371     -5.370      5.547      0.140
  1103        211  pi+                 84  1086  1092     0     0     0     0     -0.440      0.382     -2.176      2.257      0.140
  1104       -211  pi-                 84  1086  1092     0     0     0     0     -0.843      1.261     -7.179      7.339      0.140
  1105          2  (u)                -71   813   813  1107  1113   811     0      0.063     -1.052   -156.472    156.476      0.330
  1106         -1  (dbar)             -71   750   750  1107  1113     0   811      0.437     -1.821     -1.714      2.560      0.330
  1107       2114  (Delta0)           -83  1105  1106  1489  1490     0     0      0.034     -0.609    -73.498     73.510      1.167
  1108      -1114  (Deltabar+)        -83  1105  1106  1491  1492     0     0     -0.353     -0.265    -46.319     46.341      1.365
  1109        111  (pi0)              -83  1105  1106  1671  1672     0     0      0.118      0.156    -14.183     14.185      0.135
  1110       -211  pi-                 83  1105  1106     0     0     0     0      0.105     -0.677    -20.510     20.522      0.140
  1111        211  pi+                 83  1105  1106     0     0     0     0      0.009      0.047     -1.655      1.661      0.140
  1112        311  (K0)               -84  1105  1106  1493  1493     0     0      0.114     -0.751     -0.751      1.178      0.498
  1113       -311  (Kbar0)            -84  1105  1106  1494  1494     0     0      0.474     -0.774     -1.270      1.639      0.498
  1114          1  (d)                -71   911   911  1116  1123  1712     0     -0.226      0.244      1.383      1.460      0.330
  1115         -2  (ubar)             -71   927   927  1116  1123     0  1712     -0.327     -0.373    -55.758     55.761      0.330
  1116       -213  (rho-)             -83  1114  1115  1495  1496     0     0     -0.345     -0.118      0.364      0.949      0.797
  1117        211  pi+                 83  1114  1115     0     0     0     0      0.126      0.159      0.551      0.604      0.140
  1118       -211  pi-                 83  1114  1115     0     0     0     0      0.302      0.315     -1.182      1.268      0.140
  1119        213  (rho+)             -83  1114  1115  1497  1498     0     0     -0.435     -0.011     -3.527      3.632      0.747
  1120        311  (K0)               -83  1114  1115  1499  1499     0     0     -0.291     -0.584     -2.732      2.852      0.498
  1121       -323  (K*-)              -84  1114  1115  1500  1501     0     0      0.076      0.388    -21.561     21.593      1.100
  1122        113  (rho0)             -84  1114  1115  1502  1503     0     0     -0.197     -0.385    -24.270     24.287      0.795
  1123        111  (pi0)              -84  1114  1115  1673  1674     0     0      0.211      0.108     -2.018      2.036      0.135
  1124          1  (d)                -71   736   736  1133  1145   700     0     -1.615     -1.824      0.191      2.466      0.330
  1125         21  (g)                -71   685   685  1133  1145   611   700     -2.681     -3.073      1.924      4.509      0.000
  1126         21  (g)                -71   981   981  1133  1145  1628   611     -2.402     -0.979      0.928      2.760      0.160
  1127         21  (g)                -71   676   676  1133  1145   604  1628     -3.802     -0.884     -0.747      3.974      0.000
  1128         21  (g)                -71   978   978  1133  1145  2549   604     -1.385     -0.426     -0.649      1.590      0.086
  1129         21  (g)                -71   980   980  1133  1145  2300  2549     -1.014      0.420     -0.725      1.321      0.115
  1130         21  (g)                -71   983   983  1133  1145  1415  2300     -1.920     -1.819     -4.611      5.335      0.455
  1131         21  (g)                -71   979   979  1133  1145  3216  1415     -0.186     -0.911     -2.041      2.246      0.103
  1132         -2  (ubar)             -71   800   800  1133  1145     0  3216      0.510     -0.207     -4.918      4.960      0.330
  1133       -211  pi-                 83  1124  1132     0     0     0     0     -1.947     -2.237      0.837      3.085      0.140
  1134        211  pi+                 83  1124  1132     0     0     0     0     -2.375     -1.632      0.882      3.017      0.140
  1135        223  (omega)            -83  1124  1132  1675  1677     0     0     -1.522     -1.642      0.737      2.484      0.784
  1136       -211  pi-                 84  1124  1132     0     0     0     0     -1.235     -0.341     -0.488      1.378      0.140
  1137        113  (rho0)             -84  1124  1132  1504  1505     0     0     -1.234     -0.299      0.069      1.619      1.003
  1138        213  (rho+)             -84  1124  1132  1506  1507     0     0     -3.015     -0.667     -0.264      3.261      1.016
  1139        111  (pi0)              -84  1124  1132  1678  1679     0     0     -0.661     -0.169     -0.473      0.841      0.135
  1140       -211  pi-                 84  1124  1132     0     0     0     0     -0.266     -0.216     -0.256      0.450      0.140
  1141        211  pi+                 84  1124  1132     0     0     0     0     -0.757     -0.160     -0.761      1.094      0.140
  1142        111  (pi0)              -84  1124  1132  1680  1681     0     0     -0.667     -0.563     -2.271      2.437      0.135
  1143       -213  (rho-)             -84  1124  1132  1508  1509     0     0     -0.008     -0.450     -1.860      2.303      1.282
  1144        211  pi+                 84  1124  1132     0     0     0     0     -0.716     -0.595     -3.084      3.225      0.140
  1145       -213  (rho-)             -84  1124  1132  1510  1511     0     0     -0.093     -0.731     -3.718      3.967      1.170
  1146          3  (s)                -71   675   675  1158  1176   841     0      0.033      0.402     -0.160      0.662      0.500
  1147         21  (g)                -71  1006  1006  1158  1176   603   841      2.216      2.443     -1.436      3.609      0.291
  1148         21  (g)                -71  1001  1001  1158  1176  2578   603      0.034      1.362      0.128      1.369      0.019
  1149         21  (g)                -71   686   686  1158  1176  2373  2578     -0.668      1.693     -0.487      1.884      0.000
  1150         21  (g)                -71   704   704  1158  1176  2107  2373     -2.296      3.714     -2.982      5.287      0.000
  1151         21  (g)                -71  1003  1003  1158  1176  1289  2107     -0.960      0.439      0.025      1.070      0.172
  1152         21  (g)                -71   703   703  1158  1176   683  1289     -1.001      1.091      0.473      1.554      0.000
  1153         21  (g)                -71   875   875  1158  1176  2262   683      0.247      0.385      0.273      0.533      0.000
  1154         21  (g)                -71   783   783  1158  1176   970  2262      0.746      0.528      1.773      1.995      0.000
  1155         21  (g)                -71  1007  1007  1158  1176  2541   970      2.247     -0.295      1.200      2.587      0.342
  1156         21  (g)                -71  1005  1005  1158  1176  1463  2541     -0.801     -0.263      1.975      2.158      0.208
  1157         -1  (dbar)             -71  1008  1008  1158  1176     0  1463     -2.762      0.467      2.771      4.027      0.829
  1158       -313  (K*bar0)           -83  1146  1157  1512  1513     0     0      1.071      1.402     -0.597      2.110      0.992
  1159       -213  (rho-)             -83  1146  1157  1514  1515     0     0     -0.258      1.375     -0.417      1.611      0.682
  1160        211  pi+                 83  1146  1157     0     0     0     0      0.673      0.482     -0.141      0.851      0.140
  1161       -211  pi-                 83  1146  1157     0     0     0     0      0.259      0.172     -0.451      0.565      0.140
  1162        111  (pi0)              -83  1146  1157  1682  1683     0     0     -0.649      2.315     -1.627      2.907      0.135
  1163        211  pi+                 83  1146  1157     0     0     0     0     -1.090      2.087      0.007      2.359      0.140
  1164        223  (omega)            -83  1146  1157  1684  1686     0     0     -0.964      1.053     -0.071      1.632      0.788
  1165        221  (eta)              -83  1146  1157  1687  1688     0     0     -0.359      1.152     -0.822      1.559      0.548
  1166       -211  pi-                 83  1146  1157     0     0     0     0     -0.204      0.038      0.286      0.380      0.140
  1167        113  (rho0)             -83  1146  1157  1516  1517     0     0      0.758      0.690      0.166      1.277      0.742
  1168        211  pi+                 83  1146  1157     0     0     0     0     -1.290      0.736      0.744      1.667      0.140
  1169        111  (pi0)              -84  1146  1157  1689  1690     0     0      0.227     -0.024     -0.156      0.308      0.135
  1170        113  (rho0)             -84  1146  1157  1518  1519     0     0      1.063      0.467      1.001      1.711      0.760
  1171       -211  pi-                 84  1146  1157     0     0     0     0      0.005      0.076      0.020      0.160      0.140
  1172        111  (pi0)              -84  1146  1157  1691  1692     0     0      0.045      0.038      0.407      0.433      0.135
  1173        321  K+                  84  1146  1157     0     0     0     0      0.676     -0.288      1.212      1.501      0.494
  1174       -321  K-                  84  1146  1157     0     0     0     0     -0.042     -0.340      0.273      0.660      0.494
  1175        323  (K*+)              -84  1146  1157  1520  1521     0     0     -1.105      0.357      2.224      2.660      0.886
  1176       -311  (Kbar0)            -84  1146  1157  1522  1522     0     0     -1.782      0.179      1.494      2.385      0.498
  1177          2  (u)                -71   661   661  1185  1196  1403     0      2.675      8.086    136.233    136.499      0.330
  1178         21  (g)                -71   667   667  1185  1196   511  1403     22.233     66.119   1194.003   1196.039      0.000
  1179         21  (g)                -71   663   663  1185  1196  1987   511      3.761     11.380    199.192    199.552      0.000
  1180         21  (g)                -71   670   670  1185  1196  3139  1987      0.739      0.992     17.585     17.629      0.000
  1181         21  (g)                -71   812   812  1185  1196  1079  3139      2.093      0.510     45.475     45.526      0.000
  1182         21  (g)                -71   672   672  1185  1196  2495  1079      0.639      1.217     41.003     41.026      0.000
  1183         21  (g)                -71  1012  1012  1185  1196  3193  2495     -1.440      3.532    103.965    104.036      0.598
  1184         -1  (dbar)             -71  1009  1009  1185  1196     0  3193     -0.149      0.462     14.959     14.972      0.393
  1185        223  (omega)            -83  1177  1184  1693  1695     0     0     12.667     38.988    698.284    699.487      0.784
  1186        321  K+                  83  1177  1184     0     0     0     0      3.042      7.517    130.443    130.696      0.494
  1187       -323  (K*-)              -83  1177  1184  1523  1524     0     0      5.003     14.466    266.209    266.651      0.854
  1188        211  pi+                 83  1177  1184     0     0     0     0      7.209     18.977    323.038    323.675      0.140
  1189       -211  pi-                 83  1177  1184     0     0     0     0      0.900      4.453    103.812    103.911      0.140
  1190        211  pi+                 83  1177  1184     0     0     0     0      0.580      0.591     11.366     11.397      0.140
  1191        111  (pi0)              -83  1177  1184  1696  1697     0     0     -0.030      0.050      2.841      2.845      0.135
  1192       -211  pi-                 83  1177  1184     0     0     0     0      1.022      1.502     42.293     42.332      0.140
  1193        321  K+                  83  1177  1184     0     0     0     0      1.054      0.757     19.195     19.245      0.494
  1194        333  (phi)              -84  1177  1184  1698  1699     0     0     -0.461      2.231     65.703     65.751      1.025
  1195       -313  (K*bar0)           -84  1177  1184  1525  1526     0     0      0.090      1.721     59.354     59.386      0.914
  1196        221  (eta)              -84  1177  1184  1700  1701     0     0     -0.524      1.046     29.877     29.905      0.548
  1197          2  (u)                -71   910   910  1199  1205  3220     0      0.160      0.335    201.624    201.625      0.330
  1198         -2  (ubar)             -71   714   714  1199  1205     0  3220      1.186     -3.610      3.877      5.439      0.330
  1199        111  (pi0)              -83  1197  1198  1702  1703     0     0     -0.107      0.371     16.058     16.063      0.135
  1200        213  (rho+)             -83  1197  1198  1527  1528     0     0      0.574      0.182     62.648     62.655      0.703
  1201        223  (omega)            -83  1197  1198  1704  1706     0     0     -0.090     -0.126    104.647    104.650      0.761
  1202       -213  (rho-)             -83  1197  1198  1529  1530     0     0     -0.317     -0.325     16.653     16.677      0.762
  1203        221  (eta)              -83  1197  1198  1707  1709     0     0      0.297     -0.377      2.471      2.576      0.548
  1204        211  pi+                 84  1197  1198     0     0     0     0      0.592     -2.432      2.628      3.632      0.140
  1205       -211  pi-                 84  1197  1198     0     0     0     0      0.397     -0.568      0.395      0.810      0.140
  1206          2  (u)                -71   974   974  1215  1225  1318     0     -1.459     -1.986    -25.539     25.682      1.110
  1207         21  (g)                -71   971   971  1215  1225  1714  1318     -3.626     -2.651    -33.364     33.668      0.458
  1208         21  (g)                -71   972   972  1215  1225  3177  1714     -0.215     -1.851    -10.946     11.113      0.465
  1209         21  (g)                -71   966   966  1215  1225   749  3177      0.423     -2.986    -29.982     30.134      0.082
  1210         21  (g)                -71   965   965  1215  1225   685   749      0.244     -0.311     -7.300      7.311      0.030
  1211         21  (g)                -71   970   970  1215  1225  1583   685      1.160     -0.253    -21.337     21.373      0.331
  1212         21  (g)                -71   671   671  1215  1225  2905  1583      9.478     -5.780    -94.413     95.063      0.000
  1213         21  (g)                -71   969   969  1215  1225  1118  2905      1.438     -1.456    -14.408     14.555      0.277
  1214         -4  (cbar)             -71   662   662  1215  1225     0  1118     14.310    -11.789   -162.163    163.226      1.500
  1215        223  (omega)            -83  1206  1214  1710  1712     0     0     -2.192     -1.671    -24.631     24.797      0.784
  1216        221  (eta)              -83  1206  1214  1713  1714     0     0     -0.415     -0.829     -7.846      7.919      0.548
  1217        213  (rho+)             -83  1206  1214  1531  1532     0     0     -1.066     -1.392    -14.927     15.054      0.849
  1218        111  (pi0)              -83  1206  1214  1715  1716     0     0     -0.882     -0.866    -12.537     12.599      0.135
  1219        113  (rho0)             -84  1206  1214  1533  1534     0     0      0.553     -1.577    -19.296     19.390      0.918
  1220       2112  n0                  84  1206  1214     0     0     0     0     -0.730     -1.486    -11.168     11.329      0.940
  1221      -3122  Lambdabar0          84  1206  1214     0     0     0     0      0.925     -1.855    -19.616     19.757      1.116
  1222       -323  (K*-)              -84  1206  1214  1535  1536     0     0      1.709     -1.138    -28.537     28.625      0.879
  1223       2212  p+                  84  1206  1214     0     0     0     0      3.402     -2.376    -39.098     39.329      0.938
  1224      -2212  pbar-               84  1206  1214     0     0     0     0      4.250     -2.692    -40.963     41.281      0.938
  1225       -423  (D*bar0)           -84  1206  1214  1717  1718     0     0     16.197    -13.181   -180.832    182.045      2.007
  1226          2  (u)                -71   918   918  1228  1235   744     0     -0.251      0.050      2.637      2.670      0.330
  1227         -1  (dbar)             -71   687   687  1228  1235     0   744      0.052      0.497    -74.307     74.310      0.330
  1228        213  (rho+)             -83  1226  1227  1537  1538     0     0     -0.182     -0.255      0.604      1.010      0.746
  1229        223  (omega)            -83  1226  1227  1719  1721     0     0      0.392     -0.005      1.062      1.375      0.780
  1230       2112  n0                  84  1226  1227     0     0     0     0     -0.296      0.595     -0.482      1.248      0.940
  1231      -2112  nbar0               84  1226  1227     0     0     0     0     -0.260     -0.062     -3.926      4.045      0.940
  1232        111  (pi0)              -84  1226  1227  1722  1723     0     0      0.095     -0.387     -0.764      0.872      0.135
  1233       2112  n0                  84  1226  1227     0     0     0     0      0.135     -0.343     -2.285      2.498      0.940
  1234      -2112  nbar0               84  1226  1227     0     0     0     0     -0.345      0.960    -21.008     21.054      0.940
  1235        113  (rho0)             -84  1226  1227  1539  1540     0     0      0.262      0.044    -44.871     44.878      0.724
  1236          1  (d)                -71   915   915  1238  1246  3245     0     -0.139      0.952    324.648    324.650      0.330
  1237         -3  (sbar)             -71   917   917  1238  1246     0  3245     -0.099      1.823      0.584      1.981      0.500
  1238        111  (pi0)              -83  1236  1237  1724  1725     0     0     -0.343      0.445     40.868     40.872      0.135
  1239        111  (pi0)              -83  1236  1237  1726  1727     0     0      0.576      0.204    206.158    206.159      0.135
  1240        221  (eta)              -83  1236  1237  1728  1730     0     0     -0.487      0.088     18.525     18.540      0.548
  1241       -211  pi-                 83  1236  1237     0     0     0     0     -0.326      0.058     17.909     17.913      0.140
  1242        211  pi+                 83  1236  1237     0     0     0     0      0.127      0.359     33.918     33.920      0.140
  1243        311  (K0)               -84  1236  1237  1541  1541     0     0      0.431     -0.227      4.849      4.899      0.498
  1244       -323  (K*-)              -84  1236  1237  1542  1543     0     0     -0.163      0.538      1.840      2.152      0.964
  1245        111  (pi0)              -84  1236  1237  1731  1732     0     0      0.217      0.047      0.258      0.366      0.135
  1246        323  (K*+)              -84  1236  1237  1544  1545     0     0     -0.270      1.263      0.906      1.809      0.885
  1247          1  (d)                -71   997   997  1260  1281   698     0      0.388      3.913     25.379     25.709      1.184
  1248         21  (g)                -71   845   845  1260  1281  3168   698     -1.692      1.317     12.979     13.155      0.000
  1249         21  (g)                -71   742   742  1260  1281   735  3168     -1.148      2.685      9.143      9.598      0.000
  1250         21  (g)                -71   843   843  1260  1281  1189   735      0.029      0.842      2.217      2.372      0.000
  1251         21  (g)                -71   830   830  1260  1281  1122  1189     -0.826      0.291      2.489      2.639      0.000
  1252         21  (g)                -71  1000  1000  1260  1281  1123  1122     -1.777     -0.390     14.698     14.822      0.597
  1253         21  (g)                -71   780   780  1260  1281  1679  1123      0.923     -1.294      4.243      4.531      0.000
  1254         21  (g)                -71   999   999  1260  1281  2202  1679      1.054     -1.897     16.437     16.590      0.576
  1255         21  (g)                -71   998   998  1260  1281  3114  2202      2.873     -2.349     47.120     47.267      0.322
  1256         21  (g)                -71   992   992  1260  1281  2583  3114     -0.334     -0.604      7.257      7.291      0.155
  1257         21  (g)                -71   991   991  1260  1281   977  2583     -0.026     -0.809     27.679     27.691      0.097
  1258         21  (g)                -71   819   819  1260  1281  3236   977      0.772     -2.842    139.201    139.232      0.000
  1259         -2  (ubar)             -71   994   994  1260  1281     0  3236     -1.010      0.087     30.014     30.037      0.608
  1260        221  (eta)              -83  1247  1259  1733  1734     0     0      0.133      2.779     14.904     15.172      0.548
  1261        223  (omega)            -83  1247  1259  1735  1737     0     0     -0.478      0.877     10.436     10.514      0.799
  1262        313  (K*0)              -83  1247  1259  1546  1547     0     0     -0.446      1.207      8.191      8.335      0.859
  1263       -311  (Kbar0)            -83  1247  1259  1548  1548     0     0     -1.160      2.311      8.845      9.228      0.498
  1264       -211  pi-                 83  1247  1259     0     0     0     0     -0.471     -0.097      4.679      4.705      0.140
  1265        321  K+                  83  1247  1259     0     0     0     0     -0.739      1.270      5.312      5.533      0.494
  1266       3114  (Sigma*-)          -83  1247  1259  1549  1550     0     0     -0.171     -0.015      7.241      7.363      1.324
  1267        211  pi+                 83  1247  1259     0     0     0     0     -0.173     -0.218      0.340      0.461      0.140
  1268      -2212  pbar-               83  1247  1259     0     0     0     0     -0.743      0.162      4.749      4.900      0.938
  1269        223  (omega)            -83  1247  1259  1738  1740     0     0     -0.169     -0.888      6.581      6.689      0.783
  1270        211  pi+                 84  1247  1259     0     0     0     0      0.845     -0.802     12.374     12.430      0.140
  1271       2112  n0                  84  1247  1259     0     0     0     0      0.438     -0.543      8.298      8.380      0.940
  1272      -2112  nbar0               84  1247  1259     0     0     0     0      1.003     -1.739     16.755     16.901      0.940
  1273       -211  pi-                 84  1247  1259     0     0     0     0      0.384     -0.703     20.944     20.960      0.140
  1274        111  (pi0)              -84  1247  1259  1741  1742     0     0      0.194     -0.170      2.077      2.097      0.135
  1275        323  (K*+)              -84  1247  1259  1551  1552     0     0      2.004     -2.604     92.107     92.170      0.920
  1276       -311  (Kbar0)            -84  1247  1259  1553  1553     0     0     -0.604     -0.423     16.059     16.084      0.498
  1277        311  (K0)               -84  1247  1259  1554  1554     0     0      0.054      0.078     16.426     16.434      0.498
  1278       -323  (K*-)              -84  1247  1259  1555  1556     0     0     -0.403     -1.070     51.468     51.490      0.977
  1279        211  pi+                 84  1247  1259     0     0     0     0      0.001     -0.273     10.027     10.032      0.140
  1280       -211  pi-                 84  1247  1259     0     0     0     0      0.087      0.083      3.018      3.024      0.140
  1281        111  (pi0)              -84  1247  1259  1743  1744     0     0     -0.360     -0.271     18.026     18.033      0.135
  1282          3  (s)                -71   924   924  1300  1326   612     0     -0.139     -0.548    -10.966     10.992      0.500
  1283         21  (g)                -71   665   665  1300  1326  2152   612      0.400     -0.062    -82.487     82.488      0.000
  1284         21  (g)                -71   951   951  1300  1326  2761  2152      1.186     -1.414   -190.154    190.163      0.218
  1285         21  (g)                -71   953   953  1300  1326  2200  2761     -0.372     -0.678   -114.793    114.797      0.400
  1286         21  (g)                -71   669   669  1300  1326   502  2200     -0.328     -1.277   -106.916    106.924      0.000
  1287         21  (g)                -71   945   945  1300  1326  3203   502     -0.740     -0.844    -48.157     48.170      0.161
  1288         21  (g)                -71   956   956  1300  1326   987  3203      0.158     -4.319   -176.013    176.067      0.587
  1289         21  (g)                -71   684   684  1300  1326   613   987      2.336     -2.039   -124.493    124.531      0.000
  1290         21  (g)                -71   952   952  1300  1326  2500   613      0.790     -0.409    -25.365     25.382      0.262
  1291         21  (g)                -71   954   954  1300  1326  1422  2500      3.968      0.486   -168.233    168.281      0.432
  1292         21  (g)                -71   948   948  1300  1326  2240  1422      1.481      1.470    -54.902     54.942      0.187
  1293         21  (g)                -71   947   947  1300  1326  1437  2240     -0.277      0.381   -215.926    215.926      0.165
  1294         21  (g)                -71   946   946  1300  1326  1594  1437     -0.811      0.217   -166.744    166.746      0.163
  1295         21  (g)                -71   762   762  1300  1326  3064  1594     -0.453      1.003   -114.197    114.202      0.000
  1296         21  (g)                -71   950   950  1300  1326   812  3064     -0.582      1.671    -92.744     92.761      0.210
  1297         21  (g)                -71   955   955  1300  1326  2892   812     -2.991      1.512   -158.070    158.107      0.476
  1298         21  (g)                -71   949   949  1300  1326  2818  2892     -0.899      0.628    -12.005     12.057      0.203
  1299         -2  (ubar)             -71   816   816  1300  1326     0  2818     -0.432      1.006    -18.730     18.764      0.330
  1300       -313  (K*bar0)           -83  1282  1299  1557  1558     0     0     -0.050     -0.630    -48.705     48.723      1.170
  1301       -211  pi-                 83  1282  1299     0     0     0     0      0.355     -0.092    -48.557     48.559      0.140
  1302        211  pi+                 83  1282  1299     0     0     0     0      0.398     -0.938   -106.032    106.037      0.140
  1303        111  (pi0)              -83  1282  1299  1745  1746     0     0     -0.693     -0.309    -29.827     29.837      0.135
  1304        223  (omega)            -83  1282  1299  1747  1749     0     0     -0.283     -0.141    -69.349     69.354      0.772
  1305        113  (rho0)             -83  1282  1299  1559  1560     0     0      1.009     -2.237   -155.646    155.668      0.940
  1306       2112  n0                  83  1282  1299     0     0     0     0     -0.103     -2.099   -113.362    113.385      0.940
  1307        111  (pi0)              -83  1282  1299  1750  1751     0     0      0.825     -0.901   -104.251    104.259      0.135
  1308      -2212  pbar-               83  1282  1299     0     0     0     0     -0.149     -1.295    -59.055     59.076      0.938
  1309       2212  p+                  83  1282  1299     0     0     0     0      0.765     -0.994    -57.810     57.831      0.938
  1310      -2112  nbar0               83  1282  1299     0     0     0     0      0.678      0.202    -33.746     33.766      0.940
  1311       -211  pi-                 83  1282  1299     0     0     0     0      2.538     -1.509   -123.288    123.324      0.140
  1312        211  pi+                 84  1282  1299     0     0     0     0     -0.173     -0.210     -5.362      5.370      0.140
  1313        111  (pi0)              -84  1282  1299  1752  1753     0     0      1.437      0.668    -65.937     65.956      0.135
  1314       -211  pi-                 84  1282  1299     0     0     0     0      1.404      0.427    -66.749     66.766      0.140
  1315        111  (pi0)              -84  1282  1299  1754  1755     0     0      0.091      0.283     -6.671      6.679      0.135
  1316        111  (pi0)              -84  1282  1299  1756  1757     0     0      0.594      0.041    -17.245     17.256      0.135
  1317        211  pi+                 84  1282  1299     0     0     0     0      0.029      0.055    -18.287     18.288      0.140
  1318       -211  pi-                 84  1282  1299     0     0     0     0     -0.655      0.046   -120.239    120.241      0.140
  1319        111  (pi0)              -84  1282  1299  1758  1759     0     0     -0.045      0.871    -61.370     61.376      0.135
  1320       2212  p+                  84  1282  1299     0     0     0     0     -0.661      0.668   -190.666    190.670      0.938
  1321      -2112  nbar0               84  1282  1299     0     0     0     0     -0.744      0.213   -106.327    106.334      0.940
  1322       -211  pi-                 84  1282  1299     0     0     0     0     -0.681      1.047    -87.623     87.632      0.140
  1323        211  pi+                 84  1282  1299     0     0     0     0     -0.045      0.030    -15.588     15.589      0.140
  1324        313  (K*0)              -84  1282  1299  1561  1562     0     0     -1.052      1.300    -78.669     78.692      0.911
  1325       -323  (K*-)              -84  1282  1299  1563  1564     0     0     -1.893      1.143    -61.432     61.479      0.910
  1326        113  (rho0)             -84  1282  1299  1565  1566     0     0     -0.603      1.141    -29.102     29.154      1.172
  1327          1  (d)                -71   897   897  1329  1337  1355     0      0.230      0.775   -139.930    139.933      0.330
  1328         -2  (ubar)             -71   849   849  1329  1337     0  1355     -0.364      2.567      5.871      6.426      0.330
  1329       -213  (rho-)             -83  1327  1328  1567  1568     0     0     -0.199      0.303    -96.783     96.788      0.919
  1330        113  (rho0)             -83  1327  1328  1569  1570     0     0      0.497     -0.093    -14.498     14.538      0.954
  1331        111  (pi0)              -83  1327  1328  1760  1761     0     0     -0.380      0.412    -18.576     18.585      0.135
  1332        111  (pi0)              -83  1327  1328  1762  1763     0     0      0.691     -0.051     -7.118      7.153      0.135
  1333        211  pi+                 83  1327  1328     0     0     0     0     -0.431      0.031     -1.577      1.641      0.140
  1334        223  (omega)            -84  1327  1328  1764  1766     0     0      0.122      0.645     -0.718      1.243      0.775
  1335       -211  pi-                 84  1327  1328     0     0     0     0     -0.046     -0.496      0.287      0.592      0.140
  1336        111  (pi0)              -84  1327  1328  1767  1768     0     0     -0.029      2.147      2.372      3.202      0.135
  1337        111  (pi0)              -84  1327  1328  1769  1770     0     0     -0.359      0.444      2.551      2.618      0.135
  1338          3  (s)                -71   914   914  1340  1349  1078     0     -1.014      0.400     36.578     36.597      0.500
  1339         -1  (dbar)             -71   923   923  1340  1349     0  1078     -0.371     -0.496    -24.840     24.850      0.330
  1340       -311  (Kbar0)            -83  1338  1339  1571  1571     0     0     -0.379      0.182     20.963     20.973      0.498
  1341        111  (pi0)              -83  1338  1339  1771  1772     0     0     -0.135      0.079      1.637      1.650      0.135
  1342       -211  pi-                 83  1338  1339     0     0     0     0     -0.395      0.395      7.398      7.420      0.140
  1343        213  (rho+)             -83  1338  1339  1572  1573     0     0     -0.138     -0.767      4.193      4.348      0.849
  1344        111  (pi0)              -83  1338  1339  1773  1774     0     0      0.180      0.908      1.292      1.595      0.135
  1345        111  (pi0)              -83  1338  1339  1775  1776     0     0     -0.018     -0.075      0.586      0.606      0.135
  1346        113  (rho0)             -84  1338  1339  1574  1575     0     0     -0.233     -0.386     -0.467      0.972      0.724
  1347        111  (pi0)              -84  1338  1339  1777  1778     0     0      0.042     -0.376     -9.858      9.866      0.135
  1348       -211  pi-                 84  1338  1339     0     0     0     0     -0.223      0.030    -11.613     11.616      0.140
  1349        211  pi+                 84  1338  1339     0     0     0     0     -0.087     -0.087     -2.394      2.401      0.140
  1350          2  (u)                -71   913   913  1352  1360  1368     0     -0.488      0.620    736.491    736.491      0.330
  1351         -3  (sbar)             -71   823   823  1352  1360     0  1368     -0.471     -0.223     -1.181      1.384      0.500
  1352        111  (pi0)              -83  1350  1351  1779  1780     0     0      0.067      0.014    208.775    208.775      0.135
  1353        221  (eta)              -83  1350  1351  1781  1783     0     0     -0.754      0.354    408.611    408.612      0.548
  1354        113  (rho0)             -83  1350  1351  1576  1577     0     0      0.043     -0.140     61.158     61.169      1.186
  1355        223  (omega)            -83  1350  1351  1784  1786     0     0     -0.099      0.176     37.884     37.893      0.778
  1356        321  K+                  83  1350  1351     0     0     0     0     -0.511     -0.187     12.160     12.182      0.494
  1357        333  (phi)              -84  1350  1351  1787  1788     0     0      0.609      0.345      5.612      5.746      1.020
  1358       -323  (K*-)              -84  1350  1351  1578  1579     0     0      0.016     -0.139      0.787      1.185      0.875
  1359        213  (rho+)             -84  1350  1351  1580  1581     0     0     -0.275      0.111      0.892      1.261      0.840
  1360        313  (K*0)              -84  1350  1351  1582  1583     0     0     -0.055     -0.137     -0.569      1.052      0.872
  1361          5  (b)                -71   977   977  1365  1370  3321     0    -32.346   -107.024    169.435    203.063      5.115
  1362         21  (g)                -71   937   937  1365  1370  3325  3321     -0.997     -1.834      2.722      3.430      0.000
  1363         21  (g)                -71   936   936  1365  1370   512  3325     -0.108     -0.257      1.815      1.837      0.000
  1364         -5  (bbar)             -71   932   932  1365  1370     0   512    -18.361     34.762     68.518     79.141      4.800
  1365       -523  (B*-)              -83  1361  1364  1789  1790     0     0    -30.991   -100.582    159.151    190.878      5.325
  1366        113  (rho0)             -83  1361  1364  1584  1585     0     0     -1.778     -5.834      9.141     11.026      0.911
  1367        323  (K*+)              -83  1361  1364  1586  1587     0     0     -0.254     -2.191      3.649      4.383      1.015
  1368       -321  K-                  84  1361  1364     0     0     0     0     -0.890      0.531      2.556      2.802      0.494
  1369        213  (rho+)             -84  1361  1364  1588  1589     0     0     -0.213      0.568      2.318      2.533      0.820
  1370        511  (B0)               -84  1361  1364  1791  1793     0     0    -17.686     33.154     65.676     75.850      5.280
  1371          2  (u)                -71   921   921  1373  1381  1589     0     -0.438     -0.626   -118.936    118.939      0.330
  1372         -2  (ubar)             -71   827   827  1373  1381     0  1589     -0.143     -0.565    165.062    165.063      0.330
  1373        223  (omega)            -83  1371  1372  1794  1796     0     0     -0.059     -0.884   -107.409    107.415      0.790
  1374        211  pi+                 83  1371  1372     0     0     0     0     -0.809      0.311     -5.277      5.349      0.140
  1375        113  (rho0)             -83  1371  1372  1590  1591     0     0     -0.245      0.133     -2.767      2.865      0.689
  1376        111  (pi0)              -83  1371  1372  1797  1798     0     0      0.376     -0.088     -2.240      2.277      0.135
  1377       -213  (rho-)             -83  1371  1372  1592  1593     0     0      0.842      0.010     -0.533      1.351      0.912
  1378        211  pi+                 83  1371  1372     0     0     0     0     -0.759     -0.035      0.853      1.151      0.140
  1379       1114  (Delta-)           -83  1371  1372  1594  1595     0     0      0.048     -0.180     20.163     20.212      1.391
  1380        211  pi+                 83  1371  1372     0     0     0     0     -0.050      0.215      0.769      0.812      0.140
  1381      -2212  pbar-               84  1371  1372     0     0     0     0      0.075     -0.672    142.566    142.570      0.938
  1382          3  (s)                -71   922   922  1385  1399  3252     0     -0.331     -0.096   -988.747    988.747      0.500
  1383          1  (d)                -71   916   916  1385  1399   815     0     -0.193      0.502    178.569    178.570      0.330
  1384          3  (s)                -71   896   896  1385  1399  3172     0     -0.193     -0.060     -1.396      1.497      0.500
  1385       -321  K-                  86  1382  1384     0     0     0     0     -0.309     -0.217   -329.621    329.621      0.494
  1386        323  (K*+)              -86  1382  1384  1596  1597     0     0      0.194     -0.171   -535.003    535.003      0.865
  1387       -313  (K*bar0)           -86  1382  1384  1598  1599     0     0     -0.525      0.395    -90.549     90.556      0.869
  1388        311  (K0)               -86  1382  1384  1600  1600     0     0      0.275     -0.432    -21.653     21.665      0.498
  1389        111  (pi0)              -83  1382  1384  1799  1800     0     0      0.085     -0.096     33.041     33.041      0.135
  1390       -213  (rho-)             -83  1382  1384  1601  1602     0     0     -0.571      1.375    103.191    103.205      0.748
  1391       2212  p+                  83  1382  1384     0     0     0     0      0.451     -0.712     35.574     35.597      0.938
  1392      -2112  nbar0               83  1382  1384     0     0     0     0     -0.351     -0.334      5.086      5.194      0.940
  1393        111  (pi0)              -83  1382  1384  1801  1802     0     0      0.166      0.244     -0.254      0.412      0.135
  1394       -211  pi-                 83  1382  1384     0     0     0     0      0.203     -0.088      0.343      0.432      0.140
  1395        223  (omega)            -84  1382  1384  1803  1805     0     0     -0.002      0.205     -0.341      0.887      0.793
  1396        213  (rho+)             -84  1382  1384  1603  1604     0     0      0.015      0.049     -1.479      1.683      0.803
  1397       -211  pi-                 84  1382  1384     0     0     0     0     -0.139     -0.385      0.488      0.652      0.140
  1398        323  (K*+)              -84  1382  1384  1605  1606     0     0     -0.666      0.513     -2.840      3.112      0.954
  1399       3334  Omega-              88  1382  1384     0     0     0     0      0.458     -0.001     -7.558      7.754      1.672
  1400         21  (g)                -71   941   941  1414  1446  2056  1571      0.497     -0.061    270.099    270.100      0.213
  1401         21  (g)                -71   801   801  1414  1446  1571  1866      0.646      0.338    171.472    171.474      0.000
  1402         21  (g)                -71   861   861  1414  1446  1866  1121      0.052      0.862    175.504    175.506      0.000
  1403         21  (g)                -71   836   836  1414  1446  1121  1317     -0.174      0.107    197.718    197.718      0.000
  1404         21  (g)                -71   724   724  1414  1446  1317   691     -1.460      0.380    498.123    498.125      0.000
  1405         21  (g)                -71   943   943  1414  1446   691  2211     -2.117      0.239    211.339    211.350      0.497
  1406         21  (g)                -71   848   848  1414  1446  2211  2437     -0.045     -2.306    224.710    224.722      0.000
  1407         21  (g)                -71   837   837  1414  1446  2437  2485      1.255     -1.894    420.866    420.872      0.000
  1408         21  (g)                -71   942   942  1414  1446  2485   699      1.025     -0.846    146.649    146.656      0.347
  1409         21  (g)                -71   723   723  1414  1446   699  1409      3.519     -0.045    212.991    213.020      0.000
  1410         21  (g)                -71   855   855  1414  1446  1409   975      2.116      0.636    113.685    113.706      0.000
  1411          2  (u)                -71   761   761  1414  1446   975     0      1.168     -1.266     86.524     86.542      0.330
  1412          3  (s)                -71   926   926  1414  1446   928     0     -0.312     -0.625   -649.419    649.419      0.500
  1413          2  (u)                -71   760   760  1414  1446  1310     0      0.085     -1.096   -160.892    160.896      0.330
  1414       -323  (K*-)              -86  1400  1413  1607  1608     0     0     -0.575     -0.817   -462.537    462.539      0.920
  1415        211  pi+                 83  1400  1413     0     0     0     0      0.607     -0.415     26.901     26.912      0.140
  1416       -211  pi-                 83  1400  1413     0     0     0     0      0.132      0.005     11.986     11.987      0.140
  1417        113  (rho0)             -83  1400  1413  1609  1610     0     0      1.699     -0.364    115.090    115.108      0.968
  1418        323  (K*+)              -83  1400  1413  1611  1612     0     0      1.801     -0.005    124.920    124.937      0.998
  1419       -311  (Kbar0)            -83  1400  1413  1613  1613     0     0      0.991     -0.483     71.745     71.755      0.498
  1420       -213  (rho-)             -83  1400  1413  1614  1615     0     0      1.621      0.044    159.545    159.556      0.926
  1421        211  pi+                 83  1400  1413     0     0     0     0      1.216     -0.255    148.853    148.858      0.140
  1422       -211  pi-                 83  1400  1413     0     0     0     0      0.289     -1.784    151.714    151.725      0.140
  1423        111  (pi0)              -83  1400  1413  1806  1807     0     0     -0.006     -0.873    239.057    239.059      0.135
  1424        321  K+                  83  1400  1413     0     0     0     0      0.123     -0.019     79.956     79.958      0.494
  1425       -311  (Kbar0)            -83  1400  1413  1616  1616     0     0      0.359     -1.387    159.344    159.351      0.498
  1426        311  (K0)               -84  1400  1413  1617  1617     0     0     -1.556      0.344    257.142    257.147      0.498
  1427       -321  K-                  84  1400  1413     0     0     0     0     -0.906     -0.052    139.132    139.136      0.494
  1428        211  pi+                 84  1400  1413     0     0     0     0      0.294     -0.040     35.901     35.903      0.140
  1429        311  (K0)               -84  1400  1413  1618  1618     0     0      0.020      0.655    253.000    253.002      0.498
  1430       -311  (Kbar0)            -84  1400  1413  1619  1619     0     0     -1.128     -0.126    333.939    333.941      0.498
  1431        223  (omega)            -84  1400  1413  1808  1809     0     0      0.348      0.591    198.961    198.963      0.782
  1432       -213  (rho-)             -84  1400  1413  1620  1621     0     0      0.400      0.454    125.137    125.143      1.079
  1433        211  pi+                 84  1400  1413     0     0     0     0     -0.213      0.244     40.451     40.452      0.140
  1434        113  (rho0)             -84  1400  1413  1622  1623     0     0      0.341     -0.417     45.388     45.399      0.793
  1435       2112  n0                  84  1400  1413     0     0     0     0     -0.122     -0.068      6.352      6.423      0.940
  1436        211  pi+                 84  1400  1413     0     0     0     0      0.284      0.173      0.413      0.548      0.140
  1437      -2224  (Deltabar--)       -84  1400  1413  1624  1625     0     0      0.024      0.463      2.992      3.277      1.255
  1438        323  (K*+)              -84  1400  1413  1626  1627     0     0     -0.455     -0.892      0.317      1.384      0.902
  1439       -313  (K*bar0)           -84  1400  1413  1628  1629     0     0     -0.135      0.267     -0.539      1.053      0.853
  1440       -211  pi-                 84  1400  1413     0     0     0     0      0.882      0.396     -1.202      1.549      0.140
  1441        321  K+                  84  1400  1413     0     0     0     0     -0.176     -0.181     -0.421      0.696      0.494
  1442       -321  K-                  84  1400  1413     0     0     0     0     -0.330     -0.368     -3.753      3.817      0.494
  1443        321  K+                  84  1400  1413     0     0     0     0     -0.202      0.392     -3.280      3.346      0.494
  1444       -311  (Kbar0)            -84  1400  1413  1630  1630     0     0     -0.033     -0.391     -5.606      5.642      0.498
  1445       -213  (rho-)             -84  1400  1413  1631  1632     0     0      0.299     -0.277    -95.265     95.269      0.805
  1446       2224  (Delta++)          -88  1400  1413  1633  1634     0     0      0.362     -0.390   -236.266    236.270      1.263
  1447        211  pi+                 91  1019     0     0     0     0     0      0.359      0.405      2.845      2.900      0.140
  1448        111  (pi0)              -91  1019     0  1810  1811     0     0     -0.356      0.323      1.901      1.965      0.135
  1449        310  K_S0                91  1020  1020     0     0     0     0     -0.887      0.575      0.932      1.494      0.498
  1450        130  K_L0                91  1021  1021     0     0     0     0     -0.471      0.139      3.363      3.435      0.498
  1451        211  pi+                 91  1024     0     0     0     0     0      0.182     -0.234      0.831      0.894      0.140
  1452       -211  pi-                 91  1024     0     0     0     0     0     -0.231     -0.704      3.935      4.006      0.140
  1453       -211  pi-                 91  1026     0     0     0     0     0     -0.060      0.119      0.650      0.678      0.140
  1454        111  (pi0)              -91  1026     0  1812  1813     0     0     -0.490      0.072     -0.035      0.515      0.135
  1455        211  pi+                 91  1038     0     0     0     0     0     -0.262     -0.192      0.122      0.374      0.140
  1456       -211  pi-                 91  1038     0     0     0     0     0      0.072      0.417     -0.027      0.446      0.140
  1457        311  (K0)               -91  1041     0  1635  1635     0     0     -0.179      0.222      1.022      1.172      0.498
  1458        211  pi+                 91  1041     0     0     0     0     0      0.184      0.069      0.047      0.246      0.140
  1459       -311  (Kbar0)            -91  1044     0  1636  1636     0     0     -0.191     -0.069    -31.503     31.508      0.498
  1460       -211  pi-                 91  1044     0     0     0     0     0      0.295     -0.102    -35.301     35.303      0.140
  1461        211  pi+                 91  1046     0     0     0     0     0     -0.459      0.063    -25.968     25.973      0.140
  1462        111  (pi0)              -91  1046     0  1814  1815     0     0      0.213      0.409    -28.391     28.395      0.135
  1463       -211  pi-                 91  1047     0     0     0     0     0     -0.080      0.294     -2.120      2.147      0.140
  1464        111  (pi0)              -91  1047     0  1816  1817     0     0     -0.073     -0.261     -7.825      7.831      0.135
  1465       -211  pi-                 91  1052     0     0     0     0     0     -0.448     -0.222   -144.559    144.560      0.140
  1466        111  (pi0)              -91  1052     0  1818  1819     0     0      0.073      0.377    -51.581     51.583      0.135
  1467        310  K_S0                91  1054  1054     0     0     0     0     -0.615     -0.329     -6.047      6.107      0.498
  1468        130  K_L0                91  1055  1055     0     0     0     0     -0.067      0.129     -6.687      6.707      0.498
  1469        211  pi+                 91  1060     0     0     0     0     0      0.675     -0.265     -1.922      2.059      0.140
  1470       -211  pi-                 91  1060     0     0     0     0     0     -0.077      0.083     -1.341      1.353      0.140
  1471        211  pi+                 91  1062     0     0     0     0     0      0.260      0.278     -1.144      1.214      0.140
  1472       -211  pi-                 91  1062     0     0     0     0     0      0.689     -0.071     -2.097      2.213      0.140
  1473        211  pi+                 91  1067     0     0     0     0     0     -0.079     -0.045    -15.017     15.018      0.140
  1474        111  (pi0)              -91  1067     0  1820  1821     0     0      0.618     -0.398    -33.201     33.210      0.135
  1475        211  pi+                 91  1078     0     0     0     0     0      0.752     -0.239     -1.257      1.491      0.140
  1476       -211  pi-                 91  1078     0     0     0     0     0      0.499      0.345     -0.585      0.854      0.140
  1477       -321  K-                  91  1081     0     0     0     0     0      0.581      0.139     -0.215      0.804      0.494
  1478        111  (pi0)              -91  1081     0  1822  1823     0     0      0.781     -0.014     -0.856      1.167      0.135
  1479        211  pi+                 91  1084     0     0     0     0     0      0.509     -0.393     -0.044      0.660      0.140
  1480       -211  pi-                 91  1084     0     0     0     0     0      0.563      0.611     -0.303      0.895      0.140
  1481        311  (K0)               -91  1085     0  1637  1637     0     0      0.887      0.914     -2.041      2.457      0.498
  1482        211  pi+                 91  1085     0     0     0     0     0      0.411      1.180     -1.271      1.788      0.140
  1483       3122  Lambda0             91  1093     0     0     0     0     0      0.514      1.297    -23.416     23.485      1.116
  1484        211  pi+                 91  1093     0     0     0     0     0      0.512      0.186     -6.713      6.737      0.140
  1485        211  pi+                 91  1098     0     0     0     0     0      0.412      1.294     -7.818      7.936      0.140
  1486        111  (pi0)              -91  1098     0  1824  1825     0     0     -0.035      0.155     -4.360      4.365      0.135
  1487        211  pi+                 91  1101     0     0     0     0     0     -0.425      0.048     -2.203      2.248      0.140
  1488        111  (pi0)              -91  1101     0  1826  1827     0     0     -0.600      1.007     -3.312      3.516      0.135
  1489       2212  p+                  91  1107     0     0     0     0     0      0.043     -0.314    -55.358     55.367      0.938
  1490       -211  pi-                 91  1107     0     0     0     0     0     -0.009     -0.295    -18.140     18.143      0.140
  1491      -2112  nbar0               91  1108     0     0     0     0     0     -0.413      0.097    -30.712     30.729      0.940
  1492        211  pi+                 91  1108     0     0     0     0     0      0.059     -0.361    -15.607     15.612      0.140
  1493        130  K_L0                91  1112  1112     0     0     0     0      0.114     -0.751     -0.751      1.178      0.498
  1494        130  K_L0                91  1113  1113     0     0     0     0      0.474     -0.774     -1.270      1.639      0.498
  1495       -211  pi-                 91  1116     0     0     0     0     0     -0.002     -0.278     -0.109      0.329      0.140
  1496        111  (pi0)              -91  1116     0  1828  1829     0     0     -0.343      0.159      0.473      0.620      0.135
  1497        211  pi+                 91  1119     0     0     0     0     0     -0.052      0.280     -0.829      0.887      0.140
  1498        111  (pi0)              -91  1119     0  1830  1831     0     0     -0.383     -0.291     -2.698      2.744      0.135
  1499        130  K_L0                91  1120  1120     0     0     0     0     -0.291     -0.584     -2.732      2.852      0.498
  1500       -321  K-                  91  1121     0     0     0     0     0      0.273      0.615    -16.308     16.329      0.494
  1501        111  (pi0)              -91  1121     0  1832  1833     0     0     -0.197     -0.227     -5.253      5.264      0.135
  1502        211  pi+                 91  1122     0     0     0     0     0     -0.294     -0.329     -6.703      6.719      0.140
  1503       -211  pi-                 91  1122     0     0     0     0     0      0.098     -0.057    -17.567     17.567      0.140
  1504        211  pi+                 91  1137     0     0     0     0     0     -0.270      0.333     -0.045      0.452      0.140
  1505       -211  pi-                 91  1137     0     0     0     0     0     -0.964     -0.632      0.114      1.167      0.140
  1506        211  pi+                 91  1138     0     0     0     0     0     -0.552     -0.081     -0.434      0.720      0.140
  1507        111  (pi0)              -91  1138     0  1834  1835     0     0     -2.463     -0.586      0.170      2.541      0.135
  1508       -211  pi-                 91  1143     0     0     0     0     0      0.375      0.216     -1.195      1.278      0.140
  1509        111  (pi0)              -91  1143     0  1836  1837     0     0     -0.383     -0.666     -0.665      1.025      0.135
  1510       -211  pi-                 91  1145     0     0     0     0     0     -0.265      0.239     -0.883      0.962      0.140
  1511        111  (pi0)              -91  1145     0  1838  1839     0     0      0.171     -0.970     -2.835      3.005      0.135
  1512       -321  K-                  91  1158     0     0     0     0     0      1.091      1.359     -0.687      1.937      0.494
  1513        211  pi+                 91  1158     0     0     0     0     0     -0.020      0.043      0.090      0.173      0.140
  1514       -211  pi-                 91  1159     0     0     0     0     0     -0.417      0.557     -0.239      0.749      0.140
  1515        111  (pi0)              -91  1159     0  1840  1841     0     0      0.159      0.817     -0.179      0.862      0.135
  1516        211  pi+                 91  1167     0     0     0     0     0      0.260     -0.093      0.135      0.338      0.140
  1517       -211  pi-                 91  1167     0     0     0     0     0      0.498      0.783      0.031      0.939      0.140
  1518        211  pi+                 91  1170     0     0     0     0     0      0.002     -0.066      0.266      0.308      0.140
  1519       -211  pi-                 91  1170     0     0     0     0     0      1.061      0.533      0.735      1.403      0.140
  1520        311  (K0)               -91  1175     0  1638  1638     0     0     -1.015      0.352      1.464      1.883      0.498
  1521        211  pi+                 91  1175     0     0     0     0     0     -0.089      0.005      0.759      0.777      0.140
  1522        310  K_S0                91  1176  1176     0     0     0     0     -1.782      0.179      1.494      2.385      0.498
  1523       -311  (Kbar0)            -91  1187     0  1639  1639     0     0      3.530     10.136    182.206    182.523      0.498
  1524       -211  pi-                 91  1187     0     0     0     0     0      1.474      4.330     84.003     84.128      0.140
  1525       -321  K-                  91  1195     0     0     0     0     0      0.237      0.645     22.974     22.990      0.494
  1526        211  pi+                 91  1195     0     0     0     0     0     -0.147      1.075     36.381     36.397      0.140
  1527        211  pi+                 91  1200     0     0     0     0     0      0.220     -0.027      6.637      6.643      0.140
  1528        111  (pi0)              -91  1200     0  1842  1843     0     0      0.354      0.208     56.011     56.012      0.135
  1529       -211  pi-                 91  1202     0     0     0     0     0     -0.121     -0.211      1.845      1.866      0.140
  1530        111  (pi0)              -91  1202     0  1844  1845     0     0     -0.196     -0.114     14.809     14.811      0.135
  1531        211  pi+                 91  1217     0     0     0     0     0     -0.409     -0.986     -6.322      6.413      0.140
  1532        111  (pi0)              -91  1217     0  1846  1847     0     0     -0.656     -0.407     -8.605      8.641      0.135
  1533        211  pi+                 91  1219     0     0     0     0     0      0.020     -0.086     -5.533      5.535      0.140
  1534       -211  pi-                 91  1219     0     0     0     0     0      0.533     -1.491    -13.764     13.855      0.140
  1535       -321  K-                  91  1222     0     0     0     0     0      1.375     -1.112    -21.612     21.690      0.494
  1536        111  (pi0)              -91  1222     0  1848  1849     0     0      0.333     -0.026     -6.925      6.935      0.135
  1537        211  pi+                 91  1228     0     0     0     0     0      0.228     -0.266      0.295      0.479      0.140
  1538        111  (pi0)              -91  1228     0  1850  1851     0     0     -0.410      0.011      0.308      0.531      0.135
  1539        211  pi+                 91  1235     0     0     0     0     0      0.086      0.262    -35.554     35.556      0.140
  1540       -211  pi-                 91  1235     0     0     0     0     0      0.177     -0.218     -9.317      9.322      0.140
  1541        310  K_S0                91  1243  1243     0     0     0     0      0.431     -0.227      4.849      4.899      0.498
  1542       -311  (Kbar0)            -91  1244     0  1640  1640     0     0     -0.271      0.040      1.152      1.284      0.498
  1543       -211  pi-                 91  1244     0     0     0     0     0      0.108      0.498      0.688      0.868      0.140
  1544        311  (K0)               -91  1246     0  1641  1641     0     0     -0.376      0.921      0.419      1.188      0.498
  1545        211  pi+                 91  1246     0     0     0     0     0      0.106      0.343      0.487      0.621      0.140
  1546        321  K+                  91  1262     0     0     0     0     0     -0.434      0.516      4.074      4.159      0.494
  1547       -211  pi-                 91  1262     0     0     0     0     0     -0.011      0.691      4.117      4.176      0.140
  1548        310  K_S0                91  1263  1263     0     0     0     0     -1.160      2.311      8.845      9.228      0.498
  1549       3122  Lambda0             91  1266     0     0     0     0     0     -0.171     -0.050      6.914      7.006      1.116
  1550       -211  pi-                 91  1266     0     0     0     0     0      0.001      0.035      0.327      0.357      0.140
  1551        311  (K0)               -91  1275     0  1642  1642     0     0      1.563     -2.295     81.216     81.265      0.498
  1552        211  pi+                 91  1275     0     0     0     0     0      0.441     -0.309     10.891     10.905      0.140
  1553        310  K_S0                91  1276  1276     0     0     0     0     -0.604     -0.423     16.059     16.084      0.498
  1554        130  K_L0                91  1277  1277     0     0     0     0      0.054      0.078     16.426     16.434      0.498
  1555       -311  (Kbar0)            -91  1278     0  1643  1643     0     0      0.086     -0.629     23.406     23.420      0.498
  1556       -211  pi-                 91  1278     0     0     0     0     0     -0.489     -0.441     28.062     28.070      0.140
  1557       -321  K-                  91  1300     0     0     0     0     0     -0.442     -0.174    -20.685     20.696      0.494
  1558        211  pi+                 91  1300     0     0     0     0     0      0.392     -0.456    -28.021     28.027      0.140
  1559        211  pi+                 91  1305     0     0     0     0     0      0.626     -2.073   -121.648    121.667      0.140
  1560       -211  pi-                 91  1305     0     0     0     0     0      0.383     -0.165    -33.998     34.001      0.140
  1561        321  K+                  91  1324     0     0     0     0     0     -0.354      0.369    -24.195     24.205      0.494
  1562       -211  pi-                 91  1324     0     0     0     0     0     -0.699      0.931    -54.474     54.486      0.140
  1563       -311  (Kbar0)            -91  1325     0  1644  1644     0     0     -0.987      0.936    -35.665     35.694      0.498
  1564       -211  pi-                 91  1325     0     0     0     0     0     -0.906      0.207    -25.768     25.785      0.140
  1565        211  pi+                 91  1326     0     0     0     0     0     -0.012      1.089    -21.372     21.400      0.140
  1566       -211  pi-                 91  1326     0     0     0     0     0     -0.591      0.053     -7.730      7.754      0.140
  1567       -211  pi-                 91  1329     0     0     0     0     0     -0.375      0.529    -59.148     59.152      0.140
  1568        111  (pi0)              -91  1329     0  1852  1853     0     0      0.175     -0.226    -37.634     37.636      0.135
  1569        211  pi+                 91  1330     0     0     0     0     0      0.689     -0.041     -6.826      6.862      0.140
  1570       -211  pi-                 91  1330     0     0     0     0     0     -0.193     -0.052     -7.672      7.676      0.140
  1571        130  K_L0                91  1340  1340     0     0     0     0     -0.379      0.182     20.963     20.973      0.498
  1572        211  pi+                 91  1343     0     0     0     0     0     -0.132     -0.240      3.212      3.227      0.140
  1573        111  (pi0)              -91  1343     0  1854  1855     0     0     -0.005     -0.527      0.981      1.121      0.135
  1574        211  pi+                 91  1346     0     0     0     0     0     -0.105      0.161     -0.273      0.362      0.140
  1575       -211  pi-                 91  1346     0     0     0     0     0     -0.128     -0.547     -0.194      0.611      0.140
  1576        211  pi+                 91  1354     0     0     0     0     0     -0.268     -0.063      4.493      4.503      0.140
  1577       -211  pi-                 91  1354     0     0     0     0     0      0.311     -0.076     56.665     56.666      0.140
  1578       -311  (Kbar0)            -91  1358     0  1645  1645     0     0      0.270     -0.172      0.479      0.761      0.498
  1579       -211  pi-                 91  1358     0     0     0     0     0     -0.254      0.033      0.308      0.424      0.140
  1580        211  pi+                 91  1359     0     0     0     0     0     -0.091      0.450      0.436      0.649      0.140
  1581        111  (pi0)              -91  1359     0  1856  1857     0     0     -0.184     -0.339      0.456      0.612      0.135
  1582        321  K+                  91  1360     0     0     0     0     0     -0.065     -0.365     -0.407      0.739      0.494
  1583       -211  pi-                 91  1360     0     0     0     0     0      0.010      0.227     -0.163      0.313      0.140
  1584        211  pi+                 91  1366     0     0     0     0     0     -0.028     -0.328      0.830      0.904      0.140
  1585       -211  pi-                 91  1366     0     0     0     0     0     -1.750     -5.506      8.311     10.122      0.140
  1586        311  (K0)               -91  1367     0  1646  1646     0     0     -0.204     -1.395      1.653      2.229      0.498
  1587        211  pi+                 91  1367     0     0     0     0     0     -0.050     -0.796      1.996      2.154      0.140
  1588        211  pi+                 91  1369     0     0     0     0     0     -0.066     -0.146      0.214      0.301      0.140
  1589        111  (pi0)              -91  1369     0  1858  1859     0     0     -0.148      0.714      2.104      2.231      0.135
  1590        211  pi+                 91  1375     0     0     0     0     0     -0.067      0.284     -0.607      0.688      0.140
  1591       -211  pi-                 91  1375     0     0     0     0     0     -0.178     -0.151     -2.160      2.177      0.140
  1592       -211  pi-                 91  1377     0     0     0     0     0      0.725      0.346     -0.528      0.971      0.140
  1593        111  (pi0)              -91  1377     0  1860  1861     0     0      0.117     -0.335     -0.006      0.380      0.135
  1594       2112  n0                  91  1379     0     0     0     0     0      0.002      0.130     10.525     10.568      0.940
  1595       -211  pi-                 91  1379     0     0     0     0     0      0.046     -0.310      9.638      9.644      0.140
  1596        311  (K0)               -91  1386     0  1647  1647     0     0      0.342     -0.138   -475.669    475.669      0.498
  1597        211  pi+                 91  1386     0     0     0     0     0     -0.148     -0.032    -59.334     59.334      0.140
  1598       -321  K-                  91  1387     0     0     0     0     0     -0.656      0.333    -71.304     71.309      0.494
  1599        211  pi+                 91  1387     0     0     0     0     0      0.131      0.062    -19.245     19.246      0.140
  1600        310  K_S0                91  1388  1388     0     0     0     0      0.275     -0.432    -21.653     21.665      0.498
  1601       -211  pi-                 91  1390     0     0     0     0     0     -0.595      1.337     99.246     99.257      0.140
  1602        111  (pi0)              -91  1390     0  1862  1863     0     0      0.024      0.038      3.945      3.948      0.135
  1603        211  pi+                 91  1396     0     0     0     0     0      0.287      0.206     -0.398      0.550      0.140
  1604        111  (pi0)              -91  1396     0  1864  1865     0     0     -0.271     -0.156     -1.081      1.134      0.135
  1605        321  K+                  91  1398     0     0     0     0     0     -0.186      0.523     -1.359      1.549      0.494
  1606        111  (pi0)              -91  1398     0  1866  1867     0     0     -0.480     -0.010     -1.481      1.563      0.135
  1607       -321  K-                  91  1414     0     0     0     0     0     -0.047     -0.201   -186.159    186.159      0.494
  1608        111  (pi0)              -91  1414     0  1868  1869     0     0     -0.529     -0.616   -276.378    276.379      0.135
  1609        211  pi+                 91  1417     0     0     0     0     0      0.462      0.024     59.239     59.241      0.140
  1610       -211  pi-                 91  1417     0     0     0     0     0      1.237     -0.388     55.851     55.866      0.140
  1611        311  (K0)               -91  1418     0  1648  1648     0     0      1.511     -0.000     79.975     79.991      0.498
  1612        211  pi+                 91  1418     0     0     0     0     0      0.290     -0.005     44.945     44.946      0.140
  1613        130  K_L0                91  1419  1419     0     0     0     0      0.991     -0.483     71.745     71.755      0.498
  1614       -211  pi-                 91  1420     0     0     0     0     0      1.452      0.005    153.517    153.524      0.140
  1615        111  (pi0)              -91  1420     0  1870  1871     0     0      0.169      0.039      6.028      6.032      0.135
  1616        310  K_S0                91  1425  1425     0     0     0     0      0.359     -1.387    159.344    159.351      0.498
  1617        130  K_L0                91  1426  1426     0     0     0     0     -1.556      0.344    257.142    257.147      0.498
  1618        130  K_L0                91  1429  1429     0     0     0     0      0.020      0.655    253.000    253.002      0.498
  1619        130  K_L0                91  1430  1430     0     0     0     0     -1.128     -0.126    333.939    333.941      0.498
  1620       -211  pi-                 91  1432     0     0     0     0     0      0.211      0.784     90.819     90.823      0.140
  1621        111  (pi0)              -91  1432     0  1872  1873     0     0      0.189     -0.331     34.318     34.320      0.135
  1622        211  pi+                 91  1434     0     0     0     0     0      0.131      0.187      8.284      8.288      0.140
  1623       -211  pi-                 91  1434     0     0     0     0     0      0.209     -0.604     37.105     37.110      0.140
  1624      -2212  pbar-               91  1437     0     0     0     0     0      0.115      0.465      2.904      3.089      0.938
  1625       -211  pi-                 91  1437     0     0     0     0     0     -0.091     -0.002      0.088      0.188      0.140
  1626        321  K+                  91  1438     0     0     0     0     0     -0.251     -0.945      0.285      1.132      0.494
  1627        111  (pi0)              -91  1438     0  1874  1875     0     0     -0.204      0.053      0.032      0.252      0.135
  1628       -311  (Kbar0)            -91  1439     0  1649  1649     0     0      0.139      0.043     -0.374      0.639      0.498
  1629        111  (pi0)              -91  1439     0  1876  1877     0     0     -0.274      0.224     -0.165      0.413      0.135
  1630        310  K_S0                91  1444  1444     0     0     0     0     -0.033     -0.391     -5.606      5.642      0.498
  1631       -211  pi-                 91  1445     0     0     0     0     0      0.007      0.249    -29.318     29.319      0.140
  1632        111  (pi0)              -91  1445     0  1878  1879     0     0      0.291     -0.526    -65.947     65.950      0.135
  1633       2212  p+                  91  1446     0     0     0     0     0      0.149     -0.202   -206.741    206.743      0.938
  1634        211  pi+                 91  1446     0     0     0     0     0      0.213     -0.187    -29.525     29.527      0.140
  1635        130  K_L0                91  1457  1457     0     0     0     0     -0.179      0.222      1.022      1.172      0.498
  1636        310  K_S0                91  1459  1459     0     0     0     0     -0.191     -0.069    -31.503     31.508      0.498
  1637        310  K_S0                91  1481  1481     0     0     0     0      0.887      0.914     -2.041      2.457      0.498
  1638        130  K_L0                91  1520  1520     0     0     0     0     -1.015      0.352      1.464      1.883      0.498
  1639        130  K_L0                91  1523  1523     0     0     0     0      3.530     10.136    182.206    182.523      0.498
  1640        130  K_L0                91  1542  1542     0     0     0     0     -0.271      0.040      1.152      1.284      0.498
  1641        130  K_L0                91  1544  1544     0     0     0     0     -0.376      0.921      0.419      1.188      0.498
  1642        310  K_S0                91  1551  1551     0     0     0     0      1.563     -2.295     81.216     81.265      0.498
  1643        130  K_L0                91  1555  1555     0     0     0     0      0.086     -0.629     23.406     23.420      0.498
  1644        310  K_S0                91  1563  1563     0     0     0     0     -0.987      0.936    -35.665     35.694      0.498
  1645        130  K_L0                91  1578  1578     0     0     0     0      0.270     -0.172      0.479      0.761      0.498
  1646        130  K_L0                91  1586  1586     0     0     0     0     -0.204     -1.395      1.653      2.229      0.498
  1647        130  K_L0                91  1596  1596     0     0     0     0      0.342     -0.138   -475.669    475.669      0.498
  1648        130  K_L0                91  1611  1611     0     0     0     0      1.511     -0.000     79.975     79.991      0.498
  1649        130  K_L0                91  1628  1628     0     0     0     0      0.139      0.043     -0.374      0.639      0.498
  1650         22  gamma               91  1015     0     0     0     0     0     -0.379      0.104     -2.342      2.375      0.000
  1651         22  gamma               91  1015     0     0     0     0     0     -0.114     -0.039     -0.589      0.601      0.000
  1652         22  gamma               91  1032     0     0     0     0     0      0.383      0.024     -0.717      0.813      0.000
  1653         22  gamma               91  1032     0     0     0     0     0      0.171      0.096     -0.288      0.348      0.000
  1654        211  pi+                 91  1045     0     0     0     0     0     -0.120      0.049     -2.485      2.492      0.140
  1655       -211  pi-                 91  1045     0     0     0     0     0     -0.088      0.101    -17.812     17.813      0.140
  1656        111  (pi0)              -91  1045     0  1880  1881     0     0      0.172      0.032     -8.618      8.621      0.135
  1657         22  gamma               91  1059     0     0     0     0     0     -0.046      0.104     -0.198      0.228      0.000
  1658         22  gamma               91  1059     0     0     0     0     0     -0.195      0.202     -0.201      0.346      0.000
  1659         22  gamma               91  1061     0     0     0     0     0      0.032     -0.121     -1.441      1.446      0.000
  1660         22  gamma               91  1061     0     0     0     0     0     -0.039      0.002     -0.161      0.166      0.000
  1661         22  gamma               91  1065     0     0     0     0     0      0.002     -0.007     -7.126      7.126      0.000
  1662         22  gamma               91  1065     0     0     0     0     0     -1.113     -0.146  -1254.004   1254.004      0.000
  1663         22  gamma               91  1079     0     0     0     0     0      0.504     -0.500     -0.952      1.188      0.000
  1664         22  gamma               91  1079     0     0     0     0     0      0.398     -0.243     -0.605      0.764      0.000
  1665         22  gamma               91  1094     0     0     0     0     0      0.160      0.218     -2.186      2.203      0.000
  1666         22  gamma               91  1094     0     0     0     0     0      0.220      0.656     -5.366      5.411      0.000
  1667         22  gamma               91  1097     0     0     0     0     0     -0.000     -0.020     -0.666      0.666      0.000
  1668         22  gamma               91  1097     0     0     0     0     0     -0.150      0.117     -1.943      1.952      0.000
  1669         22  gamma               91  1099     0     0     0     0     0      0.115      0.657     -3.987      4.043      0.000
  1670         22  gamma               91  1099     0     0     0     0     0      0.194      2.559    -15.851     16.058      0.000
  1671         22  gamma               91  1109     0     0     0     0     0      0.007     -0.008     -0.093      0.093      0.000
  1672         22  gamma               91  1109     0     0     0     0     0      0.111      0.164    -14.090     14.092      0.000
  1673         22  gamma               91  1123     0     0     0     0     0      0.016      0.023     -0.053      0.060      0.000
  1674         22  gamma               91  1123     0     0     0     0     0      0.195      0.085     -1.965      1.976      0.000
  1675        211  pi+                 91  1135     0     0     0     0     0     -0.227     -0.150      0.097      0.321      0.140
  1676       -211  pi-                 91  1135     0     0     0     0     0     -0.854     -0.883      0.654      1.399      0.140
  1677        111  (pi0)              -91  1135     0  1882  1883     0     0     -0.441     -0.610     -0.015      0.765      0.135
  1678         22  gamma               91  1139     0     0     0     0     0     -0.135     -0.084     -0.147      0.217      0.000
  1679         22  gamma               91  1139     0     0     0     0     0     -0.525     -0.085     -0.327      0.624      0.000
  1680         22  gamma               91  1142     0     0     0     0     0     -0.433     -0.302     -1.487      1.578      0.000
  1681         22  gamma               91  1142     0     0     0     0     0     -0.233     -0.261     -0.784      0.859      0.000
  1682         22  gamma               91  1162     0     0     0     0     0     -0.413      1.664     -1.198      2.092      0.000
  1683         22  gamma               91  1162     0     0     0     0     0     -0.236      0.651     -0.429      0.815      0.000
  1684        211  pi+                 91  1164     0     0     0     0     0     -0.548      0.696      0.099      0.902      0.140
  1685       -211  pi-                 91  1164     0     0     0     0     0     -0.430      0.323     -0.192      0.588      0.140
  1686        111  (pi0)              -91  1164     0  1884  1885     0     0      0.014      0.034      0.022      0.142      0.135
  1687         22  gamma               91  1165     0     0     0     0     0     -0.240      1.000     -0.416      1.109      0.000
  1688         22  gamma               91  1165     0     0     0     0     0     -0.120      0.151     -0.406      0.450      0.000
  1689         22  gamma               91  1169     0     0     0     0     0     -0.012      0.017     -0.021      0.030      0.000
  1690         22  gamma               91  1169     0     0     0     0     0      0.239     -0.041     -0.135      0.278      0.000
  1691         22  gamma               91  1172     0     0     0     0     0      0.036      0.072      0.124      0.147      0.000
  1692         22  gamma               91  1172     0     0     0     0     0      0.009     -0.033      0.283      0.286      0.000
  1693        211  pi+                 91  1185     0     0     0     0     0      6.323     19.084    341.050    341.642      0.140
  1694       -211  pi-                 91  1185     0     0     0     0     0      0.677      2.381     42.914     42.985      0.140
  1695        111  (pi0)              -91  1185     0  1886  1887     0     0      5.667     17.523    314.320    314.859      0.135
  1696         22  gamma               91  1191     0     0     0     0     0     -0.051     -0.000      0.403      0.406      0.000
  1697         22  gamma               91  1191     0     0     0     0     0      0.021      0.051      2.438      2.439      0.000
  1698        321  K+                  91  1194     0     0     0     0     0     -0.234      1.066     28.138     28.163      0.494
  1699       -321  K-                  91  1194     0     0     0     0     0     -0.227      1.166     37.566     37.588      0.494
  1700         22  gamma               91  1196     0     0     0     0     0     -0.402      1.025     28.765     28.786      0.000
  1701         22  gamma               91  1196     0     0     0     0     0     -0.122      0.021      1.111      1.118      0.000
  1702         22  gamma               91  1199     0     0     0     0     0     -0.034      0.229     11.676     11.679      0.000
  1703         22  gamma               91  1199     0     0     0     0     0     -0.073      0.142      4.381      4.384      0.000
  1704        211  pi+                 91  1201     0     0     0     0     0     -0.137      0.100     47.218     47.219      0.140
  1705       -211  pi-                 91  1201     0     0     0     0     0     -0.088     -0.242     23.226     23.228      0.140
  1706        111  (pi0)              -91  1201     0  1888  1889     0     0      0.134      0.016     34.203     34.203      0.135
  1707        111  (pi0)              -91  1203     0  1890  1891     0     0      0.019     -0.157      0.861      0.885      0.135
  1708        111  (pi0)              -91  1203     0  1892  1893     0     0      0.224     -0.076      1.219      1.249      0.135
  1709        111  (pi0)              -91  1203     0  1894  1895     0     0      0.054     -0.144      0.391      0.441      0.135
  1710        211  pi+                 91  1215     0     0     0     0     0     -0.840     -0.458     -8.527      8.582      0.140
  1711       -211  pi-                 91  1215     0     0     0     0     0     -0.687     -0.333     -7.503      7.543      0.140
  1712        111  (pi0)              -91  1215     0  1896  1897     0     0     -0.665     -0.880     -8.600      8.672      0.135
  1713         22  gamma               91  1216     0     0     0     0     0     -0.483     -0.851     -7.609      7.671      0.000
  1714         22  gamma               91  1216     0     0     0     0     0      0.069      0.022     -0.237      0.248      0.000
  1715         22  gamma               91  1218     0     0     0     0     0     -0.487     -0.456     -7.421      7.451      0.000
  1716         22  gamma               91  1218     0     0     0     0     0     -0.395     -0.410     -5.116      5.148      0.000
  1717       -421  (Dbar0)            -91  1225     0  1898  1900     0     0     15.226    -12.352   -169.562    170.702      1.865
  1718        111  (pi0)              -91  1225     0  1901  1902     0     0      0.971     -0.830    -11.270     11.343      0.135
  1719        211  pi+                 91  1229     0     0     0     0     0      0.321      0.168      0.360      0.530      0.140
  1720       -211  pi-                 91  1229     0     0     0     0     0      0.137     -0.134      0.633      0.676      0.140
  1721        111  (pi0)              -91  1229     0  1903  1904     0     0     -0.066     -0.039      0.069      0.170      0.135
  1722         22  gamma               91  1232     0     0     0     0     0      0.077     -0.282     -0.417      0.509      0.000
  1723         22  gamma               91  1232     0     0     0     0     0      0.018     -0.105     -0.347      0.363      0.000
  1724         22  gamma               91  1238     0     0     0     0     0     -0.238      0.213     25.002     25.004      0.000
  1725         22  gamma               91  1238     0     0     0     0     0     -0.104      0.232     15.866     15.868      0.000
  1726         22  gamma               91  1239     0     0     0     0     0      0.271      0.086    118.113    118.113      0.000
  1727         22  gamma               91  1239     0     0     0     0     0      0.305      0.118     88.045     88.046      0.000
  1728        111  (pi0)              -91  1240     0  1905  1906     0     0     -0.082      0.079      3.929      3.933      0.135
  1729        111  (pi0)              -91  1240     0  1907  1908     0     0     -0.372     -0.031      8.848      8.857      0.135
  1730        111  (pi0)              -91  1240     0  1909  1910     0     0     -0.032      0.041      5.749      5.751      0.135
  1731         22  gamma               91  1245     0     0     0     0     0      0.022     -0.035      0.078      0.089      0.000
  1732         22  gamma               91  1245     0     0     0     0     0      0.195      0.082      0.180      0.278      0.000
  1733         22  gamma               91  1260     0     0     0     0     0      0.330      1.291      6.709      6.840      0.000
  1734         22  gamma               91  1260     0     0     0     0     0     -0.197      1.488      8.195      8.331      0.000
  1735        211  pi+                 91  1261     0     0     0     0     0     -0.361      0.413      6.480      6.504      0.140
  1736       -211  pi-                 91  1261     0     0     0     0     0     -0.156      0.240      1.227      1.268      0.140
  1737        111  (pi0)              -91  1261     0  1911  1912     0     0      0.039      0.225      2.729      2.742      0.135
  1738        211  pi+                 91  1269     0     0     0     0     0      0.030     -0.172      2.587      2.597      0.140
  1739       -211  pi-                 91  1269     0     0     0     0     0     -0.307     -0.351      2.233      2.286      0.140
  1740        111  (pi0)              -91  1269     0  1913  1914     0     0      0.107     -0.366      1.761      1.806      0.135
  1741         22  gamma               91  1274     0     0     0     0     0      0.166     -0.062      1.411      1.422      0.000
  1742         22  gamma               91  1274     0     0     0     0     0      0.028     -0.108      0.666      0.675      0.000
  1743         22  gamma               91  1281     0     0     0     0     0     -0.287     -0.141     12.945     12.949      0.000
  1744         22  gamma               91  1281     0     0     0     0     0     -0.073     -0.130      5.082      5.084      0.000
  1745         22  gamma               91  1303     0     0     0     0     0     -0.500     -0.206    -18.782     18.790      0.000
  1746         22  gamma               91  1303     0     0     0     0     0     -0.193     -0.102    -11.045     11.047      0.000
  1747        211  pi+                 91  1304     0     0     0     0     0     -0.205      0.029    -44.983     44.984      0.140
  1748       -211  pi-                 91  1304     0     0     0     0     0     -0.002     -0.247    -16.422     16.425      0.140
  1749        111  (pi0)              -91  1304     0  1915  1916     0     0     -0.075      0.077     -7.944      7.946      0.135
  1750         22  gamma               91  1307     0     0     0     0     0      0.565     -0.682    -71.682     71.687      0.000
  1751         22  gamma               91  1307     0     0     0     0     0      0.260     -0.219    -32.569     32.571      0.000
  1752         22  gamma               91  1313     0     0     0     0     0      1.329      0.584    -59.238     59.256      0.000
  1753         22  gamma               91  1313     0     0     0     0     0      0.108      0.084     -6.699      6.701      0.000
  1754         22  gamma               91  1315     0     0     0     0     0      0.115      0.240     -4.828      4.835      0.000
  1755         22  gamma               91  1315     0     0     0     0     0     -0.024      0.043     -1.843      1.844      0.000
  1756         22  gamma               91  1316     0     0     0     0     0      0.427      0.007    -13.793     13.800      0.000
  1757         22  gamma               91  1316     0     0     0     0     0      0.166      0.034     -3.452      3.456      0.000
  1758         22  gamma               91  1319     0     0     0     0     0     -0.016      0.248    -21.997     21.998      0.000
  1759         22  gamma               91  1319     0     0     0     0     0     -0.029      0.624    -39.373     39.378      0.000
  1760         22  gamma               91  1331     0     0     0     0     0     -0.052      0.016     -1.074      1.076      0.000
  1761         22  gamma               91  1331     0     0     0     0     0     -0.327      0.396    -17.502     17.509      0.000
  1762         22  gamma               91  1332     0     0     0     0     0      0.282      0.043     -2.682      2.697      0.000
  1763         22  gamma               91  1332     0     0     0     0     0      0.409     -0.093     -4.436      4.456      0.000
  1764        211  pi+                 91  1334     0     0     0     0     0     -0.080      0.387     -0.535      0.680      0.140
  1765       -211  pi-                 91  1334     0     0     0     0     0      0.027     -0.012      0.042      0.149      0.140
  1766        111  (pi0)              -91  1334     0  1917  1918     0     0      0.175      0.270     -0.225      0.415      0.135
  1767         22  gamma               91  1336     0     0     0     0     0      0.045      1.372      1.492      2.027      0.000
  1768         22  gamma               91  1336     0     0     0     0     0     -0.073      0.774      0.880      1.175      0.000
  1769         22  gamma               91  1337     0     0     0     0     0     -0.184      0.136      1.149      1.172      0.000
  1770         22  gamma               91  1337     0     0     0     0     0     -0.174      0.308      1.402      1.446      0.000
  1771         22  gamma               91  1341     0     0     0     0     0      0.021      0.036      0.234      0.238      0.000
  1772         22  gamma               91  1341     0     0     0     0     0     -0.157      0.043      1.403      1.412      0.000
  1773         22  gamma               91  1344     0     0     0     0     0      0.042      0.062      0.070      0.102      0.000
  1774         22  gamma               91  1344     0     0     0     0     0      0.139      0.845      1.223      1.493      0.000
  1775         22  gamma               91  1345     0     0     0     0     0      0.046      0.005      0.113      0.122      0.000
  1776         22  gamma               91  1345     0     0     0     0     0     -0.064     -0.080      0.473      0.484      0.000
  1777         22  gamma               91  1347     0     0     0     0     0      0.052     -0.376     -9.795      9.802      0.000
  1778         22  gamma               91  1347     0     0     0     0     0     -0.010      0.000     -0.063      0.064      0.000
  1779         22  gamma               91  1352     0     0     0     0     0      0.011     -0.001    177.622    177.622      0.000
  1780         22  gamma               91  1352     0     0     0     0     0      0.056      0.016     31.153     31.153      0.000
  1781        211  pi+                 91  1353     0     0     0     0     0     -0.156      0.210    107.002    107.002      0.140
  1782       -211  pi-                 91  1353     0     0     0     0     0     -0.361      0.038    139.417    139.418      0.140
  1783        111  (pi0)              -91  1353     0  1919  1920     0     0     -0.238      0.106    162.192    162.192      0.135
  1784        211  pi+                 91  1355     0     0     0     0     0      0.088      0.065      8.986      8.987      0.140
  1785       -211  pi-                 91  1355     0     0     0     0     0     -0.042     -0.181     16.895     16.897      0.140
  1786        111  (pi0)              -91  1355     0  1921  1922     0     0     -0.144      0.292     12.004     12.009      0.135
  1787        130  K_L0                91  1357     0     0     0     0     0      0.432      0.213      3.192      3.266      0.498
  1788        310  K_S0                91  1357     0     0     0     0     0      0.177      0.132      2.420      2.480      0.498
  1789       -521  (B-)               -91  1365     0  1923  1925     0     0    -30.897   -100.155    158.521    190.112      5.279
  1790         22  gamma               91  1365     0     0     0     0     0     -0.095     -0.427      0.630      0.767      0.000
  1791         12  nu_e                91  1370     0     0     0     0     0     -1.675      2.604      6.444      7.149      0.000
  1792        -11  e+                  91  1370     0     0     0     0     0     -7.458     11.460     20.510     24.650      0.001
  1793       -411  (D-)               -91  1370     0  1926  1928     0     0     -8.553     19.091     38.722     44.051      1.870
  1794        211  pi+                 91  1373     0     0     0     0     0     -0.267     -0.228    -32.349     32.351      0.140
  1795       -211  pi-                 91  1373     0     0     0     0     0      0.043     -0.518    -57.435     57.438      0.140
  1796        111  (pi0)              -91  1373     0  1929  1930     0     0      0.165     -0.139    -17.624     17.626      0.135
  1797         22  gamma               91  1376     0     0     0     0     0      0.019      0.028     -0.169      0.173      0.000
  1798         22  gamma               91  1376     0     0     0     0     0      0.357     -0.116     -2.070      2.104      0.000
  1799         22  gamma               91  1389     0     0     0     0     0     -0.001     -0.039     22.192     22.192      0.000
  1800         22  gamma               91  1389     0     0     0     0     0      0.086     -0.057     10.849     10.849      0.000
  1801         22  gamma               91  1393     0     0     0     0     0     -0.005      0.092     -0.046      0.102      0.000
  1802         22  gamma               91  1393     0     0     0     0     0      0.171      0.152     -0.209      0.310      0.000
  1803        211  pi+                 91  1395     0     0     0     0     0     -0.026     -0.062      0.085      0.177      0.140
  1804       -211  pi-                 91  1395     0     0     0     0     0      0.058     -0.020     -0.351      0.383      0.140
  1805        111  (pi0)              -91  1395     0  1931  1932     0     0     -0.034      0.287     -0.075      0.327      0.135
  1806         22  gamma               91  1423     0     0     0     0     0      0.045     -0.414    100.697    100.698      0.000
  1807         22  gamma               91  1423     0     0     0     0     0     -0.051     -0.458    138.360    138.361      0.000
  1808        111  (pi0)              -91  1431     0  1933  1934     0     0      0.120      0.527    183.920    183.921      0.135
  1809         22  gamma               91  1431     0     0     0     0     0      0.229      0.064     15.040     15.042      0.000
  1810         22  gamma               91  1448     0     0     0     0     0     -0.174      0.074      0.805      0.827      0.000
  1811         22  gamma               91  1448     0     0     0     0     0     -0.182      0.249      1.096      1.138      0.000
  1812         22  gamma               91  1454     0     0     0     0     0     -0.046     -0.019     -0.035      0.061      0.000
  1813         22  gamma               91  1454     0     0     0     0     0     -0.444      0.092     -0.000      0.454      0.000
  1814         22  gamma               91  1462     0     0     0     0     0     -0.001      0.046     -5.438      5.438      0.000
  1815         22  gamma               91  1462     0     0     0     0     0      0.214      0.363    -22.953     22.957      0.000
  1816         22  gamma               91  1464     0     0     0     0     0     -0.038     -0.040     -3.162      3.162      0.000
  1817         22  gamma               91  1464     0     0     0     0     0     -0.035     -0.222     -4.663      4.669      0.000
  1818         22  gamma               91  1466     0     0     0     0     0      0.112      0.252    -35.794     35.795      0.000
  1819         22  gamma               91  1466     0     0     0     0     0     -0.039      0.125    -15.787     15.788      0.000
  1820         22  gamma               91  1474     0     0     0     0     0      0.398     -0.195    -21.597     21.602      0.000
  1821         22  gamma               91  1474     0     0     0     0     0      0.220     -0.203    -11.604     11.607      0.000
  1822         22  gamma               91  1478     0     0     0     0     0      0.018      0.002     -0.065      0.067      0.000
  1823         22  gamma               91  1478     0     0     0     0     0      0.763     -0.016     -0.791      1.100      0.000
  1824         22  gamma               91  1486     0     0     0     0     0     -0.020      0.156     -2.494      2.499      0.000
  1825         22  gamma               91  1486     0     0     0     0     0     -0.015     -0.000     -1.866      1.866      0.000
  1826         22  gamma               91  1488     0     0     0     0     0     -0.127      0.233     -0.929      0.966      0.000
  1827         22  gamma               91  1488     0     0     0     0     0     -0.473      0.773     -2.383      2.550      0.000
  1828         22  gamma               91  1496     0     0     0     0     0     -0.090     -0.018      0.094      0.131      0.000
  1829         22  gamma               91  1496     0     0     0     0     0     -0.253      0.178      0.378      0.489      0.000
  1830         22  gamma               91  1498     0     0     0     0     0     -0.209     -0.214     -1.368      1.400      0.000
  1831         22  gamma               91  1498     0     0     0     0     0     -0.174     -0.077     -1.331      1.344      0.000
  1832         22  gamma               91  1501     0     0     0     0     0      0.000      0.006     -0.732      0.732      0.000
  1833         22  gamma               91  1501     0     0     0     0     0     -0.197     -0.233     -4.522      4.532      0.000
  1834         22  gamma               91  1507     0     0     0     0     0     -0.957     -0.184      0.115      0.981      0.000
  1835         22  gamma               91  1507     0     0     0     0     0     -1.506     -0.403      0.055      1.560      0.000
  1836         22  gamma               91  1509     0     0     0     0     0     -0.319     -0.480     -0.434      0.721      0.000
  1837         22  gamma               91  1509     0     0     0     0     0     -0.063     -0.186     -0.232      0.304      0.000
  1838         22  gamma               91  1511     0     0     0     0     0      0.137     -0.418     -1.335      1.406      0.000
  1839         22  gamma               91  1511     0     0     0     0     0      0.035     -0.552     -1.500      1.599      0.000
  1840         22  gamma               91  1515     0     0     0     0     0      0.170      0.786     -0.149      0.817      0.000
  1841         22  gamma               91  1515     0     0     0     0     0     -0.011      0.032     -0.030      0.045      0.000
  1842         22  gamma               91  1528     0     0     0     0     0      0.049      0.016      2.963      2.963      0.000
  1843         22  gamma               91  1528     0     0     0     0     0      0.306      0.193     53.048     53.049      0.000
  1844         22  gamma               91  1530     0     0     0     0     0     -0.091     -0.126      7.691      7.692      0.000
  1845         22  gamma               91  1530     0     0     0     0     0     -0.105      0.012      7.118      7.119      0.000
  1846         22  gamma               91  1532     0     0     0     0     0     -0.431     -0.297     -5.144      5.171      0.000
  1847         22  gamma               91  1532     0     0     0     0     0     -0.225     -0.110     -3.461      3.470      0.000
  1848         22  gamma               91  1536     0     0     0     0     0      0.066     -0.061     -1.927      1.929      0.000
  1849         22  gamma               91  1536     0     0     0     0     0      0.268      0.035     -4.999      5.006      0.000
  1850         22  gamma               91  1538     0     0     0     0     0     -0.013      0.024      0.050      0.057      0.000
  1851         22  gamma               91  1538     0     0     0     0     0     -0.397     -0.013      0.258      0.474      0.000
  1852         22  gamma               91  1568     0     0     0     0     0      0.182     -0.209    -37.095     37.096      0.000
  1853         22  gamma               91  1568     0     0     0     0     0     -0.007     -0.016     -0.539      0.540      0.000
  1854         22  gamma               91  1573     0     0     0     0     0     -0.066     -0.363      0.645      0.743      0.000
  1855         22  gamma               91  1573     0     0     0     0     0      0.060     -0.164      0.335      0.378      0.000
  1856         22  gamma               91  1581     0     0     0     0     0      0.016     -0.033      0.015      0.039      0.000
  1857         22  gamma               91  1581     0     0     0     0     0     -0.200     -0.306      0.441      0.573      0.000
  1858         22  gamma               91  1589     0     0     0     0     0     -0.033      0.027      0.084      0.094      0.000
  1859         22  gamma               91  1589     0     0     0     0     0     -0.115      0.687      2.021      2.137      0.000
  1860         22  gamma               91  1593     0     0     0     0     0      0.132     -0.228      0.032      0.266      0.000
  1861         22  gamma               91  1593     0     0     0     0     0     -0.015     -0.107     -0.038      0.114      0.000
  1862         22  gamma               91  1602     0     0     0     0     0      0.042     -0.020      0.538      0.540      0.000
  1863         22  gamma               91  1602     0     0     0     0     0     -0.018      0.058      3.407      3.408      0.000
  1864         22  gamma               91  1604     0     0     0     0     0     -0.225     -0.175     -0.984      1.025      0.000
  1865         22  gamma               91  1604     0     0     0     0     0     -0.047      0.018     -0.097      0.109      0.000
  1866         22  gamma               91  1606     0     0     0     0     0     -0.069      0.022     -0.385      0.392      0.000
  1867         22  gamma               91  1606     0     0     0     0     0     -0.411     -0.032     -1.095      1.170      0.000
  1868         22  gamma               91  1608     0     0     0     0     0     -0.259     -0.239   -102.093    102.094      0.000
  1869         22  gamma               91  1608     0     0     0     0     0     -0.269     -0.377   -174.285    174.286      0.000
  1870         22  gamma               91  1615     0     0     0     0     0     -0.001     -0.025      0.258      0.259      0.000
  1871         22  gamma               91  1615     0     0     0     0     0      0.169      0.064      5.770      5.773      0.000
  1872         22  gamma               91  1621     0     0     0     0     0      0.177     -0.343     32.694     32.696      0.000
  1873         22  gamma               91  1621     0     0     0     0     0      0.012      0.013      1.624      1.624      0.000
  1874         22  gamma               91  1627     0     0     0     0     0     -0.023      0.057     -0.020      0.064      0.000
  1875         22  gamma               91  1627     0     0     0     0     0     -0.181     -0.003      0.052      0.188      0.000
  1876         22  gamma               91  1629     0     0     0     0     0     -0.076      0.146     -0.089      0.187      0.000
  1877         22  gamma               91  1629     0     0     0     0     0     -0.198      0.078     -0.076      0.226      0.000
  1878         22  gamma               91  1632     0     0     0     0     0      0.220     -0.429    -57.538     57.540      0.000
  1879         22  gamma               91  1632     0     0     0     0     0      0.071     -0.097     -8.409      8.410      0.000
  1880         22  gamma               91  1656     0     0     0     0     0      0.194      0.037     -7.754      7.757      0.000
  1881         22  gamma               91  1656     0     0     0     0     0     -0.022     -0.005     -0.864      0.864      0.000
  1882         22  gamma               91  1677     0     0     0     0     0     -0.393     -0.565      0.024      0.688      0.000
  1883         22  gamma               91  1677     0     0     0     0     0     -0.048     -0.045     -0.038      0.076      0.000
  1884         22  gamma               91  1686     0     0     0     0     0     -0.002      0.003      0.077      0.077      0.000
  1885         22  gamma               91  1686     0     0     0     0     0      0.017      0.031     -0.055      0.065      0.000
  1886         22  gamma               91  1695     0     0     0     0     0      1.270      3.752     67.848     67.964      0.000
  1887         22  gamma               91  1695     0     0     0     0     0      4.397     13.771    246.472    246.895      0.000
  1888         22  gamma               91  1706     0     0     0     0     0      0.142     -0.021     30.709     30.709      0.000
  1889         22  gamma               91  1706     0     0     0     0     0     -0.008      0.037      3.494      3.494      0.000
  1890         22  gamma               91  1707     0     0     0     0     0      0.052     -0.144      0.805      0.820      0.000
  1891         22  gamma               91  1707     0     0     0     0     0     -0.033     -0.013      0.055      0.066      0.000
  1892         22  gamma               91  1708     0     0     0     0     0      0.201     -0.082      0.785      0.814      0.000
  1893         22  gamma               91  1708     0     0     0     0     0      0.024      0.006      0.435      0.435      0.000
  1894         22  gamma               91  1709     0     0     0     0     0      0.085     -0.037      0.188      0.210      0.000
  1895         22  gamma               91  1709     0     0     0     0     0     -0.031     -0.107      0.203      0.232      0.000
  1896         22  gamma               91  1712     0     0     0     0     0     -0.164     -0.265     -2.860      2.877      0.000
  1897         22  gamma               91  1712     0     0     0     0     0     -0.501     -0.615     -5.740      5.795      0.000
  1898        310  K_S0                91  1717     0     0     0     0     0      2.826     -2.482    -30.130     30.368      0.498
  1899       -211  pi-                 91  1717     0     0     0     0     0      5.664     -5.156    -68.408     68.836      0.140
  1900        211  pi+                 91  1717     0     0     0     0     0      6.736     -4.714    -71.024     71.498      0.140
  1901         22  gamma               91  1718     0     0     0     0     0      0.741     -0.704     -9.026      9.084      0.000
  1902         22  gamma               91  1718     0     0     0     0     0      0.230     -0.126     -2.244      2.259      0.000
  1903         22  gamma               91  1721     0     0     0     0     0     -0.017      0.004      0.097      0.099      0.000
  1904         22  gamma               91  1721     0     0     0     0     0     -0.049     -0.043     -0.028      0.071      0.000
  1905         22  gamma               91  1728     0     0     0     0     0     -0.060     -0.018      0.838      0.841      0.000
  1906         22  gamma               91  1728     0     0     0     0     0     -0.022      0.097      3.090      3.092      0.000
  1907         22  gamma               91  1729     0     0     0     0     0     -0.254     -0.076      5.243      5.250      0.000
  1908         22  gamma               91  1729     0     0     0     0     0     -0.118      0.045      3.604      3.607      0.000
  1909         22  gamma               91  1730     0     0     0     0     0     -0.062      0.075      3.478      3.479      0.000
  1910         22  gamma               91  1730     0     0     0     0     0      0.030     -0.034      2.271      2.272      0.000
  1911         22  gamma               91  1737     0     0     0     0     0     -0.050      0.083      1.105      1.109      0.000
  1912         22  gamma               91  1737     0     0     0     0     0      0.089      0.142      1.624      1.632      0.000
  1913         22  gamma               91  1740     0     0     0     0     0      0.057     -0.089      0.281      0.300      0.000
  1914         22  gamma               91  1740     0     0     0     0     0      0.050     -0.276      1.480      1.506      0.000
  1915         22  gamma               91  1749     0     0     0     0     0      0.012     -0.023     -2.961      2.961      0.000
  1916         22  gamma               91  1749     0     0     0     0     0     -0.088      0.100     -4.982      4.984      0.000
  1917         22  gamma               91  1766     0     0     0     0     0      0.064      0.216     -0.139      0.264      0.000
  1918         22  gamma               91  1766     0     0     0     0     0      0.111      0.054     -0.086      0.151      0.000
  1919         22  gamma               91  1783     0     0     0     0     0     -0.122      0.056     45.914     45.914      0.000
  1920         22  gamma               91  1783     0     0     0     0     0     -0.115      0.051    116.278    116.278      0.000
  1921         22  gamma               91  1786     0     0     0     0     0     -0.053      0.236      7.480      7.484      0.000
  1922         22  gamma               91  1786     0     0     0     0     0     -0.092      0.056      4.523      4.525      0.000
  1923        421  (D0)               -91  1789     0  1935  1937     0     0    -16.579    -47.108     73.837     89.160      1.865
  1924        111  (pi0)              -91  1789     0  1938  1939     0     0     -9.407    -35.694     57.590     68.405      0.135
  1925       -211  pi-                 91  1789     0     0     0     0     0     -4.910    -17.352     27.094     32.547      0.140
  1926       -311  (Kbar0)            -91  1793     0  1940  1940     0     0     -2.126      4.332      8.593      9.868      0.498
  1927       -211  pi-                 91  1793     0     0     0     0     0     -2.186      3.706      7.728      8.846      0.140
  1928        111  (pi0)              -91  1793     0  1941  1942     0     0     -4.241     11.052     22.401     25.337      0.135
  1929         22  gamma               91  1796     0     0     0     0     0      0.005      0.006     -4.945      4.945      0.000
  1930         22  gamma               91  1796     0     0     0     0     0      0.160     -0.144    -12.679     12.681      0.000
  1931         22  gamma               91  1805     0     0     0     0     0     -0.048      0.294     -0.057      0.303      0.000
  1932         22  gamma               91  1805     0     0     0     0     0      0.014     -0.007     -0.018      0.024      0.000
  1933         22  gamma               91  1808     0     0     0     0     0     -0.028      0.077     32.171     32.171      0.000
  1934         22  gamma               91  1808     0     0     0     0     0      0.148      0.449    151.749    151.750      0.000
  1935       -321  K-                  91  1923     0     0     0     0     0     -4.241    -13.582     21.133     25.481      0.494
  1936        211  pi+                 91  1923     0     0     0     0     0     -4.052    -11.487     18.708     22.325      0.140
  1937        111  (pi0)              -91  1923     0  1943  1944     0     0     -8.285    -22.039     33.996     41.354      0.135
  1938         22  gamma               91  1924     0     0     0     0     0     -9.085    -34.467     55.656     66.092      0.000
  1939         22  gamma               91  1924     0     0     0     0     0     -0.323     -1.227      1.934      2.313      0.000
  1940        130  K_L0                91  1926  1926     0     0     0     0     -2.126      4.332      8.593      9.868      0.498
  1941         22  gamma               91  1928     0     0     0     0     0     -3.450      9.005     18.135     20.540      0.000
  1942         22  gamma               91  1928     0     0     0     0     0     -0.791      2.047      4.266      4.797      0.000
  1943         22  gamma               91  1937     0     0     0     0     0     -4.617    -12.471     19.212     23.365      0.000
  1944         22  gamma               91  1937     0     0     0     0     0     -3.668     -9.569     14.784     17.988      0.000
                                   Charge sum:  2.000           Momentum sum:      0.000      0.000      0.000  13600.000  13600.000

 --------  End PYTHIA Event Listing  -----------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------
#                         FastJet release 3.4.0
#                 M. Cacciari, G.P. Salam and G. Soyez                  
#     A software package for jet finding and analysis at colliders      
#                           http://fastjet.fr                           
#	                                                                      
# Please cite EPJC72(2012)1896 [arXiv:1111.6097] if you use this package
# for scientific work and optionally PLB641(2006)57 [hep-ph/0512210].   
#                                                                       
# FastJet is provided without warranty under the GNU GPL v2 or higher.  
# It uses T. Chan's closest pair algorithm, S. Fortune's Voronoi code
# and 3rd party plugin jet algorithms. See COPYING file for details.
#--------------------------------------------------------------------------
Begin processing the 2nd record. Run 1, Event 2, LumiSection 1 on stream 0 at 21-May-2025 03:32:19.780 CEST
Begin processing the 3rd record. Run 1, Event 3, LumiSection 1 on stream 0 at 21-May-2025 03:32:21.944 CEST
Begin processing the 4th record. Run 1, Event 4, LumiSection 1 on stream 0 at 21-May-2025 03:32:28.438 CEST
Begin processing the 5th record. Run 1, Event 5, LumiSection 1 on stream 0 at 21-May-2025 03:32:37.008 CEST
Begin processing the 6th record. Run 1, Event 6, LumiSection 1 on stream 0 at 21-May-2025 03:32:47.804 CEST
Begin processing the 7th record. Run 1, Event 7, LumiSection 1 on stream 0 at 21-May-2025 03:32:54.697 CEST
Begin processing the 8th record. Run 1, Event 8, LumiSection 1 on stream 0 at 21-May-2025 03:33:03.909 CEST
Begin processing the 9th record. Run 1, Event 9, LumiSection 1 on stream 0 at 21-May-2025 03:33:13.847 CEST
Begin processing the 10th record. Run 1, Event 10, LumiSection 1 on stream 0 at 21-May-2025 03:33:22.706 CEST

 *-------  PYTHIA Event and Cross Section Statistics  -------------------------------------------------------------*
 |                                                                                                                 |
 | Subprocess                                    Code |            Number of events       |      sigma +- delta    |
 |                                                    |       Tried   Selected   Accepted |     (estimated) (mb)   |
 |                                                    |                                   |                        |
 |-----------------------------------------------------------------------------------------------------------------|
 |                                                    |                                   |                        |
 | Les Houches User Process(es)                  9999 |          10         10         10 |   4.164e-09  0.000e+00 |
 |    ... whereof user classification code       9999 |          10         10         10 |                        | 
 |                                                    |                                   |                        |
 | sum                                                |          10         10         10 |   4.164e-09  0.000e+00 |
 |                                                                                                                 |
 *-------  End PYTHIA Event and Cross Section Statistics ----------------------------------------------------------*

 *-------  PYTHIA Error and Warning Messages Statistics  ----------------------------------------------------------* 
 |                                                                                                                 | 
 |  times   message                                                                                                | 
 |                                                                                                                 | 
 |      1   Warning in MultipartonInteractions::init: maximum increased                                            | 
 |                                                                                                                 | 
 *-------  End PYTHIA Error and Warning Messages Statistics  ------------------------------------------------------* 

Number of ISR vetoed = 613
Number of FSR vetoed = 49
21-May-2025 03:33:32 CEST  Closed LHE file thread0/cmsgrid_final.lhe
         4.158         0.017         1.000          9999
 

------------------------------------
GenXsecAnalyzer:
------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
Overall cross-section summary 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Process		xsec_before [pb]		passed	nposw	nnegw	tried	nposw	nnegw 	xsec_match [pb]			accepted [%]	 event_eff [%]
0		4.158e+00 +/- 1.710e-02		10	10	0	10	10	0	4.158e+00 +/- 1.710e-02		100.0 +/- 0.0	100.0 +/- 0.0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
Total		4.158e+00 +/- 1.710e-02		10	10	0	10	10	0	4.158e+00 +/- 1.710e-02		100.0 +/- 0.0	100.0 +/- 0.0
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Before matching: total cross section = 4.158e+00 +- 1.710e-02 pb
After matching: total cross section = 4.158e+00 +- 1.710e-02 pb
Matching efficiency = 1.0 +/- 0.0   [TO BE USED IN MCM]
Filter efficiency (taking into account weights)= (41.6366) / (41.6366) = 1.000e+00 +- 0.000e+00
Filter efficiency (event-level)= (10) / (10) = 1.000e+00 +- 0.000e+00    [TO BE USED IN MCM]

After filter: final cross section = 4.158e+00 +- 1.710e-02 pb
After filter: final fraction of events with negative weights = 0.000e+00 +- 0.000e+00
After filter: final equivalent lumi for 1M events (1/fb) = 2.405e+02 +- 1.018e+00
TimeReport> Time report complete in 239.558 seconds
 Time Summary: 
 - Min event:   2.16321
 - Max event:   12.2082
 - Avg event:   8.48682
 - Total loop:  231.671
 - Total init:  7.87626
 - Total job:   239.558
 - EventSetup Lock: 0
 - EventSetup Get:  0
 Event Throughput: 0.0431647 ev/s
 CPU Summary: 
 - Total loop:     199.542
 - Total init:     4.2993
 - Total extra:    0
 - Total children: 77.6215
 - Total job:      203.852
 Processing Summary: 
 - Number of Events:  10
 - Number of Global Begin Lumi Calls:  1
 - Number of Global Begin Run Calls: 1

Thanks for using LHAPDF 6.4.0. Please make sure to cite the paper:
  Eur.Phys.J. C75 (2015) 3, 132  (http://arxiv.org/abs/1412.7420)



[dshekar@lxplus807 src]$ cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 130X_mcRun3_2023_realistic_v14  --fileout file:vbfhToWW2L2Nu_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3_2023  --filein file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12,ENDJOB
with DB:
entry file:vbfhToWW2L2Nu_LHEGS.root
Step: DIGI Spec: 
Step: DATAMIX Spec: 
the query is file dataset = /Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX
Sleeping, then retrying DAS
Sleeping, then retrying DAS
DAS failed 3 times- I give up
found files:  []
Step: L1 Spec: 
Step: DIGI2RAW Spec: 
Step: HLT Spec: ['2023v12']
Step: ENDJOB Spec: 
customising the process with addMonitoring from Configuration/DataProcessing/Utils
customising the process with customizeHLTforMC from HLTrigger/Configuration/customizeHLTforMC
Config file DRPremix_cfg.py created
[dshekar@lxplus807 src]$ dasgoclient -query="dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX"
Neither X509_USER_PROXY or X509_USER_KEY/X509_USER_CERT are set
In order to run please obtain valid proxy via "voms-proxy-init -voms cms -rfc"
and setup X509_USER_PROXY or setup X509_USER_KEY/X509_USER_CERT in your environment
[dshekar@lxplus807 src]$ voms-proxy-init -voms cms -rfc
Enter GRID pass phrase for this identity:
Contacting voms-cms-auth.cern.ch:443 [/DC=ch/DC=cern/OU=computers/CN=cms-auth.cern.ch] "cms"...
Remote VOMS server contacted succesfully.


Created proxy in /tmp/x509up_u154072.

Your proxy is valid until Wed May 21 15:41:57 CEST 2025
[dshekar@lxplus807 src]$ dasgoclient -query="dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX"
/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX
[dshekar@lxplus807 src]$ cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 130X_mcRun3_2023_realistic_v14  --fileout file:vbfhToWW2L2Nu_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3_2023  --filein file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12,ENDJOB
with DB:
entry file:vbfhToWW2L2Nu_LHEGS.root
Step: DIGI Spec: 
Step: DATAMIX Spec: 
the query is file dataset = /Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX
DAS succeeded after 1 attempts 0
found files:  ['/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/00320c57-165d-49c4-8a18-23d8d153f396.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/0049042d-e477-4f1d-b5aa-9fcbb1a46a0d.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/00c4e2d0-b801-4aba-8757-d0649f3e853d.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/00d932fc-498e-4124-847e-b8d80f2abbbf.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/0113f3ab-e645-46f7-8d3c-044507157a0b.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/0129a84a-9b62-4c03-8a3f-fa064ab89121.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/01a9a634-4144-4714-a3d4-f1a49b6c1da0.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/01b81b54-b675-44c1-be48-ee0ab24ebf58.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/01bbcfb4-001f-4096-bdab-d104c2285d1a.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/2550000/01db3a80-85de-49df-9b1b-f0a41ea6a9b0.root', 
...
Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/c88c2981-6387-4bdb-9b80-697b9c42d15d.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/c8d791ff-6e3b-4e8d-877e-67821626a2fe.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/cae1c655-1605-49cd-a799-f92e486b140d.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/d584b6f5-17ba-4bc8-abbd-8ef74ae64c73.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/df472aa9-544d-4721-b208-675fc9aba360.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/e21d0835-9dd6-4f0e-ae87-a9b7771d680d.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/f3317119-4744-40bf-8f4c-1506dbee877c.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/fa435085-68f5-4213-80a0-0261d59802f2.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/fc1a311e-d438-48a8-9164-793137dffbd3.root', '/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/410000/ff2f1418-db7e-44c2-a7c4-ca9e0245e80f.root']
Step: L1 Spec: 
Step: DIGI2RAW Spec: 
Step: HLT Spec: ['2023v12']
Step: ENDJOB Spec: 
customising the process with addMonitoring from Configuration/DataProcessing/Utils
customising the process with customizeHLTforMC from HLTrigger/Configuration/customizeHLTforMC
Config file DRPremix_cfg.py created


DS - After manually editing the DRPremix_cfg.py file with the updated list of root pileup files that can be accessed from lxplus only using root, I continue to the following:

[dshekar@lxplus811 src]$ cmsRun DRPremix_cfg.py
%MSG-i ThreadStreamSetup:  (NoModuleName) 21-May-2025 05:21:30 CEST pre-events
setting # threads 4
setting # streams 4
%MSG
21-May-2025 05:21:34 CEST  Initiating request to open file file:vbfhToWW2L2Nu_LHEGS.root
21-May-2025 05:21:35 CEST  Successfully opened file file:vbfhToWW2L2Nu_LHEGS.root
21-May-2025 05:21:43 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/50002/a92fcde6-3636-4818-8724-6d5ee0dd7467.root
21-May-2025 05:21:45 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/50002/a92fcde6-3636-4818-8724-6d5ee0dd7467.root
21-May-2025 05:21:46 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2520001/4d0e8773-9523-42a8-a7a3-328b78af4c18.root
21-May-2025 05:21:48 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2520001/4d0e8773-9523-42a8-a7a3-328b78af4c18.root
21-May-2025 05:21:49 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/50000/0dda5807-9d8c-4008-8763-474730149b4c.root
21-May-2025 05:21:51 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/50000/0dda5807-9d8c-4008-8763-474730149b4c.root
21-May-2025 05:21:51 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/30004/c51526b5-13c1-4c0f-93f1-2081f619383c.root
21-May-2025 05:21:53 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/30004/c51526b5-13c1-4c0f-93f1-2081f619383c.root
%MSG-w UnusedProductsForCanDeleteEarly:  AfterModDestruction  21-May-2025 05:21:58 CEST pre-events
The following products in the 'canDeleteEarly' list are not used in this job and will be ignored.
 If possible, remove the producer from the job.
 IntermediateHitDoublets_hltElePixelHitDoubletsUnseeded__HLT
 IntermediateHitDoublets_hltElePixelHitDoublets__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTripletsUnseeded__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTriplets__HLT
%MSG
%MSG-w UnusedProductsForCanDeleteEarly:  AfterModDestruction  21-May-2025 05:21:58 CEST pre-events
The following products in the 'canDeleteEarly' list are not used in this job and will be ignored.
 If possible, remove the producer from the job.
 IntermediateHitDoublets_hltElePixelHitDoubletsUnseeded__HLT
 IntermediateHitDoublets_hltElePixelHitDoublets__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTripletsUnseeded__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTriplets__HLT
%MSG
%MSG-w UnusedProductsForCanDeleteEarly:  AfterModDestruction  21-May-2025 05:21:58 CEST pre-events
The following products in the 'canDeleteEarly' list are not used in this job and will be ignored.
 If possible, remove the producer from the job.
 IntermediateHitDoublets_hltElePixelHitDoubletsUnseeded__HLT
 IntermediateHitDoublets_hltElePixelHitDoublets__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTripletsUnseeded__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTriplets__HLT
%MSG
%MSG-w UnusedProductsForCanDeleteEarly:  AfterModDestruction  21-May-2025 05:21:58 CEST pre-events
The following products in the 'canDeleteEarly' list are not used in this job and will be ignored.
 If possible, remove the producer from the job.
 IntermediateHitDoublets_hltElePixelHitDoubletsUnseeded__HLT
 IntermediateHitDoublets_hltElePixelHitDoublets__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTripletsUnseeded__HLT
 RegionsSeedingHitSets_hltElePixelHitDoubletsForTriplets__HLT
%MSG
Begin processing the 1st record. Run 1, Event 1, LumiSection 1 on stream 3 at 21-May-2025 05:22:02.153 CEST
Begin processing the 2nd record. Run 1, Event 2, LumiSection 1 on stream 1 at 21-May-2025 05:22:02.154 CEST
Begin processing the 3rd record. Run 1, Event 3, LumiSection 1 on stream 2 at 21-May-2025 05:22:02.155 CEST
Begin processing the 4th record. Run 1, Event 4, LumiSection 1 on stream 0 at 21-May-2025 05:22:02.156 CEST
#--------------------------------------------------------------------------
#                         FastJet release 3.4.0
#                 M. Cacciari, G.P. Salam and G. Soyez                  
#     A software package for jet finding and analysis at colliders      
#                           http://fastjet.fr                           
#	                                                                      
# Please cite EPJC72(2012)1896 [arXiv:1111.6097] if you use this package
# for scientific work and optionally PLB641(2006)57 [hep-ph/0512210].   
#                                                                       
# FastJet is provided without warranty under the GNU GPL v2 or higher.  
# It uses T. Chan's closest pair algorithm, S. Fortune's Voronoi code
# and 3rd party plugin jet algorithms. See COPYING file for details.
#--------------------------------------------------------------------------
21-May-2025 05:22:26 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/50000/0dda5807-9d8c-4008-8763-474730149b4c.root
21-May-2025 05:22:26 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2520004/74a7bd1c-9172-41bd-8d51-7e86fd0e07db.root
21-May-2025 05:22:28 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2520004/74a7bd1c-9172-41bd-8d51-7e86fd0e07db.root
21-May-2025 05:22:28 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/30004/c51526b5-13c1-4c0f-93f1-2081f619383c.root
21-May-2025 05:22:28 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/50002/a92fcde6-3636-4818-8724-6d5ee0dd7467.root
21-May-2025 05:22:28 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2540005/07d1c1e5-20b9-4a6a-9939-5455febba15d.root
21-May-2025 05:22:28 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2520001/4d0e8773-9523-42a8-a7a3-328b78af4c18.root
21-May-2025 05:22:28 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/30004/f83b82c4-bd0b-486c-8e6a-7c13809028e8.root
21-May-2025 05:22:28 CEST  Initiating request to open file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2530000/e2545d27-bab4-4748-9af8-2f7da3be36ce.root
21-May-2025 05:22:30 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2540005/07d1c1e5-20b9-4a6a-9939-5455febba15d.root
21-May-2025 05:22:33 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2530000/e2545d27-bab4-4748-9af8-2f7da3be36ce.root
21-May-2025 05:22:35 CEST  Successfully opened file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/30004/f83b82c4-bd0b-486c-8e6a-7c13809028e8.root
Begin processing the 5th record. Run 1, Event 5, LumiSection 1 on stream 0 at 21-May-2025 05:22:40.200 CEST
Begin processing the 6th record. Run 1, Event 6, LumiSection 1 on stream 1 at 21-May-2025 05:22:40.289 CEST
Begin processing the 7th record. Run 1, Event 7, LumiSection 1 on stream 2 at 21-May-2025 05:22:40.419 CEST
Begin processing the 8th record. Run 1, Event 8, LumiSection 1 on stream 3 at 21-May-2025 05:22:40.419 CEST
Begin processing the 9th record. Run 1, Event 9, LumiSection 1 on stream 3 at 21-May-2025 05:22:45.379 CEST
Begin processing the 10th record. Run 1, Event 10, LumiSection 1 on stream 1 at 21-May-2025 05:22:45.515 CEST
21-May-2025 05:22:49 CEST  Closed file file:vbfhToWW2L2Nu_LHEGS.root
21-May-2025 05:22:51 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/30004/f83b82c4-bd0b-486c-8e6a-7c13809028e8.root
21-May-2025 05:22:51 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2540005/07d1c1e5-20b9-4a6a-9939-5455febba15d.root
21-May-2025 05:22:51 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2530000/e2545d27-bab4-4748-9af8-2f7da3be36ce.root
21-May-2025 05:22:51 CEST  Closed file root://eoscms.cern.ch//eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/2520004/74a7bd1c-9172-41bd-8d51-7e86fd0e07db.root
TimeReport> Time report complete in 87.2698 seconds
 Time Summary: 
 - Min event:   3.60881
 - Max event:   38.2255
 - Avg event:   18.1361
 - Total loop:  52.5845
 - Total init:  34.6618
 - Total job:   87.2698
 - EventSetup Lock: 0
 - EventSetup Get:  0
 Event Throughput: 0.19017 ev/s
 CPU Summary: 
 - Total loop:     151.81
 - Total init:     19.2693
 - Total extra:    0
 - Total children: 0.110996
 - Total job:      171.103
 Processing Summary: 
 - Number of Events:  10
 - Number of Global Begin Lumi Calls:  1
 - Number of Global Begin Run Calls: 1


[dshekar@lxplus811 src]$ cmsDriver.py --python_filename aod_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 4 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_DRPremix.root --fileout file:vbfhToWW2L2Nu_AOD.root --no_exec --mc -n 10
RAW2DIGI,L1Reco,RECO,RECOSIM,ENDJOB
with DB:
entry file:vbfhToWW2L2Nu_DRPremix.root
Step: RAW2DIGI Spec: 
Step: L1Reco Spec: 
Step: RECO Spec: 
Step: RECOSIM Spec: 
Step: ENDJOB Spec: 
customising the process with addMonitoring from Configuration/DataProcessing/Utils
Config file aod_cfg.py created

[dshekar@lxplus811 src]$ cmsRun aod_cfg.py
%MSG-i ThreadStreamSetup:  (NoModuleName) 21-May-2025 05:38:28 CEST pre-events
setting # threads 4
setting # streams 4
%MSG
21-May-2025 05:38:32 CEST  Initiating request to open file file:vbfhToWW2L2Nu_DRPremix.root
21-May-2025 05:38:33 CEST  Successfully opened file file:vbfhToWW2L2Nu_DRPremix.root
2025-05-21 05:38:39.177706: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Begin processing the 1st record. Run 1, Event 4, LumiSection 1 on stream 2 at 21-May-2025 05:38:46.852 CEST
Begin processing the 2nd record. Run 1, Event 2, LumiSection 1 on stream 1 at 21-May-2025 05:38:46.853 CEST
Begin processing the 3rd record. Run 1, Event 3, LumiSection 1 on stream 0 at 21-May-2025 05:38:46.854 CEST
Begin processing the 4th record. Run 1, Event 1, LumiSection 1 on stream 3 at 21-May-2025 05:38:46.854 CEST
#--------------------------------------------------------------------------
#                         FastJet release 3.4.0
#                 M. Cacciari, G.P. Salam and G. Soyez                  
#     A software package for jet finding and analysis at colliders      
#                           http://fastjet.fr                           
#	                                                                      
# Please cite EPJC72(2012)1896 [arXiv:1111.6097] if you use this package
# for scientific work and optionally PLB641(2006)57 [hep-ph/0512210].   
#                                                                       
# FastJet is provided without warranty under the GNU GPL v2 or higher.  
# It uses T. Chan's closest pair algorithm, S. Fortune's Voronoi code
# and 3rd party plugin jet algorithms. See COPYING file for details.
#--------------------------------------------------------------------------
Begin processing the 5th record. Run 1, Event 8, LumiSection 1 on stream 2 at 21-May-2025 05:38:55.856 CEST
Begin processing the 6th record. Run 1, Event 6, LumiSection 1 on stream 1 at 21-May-2025 05:38:57.699 CEST
Begin processing the 7th record. Run 1, Event 7, LumiSection 1 on stream 3 at 21-May-2025 05:38:58.538 CEST
Begin processing the 8th record. Run 1, Event 5, LumiSection 1 on stream 0 at 21-May-2025 05:38:59.966 CEST
Begin processing the 9th record. Run 1, Event 10, LumiSection 1 on stream 2 at 21-May-2025 05:39:00.986 CEST
Begin processing the 10th record. Run 1, Event 9, LumiSection 1 on stream 2 at 21-May-2025 05:39:02.642 CEST
21-May-2025 05:39:11 CEST  Closed file file:vbfhToWW2L2Nu_DRPremix.root
TimeReport> Time report complete in 50.9501 seconds
 Time Summary: 
 - Min event:   1.64837
 - Max event:   13.0449
 - Avg event:   7.91282
 - Total loop:  31.3773
 - Total init:  19.5727
 - Total job:   50.9501
 - EventSetup Lock: 0
 - EventSetup Get:  0
 Event Throughput: 0.318702 ev/s
 CPU Summary: 
 - Total loop:     79.1265
 - Total init:     13.8912
 - Total extra:    0
 - Total children: 0.098354
 - Total job:      93.0182
 Processing Summary: 
 - Number of Events:  10
 - Number of Global Begin Lumi Calls:  1
 - Number of Global Begin Run Calls: 1

[dshekar@lxplus811 src]$ cmsDriver.py --python_filename miniAOD_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step PAT --nThreads 2 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_AOD.root --fileout file:vbfhToWW2L2Nu_miniAOD.root --no_exec --mc -n 10
PAT,ENDJOB
with DB:
entry file:vbfhToWW2L2Nu_AOD.root
Step: PAT Spec: 
Step: ENDJOB Spec: 
customising the process with addMonitoring from Configuration/DataProcessing/Utils
customising the process with miniAOD_customizeAllMC from PhysicsTools/PatAlgos/slimming/miniAOD_tools
Config file miniAOD_cfg.py created

[dshekar@lxplus811 src]$ cmsRun miniAOD_cfg.py
%MSG-i ThreadStreamSetup:  (NoModuleName) 21-May-2025 05:42:36 CEST pre-events
setting # threads 2
setting # streams 2
%MSG
21-May-2025 05:42:39 CEST  Initiating request to open file file:vbfhToWW2L2Nu_AOD.root
21-May-2025 05:42:41 CEST  Successfully opened file file:vbfhToWW2L2Nu_AOD.root
2025-05-21 05:42:45.543528: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  SSE4.1 SSE4.2 AVX AVX2 AVX512F FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Begin processing the 1st record. Run 1, Event 4, LumiSection 1 on stream 0 at 21-May-2025 05:42:53.798 CEST
Begin processing the 2nd record. Run 1, Event 2, LumiSection 1 on stream 1 at 21-May-2025 05:42:54.291 CEST
#--------------------------------------------------------------------------
#                         FastJet release 3.4.0
#                 M. Cacciari, G.P. Salam and G. Soyez                  
#     A software package for jet finding and analysis at colliders      
#                           http://fastjet.fr                           
#	                                                                      
# Please cite EPJC72(2012)1896 [arXiv:1111.6097] if you use this package
# for scientific work and optionally PLB641(2006)57 [hep-ph/0512210].   
#                                                                       
# FastJet is provided without warranty under the GNU GPL v2 or higher.  
# It uses T. Chan's closest pair algorithm, S. Fortune's Voronoi code
# and 3rd party plugin jet algorithms. See COPYING file for details.
#--------------------------------------------------------------------------
Begin processing the 3rd record. Run 1, Event 1, LumiSection 1 on stream 1 at 21-May-2025 05:42:55.532 CEST
Begin processing the 4th record. Run 1, Event 3, LumiSection 1 on stream 0 at 21-May-2025 05:42:55.634 CEST
Begin processing the 5th record. Run 1, Event 8, LumiSection 1 on stream 1 at 21-May-2025 05:42:55.950 CEST
Begin processing the 6th record. Run 1, Event 10, LumiSection 1 on stream 0 at 21-May-2025 05:42:55.999 CEST
Begin processing the 7th record. Run 1, Event 7, LumiSection 1 on stream 0 at 21-May-2025 05:42:56.256 CEST
Begin processing the 8th record. Run 1, Event 5, LumiSection 1 on stream 1 at 21-May-2025 05:42:56.334 CEST
Begin processing the 9th record. Run 1, Event 6, LumiSection 1 on stream 0 at 21-May-2025 05:42:56.572 CEST
Begin processing the 10th record. Run 1, Event 9, LumiSection 1 on stream 1 at 21-May-2025 05:42:56.745 CEST
21-May-2025 05:42:57 CEST  Closed file file:vbfhToWW2L2Nu_AOD.root
TimeReport> Time report complete in 30.3057 seconds
 Time Summary: 
 - Min event:   0.254181
 - Max event:   1.83316
 - Avg event:   0.576721
 - Total loop:  7.3262
 - Total init:  22.9793
 - Total job:   30.3057
 - EventSetup Lock: 0
 - EventSetup Get:  0
 Event Throughput: 1.36496 ev/s
 CPU Summary: 
 - Total loop:     9.07604
 - Total init:     20.9991
 - Total extra:    0
 - Total children: 0.094418
 - Total job:      30.0755
 Processing Summary: 
 - Number of Events:  10
 - Number of Global Begin Lumi Calls:  1
 - Number of Global Begin Run Calls: 1

[dshekar@lxplus811 src]$ cmsDriver.py --python_filename nanoAOD_cfg.py --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step NANO --nThreads 4 --scenario pp --era Run3_2023  --filein file:vbfhToWW2L2Nu_miniAOD.root --fileout file:vbfhToWW2L2Nu_nanoAOD.root --no_exec --mc -n 10
NANO,ENDJOB
entry file:vbfhToWW2L2Nu_miniAOD.root
Step: NANO Spec: 
in prepare_nano nanoSequenceMC
Step: ENDJOB Spec: 
customising the process with nanoAOD_customizeCommon from PhysicsTools/NanoAOD/nano_cff
Config file nanoAOD_cfg.py created
[dshekar@lxplus811 src]$ 
[dshekar@lxplus811 src]$ 
[dshekar@lxplus811 src]$ cmsRun nanoAOD_cfg.py
%MSG-i ThreadStreamSetup:  (NoModuleName) 21-May-2025 05:44:54 CEST pre-events
setting # threads 4
setting # streams 4
%MSG
21-May-2025 05:44:56 CEST  Initiating request to open file file:vbfhToWW2L2Nu_miniAOD.root
21-May-2025 05:44:58 CEST  Successfully opened file file:vbfhToWW2L2Nu_miniAOD.root
                         : Booking "electronMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "electronMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "electronMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "electronMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/el_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVALowPt" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVALowPt" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVALowPt" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVALowPt" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_lowpt.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
                         : Booking "muonMVATTH" of type "BDT" from /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml.
                         : Reading weight file: /cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/external/el8_amd64_gcc11/data/PhysicsTools/NanoAOD/data/mu_BDTG_2017.weights.xml
<HEADER> DataSetInfo              : [Default] : Added class "Signal"
<HEADER> DataSetInfo              : [Default] : Added class "Background"
                         : Booked classifier "BDTG" of type: "BDT"
%MSG-w LogicError:  GenWeightsTableProducer:genWeightsTable@beginRun  21-May-2025 05:45:07 CEST Run: 1
::getByLabel: An attempt was made to read a Run product before endRun() was called.
The product is of type 'LHERunInfoProduct'.
The specified ModuleLabel was 'externalLHEProducer'.
The specified productInstanceName was ''.

%MSG
%MSG-w LogicError:  HTXSRivetProducer:rivetProducerHTXS@beginRun  21-May-2025 05:45:07 CEST Run: 1
::getByLabel: An attempt was made to read a Run product before endRun() was called.
The product is of type 'LHERunInfoProduct'.
The specified ModuleLabel was 'externalLHEProducer'.
The specified productInstanceName was ''.

%MSG
Begin processing the 1st record. Run 1, Event 2, LumiSection 1 on stream 0 at 21-May-2025 05:45:07.575 CEST
Begin processing the 2nd record. Run 1, Event 4, LumiSection 1 on stream 1 at 21-May-2025 05:45:07.575 CEST
Begin processing the 3rd record. Run 1, Event 1, LumiSection 1 on stream 2 at 21-May-2025 05:45:07.575 CEST
Begin processing the 4th record. Run 1, Event 3, LumiSection 1 on stream 3 at 21-May-2025 05:45:07.575 CEST
Rivet.AnalysisHandler: INFO  Using named weights
Rivet.AnalysisHandler: WARN  Analysis 'HiggsTemplateCrossSections' is unvalidated: be careful, it may be broken!
==============================================================
========     HiggsTemplateCrossSections Initialization     =========
==============================================================
==============================================================
========             Higgs prod mode 2              =========
========          Sucessful Initialization           =========
==============================================================
Rivet.AnalysisHandler: INFO  Using named weights
                         : Rebuilding Dataset Default
                         : Rebuilding Dataset Default
                         : Rebuilding Dataset Default
Begin processing the 5th record. Run 1, Event 10, LumiSection 1 on stream 0 at 21-May-2025 05:45:10.094 CEST
Begin processing the 6th record. Run 1, Event 8, LumiSection 1 on stream 1 at 21-May-2025 05:45:10.098 CEST
Begin processing the 7th record. Run 1, Event 7, LumiSection 1 on stream 2 at 21-May-2025 05:45:10.098 CEST
Begin processing the 8th record. Run 1, Event 5, LumiSection 1 on stream 3 at 21-May-2025 05:45:10.098 CEST
                         : Rebuilding Dataset Default
                         : Rebuilding Dataset Default
                         : Rebuilding Dataset Default
                         : Rebuilding Dataset Default
Begin processing the 9th record. Run 1, Event 6, LumiSection 1 on stream 0 at 21-May-2025 05:45:10.145 CEST
Begin processing the 10th record. Run 1, Event 9, LumiSection 1 on stream 1 at 21-May-2025 05:45:10.153 CEST
                         : Rebuilding Dataset Default
                         : Rebuilding Dataset Default
                         : Rebuilding Dataset Default
Rivet.Analysis.HiggsTemplateCrossSections: INFO   ====================================================== 
Rivet.Analysis.HiggsTemplateCrossSections: INFO        Higgs Template X-Sec Categorization Tool          
Rivet.Analysis.HiggsTemplateCrossSections: INFO                  Status Code Summary                     
Rivet.Analysis.HiggsTemplateCrossSections: INFO   ====================================================== 
Rivet.Analysis.HiggsTemplateCrossSections: INFO       >>>> All 10 events successfully categorized!
Rivet.Analysis.HiggsTemplateCrossSections: INFO   ====================================================== 
Rivet.Analysis.HiggsTemplateCrossSections: INFO   ====================================================== 
21-May-2025 05:45:10 CEST  Closed file file:vbfhToWW2L2Nu_miniAOD.root

The MCnet usage guidelines apply to Rivet: see http://www.montecarlonet.org/GUIDELINES
Please acknowledge Rivet in results made using it, and cite https://arxiv.org/abs/1912.05451
