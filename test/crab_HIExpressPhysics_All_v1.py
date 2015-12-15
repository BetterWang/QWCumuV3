from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HIExpressPhysics_All_Cumu_v1'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_ExpAll_rfp24_poieta10_cent_noacc_noeff_Prompt_cm1.py'

config.Data.inputDataset = '/HIExpressPhysics/HIRun2015-Express-v1/FEVT'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
config.Data.lumiMask = 'json_DCSONLY.txt'
#config.Data.runRange = '262480-263000'
config.Data.publication = False
config.Data.useParent = False

config.Site.storageSite = 'T2_CH_CERN'

