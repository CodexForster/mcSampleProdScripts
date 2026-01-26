from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
jobName = 'LHEGS_cfg_test0'
# Can resubmit or check status/report/log/output of crab job with 'crab resubmit/status/report/getlog/getoutput crabLHEGSsample/LHEGS_cfg_test0
config.General.requestName = jobName
config.General.workArea = 'crabLHEGSsample'
# config.General.workArea = '/afs/cern.ch/user/d/dshekar/private/mcSamples/powheg/ZH_HWW_Z2L_centralSample_crab/wmLHEGS_CMSSW_12_4_24/CMSSW_12_4_24/src/'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'LHEGS_cfg.py'
# config.JobType.numCores = 4
config.JobType.maxJobRuntimeMin = 1500
# config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.outputPrimaryDataset = jobName
config.Data.outLFNDirBase = '/store/user/dshekar/'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5000
NJOBS = 5 # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_LHEGS_generation_test0'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
# config.Site.whitelist = ['T2_US_Purdue','T3_US_Rice','T3_US_Rutgers','T3_US_FIT','T3_US_PSC','T3_US_OSU','T3_US_TAMU','T3_US_UMD','T3_US_VC3_NotreDame','T3_US_SDSC','T3_US_Colorado','T3_US_OSG','T3_US_Princeton_ICSE','T3_US_NERSC','T3_US_Baylor','T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T2_US_MIT','T3_US_TACC','T3_US_UMiss','T2_US_Caltech', 'T2_US_Florida','T2_US_Vanderbilt']