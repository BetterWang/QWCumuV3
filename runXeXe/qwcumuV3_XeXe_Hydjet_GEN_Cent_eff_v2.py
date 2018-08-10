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
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_ForXeXe_v7', '') #for now track GT manually, since centrality tables updated ex post facto
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
   cms.PSet(record = cms.string("HeavyIonRcd"),
      tag = cms.string("CentralityTable_HFtowers200_XeXe5p44TeVHYDJET_v941x01_mc"),
      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
      label = cms.untracked.string("HFtowersHYDJET")
   ),
])


process.load('RecoHI.HiCentralityAlgos.HiCentrality_cfi')
process.hiCentrality.produceHFhits = False
process.hiCentrality.produceHFtowers = False
process.hiCentrality.produceEcalhits = False
process.hiCentrality.produceZDChits = False
process.hiCentrality.produceETmidRapidity = False
process.hiCentrality.producePixelhits = False
process.hiCentrality.produceTracks = False
process.hiCentrality.producePixelTracks = False
process.hiCentrality.reUseCentrality = True
process.hiCentrality.srcReUse = cms.InputTag("hiCentrality","","RECO")

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("HYDJET")


process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

process.source = cms.Source("PoolSource",
#	fileNames = cms.untracked.vstring("root://cms-xrd-global.cern.ch//store/himc/HINXeXeFall17DR/XeXeMinBias_5p44TeV-HydjetCymb5Ev8/GEN-SIM-RECO/94X_mc2017_realistic_ForXeXe_v7-v2/40000/00261A37-470C-E811-A936-02163E01191C.root")
	fileNames = cms.untracked.vstring("/store/himc/HINXeXeFall17DR/XeXeMinBias_5p44TeV-HydjetCymb5Ev8/GEN-SIM-RECO/94X_mc2017_realistic_ForXeXe_v7-v2/40000/00261A37-470C-E811-A936-02163E01191C.root")
)


import HLTrigger.HLTfilters.hltHighLevel_cfi

process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
	"HLT_HIL1MinimumBiasHF_OR_SinglePixelTrack_part*"
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
	, centrality = cms.untracked.InputTag('centralityBin', 'HFtowers')
	, minvz = cms.untracked.double(-15.0)
	, maxvz = cms.untracked.double(15.0)
	, rfpmineta = cms.untracked.double(-2.4)
	, rfpmaxeta = cms.untracked.double(2.4)
	, rfpminpt = cms.untracked.double(0.3)
	, rfpmaxpt = cms.untracked.double(3.0)
	, poimineta = cms.untracked.double(-2.4)
	, poimaxeta = cms.untracked.double(2.4)
	, poiminpt = cms.untracked.double(0.3)
	, poimaxpt = cms.untracked.double(10.0)
	, b2PartGap = cms.untracked.bool(True)
	, dEtaGap = cms.untracked.double(2.0)
	, cmode = cms.untracked.int32(1)
	, nvtx = cms.untracked.int32(100)
	, ptBin = cms.untracked.vdouble(0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0)
	, etaBin = cms.untracked.vdouble(-2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4)
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
)


process.primaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True), # otherwise it won't filter the events
)

process.NoScraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)

process.load("HeavyIonsAnalysis.Configuration.hfCoincFilter_cff")
#process.hfPosFilter3 = process.hfPosFilter.clone(minNumber=cms.uint32(3))
#process.hfNegFilter3 = process.hfNegFilter.clone(minNumber=cms.uint32(3))
#process.hfCoincFilter3 = cms.Sequence(
#    process.towersAboveThreshold 
#    + process.hfPosTowers 
#    + process.hfNegTowers 
#    + process.hfPosFilter3 
#    + process.hfNegFilter3
#)

process.eventSelection = cms.Sequence(
        process.hfCoincFilter3
        + process.primaryVertexFilter
        + process.NoScraping
)

process.QWEvent = cms.EDProducer("QWGenEventProducer",
		trackSrc  = cms.untracked.InputTag("genParticles"),
		ptMin = cms.untracked.double(0.3),
		ptMax = cms.untracked.double(10.),
		isPrompt  = cms.untracked.bool(True),
		doFilterPdg = cms.untracked.bool(True),
		pdgId = cms.untracked.vint32(211, -211, 321, -321, 2212, -2212),
		)


# monitoring
process.histCent = cms.EDAnalyzer('QWHistAnalyzer',
		src = cms.untracked.InputTag("centralityBin", 'HFtowers'),
		Nbins = cms.untracked.int32(200),
		start = cms.untracked.double(0),
		end = cms.untracked.double(200),
		)


process.vectPhi = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "phi"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(-3.14159265358979323846),
		cend = cms.untracked.double(3.14159265358979323846),
		)

process.vectPt = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "pt"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(0),
		cend = cms.untracked.double(5),
		)

process.vectEta = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "eta"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(-2.5),
		cend = cms.untracked.double(2.5),
		)

process.PhiEta2D = cms.EDAnalyzer('QWVCorrAnalyzer',
		srcX = cms.untracked.InputTag('QWEvent', 'eta'),
		NbinsX = cms.untracked.int32(48),
		hstartX = cms.untracked.double(-2.4),
		hendX = cms.untracked.double(2.4),
		srcY = cms.untracked.InputTag('QWEvent', 'phi'),
		NbinsY = cms.untracked.int32(48),
		hstartY = cms.untracked.double(-3.14159265358979323846),
		hendY = cms.untracked.double(3.14159265358979323846),
		)

#process.NoffCent2D = cms.EDAnalyzer('QWCorrAnalyzer',
#		srcX = cms.untracked.InputTag('dbNoff'),
#		NbinsX = cms.untracked.int32(5000),
#		hstartX = cms.untracked.double(0),
#		hendX = cms.untracked.double(5000),
#		srcY = cms.untracked.InputTag('dbCent'),
#		NbinsY = cms.untracked.int32(200),
#		hstartY = cms.untracked.double(0),
#		hendY = cms.untracked.double(200),
#		)


process.vectMon = cms.Sequence(process.histCent * process.vectPhi * process.vectPt * process.vectEta * process.PhiEta2D )

process.ana = cms.Path(
#		process.eventSelection *
		process.hiCentrality *
		process.centralityBin *
		process.QWEvent *
		process.cumulantMB *
		process.vectMon )

process.RECO = cms.OutputModule("PoolOutputModule",
		outputCommands = cms.untracked.vstring('keep *'),
		SelectEvents = cms.untracked.PSet(
			SelectEvents = cms.vstring('ana')
			),
		fileName = cms.untracked.string('reco.root')
		)

process.out = cms.EndPath(process.RECO)

process.schedule = cms.Schedule(
	process.ana,
)
