from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HIHardProbes_Skim_cumu_v7'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_rfp24_poieta10_Calo_cent_noacc_noeff_EP_Prompt_cm1.py'

config.Data.inputDataset = '/HIHardProbes/qwang-HIHardProbes_FullTrackSkim2015_v5-82d3c5ee469522058df894563cd74923/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
#config.Data.lumiMask = 'json_DCSONLY.txt'
config.Data.publication = False
config.Data.useParent = False

config.Site.storageSite = 'T2_CH_CERN'

