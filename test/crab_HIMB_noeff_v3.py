from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB3_cal_noeff_v13'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2.py'
#config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
config.Data.inputDataset = '/HIMinimumBias3/HIRun2015-PromptReco-v1/AOD'
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 25
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
'''
config.General.requestName = 'HIMB3_cal_noeff_sysCalo_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysCalo.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB3_cal_noeff_sysTight_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysTight.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB3_cal_noeff_sysLoose_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysLoose.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB3_cal_noeff_sysVz0_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz0.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB3_cal_noeff_sysVz1_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz1.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB3_cal_eff_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysEff.py'
config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

# MB1
config.General.requestName = 'HIMB1_cal_noeff_v13'
config.Data.inputDataset = '/HIMinimumBias1/HIRun2015-PromptReco-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB1_cal_noeff_sysCalo_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysCalo.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB1_cal_noeff_sysTight_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysTight.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB1_cal_noeff_sysLoose_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysLoose.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB1_cal_noeff_sysVz0_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz0.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB1_cal_noeff_sysVz1_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz1.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB1_cal_eff_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysEff.py'
config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


# MB2
config.General.requestName = 'HIMB2_cal_noeff_v13'
config.Data.inputDataset = '/HIMinimumBias2/HIRun2015-PromptReco-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB2_cal_noeff_sysCalo_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysCalo.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB2_cal_noeff_sysTight_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysTight.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB2_cal_noeff_sysLoose_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysLoose.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB2_cal_noeff_sysVz0_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz0.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB2_cal_noeff_sysVz1_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz1.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB2_cal_eff_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysEff.py'
config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


'''
# MB4
config.General.requestName = 'HIMB4_cal_noeff_v13'
config.Data.inputDataset = '/HIMinimumBias4/HIRun2015-PromptReco-v1/AOD'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#
#

config.General.requestName = 'HIMB4_cal_noeff_sysCalo_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysCalo.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB4_cal_noeff_sysTight_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysTight.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB4_cal_noeff_sysLoose_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysLoose.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


config.General.requestName = 'HIMB4_cal_noeff_sysVz0_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz0.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB4_cal_noeff_sysVz1_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysVz1.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config.General.requestName = 'HIMB4_cal_eff_v13'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_v2_sysEff.py'
config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

