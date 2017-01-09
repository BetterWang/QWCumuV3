import FWCore.ParameterSet.Config as cms

process = cms.Process("CumuV3")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_dataRun2_v13', '')

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring("file:/afs/cern.ch/user/q/qwang/work/cleanroomRun2/Ana/data/pixeltracking_1.root")
)

import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_HIL1MinimumBiasHF2AND*",
	"HLT_HIL1MinimumBiasHF1AND*",
]
process.hltMB.andOr = cms.bool(True)
process.hltMB.throw = cms.bool(False)


process.cumulantMB = cms.EDAnalyzer('QWCumuV3'
	, trackEta = cms.untracked.InputTag('QWEvent', "eta")
	, trackPhi = cms.untracked.InputTag('QWEvent', "phi")
	, trackPt = cms.untracked.InputTag('QWEvent', "pt")
	, trackWeight = cms.untracked.InputTag('QWEvent', "weight")
	, trackCharge = cms.untracked.InputTag('QWEvent', "charge")
	, vertexZ = cms.untracked.InputTag('QWEvent', "vz")
	, centrality = cms.untracked.InputTag('centralityBin', "HFtowers")
	, minvz = cms.untracked.double(-15.0)
	, maxvz = cms.untracked.double(15.0)
	, rfpmineta = cms.untracked.double(-2.4)
	, rfpmaxeta = cms.untracked.double(2.4)
	, rfpminpt = cms.untracked.double(0.3)
	, rfpmaxpt = cms.untracked.double(3.0)
	, poimineta = cms.untracked.double(-2.4)
	, poimaxeta = cms.untracked.double(2.4)
	, poiminpt = cms.untracked.double(0.3)
	, poimaxpt = cms.untracked.double(20.0)
	, b2PartGap = cms.untracked.bool(True)
	, dEtaGap = cms.untracked.double(2.0)
	, cmode = cms.untracked.int32(1)
	, nvtx = cms.untracked.int32(100)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
)

process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')
process.clusterCompatibilityFilter.clusterPars = cms.vdouble(0.0,0.006)


process.eventSelection = cms.Sequence(
        process.hfCoincFilter3
        + process.primaryVertexFilter
        + process.clusterCompatibilityFilter
)

process.load('PbPb_HIMB2_pixel_eff')
process.QWEvent.ptMax = cms.untracked.double(20.0)

process.QWEvent.Etamin = cms.untracked.double(-1.0)
process.QWEvent.Etamax = cms.untracked.double(1.0)

process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')
process.CentFilter0_5 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(0, 10)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter5_10 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(10, 20)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter10_20 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(20, 40)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter20_30 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(40, 60)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter30_40 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(60, 80)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter40_50 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(80, 100)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter50_60 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(100, 120)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)
process.CentFilter60_70 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(120, 140)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter70_80 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(140, 160)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)
process.CentFilter80_90 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(160, 180)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.CentFilter90_100 = process.centralityFilter.clone(
	selectedBins = cms.vint32(
		*range(180, 200)
		),
	BinLabel = cms.InputTag("centralityBin", "HFtowers")
	)

process.vectPhi0_5    = process.vectPhi.clone()
process.vectPhi5_10   = process.vectPhi.clone()
process.vectPhi10_20  = process.vectPhi.clone()
process.vectPhi20_30  = process.vectPhi.clone()
process.vectPhi30_40  = process.vectPhi.clone()
process.vectPhi40_50  = process.vectPhi.clone()
process.vectPhi50_60  = process.vectPhi.clone()
process.vectPhi60_70  = process.vectPhi.clone()
process.vectPhi70_80  = process.vectPhi.clone()
process.vectPhi80_90  = process.vectPhi.clone()
process.vectPhi90_100 = process.vectPhi.clone()

process.vectPhiW0_5    = process.vectPhiW.clone()
process.vectPhiW5_10   = process.vectPhiW.clone()
process.vectPhiW10_20  = process.vectPhiW.clone()
process.vectPhiW20_30  = process.vectPhiW.clone()
process.vectPhiW30_40  = process.vectPhiW.clone()
process.vectPhiW40_50  = process.vectPhiW.clone()
process.vectPhiW50_60  = process.vectPhiW.clone()
process.vectPhiW60_70  = process.vectPhiW.clone()
process.vectPhiW70_80  = process.vectPhiW.clone()
process.vectPhiW80_90  = process.vectPhiW.clone()
process.vectPhiW90_100 = process.vectPhiW.clone()

process.vectPt0_5    = process.vectPt.clone()
process.vectPt5_10   = process.vectPt.clone()
process.vectPt10_20  = process.vectPt.clone()
process.vectPt20_30  = process.vectPt.clone()
process.vectPt30_40  = process.vectPt.clone()
process.vectPt40_50  = process.vectPt.clone()
process.vectPt50_60  = process.vectPt.clone()
process.vectPt60_70  = process.vectPt.clone()
process.vectPt70_80  = process.vectPt.clone()
process.vectPt80_90  = process.vectPt.clone()
process.vectPt90_100 = process.vectPt.clone()

process.vectPtW0_5    = process.vectPtW.clone()
process.vectPtW5_10   = process.vectPtW.clone()
process.vectPtW10_20  = process.vectPtW.clone()
process.vectPtW20_30  = process.vectPtW.clone()
process.vectPtW30_40  = process.vectPtW.clone()
process.vectPtW40_50  = process.vectPtW.clone()
process.vectPtW50_60  = process.vectPtW.clone()
process.vectPtW60_70  = process.vectPtW.clone()
process.vectPtW70_80  = process.vectPtW.clone()
process.vectPtW80_90  = process.vectPtW.clone()
process.vectPtW90_100 = process.vectPtW.clone()

