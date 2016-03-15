from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'HIMB3_cal_noeff_sysCalo_v6'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysCalo.py'
#config.JobType.inputFiles = ['PbPb_dijet_TT_5TeV_v2.root']
config.Data.inputDataset = '/HIMinimumBias3/qwang-HIMinBias_v2-ce439b1c24fa1bf3a491f2ccb0fd72a9/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/PbPb2015/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/HI/Cert_262548-263757_PromptReco_HICollisions15_JSON_v2.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
#Calo
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)





#Tight
config.General.requestName = 'HIMB3_cal_noeff_sysTight_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysTight.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)




#Loose
config.General.requestName = 'HIMB3_cal_noeff_sysLoose_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysLoose.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)




#Vz0
config.General.requestName = 'HIMB3_cal_noeff_sysVz0_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysVz0.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)



#Vz1
config.General.requestName = 'HIMB3_cal_noeff_sysVz1_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysVz1.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)



######################################################
# MB4 Calo
config.General.requestName = 'HIMB4_cal_noeff_sysCalo_v6'
config.Data.inputDataset = '/HIMinimumBias4/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 20
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysCalo.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#








# MB4 Tight
config.General.requestName = 'HIMB4_cal_noeff_sysTight_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysTight.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)





# MB4 Loose
config.General.requestName = 'HIMB4_cal_noeff_sysLoose_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysLoose.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)





# MB4 Vz0
config.General.requestName = 'HIMB4_cal_noeff_sysVz0_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysVz0.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)







# MB4 Vz1
config.General.requestName = 'HIMB4_cal_noeff_sysVz1_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysVz1.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)


########### MB3 AOD
# MB3 Calo
config.General.requestName = 'HIMB3_cal_noeff_sysCaloAOD_v6'
config.Data.inputDataset = '/HIMinimumBias3/HIRun2015-PromptReco-v1/AOD'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 20
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysCalo.py'
#try:
#        crabCommand('submit', config = config)
#except HTTPException as hte:
#        print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#        print "Failed submitting task: %s" % (cle)
#








# MB3 Tight
config.General.requestName = 'HIMB3_cal_noeff_sysTightAOD_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysTight.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)





# MB3 Loose
config.General.requestName = 'HIMB3_cal_noeff_sysLooseAOD_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysLoose.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)





# MB3 Vz0
config.General.requestName = 'HIMB3_cal_noeff_sysVz0AOD_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysVz0.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)







# MB3 Vz1
config.General.requestName = 'HIMB3_cal_noeff_sysVz1AOD_v6'
config.JobType.psetName = 'qwcumuv2_PbPb15_HIMB_rfp24_poieta10_cent_noeff_sysVz1.py'
try:
        crabCommand('submit', config = config)
except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


