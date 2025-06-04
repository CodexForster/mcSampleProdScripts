#!/bin/bash
### Computing environments
echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
source /cvmfs/cms.cern.ch/cmsset_default.sh
export BASEDIR=`pwd`
echo "basedir = ${BASEDIR}"

### Add x509 proxy
export X509_USER_PROXY=${3}
voms-proxy-info -all
voms-proxy-info -all -file ${3}

echo "DAN "
echo "Argument 0: ${0}"
echo "Argument 1: ${1}"
echo "Argument 2: ${2}"
echo "Argument 3: ${3}"

### LHEGS step
echo "********** lhegs start **********"
export SCRAM_ARCH=el8_amd64_gcc11
scram p CMSSW_13_0_13
cd CMSSW_13_0_13/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
mv ${BASEDIR}/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py Configuration/GenProduction/python/
scram b
cmsDriver.py Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --python_filename wmLHEGS_cfg.py --mc --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions 130X_mcRun3_2023_realistic_v14 --beamspot Realistic25ns13p6TeVEarly2023Collision --customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --step LHE,GEN,SIM --geometry DB:Extended --era Run3_2023  --fileout file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
cmsRun wmLHEGS_cfg.py
echo "********** LHE End **********"
echo "Files in current directory: "
echo $(ls)
# mv ${BASEDIR}/CMSSW_13_0_13/src/vbfhToWW2L2Nu_LHEGS.root ./

### DIGI-Premix step
echo "********** DIGI Premix start **********"
cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 130X_mcRun3_2023_realistic_v14  --fileout file:vbfhToWW2L2Nu_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3_2023  --filein file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
find /eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/ -type f > find_query_list_test.txt
sed -i "s|/eos/cms/|/|g; s|root$|root|g" find_query_list_test.txt
mv ${BASEDIR}/update_paths.py ./
python3 update_paths.py
cmsRun DRPremix_cfg.py
echo "********** DIGI Premix End **********"
xrdcp -f DRPremix_cfg.py root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/DRPremix_cfg.py
xrdcp -f vbfhToWW2L2Nu_DRPremix.root root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/vbfhToWW2L2Nu_DRPremix.root

### AOD step
echo "********** AOD start **********"
cmsDriver.py --python_filename aod_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 4 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_DRPremix.root --fileout file:vbfhToWW2L2Nu_AOD.root --no_exec --mc -n 10
cmsRun aod_cfg.py
echo "********** AOD End **********"

### MINIAOD step
echo "********** MINIAOD start **********"
cmsDriver.py --python_filename miniAOD_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step PAT --nThreads 2 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_AOD.root --fileout file:vbfhToWW2L2Nu_miniAOD.root --no_exec --mc -n 10
cmsRun miniAOD_cfg.py
echo "********** MINIAOD End **********"

### NANOAOD step
echo "********** NANOAOD start **********"
cmsDriver.py --python_filename nanoAOD_cfg.py --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step NANO --nThreads 4 --scenario pp --era Run3_2023  --filein file:vbfhToWW2L2Nu_miniAOD.root --fileout file:vbfhToWW2L2Nu_nanoAOD.root --no_exec --mc -n 10
cmsRun nanoAOD_cfg.py
echo "********** NANOAOD End **********"

mv vbfhToWW2L2Nu_nanoAOD.root nanoAOD.root
# xrdfs root://eosuser.cern.ch/ mkdir -p /eos/user/d/dshekar/mcSample//
xrdcp -f nanoAOD.root root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/nanoAOD.root