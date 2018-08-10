from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()

config.General.requestName = 'XeXe1_CumuV3_eff_Cent_sysWide_v1'
config.General.workArea = 'CrabArea'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'qwcumuV3_XeXe_ppReco_Cent_eff_sysWide_v1.py'
config.Data.inputDataset = '/HIMinimumBias1/XeXeRun2017-13Dec2017-v1/AOD'
config.JobType.inputFiles = ['XeXe_eff_wide_table_94x_cent.root']
config.JobType.maxJobRuntimeMin = 2500
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 3
config.Data.outLFNDirBase = '/store/group/phys_heavyions/qwang/XeXe/'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/HI/Cert_304899-304907_5TeV_PromptReco_XeXe_Collisions17_JSON.txt'
config.Data.publication = False
config.Data.useParent = False
config.Site.storageSite = 'T2_CH_CERN'
config.Site.ignoreGlobalBlacklist = True
#config.Data.allowNonValidInputDataset = True
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#

#config.General.requestName = 'XeXe2_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias2/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#

config.General.requestName = 'XeXe3_CumuV3_eff_Cent_sysWide_v1'
config.Data.inputDataset = '/HIMinimumBias3/XeXeRun2017-13Dec2017-v1/AOD'
try:
	crabCommand('submit', config = config)
except HTTPException as hte:
	print "Failed submitting task: %s" % (hte.headers)
except ClientException as cle:
	print "Failed submitting task: %s" % (cle)

#
#config.General.requestName = 'XeXe4_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias4/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe5_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias5/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe6_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias6/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe7_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias7/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe8_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias8/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe9_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias9/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe10_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias10/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe11_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias11/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe12_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias12/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe13_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias13/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe14_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias14/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#
#config.General.requestName = 'XeXe15_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias15/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe16_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias16/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe17_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias17/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe18_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias18/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe19_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias19/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
#
#config.General.requestName = 'XeXe20_CumuV3_eff_Cent_sysWide_v1'
#config.Data.inputDataset = '/HIMinimumBias20/XeXeRun2017-13Dec2017-v1/AOD'
#try:
#	crabCommand('submit', config = config)
#except HTTPException as hte:
#	print "Failed submitting task: %s" % (hte.headers)
#except ClientException as cle:
#	print "Failed submitting task: %s" % (cle)
#