process.vectEta0_5    = process.vectEta.clone()
process.vectEta5_10   = process.vectEta.clone()
process.vectEta10_20  = process.vectEta.clone()
process.vectEta20_30  = process.vectEta.clone()
process.vectEta30_40  = process.vectEta.clone()
process.vectEta40_50  = process.vectEta.clone()
process.vectEta50_60  = process.vectEta.clone()
process.vectEta60_70  = process.vectEta.clone()
process.vectEta70_80  = process.vectEta.clone()
process.vectEta80_90  = process.vectEta.clone()
process.vectEta90_100 = process.vectEta.clone()

process.vectEtaW0_5    = process.vectEtaW.clone()
process.vectEtaW5_10   = process.vectEtaW.clone()
process.vectEtaW10_20  = process.vectEtaW.clone()
process.vectEtaW20_30  = process.vectEtaW.clone()
process.vectEtaW30_40  = process.vectEtaW.clone()
process.vectEtaW40_50  = process.vectEtaW.clone()
process.vectEtaW50_60  = process.vectEtaW.clone()
process.vectEtaW60_70  = process.vectEtaW.clone()
process.vectEtaW70_80  = process.vectEtaW.clone()
process.vectEtaW80_90  = process.vectEtaW.clone()
process.vectEtaW90_100 = process.vectEtaW.clone()


process.vectMonW0_5 = cms.Sequence(process.vectPhi0_5 * process.vectPhiW0_5 * process.vectPt0_5 * process.vectPtW0_5 * process.vectEta0_5 * process.vectEtaW0_5 )
process.vectMonW5_10 = cms.Sequence(process.vectPhi5_10 * process.vectPhiW5_10 * process.vectPt5_10 * process.vectPtW5_10 * process.vectEta5_10 * process.vectEtaW5_10 )
process.vectMonW10_20 = cms.Sequence(process.vectPhi10_20 * process.vectPhiW10_20 * process.vectPt10_20 * process.vectPtW10_20 * process.vectEta10_20 * process.vectEtaW10_20 )
process.vectMonW20_30 = cms.Sequence(process.vectPhi20_30 * process.vectPhiW20_30 * process.vectPt20_30 * process.vectPtW20_30 * process.vectEta20_30 * process.vectEtaW20_30 )
process.vectMonW30_40 = cms.Sequence(process.vectPhi30_40 * process.vectPhiW30_40 * process.vectPt30_40 * process.vectPtW30_40 * process.vectEta30_40 * process.vectEtaW30_40 )
process.vectMonW40_50 = cms.Sequence(process.vectPhi40_50 * process.vectPhiW40_50 * process.vectPt40_50 * process.vectPtW40_50 * process.vectEta40_50 * process.vectEtaW40_50 )
process.vectMonW50_60 = cms.Sequence(process.vectPhi50_60 * process.vectPhiW50_60 * process.vectPt50_60 * process.vectPtW50_60 * process.vectEta50_60 * process.vectEtaW50_60 )
process.vectMonW60_70 = cms.Sequence(process.vectPhi60_70 * process.vectPhiW60_70 * process.vectPt60_70 * process.vectPtW60_70 * process.vectEta60_70 * process.vectEtaW60_70 )
process.vectMonW70_80 = cms.Sequence(process.vectPhi70_80 * process.vectPhiW70_80 * process.vectPt70_80 * process.vectPtW70_80 * process.vectEta70_80 * process.vectEtaW70_80 )
process.vectMonW80_90 = cms.Sequence(process.vectPhi80_90 * process.vectPhiW80_90 * process.vectPt80_90 * process.vectPtW80_90 * process.vectEta80_90 * process.vectEtaW80_90 )
process.vectMonW90_100= cms.Sequence(process.vectPhi90_100* process.vectPhiW90_100* process.vectPt90_100* process.vectPtW90_100* process.vectEta90_100* process.vectEtaW90_100)


process.cumulantMB.rfpmineta = cms.untracked.double(-1.0)
process.cumulantMB.rfpmaxeta = cms.untracked.double(1.0)
process.cumulantMB.dEtaGap = cms.untracked.double(1.0)


process.ana = cms.Path(process.hltMB*process.eventSelection*process.makeEvent*process.cumulantMB * process.histNoff)
process.ana_0_5   = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter0_5 * process.vectMonW0_5 )
process.ana_5_10  = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter5_10 * process.vectMonW5_10 )
process.ana_10_20 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter10_20 * process.vectMonW10_20 )
process.ana_20_30 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter20_30 * process.vectMonW20_30 )
process.ana_30_40 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter30_40 * process.vectMonW30_40 )
process.ana_40_50 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter40_50 * process.vectMonW40_50 )
process.ana_50_60 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter50_60 * process.vectMonW50_60 )
process.ana_60_70 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter60_70 * process.vectMonW60_70 )
process.ana_70_80 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter70_80 * process.vectMonW70_80 )
process.ana_80_90 = cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter80_90 * process.vectMonW80_90 )
process.ana_90_100= cms.Path(process.hltMB*process.eventSelection*process.makeEvent* process.CentFilter90_100* process.vectMonW90_100)

process.schedule = cms.Schedule(
	process.ana,
	process.ana_0_5,
	process.ana_5_10,
	process.ana_10_20,
	process.ana_20_30,
	process.ana_30_40,
	process.ana_40_50,
	process.ana_50_60,
	process.ana_60_70,
	process.ana_70_80,
	process.ana_80_90,
	process.ana_90_100,
)
