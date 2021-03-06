from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB2_pixel_noeff_v4'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_pixel_rfp24_v1.py'
#config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
config.Data.inputDataset = '/HIMinimumBias2/qwang-crab_HIMB2_PixelTracking_v3-f359806bdfa543922b20b1cc8503759a/USER'
#config.Data.inputDataset = '/HIMinimumBias2/qwang-HIMinBias2_pixel_v3-b5f9bcb1c4c1b1713c15c00149533831/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 5
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015Pix/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


