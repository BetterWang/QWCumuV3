import FWCore.ParameterSet.Config as cms

process = cms.Process("CumuV3")

process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
#process.load('Configuration.StandardSequences.Reconstruction_cff')
#process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
#process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

#fN = cms.untracked.vstring();
#for line in open('flist').read().splitlines():
#	fN.append('file:'+line);
#
process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:FullTrack_1.root")
)

#import FWCore.PythonUtilities.LumiList as LumiList
#import FWCore.ParameterSet.Types as CfgTypes
#process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
#JSONfile = 'Cert_210498-211631_HI_PromptReco_Collisions13_JSON_v2.txt'
#myLumis = LumiList.LumiList(filename = JSONfile).getCMSSWString().split(',')
#process.source.lumisToProcess.extend(myLumis)
#
#
import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltHP10_1420 = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltHP10_1420.HLTPaths = [
	"HLT_HIFullTrack12_L1Centrality010_v*",
	"HLT_HIFullTrack12_L1MinimumBiasHF*_AND_v*",
]
process.hltHP10_1420.andOr = cms.bool(True)
process.hltHP10_1420.throw = cms.bool(False)

process.hltHP10_2026 = process.hltHP10_1420.clone()
process.hltHP10_2026.HLTPaths = [
	"HLT_HIFullTrack18_L1Centrality010_v*",
	"HLT_HIFullTrack18_L1MinimumBiasHF*_AND_v*",
]

process.hltHP10_2635 = process.hltHP10_1420.clone()
process.hltHP10_2635.HLTPaths = [
	"HLT_HIFullTrack24_v*",
]

process.hltHP10_35 = process.hltHP10_1420.clone()
process.hltHP10_35.HLTPaths = [
	"HLT_HIFullTrack34_v*",
]


process.hltHP30_1420 = process.hltHP10_1420.clone()
process.hltHP30_1420.HLTPaths = [
	"HLT_HIFullTrack12_L1MinimumBiasHF*_AND_v*",
]

process.hltHP30_2026 = process.hltHP10_1420.clone()
process.hltHP30_2026.HLTPaths = [
	"HLT_HIFullTrack18_L1MinimumBiasHF*_AND_v*",
]

process.hltHP30_2635 = process.hltHP10_1420.clone()
process.hltHP30_2635.HLTPaths = [
	"HLT_HIFullTrack24_v*",
]

process.hltHP30_35 = process.hltHP10_1420.clone()
process.hltHP30_35.HLTPaths = [
	"HLT_HIFullTrack34_v*",
]

process.hltHP100_1420 = process.hltHP10_1420.clone()
process.hltHP100_1420.HLTPaths = [
	"HLT_HIFullTrack12_L1MinimumBiasHF*_AND_v*",
]

process.hltHP100_2026 = process.hltHP10_1420.clone()
process.hltHP100_2026.HLTPaths = [
	"HLT_HIFullTrack18_L1MinimumBiasHF*_AND_v*",
]

process.hltHP100_2635 = process.hltHP10_1420.clone()
process.hltHP100_2635.HLTPaths = [
	"HLT_HIFullTrack24_v*",
]

process.hltHP100_35 = process.hltHP10_1420.clone()
process.hltHP100_35.HLTPaths = [
	"HLT_HIFullTrack34_v*",
]


process.cumulant1420 = cms.EDAnalyzer('QWCumuV3'
	, tracks_ = cms.untracked.InputTag('hiGeneralTracks')
	, centrality_ = cms.InputTag("centralityBin", "HFtowers")
	, chi2_ = cms.untracked.double(40.)
	, vertexSrc_ = cms.untracked.InputTag('hiSelectedVertex', "")
	, rfpptmin_ = cms.untracked.double(1.0)
	, rfpptmax_ = cms.untracked.double(5.0)
	, rfpmineta_ = cms.untracked.double(-2.4)
	, rfpmaxeta_ = cms.untracked.double(2.4)
	, bPhiEta_ = cms.untracked.bool(True)
	, bCentNoff_ = cms.untracked.bool(False)
	, poimineta_ = cms.untracked.double(-1.0)
	, poimaxeta_ = cms.untracked.double(1.0)
	, poiptmin_ = cms.untracked.double(14.0)
	, poiptmax_ = cms.untracked.double(20.0)
	, pterrorpt_ = cms.untracked.double(0.1)
	, Noffmin_ = cms.untracked.int32(0)
	, Noffmax_ = cms.untracked.int32(5000)
#	, fweight_ = cms.untracked.InputTag('PbPb_dijet_TT_5TeV_v2.root')
	, bEff_ = cms.untracked.bool(False)
	, cmode_ = cms.untracked.int32(1)
	, bFlipEta_ = cms.untracked.bool(False)
	, bEP = cms.untracked.bool(False)
	, EPlvl_ = cms.untracked.int32(0)
	, bCaloMaching = cms.untracked.bool(True)
	, reso = cms.untracked.double(0.5)
        , algoParameters = cms.vint32(4,5,6,7)
	, pfTag = cms.untracked.InputTag('particleFlowTmp')
	, minvz_ = cms.untracked.double(-1.0)
	, maxvz_ = cms.untracked.double(3.0)
)

