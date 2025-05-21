export SCRAM_ARCH=el8_amd64_gcc11
scram p CMSSW_13_0_13
cd CMSSW_13_0_13/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
cp /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/CMSSW_13_0_13/src/Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py ./Configuration/GenProduction/python/

scram b

cmsDriver.py Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --python_filename wmLHEGS_cfg.py --mc --eventcontent RAWSIM, LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM, LHE --conditions 130X_mcRun3_2023_realistic_v14 --beamspot Realistic25ns13p6TeVEarly2023Collision --customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --step LHE,GEN,SIM --geometry DB:Extended --era Run3_2023  --fileout file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
cmsRun wmLHEGS_cfg.py

cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 130X_mcRun3_2023_realistic_v14  --fileout file:vbfhToWW2L2Nu_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3_2023  --filein file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
cmsRun DRPremix_cfg.py
