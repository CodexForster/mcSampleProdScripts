export SCRAM_ARCH=el8_amd64_gcc11
scram p CMSSW_13_0_13
cd CMSSW_13_0_13/src
eval `scram runtime -sh`

mkdir -p Configuration/GenProduction/python/
cp /afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/CMSSW_13_0_13/src/Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py ./Configuration/GenProduction/python/

scram b

cmsDriver.py Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --python_filename wmLHEGS_cfg.py --mc --eventcontent RAWSIM, LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM, LHE --conditions 130X_mcRun3_2023_realistic_v14 --beamspot Realistic25ns13p6TeVEarly2023Collision --customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --step LHE,GEN,SIM --geometry DB:Extended --era Run3_2023  --fileout file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10
cmsRun wmLHEGS_cfg.py

cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 130X_mcRun3_2023_realistic_v14  --fileout file:vbfhToWW2L2Nu_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3_2023  --filein file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n 10

# dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX" > das_query_list.txt
# find /eos/cms/store/mc/Run3Summer21PrePremix/Neutrino_E-10_gun/PREMIX/Summer23_130X_mcRun3_2023_realistic_v13-v1/ -type f > find_query_list.txt
location=$(dasgoclient -query="file dataset=/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX" | head -n 1 | sed 's/\/[^/]*\/[^/]*$//')
full_path="/eos/cms$location/"
find "$full_path" -type f > find_query_list_test.txt
# Replace '/eos/cms/' with '/' and 'root' with 'root,' in the file
sed -i "s|/eos/cms/|/|g; s|root$|root|g" find_query_list_test.txt
# sed -i '${s|,$||}' find_query_list_test.txt

python3 update_paths.py

# Use the output of find_query_list.txt in DRPremix_cfg.py as not all secondary files in DRPremix_cfg.py are accessible.
cmsRun DRPremix_cfg.py

cmsDriver.py --python_filename aod_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 4 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_DRPremix.root --fileout file:vbfhToWW2L2Nu_AOD.root --no_exec --mc -n 10
cmsRun aod_cfg.py

cmsDriver.py --python_filename miniAOD_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step PAT --nThreads 2 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_AOD.root --fileout file:vbfhToWW2L2Nu_miniAOD.root --no_exec --mc -n 10
cmsRun miniAOD_cfg.py

cmsDriver.py --python_filename nanoAOD_cfg.py --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step NANO --nThreads 4 --scenario pp --era Run3_2023  --filein file:vbfhToWW2L2Nu_miniAOD.root --fileout file:vbfhToWW2L2Nu_nanoAOD.root --no_exec --mc -n 10
cmsRun nanoAOD_cfg.py

