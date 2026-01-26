mkdir wmLHEGS_CMSSW_12_4_24
cd wmLHEGS_CMSSW_12_4_24
export SCRAM_ARCH=el8_amd64_gcc10
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram p CMSSW CMSSW_12_4_24
cd CMSSW_12_4_24/src
eval `scram runtime -sh`
mkdir -p Configuration/GenProduction/python/
# Fragment from https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_fragment/HIG-Run3Summer22wmLHEGS-02385, 5000 events
mv ${BASEDIR}/HIG-Run3Summer22wmLHEGS-02385-fragment.py Configuration/GenProduction/python/
scram b

# Crab config file 'crabConfig_wmLHEGS.py' created, initializing crab and VOMX proxy.
source /cvmfs/oasis.opensciencegrid.org/osg-software/osg-wn-client/3.6/current/el8-x86_64/setup.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init -voms cms -rfc -valid 168:00
crab checkwrite --site=T3_US_FNALLPC

# Submitting crab jobs:
SEED=$(($(date +%s) % 100 + 1))
echo "Seed set to: ${SEED}"
# cmsDriver.py Configuration/GenProduction/python/HIG-Run3Summer22wmLHEGS-02385-fragment.py --era Run3 --customise Configuration/DataProcessing/Utils.addMonitoring --beamspot Realistic25ns13p6TeVEarly2022Collision --step LHE,GEN,SIM --geometry DB:Extended --conditions 124X_mcRun3_2022_realistic_v12 --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --datatier GEN-SIM,LHE --eventcontent RAWSIM,LHE --python_filename wmLHEGS_cfg.py --fileout file:zh_hto2w_zto2l_LHEGS.root --mc --no_exec -n 5000
# Splitting wmLHEGS into RAWSIM and LHE
cmsDriver.py Configuration/GenProduction/python/HIG-Run3Summer22wmLHEGS-02385-fragment.py --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 124X_mcRun3_2022_realistic_v12 --beamspot Realistic25ns13p6TeVEarly2022Collision --step GEN,SIM --geometry DB:Extended --era Run3 --python_filename RAWSIM_cfg.py --fileout file:zh_hto2w_zto2l_RAWSIM.root --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --no_exec -n 5000
# Template config file called 'RAWSIM_cfg.py' produced from above cmsDriver command.
crab submit -c crabConfig_RAWSIM.py

cmsDriver.py Configuration/GenProduction/python/HIG-Run3Summer22wmLHEGS-02385-fragment.py --mc --eventcontent LHE --datatier LHE --conditions 124X_mcRun3_2022_realistic_v12 --step NONE --era Run3 --python_filename LHEGS_cfg.py --filein file:zh_hto2w_zto2l_RAWSIM.root --fileout file:zh_hto2w_zto2l_LHEGS.root --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --no_exec -n 5000
crab submit -c crabConfig_LHEGS.py

cd ../../../
mkdir DRPremix_CMSSW_12_4_25
cd DRPremix_CMSSW_12_4_25
export SCRAM_ARCH=el8_amd64_gcc10
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram p CMSSW CMSSW_12_4_25
cd CMSSW_12_4_25/src
eval `scram runtime -sh`
mkdir -p Configuration/GenProduction/python/
scram b

cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 124X_mcRun3_2022_realistic_v12  --fileout file:zh_hto2w_zto2l_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v12 --procModifiers premix_stage2,siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3  --filein file:zh_hto2w_zto2l_LHEGS.root --no_exec -n 5000
# MANUAL FIX TO ACCOUNT FOR FAILED PATH INJECTION IN THE pileup_input ABOVE
mv ${BASEDIR}/update_paths.py ./
find /eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/ -type f > find_query_list_test.txt
sed -i "s|/eos/cms/|/|g; s|root$|root|g" find_query_list_test.txt
python3 update_paths.py
crab submit -c crabConfig_DRPremix.py

...