process.cumulant2026 = process.cumulant1420.clone()
process.cumulant2026.poiptmin_ = cms.untracked.double(20.0)
process.cumulant2026.poiptmax_ = cms.untracked.double(26.0)

process.cumulant2635 = process.cumulant1420.clone()
process.cumulant2635.poiptmin_ = cms.untracked.double(26.0)
process.cumulant2635.poiptmax_ = cms.untracked.double(35.0)

process.cumulant35 = process.cumulant1420.clone()
process.cumulant35.poiptmin_ = cms.untracked.double(35.0)
process.cumulant35.poiptmax_ = cms.untracked.double(100.0)



process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.clusterCompatibilityFilter.clusterPars = cms.vdouble(0.0,0.006)

process.eventSelection = cms.Sequence(
        process.hfCoincFilter3
        + process.primaryVertexFilter
        + process.clusterCompatibilityFilter
)


process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')

process.centralityFilter10 = process.centralityFilter.clone()
process.centralityFilter30 = process.centralityFilter.clone()
process.centralityFilter100 = process.centralityFilter.clone()

process.centralityFilter10.selectedBins = cms.vint32(
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

process.centralityFilter30.selectedBins = cms.vint32(
        20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
        50, 51, 52, 53, 54, 55, 56, 57, 58, 59)

process.centralityFilter100.selectedBins = cms.vint32(
        60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
        70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
        80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
        90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
        100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
        110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
        120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
        130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
        140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
        150, 151, 152, 153, 154, 155, 156, 157, 158, 159,
        160, 161, 162, 163, 164, 165, 166, 167, 168, 169,
        170, 171, 172, 173, 174, 175, 176, 177, 178, 179,
        180, 181, 182, 183, 184, 185, 186, 187, 188, 189,
        190, 191, 192, 193, 194, 195, 196, 197, 198, 199)

process.hardprobe10_1420 = cms.Path(process.hltHP10_1420*process.eventSelection*process.centralityBin*process.centralityFilter10*process.cumulant1420)
process.hardprobe10_2026 = cms.Path(process.hltHP10_2026*process.eventSelection*process.centralityBin*process.centralityFilter10*process.cumulant2026)
process.hardprobe10_2635 = cms.Path(process.hltHP10_2635*process.eventSelection*process.centralityBin*process.centralityFilter10*process.cumulant2635)
process.hardprobe10_35   = cms.Path(process.hltHP10_35  *process.eventSelection*process.centralityBin*process.centralityFilter10*process.cumulant35)

process.hardprobe30_1420 = cms.Path(process.hltHP30_1420*process.eventSelection*process.centralityBin*process.centralityFilter30*process.cumulant1420)
process.hardprobe30_2026 = cms.Path(process.hltHP30_2026*process.eventSelection*process.centralityBin*process.centralityFilter30*process.cumulant2026)
process.hardprobe30_2635 = cms.Path(process.hltHP30_2635*process.eventSelection*process.centralityBin*process.centralityFilter30*process.cumulant2635)
process.hardprobe30_35   = cms.Path(process.hltHP30_35  *process.eventSelection*process.centralityBin*process.centralityFilter30*process.cumulant35)

process.hardprobe100_1420 = cms.Path(process.hltHP100_1420*process.eventSelection*process.centralityBin*process.centralityFilter100*process.cumulant1420)
process.hardprobe100_2026 = cms.Path(process.hltHP100_2026*process.eventSelection*process.centralityBin*process.centralityFilter100*process.cumulant2026)
process.hardprobe100_2635 = cms.Path(process.hltHP100_2635*process.eventSelection*process.centralityBin*process.centralityFilter100*process.cumulant2635)
process.hardprobe100_35   = cms.Path(process.hltHP100_35  *process.eventSelection*process.centralityBin*process.centralityFilter100*process.cumulant35)


process.schedule = cms.Schedule(
	process.hardprobe10_1420,
	process.hardprobe10_2026,
	process.hardprobe10_2635,
	process.hardprobe10_35,

	process.hardprobe30_1420,
	process.hardprobe30_2026,
	process.hardprobe30_2635,
	process.hardprobe30_35,

	process.hardprobe100_1420,
	process.hardprobe100_2026,
	process.hardprobe100_2635,
	process.hardprobe100_35,
)
