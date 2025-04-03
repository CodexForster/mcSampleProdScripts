command_dict = {

    ## 2016 PreVFP
    '2016APV': {
        'LHE': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein file:{{ input }} --fileout file:lhe.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step NONE --era Run2_2016_HIPM --no_exec --mc -n {{ nevt }}',
        },
        'GEN': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe.root --fileout file:gen.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step GEN --geometry DB:Extended --era Run2_2016_HIPM --no_exec --mc -n {{ nevt }}',
        },
        'SIM': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen.root --fileout file:sim.root --nThreads 2 --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_mcRun2_asymptotic_preVFP_v8 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'DIGI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim.root --fileout file:digiPremix.root --nThreads 2 --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX" --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'HLT': {
            'scram_arch': 'slc7_amd64_gcc530',
            'cmssw': 'CMSSW_8_0_36_UL_patch2',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix.root --fileout file:hlt.root --nThreads 2 --eventcontent RAWSIM --outputCommand 'keep *_mix_*_*,keep *_genPUProtons_*_*' --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --inputCommands 'keep *','drop *_*_BMTF_*','drop *PixelFEDChannel*_*_*_*' --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:25ns15e33_v4 --geometry DB:Extended --era Run2_2016 --no_exec --mc -n {{ nevt }}",
        },
        'RECO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py --filein file:hlt.root --fileout file:reco.root --nThreads 2 --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_mcRun2_asymptotic_preVFP_v8 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'MINI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_25',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco.root --fileout file:miniaod.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_mcRun2_asymptotic_preVFP_v11 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2016_HIPM --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'NANO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod.root --fileout file:nanoaod.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --step NANO --era Run2_2016_HIPM,run2_nanoAOD_106Xv2 --no_exec --mc -n {{ nevt }}',
        },
    },

    ## 2016 PostVFP
    '2016': {
        'LHE': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein file:{{ input }} --fileout file:lhe.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step NONE --era Run2_2016 --no_exec --mc -n {{ nevt }}',
        },
        'GEN': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe.root --fileout file:gen.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step GEN --geometry DB:Extended --era Run2_2016 --no_exec --mc -n {{ nevt }}',
        },
        'SIM': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen.root --fileout file:sim.root --nThreads 2 --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step SIM --geometry DB:Extended --era Run2_2016 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'DIGI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim.root --fileout file:digiPremix.root --nThreads 2 --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX" --conditions 106X_mcRun2_asymptotic_v13 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2016 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'HLT': {
            'scram_arch': 'slc7_amd64_gcc530',
            'cmssw': 'CMSSW_8_0_36_UL_patch2',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix.root --fileout file:hlt.root --nThreads 2 --eventcontent RAWSIM --outputCommand 'keep *_mix_*_*,keep *_genPUProtons_*_*' --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --inputCommands 'keep *','drop *_*_BMTF_*','drop *PixelFEDChannel*_*_*_*' --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:25ns15e33_v4 --geometry DB:Extended --era Run2_2016 --no_exec --mc -n {{ nevt }}",
        },
        'RECO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py--filein file:hlt.root --fileout file:reco.root --nThreads 2 --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_mcRun2_asymptotic_v13 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --era Run2_2016 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'MINI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_25',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco.root --fileout file:miniaod.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_mcRun2_asymptotic_v17 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2016 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'NANO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod.root --fileout file:nanoaod.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_mcRun2_asymptotic_v17 --step NANO --era Run2_2016,run2_nanoAOD_106Xv2 --no_exec --mc -n {{ nevt }}',
        },
    },

    '2017': {
        'LHE': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein file:{{ input }} --fileout file:lhe.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_mc2017_realistic_v6 --step NONE --era Run2_2017 --no_exec --mc -n {{ nevt }}',
        },
        'GEN': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe.root --fileout file:gen.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN --geometry DB:Extended --era Run2_2017 --no_exec --mc -n {{ nevt }}',
        },
        'SIM': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen.root --fileout file:sim.root --nThreads 2 --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_mc2017_realistic_v6 --beamspot Realistic25ns13TeVEarly2017Collision --step SIM --geometry DB:Extended --era Run2_2017 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'DIGI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim.root --fileout file:digiPremix.root --nThreads 2 --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL17_106X_mc2017_realistic_v6-v3/PREMIX" --conditions 106X_mc2017_realistic_v6 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2017 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'HLT': {
            'scram_arch': 'slc7_amd64_gcc630',
            'cmssw': 'CMSSW_9_4_14_UL_patch1',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix.root --fileout file:hlt.root --nThreads 2 --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v15 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:2e34v40 --geometry DB:Extended --era Run2_2017 --no_exec --mc -n {{ nevt }}",
        },
        'RECO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py --filein file:hlt.root --fileout file:reco.root --nThreads 2 --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_mc2017_realistic_v6 --step RAW2DIGI,L1Reco,RECO,RECOSIM --geometry DB:Extended --era Run2_2017 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'MINI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_20',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco.root --fileout file:miniaod.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_mc2017_realistic_v9 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2017 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'NANO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod.root --fileout file:nanoaod.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_mc2017_realistic_v9 --step NANO --era Run2_2017,run2_nanoAOD_106Xv2 --no_exec --mc -n {{ nevt }}',
        },
    },

    '2018': {
        'LHE': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename lhe_cfg.py --filein file:{{ input }} --fileout file:lhe.root --eventcontent LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier LHE --conditions 106X_upgrade2018_realistic_v4 --step NONE --era Run2_2018 --no_exec --mc -n {{ nevt }}',
        },
        'GEN': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_30_patch1',
            'command': 'cmsDriver.py Configuration/GenProduction/python/monoWprime_hadronizer.py --python_filename gen_cfg.py --filein file:lhe.root --fileout file:gen.root --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN --geometry DB:Extended --era Run2_2018 --no_exec --mc -n {{ nevt }}',
        },
        'SIM': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename sim_cfg.py --filein file:gen.root --fileout file:sim.root --nThreads 2 --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions 106X_upgrade2018_realistic_v11_L1v1 --beamspot Realistic25ns13TeVEarly2018Collision --step SIM --geometry DB:Extended --era Run2_2018 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'DIGI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename digi_premix_cfg.py --filein file:sim.root --fileout file:digiPremix.root --nThreads 2 --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL18_106X_upgrade2018_realistic_v11_L1v1-v2/PREMIX" --conditions 106X_upgrade2018_realistic_v11_L1v1 --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --datamix PreMix --era Run2_2018 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'HLT': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_2_16_UL',
            'command': "cmsDriver.py --python_filename hlt_cfg.py --filein file:digiPremix.root --fileout file:hlt.root --nThreads 2 --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --step HLT:2018v32 --geometry DB:Extended --era Run2_2018 --no_exec --mc -n {{ nevt }}",
        },
        'RECO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_17_patch1',
            'command': 'cmsDriver.py --python_filename reco_cfg.py --filein file:hlt.root --fileout file:reco.root --nThreads 2 --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 106X_upgrade2018_realistic_v11_L1v1 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --geometry DB:Extended --era Run2_2018 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'MINI': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_20',
            'command': 'cmsDriver.py --python_filename miniaod_cfg.py --filein file:reco.root --fileout file:miniaod.root --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2018 --runUnscheduled --no_exec --mc -n {{ nevt }}',
        },
        'NANO': {
            'scram_arch': 'slc7_amd64_gcc700',
            'cmssw': 'CMSSW_10_6_32_patch1',
            'command': 'cmsDriver.py --python_filename nanoaod_cfg.py --filein file:miniaod.root --fileout file:nanoaod.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --no_exec --mc -n {{ nevt }}',
        },
    },


    '2023': {
        'LHEGS': {
            'scram_arch': 'el8_amd64_gcc11',
            'cmssw': 'CMSSW_13_0_13',
            'command': 'cmsDriver.py Configuration/GenProduction/python/vbf_h_ww_2l2Nu_el8_amd64_gcc11_CMSSW_13_0_13-fragment.py --python_filename wmLHEGS_cfg.py --mc --eventcontent RAWSIM, LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM, LHE --conditions 130X_mcRun3_2023_realistic_v14 --beamspot Realistic25ns13p6TeVEarly2023Collision --customise_commands process.source.numberEventsInLuminosityBlock="cms.untracked.uint32(100)" --step LHE,GEN,SIM --geometry DB:Extended --era Run3_2023  --fileout file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n {{ nevt }}',
        },
        'DRPremix': {
            'scram_arch': 'el8_amd64_gcc11',
            'cmssw': 'CMSSW_13_0_13',
            'command': 'cmsDriver.py --python_filename DRPremix_cfg.py --mc --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring \ --datatier GEN-SIM-RAW --conditions 130X_mcRun3_2023_realistic_v14  --fileout file:vbfhToWW2L2Nu_DRPremix.root --pileup_input "dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX" --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2023v12 --procModifiers premix_stage2 --nThreads 4 --geometry DB:Extended --datamix PreMix --era Run3_2023  --filein file:vbfhToWW2L2Nu_LHEGS.root --no_exec -n {{ nevt }}',
        },
        'AOD': {
            'scram_arch': 'el8_amd64_gcc11',
            'cmssw': 'CMSSW_13_0_13',
            'command': 'cmsDriver.py --python_filename aod_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step RAW2DIGI,L1Reco,RECO,RECOSIM --nThreads 4 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_DRPremix.root --fileout file:vbfhToWW2L2Nu_AOD.root --no_exec --mc -n {{ nevt }}',
        },
        'MINI': {
            'scram_arch': 'el8_amd64_gcc11',
            'cmssw': 'CMSSW_13_0_13',
            'command': 'cmsDriver.py --python_filename miniAOD_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step PAT --nThreads 2 --geometry DB:Extended --era Run3_2023  --filein file:vbfhToWW2L2Nu_AOD.root --fileout file:vbfhToWW2L2Nu_miniAOD.root --no_exec --mc -n {{ nevt }}',
        },
        'NANO': {
            'scram_arch': 'el8_amd64_gcc11',
            'cmssw': 'CMSSW_13_0_13',
            'command': 'cmsDriver.py --python_filename nanoAOD_cfg.py --eventcontent NANOAODSIM --datatier NANOAODSIM --conditions 130X_mcRun3_2023_realistic_v14 --step NANO --nThreads 4 --scenario pp --era Run3_2023  --filein file:vbfhToWW2L2Nu_miniAOD.root --fileout file:vbfhToWW2L2Nu_nanoAOD.root --no_exec --mc -n {{ nevt }}',
        },
    }
}