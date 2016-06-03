import FWCore.ParameterSet.Config as cms


generator = cms.EDProducer("FlowGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(12.30),
        MinPt = cms.double(0.30),
        PartID = cms.vint32(211),
        MaxEta = cms.double(2.4),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.4),
        MinPhi = cms.double(-3.14159265359) ## in radians
    ),
    FlowParameters = cms.PSet(
        modv1= cms.InputTag("0.0"),
        modv2= cms.InputTag("0.2"),
        modv3= cms.InputTag("0.0"),
        modv4= cms.InputTag("0.0"),
        modv5= cms.InputTag("0.0"),
        modv6= cms.InputTag("0.0"),
        fluct_v1= cms.double(0.0),
        fluct_v2= cms.double(0.0),
        fluct_v3= cms.double(0.0),
        fluct_v4= cms.double(0.0),
        fluct_v5= cms.double(0.0),
        fluct_v6= cms.double(0.0),
        szCluster = cms.int32(5),
        nCluster = cms.int32(100),
        modCluster = cms.InputTag("TMath::Gaus(x, 0., 0.2)"),
    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

    psethack = cms.string('pi pt 0.3 12.3'),
    AddAntiParticle = cms.bool(True),
    firstRun = cms.untracked.uint32(1)
)
