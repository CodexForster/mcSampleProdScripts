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
echo "Argument 0: ${0}" # run_MC_2023.sh file itself
echo "Argument 1: ${1}" # ClusterID file
echo "Argument 2: ${2}" # ProcID file
echo "Argument 3: ${3}" # Proxy file name
CLUSTER_ID=${1}
PROC_ID=${2}

### LHEGS step
echo "********** lhegs start **********"
# export SCRAM_ARCH=el8_amd64_gcc11
# scram p CMSSW_13_0_13
# cd CMSSW_13_0_13/src
export SCRAM_ARCH=el8_amd64_gcc10
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram p CMSSW_12_4_24
cd CMSSW_12_4_24/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
mv ${BASEDIR}/HIG-Run3Summer22wmLHEGS-ZH_Zto2L_Hto2WtoLNu2Q-fragment.py Configuration/GenProduction/python/
scram b
SEED=$((${1} + ${2}))
echo "Seed set to: ${SEED}"
cmsDriver.py Configuration/GenProduction/python/HIG-Run3Summer22wmLHEGS-ZH_Zto2L_Hto2WtoLNu2Q-fragment.py --era Run3 --customise Configuration/DataProcessing/Utils.addMonitoring --beamspot Realistic25ns13p6TeVEarly2022Collision --step LHE,GEN,SIM --geometry DB:Extended --conditions 124X_mcRun3_2022_realistic_v12 --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --datatier GEN-SIM,LHE --eventcontent RAWSIM,LHE --python_filename wmLHEGS_cfg.py --fileout file:zh_hto2w_zto2l_LHEGS.root --mc --no_exec -n 500
cmsRun wmLHEGS_cfg.py
echo "********** LHE End **********"
echo "Files in current directory: "
echo $(ls)
echo $(pwd)

cd ../../
scram p CMSSW_12_4_25
cd CMSSW_12_4_25/src
eval `scram runtime -sh`
mv ../../CMSSW_12_4_24/src/zh_hto2w_zto2l_LHEGS.root ./
### DIGI-Premix step
echo "********** DIGI Premix start **********"
cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 124X_mcRun3_2022_realistic_v12  --fileout file:zh_hto2w_zto2l_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v12 --procModifiers premix_stage2,siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3  --filein file:zh_hto2w_zto2l_LHEGS.root --no_exec -n 500
find /eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer22_124X_mcRun3_2022_realistic_v11-v2/ -type f > find_query_list_test.txt
sed -i "s|/eos/cms/|/|g; s|root$|root|g" find_query_list_test.txt
mv ${BASEDIR}/update_paths.py ./
python3 update_paths.py
cmsRun DRPremix_cfg.py
echo "********** DIGI Premix End **********"
xrdcp -f DRPremix_cfg.py root://eosuser.cern.ch//eos/user/d/dshekar/mcSample/DRPremix_cfg.py

### AOD step
echo "********** AOD start **********"
cmsDriver.py --python_filename aod_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 124X_mcRun3_2022_realistic_v12 --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --era Run3 --filein file:zh_hto2w_zto2l_DRPremix.root --fileout file:zh_hto2w_zto2l_AOD.root --no_exec --mc -n 500
cmsRun aod_cfg.py
echo "********** AOD End **********"

cd ../../
export SCRAM_ARCH=el8_amd64_gcc11
source /cvmfs/cms.cern.ch/cmsset_default.sh
scram p CMSSW_13_0_23
cd CMSSW_13_0_23/src
eval `scram runtime -sh`
mv ../../CMSSW_12_4_25/src/zh_hto2w_zto2l_AOD.root ./
### MINIAOD step
echo "********** MINIAOD start **********"
cmsDriver.py --python_filename miniAOD_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 124X_mcRun3_2022_realistic_v12 --step PAT --nThreads 2 --geometry DB:Extended --era Run3 --filein file:zh_hto2w_zto2l_AOD.root --fileout file:zh_hto2w_zto2l_miniAOD.root --no_exec --mc -n 500
cmsRun miniAOD_cfg.py
echo "********** MINIAOD End **********"

### NANOAOD step
echo "********** NANOAOD start **********"
cmsDriver.py --python_filename nanoAOD_cfg.py --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 126X_mcRun3_2022_realistic_v2 --step NANO --nThreads 4 --scenario pp --era Run3,run3_nanoAOD_124  --filein file:zh_hto2w_zto2l_miniAOD.root --fileout file:zh_hto2w_zto2l_nanoAOD.root --no_exec --mc -n 500
cmsRun nanoAOD_cfg.py
echo "********** NANOAOD End **********"

FINAL_FILE_NAME="nanoAOD_${CLUSTER_ID}_${PROC_ID}.root"
mv zh_hto2w_zto2l_nanoAOD.root ${FINAL_FILE_NAME}

# Copy the renamed file to the destination
xrdcp -f ${FINAL_FILE_NAME} root://eosuser.cern.ch//eos/user/d/dshekar/MCsamplesForBDTzh3l/mcSample_ZH_Zto2L_Hto2WtoLNu2Q_centralSampleGridpack/${FINAL_FILE_NAME}
