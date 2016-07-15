from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'pp13TeV_Totem_cumu_v2'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_pp13TeV_rfp24_poi24_noff_cm1.py'

config.Data.inputDataset = '/HighMultiplicity/davidlw-RecoSkim2015_2015DLowPU_ReTracking_v4-266f47bcc90a343001055b934437977e/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/pp13TeV/'
#config.Data.lumiMask = 'json_DCSONLY.txt'
config.Data.publication = False
config.Data.useParent = False

config.Site.storageSite = 'T2_CH_CERN'

