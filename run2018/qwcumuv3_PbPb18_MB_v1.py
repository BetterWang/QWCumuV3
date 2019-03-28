import FWCore.ParameterSet.Config as cms

process = cms.Process("CumuDiff")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi")
process.load("MergingProducer.generalAndHiPixelTracks.MergingPixAndGenProducer_cfi")


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
#process.MessageLogger.cerr.FwkReport.reportEvery = 100

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_Prompt_v2', '')

process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("HeavyIonRcd"),
        tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1031x02_offline"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        label = cms.untracked.string("HFtowers")
        ),
    ])

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")

process.dbCent = cms.EDProducer('QWInt2Double',
    src = cms.untracked.InputTag('centralityBin', 'HFtowers')
    )


process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/q/qwang/cleanroomRun2/Ana/data/PbPb2018_MB.root"),
    )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('cumu.root')
    )

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltMB = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltMB.HLTPaths = [
        "HLT_HIMinimumBias_*"
        ]
process.hltMB.andOr = cms.bool(True)
process.hltMB.throw = cms.bool(False)


process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
process.load('HeavyIonsAnalysis.Configuration.collisionEventSelection_cff')

process.eventSelection = cms.Sequence(
	process.primaryVertexFilter
	* process.hfCoincFilter2Th4
	* process.clusterCompatibilityFilter
    )



process.histCentBin = cms.EDAnalyzer('QWHistAnalyzer',
        src = cms.untracked.InputTag("centralityBin", "HFtowers"),
        Nbins = cms.untracked.int32(200),
        start = cms.untracked.double(0),
        end = cms.untracked.double(200),
        )

process.QWVertex = cms.EDProducer('QWVertexProducer',
        vertexSrc = cms.untracked.InputTag('offlinePrimaryVerticesRecovery')
        )
process.QWPrimaryVz = cms.EDProducer('QWVectorSelector',
                vectSrc = cms.untracked.InputTag('QWVertex', 'vz'),
        )
process.QWVzFilter15 = cms.EDFilter('QWDoubleFilter',
                src = cms.untracked.InputTag('QWPrimaryVz'),
                dmin = cms.untracked.double(-15.),
                dmax = cms.untracked.double(15.),
        )
process.QWPrimaryVertexSelection = cms.Sequence( process.QWVertex * process.QWPrimaryVz * process.QWVzFilter15 )

process.QWEvent = cms.EDProducer('QWEvent2018Producer',
        trackSrc = cms.untracked.InputTag('generalAndHiPixelTracks'),
        fweight = cms.untracked.InputTag('NA'),
        centralitySrc = cms.untracked.InputTag('centralityBin', 'HFtowers'),
        ptMin = cms.untracked.double(0.3),
        ptMax = cms.untracked.double(10.0),
        Etamin = cms.untracked.double(-2.4),
        Etamax = cms.untracked.double(2.4)
        )

process.vectPhi_0 = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "phi"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(-3.14159265358979323846),
		cend = cms.untracked.double(3.14159265358979323846),
		)

process.vectPt_0 = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "pt"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(0),
		cend = cms.untracked.double(10.),
		)

process.vectEta_0 = cms.EDAnalyzer('QWVectorAnalyzer',
		src = cms.untracked.InputTag("QWEvent", "eta"),
		hNbins = cms.untracked.int32(5000),
		hstart = cms.untracked.double(0),
		hend = cms.untracked.double(5000),
		cNbins = cms.untracked.int32(1000),
		cstart = cms.untracked.double(-2.5),
		cend = cms.untracked.double(2.5),
		)

process.PhiEta2D_0 = cms.EDAnalyzer('QWEtaPhiPtAnalyzer',
		srcEta = cms.untracked.InputTag('QWEvent', 'eta'),
		srcPhi = cms.untracked.InputTag('QWEvent', 'phi'),
		srcPt  = cms.untracked.InputTag('QWEvent', 'pt'),
		NbinsPhi = cms.untracked.int32(72),
		NbinsEta = cms.untracked.int32(48),
		hstartEta = cms.untracked.double(-2.4),
		hendEta = cms.untracked.double(2.4),
        ptBin = cms.untracked.vdouble(0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0)
		)

for i in range(1, 20):
    setattr(process, 'PhiEta2D_'+str(i), process.PhiEta2D_0.clone())
    setattr(process, 'vectPhi_'+str(i), process.vectPhi_0.clone())
    setattr(process, 'vectEta_'+str(i), process.vectEta_0.clone())
    setattr(process, 'vectPt_'+str(i), process.vectPt_0.clone())

process.load('RecoHI.HiCentralityAlgos.CentralityFilter_cfi')

for i in range(20):
    setattr(process, 'cent_'+str(i), process.centralityFilter.clone(selectedBins = cms.vint32(*range(i*10, i*10+10)), BinLabel = cms.InputTag('centralityBin', 'HFtowers')))

for i in range(20):
    setattr(process, 'mon_'+str(i), cms.Sequence(
        getattr(process, 'PhiEta2D_'+str(i)) +
        getattr(process, 'vectPhi_'+str(i)) +
        getattr(process, 'vectEta_'+str(i)) +
        getattr(process, 'vectPt_'+str(i))
        ) )

process.cumulantMB = cms.EDAnalyzer('QWCumuV3'
    , trackEta = cms.untracked.InputTag('QWEvent', "eta")
    , trackPhi = cms.untracked.InputTag('QWEvent', "phi")
    , trackPt = cms.untracked.InputTag('QWEvent', "pt")
    , trackWeight = cms.untracked.InputTag('QWEvent', "weight")
    , trackCharge = cms.untracked.InputTag('QWEvent', "charge")
    , centrality = cms.untracked.InputTag('centralityBin', 'HFtowers')
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


for i in range(20):
    setattr( process, 'ana_' + str(i), cms.Path(
        process.hltMB
        * process.offlinePrimaryVerticesRecovery
        * process.QWPrimaryVertexSelection
        * process.eventSelection
        * process.centralityBin
        * getattr( process, 'cent_'+str(i) )
        * process.dbCent
        * process.histCentBin
        * process.generalAndHiPixelTracks
        * process.QWEvent
        * process.cumulantMB
        * getattr( process, 'mon_'+str(i) )
        ) )

process.ana = cms.Path(
        process.hltMB
        * process.offlinePrimaryVerticesRecovery
        * process.QWPrimaryVertexSelection
        * process.eventSelection
        * process.centralityBin
        * process.dbCent
        * process.histCentBin
        )

process.schedule = cms.Schedule(
#        process.ana,
        process.ana_0,
        process.ana_1,
        process.ana_2,
        process.ana_3,
        process.ana_4,
        process.ana_5,
        process.ana_6,
        process.ana_7,
        process.ana_8,
        process.ana_9,
        process.ana_10,
        process.ana_11,
        process.ana_12,
        process.ana_13,
        process.ana_14,
        process.ana_15,
        )

from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")
process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"
