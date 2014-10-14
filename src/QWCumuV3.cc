// -*- C++ -*-
//
// Package:    QWCumuV3
// Class:      QWCumuV3
// 
/**\class QWCumuV3 QWCumuV3.cc QWAna/QWCumuV3/src/QWCumuV3.cc

Description: [one line class summary]

Implementation:
[Notes on implementation]
*/
//
// Original Author:  Quan Wang
//         Created:  05/23/2014
// $Id: QWCumuV3.cc,v 1.0 2014/05/23 15:56:58 qwang Exp $
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "TH1.h"
#include "TH2.h"
#include "TNtuple.h"
#include "TComplex.h"


#include "QWAna/QWCumuV3/interface/QWCumuV3.h"


using namespace std;

//#ifdef QW_DEBUG
//
// constructors and destructor
//
QWCumuV3::QWCumuV3(const edm::ParameterSet& iConfig)
	:
		tracks_(iConfig.getUntrackedParameter<edm::InputTag>("tracks_"))
	,	centrality_(iConfig.getParameter<edm::InputTag>("centrality_"))
	,	vertexSrc_(iConfig.getUntrackedParameter<edm::InputTag>("vertexSrc_"))
	,	bacc(false)
{
	//now do what ever initialization is needed
	minvz_ = iConfig.getUntrackedParameter<double>("minvz_", -15.);
	maxvz_ = iConfig.getUntrackedParameter<double>("maxvz_", 15.);
	dzdzerror_ = iConfig.getUntrackedParameter<double>("dzdzerror_", 3.);
	d0d0error_ = iConfig.getUntrackedParameter<double>("d0d0error_", 3.);
	chi2_ = iConfig.getUntrackedParameter<double>("chi2_", 40);
	pterrorpt_ = iConfig.getUntrackedParameter<double>("pterrorpt_", 0.1);

	rfpmineta_ = iConfig.getUntrackedParameter<double>("rfpmineta_", -2.4);
	rfpmaxeta_ = iConfig.getUntrackedParameter<double>("rfpmaxeta_", 2.4);
	rfpptmin_ = iConfig.getUntrackedParameter<double>("rfpptmin_", 0.3);
	rfpptmax_ = iConfig.getUntrackedParameter<double>("rfpptmax_", 100);

	poimineta_ = iConfig.getUntrackedParameter<double>("poimineta_", -2.4);
	poimaxeta_ = iConfig.getUntrackedParameter<double>("poimaxeta_", 2.4);
	poiptmin_ = iConfig.getUntrackedParameter<double>("poiptmin_", 0.3);
	poiptmax_ = iConfig.getUntrackedParameter<double>("poiptmax_", 3.0);

	fweight_ = iConfig.getUntrackedParameter<edm::InputTag>("fweight_", string("NA"));
	facceptance_ = iConfig.getUntrackedParameter<edm::InputTag>("facceptance_", string("NA"));
	charge_ = iConfig.getUntrackedParameter<int>("charge_", 0);
	bFak = iConfig.getUntrackedParameter<bool>("bFak_", false);
	bEff = iConfig.getUntrackedParameter<bool>("bEff_", false);
	bPhiEta = iConfig.getUntrackedParameter<bool>("bPhiEta_", false);
	bCentNoff = iConfig.getUntrackedParameter<bool>("bCentNoff_", false);
	bSim_ = iConfig.getUntrackedParameter<bool>("bSim_", false);
	Noffmin_ = iConfig.getUntrackedParameter<int>("Noffmin_", 0);
	Noffmax_ = iConfig.getUntrackedParameter<int>("Noffmax_", 5000);
	effCut_ = iConfig.getUntrackedParameter<double>("effCut_", -1.0);
	cmode_ = iConfig.getUntrackedParameter<int>("cmode_", 1);
	cweight_ = iConfig.getUntrackedParameter<int>("cweight_", 0);
	bGen_ = iConfig.getUntrackedParameter<bool>("bGen_", false);
	nvtx_ = iConfig.getUntrackedParameter<int>("nvtx_", 100);
	bFlipEta_ = iConfig.getUntrackedParameter<bool>("bFlipEta_", false);

	string streff = fweight_.label();
	if ( streff == string("NA") ) {
		bFak = false;
		bEff = false;
		fEffFak = 0;
	} else {
		fEffFak = new TFile(streff.c_str());
		if ( !fEffFak->IsOpen() ) {
			bFak = false;
			bEff = false;
		} else {
			cout << "!!! Using particle weight " << streff << endl;
			if ( bFak ) cout << "!!! Apply Fak correction" << endl;
			if ( bEff ) cout << "!!! Apply Eff correction" << endl;
			for ( int i = 0; i < 20; i++ ) {
				if ( streff == string("TrackCorrections_HIJING_538_OFFICIAL_Mar24.root") || streff == string("trkEff_pp_all_42X_origin.root") ) {
					hEff_cbin[i] = (TH2D*) fEffFak->Get("rTotalEff3D");
					hFak_cbin[i] = (TH2D*) fEffFak->Get(Form("rFak_cbin%i", i));
				}
				if ( streff == string("trkEffNew2012_HI_hiGoodTightMerged_xsec_smoothv5true.root") ) {
					hEff_cbin[i] = (TH2D*) fEffFak->Get("Tot_4");
					hFak_cbin[i] = (TH2D*) fEffFak->Get("Fak_4");
				}
			}
			cout << "!!! eff histo done" << endl;
		}
	}
	string stracc = facceptance_.label();
	if ( stracc == string("NA") ) {
		cout << "!!! acc NA" << endl;
		bacc = false;
		facc = 0;
	} else {
		facc = new TFile(stracc.c_str());
		if ( !facc->IsOpen() ) {
			bacc = false;
		} else {
			cout << "!!! Using acceptance weight " << stracc << endl;
			bacc = true;
			for ( int cent = 0; cent < nCentBins; cent++ ) {
				for ( int ipt = 0; ipt < nPtBins; ipt++ ) {
					hacc[cent][ipt][0] = (TH2D*) facc->Get(Form("hPhiEta_%i_%i_0", cent, ipt));
					hacc[cent][ipt][1] = (TH2D*) facc->Get(Form("hPhiEta_%i_%i_1", cent, ipt));
				}
			}
		}
	}

	if ( cweight_ == 0 || bEff == false ) {
		for ( int n = 1; n < 7; n++ ) {
			q[n] = correlations::QVector(0, 0, false);
		}
	}

	//
	//cout << __LINE__ << "\t" << tracks_.label().c_str() << "\t|" << tracks_.instance() << "\t|" << tracks_.process() << endl;
	//
	t = new QWEvent;
	memset(t, 0, sizeof(QWEvent));
	//
	edm::Service<TFileService> fs;
	for ( int cent = 0; cent < nCentBins; cent++ ) {
		hPt[cent] = fs->make<TH1D>(Form("hPt_%i", cent), "", 20000, 0, 100);
		if ( bPhiEta ) {
			for ( int i = 0; i < nPtBins; i++ ) {
				cout << "!! new histo cent = " << cent << " of " << nCentBins << "\t ipt = " << i  << " of " << nPtBins << endl;
				hPhiEta[cent][i][0] = fs->make<TH2D>(Form("hPhiEta_%i_%i_0", cent, i), "", 512, -Pi, Pi, 480, -2.4, 2.4);
				hPhiEta[cent][i][1] = fs->make<TH2D>(Form("hPhiEta_%i_%i_1", cent, i), "", 512, -Pi, Pi, 480, -2.4, 2.4);
			}
		}
	}
	for ( int cent = 0; cent < 20; cent++ ) {
		cout << "!! new histo cent = " << cent << endl;
		hdNdPtdEta[cent] = fs->make<TH2D>(Form("hdNdPtdEta_%i", cent), Form("hdNdPtdEta_%i", cent), nEtaBins, etabins, 38, fakpt );
		hdNdPtdEtaPt[cent] = fs->make<TH2D>(Form("hdNdPtdEtaPt_%i", cent), Form("hdNdPtdEta_%i", cent), nEtaBins, etabins, 38, fakpt );
	}


	trV = fs->make<TTree>("trV", "trV");
//		trV->SetAutoSave(10000000);
//		trV->SetAutoFlush(1000000);
	trV->Branch("Noff", &gNoff, "Noff/I");
	trV->Branch("Mult", &gMult, "Mult/I");

	for ( int n = 1; n < 7; n++ ) {
		for ( int np = 0; np < 4; np++ ) {
			trV->Branch(Form("rQ%i%i", n, 2+2*np), &rQ[n][np], Form("rQ%i%i/D", n, 2+2*np));
			trV->Branch(Form("iQ%i%i", n, 2+2*np), &iQ[n][np], Form("iQ%i%i/D", n, 2+2*np));
			trV->Branch(Form("wQ%i%i", n, 2+2*np), &wQ[n][np], Form("wQ%i%i/D", n, 2+2*np));

			trV->Branch(Form("rX%i%i", n, 2+2*np), &rX[n][np], Form("rX%i%i/D", n, 2+2*np));
			trV->Branch(Form("iX%i%i", n, 2+2*np), &iX[n][np], Form("iX%i%i/D", n, 2+2*np));
			trV->Branch(Form("wX%i%i", n, 2+2*np), &wX[n][np], Form("wX%i%i/D", n, 2+2*np));

			trV->Branch(Form("rQ%i%ic", n, 2+2*np), rQc[n][np], Form("rQ%i%ic[2]/D", n, 2+2*np));
			trV->Branch(Form("iQ%i%ic", n, 2+2*np), iQc[n][np], Form("iQ%i%ic[2]/D", n, 2+2*np));
			trV->Branch(Form("wQ%i%ic", n, 2+2*np), wQc[n][np], Form("wQ%i%ic[2]/D", n, 2+2*np));

			trV->Branch(Form("rQ%i%ip", n, 2+2*np), rQp[n][np], Form("rQ%i%ip[24]/D", n, 2+2*np));
			trV->Branch(Form("iQ%i%ip", n, 2+2*np), iQp[n][np], Form("iQ%i%ip[24]/D", n, 2+2*np));
			trV->Branch(Form("wQ%i%ip", n, 2+2*np), wQp[n][np], Form("wQ%i%ip[24]/D", n, 2+2*np));

			trV->Branch(Form("rQ%i%ieta", n, 2+2*np), rQeta[n][np], Form("rQ%i%ieta[24]/D", n, 2+2*np));
			trV->Branch(Form("iQ%i%ieta", n, 2+2*np), iQeta[n][np], Form("iQ%i%ieta[24]/D", n, 2+2*np));
			trV->Branch(Form("wQ%i%ieta", n, 2+2*np), wQeta[n][np], Form("wQ%i%ieta[24]/D", n, 2+2*np));
		}
	}

	initQ();

//	cout << cq2->name() << endl;
//	ntResult = new TNtupleD("ntResult",cq2->name(),"Noff:Mult:Cent:C22:C24:C26:C28:iC22:iC24:iC26:iC28:wC22:wC24:wC26:wC28:C32:C34:C36:C38:iC32:iC34:iC36:iC38:wC32:wC34:wC36:wC38");
//	ntResult = fs->make<TNtupleD>("ntResult",cq2->name(),"Noff:Mult:Cent:C22:C24:C26:C28:iC22:iC24:iC26:iC28:wC22:wC24:wC26:wC28:C32:C34:C36:C38:iC32:iC34:iC36:iC38:wC32:wC34:wC36:wC38");
//	ntResult->SetAutoFlush(-3000000);
//	ntResult->SetAutoSave(-30000000);

//	cout << "!! initQ" << endl;
}


QWCumuV3::~QWCumuV3()
{

	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

int
QWCumuV3::getNoffCent(const edm::Event& iEvent, const edm::EventSetup& iSetup, int& Noff)
{
	// very hard coded Noff track centrality cut
	using namespace edm;
	using namespace reco;
//	int Noff = 0;

	Handle<VertexCollection> vertexCollection;
	iEvent.getByLabel(vertexSrc_, vertexCollection);
	const VertexCollection * recoVertices = vertexCollection.product();

	int primaryvtx = 0;
	math::XYZPoint v1( (*recoVertices)[primaryvtx].position().x(), (*recoVertices)[primaryvtx].position().y(), (*recoVertices)[primaryvtx].position().z() );
	double vxError = (*recoVertices)[primaryvtx].xError();
	double vyError = (*recoVertices)[primaryvtx].yError();
	double vzError = (*recoVertices)[primaryvtx].zError();


	Handle<TrackCollection> tracks;
	iEvent.getByLabel(tracks_,tracks);
	for(TrackCollection::const_iterator itTrack = tracks->begin();
		itTrack != tracks->end();                      
		++itTrack) {

		if ( !itTrack->quality(reco::TrackBase::highPurity) ) continue;
		if ( itTrack->charge() == 0 ) continue;
		if ( itTrack->pt() < 0.4 ) continue;

		double d0 = -1.* itTrack->dxy(v1);
		double derror=sqrt(itTrack->dxyError()*itTrack->dxyError()+vxError*vyError);
		double dz=itTrack->dz(v1);
		double dzerror=sqrt(itTrack->dzError()*itTrack->dzError()+vzError*vzError);
		if ( fabs(itTrack->eta()) > 2.4 ) continue;
		if ( fabs( dz/dzerror ) > 3. ) continue;
		if ( fabs( d0/derror ) > 3. ) continue;
		if ( itTrack->ptError()/itTrack->pt() > 0.1 ) continue;
//		bool b_pix = itTrack->numberOfValidHits() < 7;
//		if ( b_pix ) {
//			if ( fabs( dz/dzerror ) > dzdzerror_ ) continue;
//			if ( itTrack->normalizedChi2() > chi2_ ) continue;
//		} else {
//			// full track
//			if ( fabs( dz/dzerror ) > 3. ) continue;
//			if ( fabs( d0/derror ) > 3. ) continue;
//			if ( itTrack->ptError()/itTrack->pt() > pterrorpt_ ) continue;
//			if ( itTrack->numberOfValidHits() < 12 ) continue;
//		}

		Noff++;
	}

	int cent = nCentNoff-1;
	while ( CentNoffCut[cent] <= Noff ) cent--;
	return cent;
}


void
QWCumuV3::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	if ( bGen_ ) analyzeGen(iEvent, iSetup);
	else analyzeData(iEvent, iSetup);
	if ( t->Mult == 0 ) return;

	for ( int n = 0; n < 7; n++ ) {
		for ( int np = 0; np < 4; np++ ) {
			rQ[n][np] = 0;
			iQ[n][np] = 0;
			wQ[n][np] = 0;
			rX[n][np] = 0;
			iX[n][np] = 0;
			wX[n][np] = 0;

			rQc[n][np][0] = 0;
			iQc[n][np][0] = 0;
			wQc[n][np][0] = 0;
			rQc[n][np][1] = 0;
			iQc[n][np][1] = 0;
			wQc[n][np][1] = 0;

			for ( int j = 0; j < 24; j++ ) {
				rQp[n][np][j] = 0;
				iQp[n][np][j] = 0;
				wQp[n][np][j] = 0;

				rQeta[n][np][j] = 0;
				iQeta[n][np][j] = 0;
				wQeta[n][np][j] = 0;
			}
		}
	}

	for ( int i = 0; i < t->Mult; i++ ) {
		if ( t->RFP[i] != 1 ) continue;
		for ( int n = 1; n < 7; n++ ) {
			q[n].fill(t->Phi[i], t->weight[i]);
		}
	}

	correlations::Result r[7][4];
	for ( int n = 1; n < 7; n++ ) {
		for ( int np = 0; np < 4; np++ ) {
			r[n][np] = cq[n]->calculate(2+2*np, hc[n]);
		}
	}

	// RFP
	for ( int n = 1; n < 7; n++ ) {
		for ( int np = 0; np < 4; np++ ) {
			rQ[n][np] = r[n][np].sum().real();
			iQ[n][np] = r[n][np].sum().imag();
			wQ[n][np] = r[n][np].weight();
		}
	}

	for ( int n = 1; n < 7; n++ ) {
		for ( int np = 0; np < 4; np++ ) {
			// cross check
			correlations::Complex qp = 0;
			double wt = 0;
			for ( int i = 0; i < t->Mult; i++ ) {
				if ( !t->RFP[i] ) continue;
				correlations::QVector tq = q[n];
				tq.unfill(t->Phi[i], t->weight[i]);
				correlations::FromQVector *cq = 0;
				switch ( cmode_ ) {
					case 1:
						cq = new correlations::closed::FromQVector(tq);
						break;
					case 2:
						cq = new correlations::recurrence::FromQVector(tq);
						break;
					case 3:
						cq = new correlations::recursive::FromQVector(tq);
						break;
				}
				correlations::Result r = cq->calculate(np*2+1, hc[n]);
				qp += t->weight[i] * correlations::Complex( TMath::Cos(t->Phi[i] * n) , TMath::Sin(t->Phi[i] * n) ) * r.sum();
				wt += t->weight[i] * r.weight();
				delete cq;
			}
			rX[n][np] = qp.real();
			iX[n][np] = qp.imag();
			wX[n][np] = wt;

			// pt differential
			for ( int ipt = 0; ipt < nPtBins; ipt++ ) {
				qp = 0;
				wt = 0;
				for ( int i = 0; i < t->Mult; i++ ) {
					if ( t->Eta[i] < poimineta_ or t->Eta[i] > poimaxeta_ ) continue;
					if ( t->Pt[i] < ptbins[ipt] || t->Pt[i] > ptbins[ipt+1] ) continue;
					correlations::QVector tq = q[n];
					if ( t->RFP[i] ) tq.unfill(t->Phi[i], t->weight[i]);
					correlations::FromQVector *cq = 0;
					switch ( cmode_ ) {
						case 1:
							cq = new correlations::closed::FromQVector(tq);
							break;
						case 2:
							cq = new correlations::recurrence::FromQVector(tq);
							break;
						case 3:
							cq = new correlations::recursive::FromQVector(tq);
							break;
					}
					correlations::Result r = cq->calculate(np*2+1, hc[n]);
					qp += t->weight[i] * correlations::Complex( TMath::Cos(t->Phi[i] * n) , TMath::Sin(t->Phi[i] * n) ) * r.sum();
					wt += t->weight[i] * r.weight();
//					if ( n == 2 && np == 1 ) {
//						cout << "!!! ipt = " << ipt << "\ti = " << i << "\twt = " << wt << "\tr.sum() = " << r.sum() << "\tr.weight() = " << r.weight() << "\tqp = " << qp << endl;
//					}
					delete cq;
				}
				rQp[n][np][ipt] = qp.real();
				iQp[n][np][ipt] = qp.imag();
				wQp[n][np][ipt] = wt;
			}
			// eta differential
			for ( int ieta = 0; ieta < nEtaBins; ieta++ ) {
				qp = 0;
				wt = 0;
				for ( int i = 0; i < t->Mult; i++ ) {
					if ( t->Pt[i] < poiptmin_ or t->Pt[i] > poiptmax_ ) continue;
					if ( t->Eta[i] < etabins[ieta] || t->Eta[i] > etabins[ieta+1] || t->RFP[i] != 1 ) continue;
					correlations::QVector tq = q[n];
					tq.unfill(t->Phi[i], t->weight[i]);
					correlations::FromQVector *cq = 0;
					switch ( cmode_ ) {
						case 1:
							cq = new correlations::closed::FromQVector(tq);
							break;
						case 2:
							cq = new correlations::recurrence::FromQVector(tq);
							break;
						case 3:
							cq = new correlations::recursive::FromQVector(tq);
							break;
					}
					correlations::Result r = cq->calculate(np*2+1, hc[n]);
					qp += t->weight[i] * correlations::Complex( TMath::Cos(t->Phi[i] * n) , TMath::Sin(t->Phi[i] * n) ) * r.sum();
					wt += t->weight[i] * r.weight();
					delete cq;
				}
				rQeta[n][np][ieta] = qp.real();
				iQeta[n][np][ieta] = qp.imag();
				wQeta[n][np][ieta] = wt;
			}
	
			// charge - differential
			for ( int i = 0; i < t->Mult; i++ ) {
				qp = 0;
				wt = 0;
				if ( t->Charge[i] > 0 || t->RFP[i] != 1 ) continue;
				correlations::QVector tq = q[n];
				tq.unfill(t->Phi[i], t->weight[i]);
				correlations::FromQVector *cq = 0;
				switch ( cmode_ ) {
					case 1:
						cq = new correlations::closed::FromQVector(tq);
						break;
					case 2:
						cq = new correlations::recurrence::FromQVector(tq);
						break;
					case 3:
						cq = new correlations::recursive::FromQVector(tq);
						break;
				}
				correlations::Result r = cq->calculate(np*2+1, hc[n]);
				qp += t->weight[i] * correlations::Complex( TMath::Cos(t->Phi[i] * n) , TMath::Sin(t->Phi[i] * n) ) * r.sum();
				wt += t->weight[i] * r.weight();
				delete cq;
			}
			rQc[n][np][0] = qp.real();
			iQc[n][np][0] = qp.imag();
			wQc[n][np][0] = wt;

			// charge + differential
			qp = 0;
			wt = 0;
			for ( int i = 0; i < t->Mult; i++ ) {
				if ( t->Charge[i] < 0 || t->RFP[i] != 1 ) continue;
				correlations::QVector tq = q[n];
				tq.unfill(t->Phi[i], t->weight[i]);
				correlations::FromQVector *cq = 0;
				switch ( cmode_ ) {
					case 1:
						cq = new correlations::closed::FromQVector(tq);
						break;
					case 2:
						cq = new correlations::recurrence::FromQVector(tq);
						break;
					case 3:
						cq = new correlations::recursive::FromQVector(tq);
						break;
				}
				correlations::Result r = cq->calculate(np*2+1, hc[n]);
				qp += t->weight[i] * correlations::Complex( TMath::Cos(t->Phi[i] * n) , TMath::Sin(t->Phi[i] * n) ) * r.sum();
				wt += t->weight[i] * r.weight();
				delete cq;
			}
			rQc[n][np][1] = qp.real();
			iQc[n][np][1] = qp.imag();
			wQc[n][np][1] = wt;
		}
	}

	gNoff = t->Noff;
	gMult = t->Mult;
	trV->Fill();

	doneQ();

}


void
QWCumuV3::analyzeGen(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	using namespace reco;

	t->Mult = 0;
	// track
	Handle< std::vector<GenParticle> > tracks;
	iEvent.getByLabel(tracks_,tracks);
	t->Noff = 0;
	for ( std::vector<GenParticle>::const_iterator itTrack = tracks->begin();
			itTrack != tracks->end();
			++itTrack
			)
	{
		if ( itTrack->status()!=1 ) continue;
		if ( itTrack->charge() == 0 ) continue;
		if ( fabs(itTrack->eta()) > 2.4 ) continue;
		if ( itTrack->pt() < 0.4 ) continue;
		t->Noff++;
	}
	t->Cent = 0;
	for ( std::vector<GenParticle>::const_iterator itTrack = tracks->begin();
			itTrack != tracks->end();
			++itTrack
			)
	{
		if ( itTrack->status()!=1 ) continue;
		if ( itTrack->charge() == 0 ) continue;
		if ( fabs(itTrack->eta()) > 2.4 ) continue;
		t->Pt[t->Mult] = itTrack->pt();
		t->Charge[t->Mult] = itTrack->charge();
		t->Eta[t->Mult] = itTrack->eta();
		if (bFlipEta_) t->Eta[t->Mult] = - t->Eta[t->Mult];

		if ( (t->Pt[t->Mult] > rfpptmin_) && (t->Pt[t->Mult] < rfpptmax_) && t->Eta[t->Mult] > rfpmineta_ && t->Eta[t->Mult] < rfpmaxeta_ ) {
			t->RFP[t->Mult] = 1;
		} else {
			t->RFP[t->Mult] = 0;
		}

		t->weight[t->Mult] = 1.;
		t->Phi[t->Mult] = itTrack->phi();

		t->Mult++;
	}
}


// ------------ method called for each event  ------------
	void
QWCumuV3::analyzeData(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;
	using namespace reco;

	t->Mult = 0;
	// vertex
	Handle<VertexCollection> vertexCollection;
	iEvent.getByLabel(vertexSrc_, vertexCollection);
	const VertexCollection * recoVertices = vertexCollection.product();
	if ( recoVertices->size() > nvtx_ ) return;

	int primaryvtx = 0;
	math::XYZPoint v1( (*recoVertices)[primaryvtx].position().x(), (*recoVertices)[primaryvtx].position().y(), (*recoVertices)[primaryvtx].position().z() );
	double vxError = (*recoVertices)[primaryvtx].xError();
	double vyError = (*recoVertices)[primaryvtx].yError();
	double vzError = (*recoVertices)[primaryvtx].zError();

//	for ( unsigned int i = 0; i < recoVertices->size(); i++ ) {
//		size_t daughter = (*recoVertices)[i].tracksSize();
//		cout << "i = " << i << "\tnTracks = " << daughter <<"\t vz = " << (*recoVertices)[i].position().z() << endl;
//		//cout << "i = " << i << "\ttrkSize = " << "\t vz = " << (*recoVertices)[i].position().z() << endl;
//	}
	double vz = (*recoVertices)[primaryvtx].z();
	if (fabs(vz) < minvz_ || fabs(vz) > maxvz_) {
		return;
	}
	
	// centrality
	int bin = 0;
	int cbin = 0;
	t->Noff = 0;

	if ( bCentNoff ) {
		cbin = getNoffCent( iEvent, iSetup, t->Noff);
		if ( (t->Noff < Noffmin_) or (t->Noff >= Noffmax_) ) {
			return;
		}
	} else {
		edm::Handle<int> ch;
		iEvent.getByLabel(centrality_,ch);
		bin = *(ch.product());
		while ( centbins[cbin+1] < bin*2.5+0.1 ) cbin++;
	}
	bin = cbin;

	// track
	Handle<TrackCollection> tracks;
	iEvent.getByLabel(tracks_,tracks);
	t->Cent = bin;
	t->vz = vz;
	//cout << __LINE__ << "\t" << bin << endl;

	for(TrackCollection::const_iterator itTrack = tracks->begin();
			itTrack != tracks->end();                      
			++itTrack) {
//		cout << "!!! " << __LINE__ << endl;
		if ( itTrack->charge() == 0 ) continue;
		if ( !itTrack->quality(reco::TrackBase::highPurity) ) continue;

//		cout << "!!! " << __LINE__ << endl;
		double d0 = -1.* itTrack->dxy(v1);
		double derror=sqrt(itTrack->dxyError()*itTrack->dxyError()+vxError*vyError);
		double dz=itTrack->dz(v1);
		double dzerror=sqrt(itTrack->dzError()*itTrack->dzError()+vzError*vzError);

//		cout << "!!! " << __LINE__ << endl;
		if ( fabs(itTrack->eta()) > 2.4 ) continue;
		if ( fabs( dz/dzerror ) > dzdzerror_ ) continue;
		if ( fabs( d0/derror ) > d0d0error_ ) continue;
		if ( itTrack->ptError()/itTrack->pt() > pterrorpt_ ) continue;

		t->RFP[t->Mult] = 1;
//		cout << "!!! " << __LINE__ << endl;
		t->Charge[t->Mult] = itTrack->charge();
		if ( (charge_ == 1) && (t->Charge[t->Mult]<0) ) {
			t->RFP[t->Mult] = 0;
		}
		if ( (charge_ == -1) && (t->Charge[t->Mult]>0) ) {
			t->RFP[t->Mult] = 0;
		}

//		cout << "!!! " << __LINE__ << endl;
		t->Pt[t->Mult] = itTrack->pt();
		if ( t->Pt[t->Mult] >= ptbins[nPtBins] || t->Pt[t->Mult] <= ptbins[0] ) {
			t->RFP[t->Mult] = 0;
		}
		t->Eta[t->Mult] = itTrack->eta();
		if (bFlipEta_) t->Eta[t->Mult] = - t->Eta[t->Mult];

		if (effCut_>0.)  {
			double eff = hEff_cbin[bin]->GetBinContent( hEff_cbin[bin]->FindBin(t->Eta[t->Mult], t->Pt[t->Mult] ) ) ;
			if ( eff > effCut_ ) {
				if ( gRandom->Rndm() < (eff-effCut_)/eff ) {
					t->RFP[t->Mult] = 0;
				}
			}
		}

		if ( bEff ) {
			t->rEff[t->Mult] = hEff_cbin[bin]->GetBinContent( hEff_cbin[bin]->FindBin(t->Eta[t->Mult], t->Pt[t->Mult] ) );
		} else {
			t->rEff[t->Mult] = 1.;
		}
		if ( bFak ) {
			t->rFak[t->Mult] = hFak_cbin[bin]->GetBinContent( hFak_cbin[bin]->FindBin(t->Eta[t->Mult], t->Pt[t->Mult] ) );
		} else {
			t->rFak[t->Mult] = 0.;
		}
		if ( t->rEff[t->Mult] <= 0.1 or TMath::IsNaN(t->rEff[t->Mult]) ) {
			t->RFP[t->Mult] = 0;
		}
		double weight = (1.-t->rFak[t->Mult])/t->rEff[t->Mult];

		double phi = itTrack->phi();

		double wacc = 1.;
		int ipt=0;
		while ( t->Pt[t->Mult] > ptbins[ipt+1] ) ipt++;
		if ( bacc ) {
			wacc = 1./hacc[t->Cent][ipt][t->Charge[t->Mult]>0]->GetBinContent(hacc[t->Cent][ipt][t->Charge[t->Mult]>0]->FindBin(phi, t->Eta[t->Mult]));
		}
		if ( bPhiEta ) hPhiEta[t->Cent][ipt][t->Charge[t->Mult]>0]->Fill(phi, t->Eta[t->Mult], wacc);

		weight *= wacc;

		if ( (t->Pt[t->Mult] < rfpptmin_) || (t->Pt[t->Mult] > rfpptmax_) || itTrack->eta() < rfpmineta_ || itTrack->eta() > rfpmaxeta_ ) {
			t->RFP[t->Mult] = 0;
		}

		t->weight[t->Mult] = weight;

		hdNdPtdEta[bin]->Fill(t->Eta[t->Mult], t->Pt[t->Mult]);
		hdNdPtdEtaPt[bin]->Fill(t->Eta[t->Mult], t->Pt[t->Mult], t->Pt[t->Mult]);

		t->Phi[t->Mult] = phi;
		hPt[t->Cent]->Fill(t->Pt[t->Mult]);

		t->Mult++;
	}
	if ( bSim_ ) Sim();
}


void
QWCumuV3::initQ()
{
	hc[1] = correlations::HarmonicVector(8);
	hc[1][0] = -1;
	hc[1][1] =  1;
	hc[1][2] = -1;
	hc[1][3] =  1;
	hc[1][4] = -1;
	hc[1][5] =  1;
	hc[1][6] = -1;
	hc[1][7] =  1;

	hc[2] = correlations::HarmonicVector(8);
	hc[2][0] = -2;
	hc[2][1] =  2;
	hc[2][2] = -2;
	hc[2][3] =  2;
	hc[2][4] = -2;
	hc[2][5] =  2;
	hc[2][6] = -2;
	hc[2][7] =  2;

	hc[3] = correlations::HarmonicVector(8);
	hc[3][0] = -3;
	hc[3][1] =  3;
	hc[3][2] = -3;
	hc[3][3] =  3;
	hc[3][4] = -3;
	hc[3][5] =  3;
	hc[3][6] = -3;
	hc[3][7] =  3;

	hc[4] = correlations::HarmonicVector(8);
	hc[4][0] = -4;
	hc[4][1] =  4;
	hc[4][2] = -4;
	hc[4][3] =  4;
	hc[4][4] = -4;
	hc[4][5] =  4;
	hc[4][6] = -4;
	hc[4][7] =  4;

	hc[5] = correlations::HarmonicVector(8);
	hc[5][0] = -5;
	hc[5][1] =  5;
	hc[5][2] = -5;
	hc[5][3] =  5;
	hc[5][4] = -5;
	hc[5][5] =  5;
	hc[5][6] = -5;
	hc[5][7] =  5;

	hc[6] = correlations::HarmonicVector(8);
	hc[6][0] = -6;
	hc[6][1] =  6;
	hc[6][2] = -6;
	hc[6][3] =  6;
	hc[6][4] = -6;
	hc[6][5] =  6;
	hc[6][6] = -6;
	hc[6][7] =  6;



	q[1].resize(hc[1]);
	q[2].resize(hc[2]);
	q[3].resize(hc[3]);
	q[4].resize(hc[4]);
	q[5].resize(hc[5]);
	q[6].resize(hc[6]);
	switch ( cmode_ ) {
		case 1:
			cq[1] = new correlations::closed::FromQVector(q[1]);
			cq[2] = new correlations::closed::FromQVector(q[2]);
			cq[3] = new correlations::closed::FromQVector(q[3]);
			cq[4] = new correlations::closed::FromQVector(q[4]);
			cq[5] = new correlations::closed::FromQVector(q[5]);
			cq[6] = new correlations::closed::FromQVector(q[6]);
			break;
		case 2:
			cq[1] = new correlations::recurrence::FromQVector(q[1]);
			cq[2] = new correlations::recurrence::FromQVector(q[2]);
			cq[3] = new correlations::recurrence::FromQVector(q[3]);
			cq[4] = new correlations::recurrence::FromQVector(q[4]);
			cq[5] = new correlations::recurrence::FromQVector(q[5]);
			cq[6] = new correlations::recurrence::FromQVector(q[6]);
			break;
		case 3:
			cq[1] = new correlations::recursive::FromQVector(q[1]);
			cq[2] = new correlations::recursive::FromQVector(q[2]);
			cq[3] = new correlations::recursive::FromQVector(q[3]);
			cq[4] = new correlations::recursive::FromQVector(q[4]);
			cq[5] = new correlations::recursive::FromQVector(q[5]);
			cq[6] = new correlations::recursive::FromQVector(q[6]);
			break;
	}
}

void
QWCumuV3::doneQ()
{
	q[1].reset();
	q[2].reset();
	q[3].reset();
	q[4].reset();
	q[5].reset();
	q[6].reset();
}

void
QWCumuV3::Sim()
{
//	if ( t->Mult == 0 ) {
//		cout << "!!! Evt skipped" << endl;
//		return;
//	}

	cout << "!!! in the Sim" << endl;

	t->Mult = 10;
	for ( int i = 0; i < t->Mult; i++ ) {
		t->Phi[i] = 0.3*i;
		t->Eta[i] = 0.1;
		if ( i < 5 ) {
			t->Pt[i] = 0.4;
			t->RFP[i] = 1;
		}
		else {
			t->Pt[i] = 0.2;
			t->RFP[i] = 0;
		}
		t->weight[i] = 1.;
	}
//	t->RFP[4] = 0;
	t->Pt[4] = 1.;
	int n = 2;
	int ipt = 1;
	correlations::Complex Q = 0;
	correlations::Complex W = 0;
	correlations::Complex Qp = 0;
	correlations::Complex Wp = 0;
	for ( int i = 0; i < t->Mult; i++ ) {
		if (!t->RFP[i] ) continue;
		for ( int j = 0; j < t->Mult; j++ ) {
			if ( !t->RFP[j] || j == i ) continue;
			for ( int k = 0; k < t->Mult; k++ ) {
				if ( !t->RFP[k] || k == j || k == i ) continue;
				for ( int l = 0; l < t->Mult; l++ ) {
					if ( !t->RFP[l] || l == k || l == j || l == i ) continue;
					correlations::Complex tq = ( correlations::Complex( TMath::Cos(t->Phi[i]*(-n)), TMath::Sin(t->Phi[i]*(-n)) ) *
						correlations::Complex( TMath::Cos(t->Phi[j]*n), TMath::Sin(t->Phi[j]*n) ) * 
						correlations::Complex( TMath::Cos(t->Phi[k]*(-n)), TMath::Sin(t->Phi[k]*(-n)) ) * 
						correlations::Complex( TMath::Cos(t->Phi[l]*n), TMath::Sin(t->Phi[l]*n) )
					     );
					double w = t->weight[i] * t->weight[j] * t->weight[k] * t->weight[l];
					Q += w*tq;
					W += w;
					cout << i << "\t" << j << "\t" << k << "\t" << l << endl;
				}
				for ( int l = 0; l < t->Mult; l++ ) {
					if ( t->Pt[l] < ptbins[ipt] || t->Pt[l] > ptbins[ipt+1] || l == k || l == j || l == i ) continue;
					correlations::Complex tq = ( correlations::Complex( TMath::Cos(t->Phi[i]*(-n)), TMath::Sin(t->Phi[i]*(-n)) ) *
						correlations::Complex( TMath::Cos(t->Phi[j]*n), TMath::Sin(t->Phi[j]*n) ) * 
						correlations::Complex( TMath::Cos(t->Phi[k]*(-n)), TMath::Sin(t->Phi[k]*(-n)) ) * 
						correlations::Complex( TMath::Cos(t->Phi[l]*n), TMath::Sin(t->Phi[l]*n) )
					     );
					double w = t->weight[i] * t->weight[j] * t->weight[k] * t->weight[l];
					Qp += w*tq;
					Wp += w;
				}
			}
		}
	}


	cout << "!!! Ref Q = " << Q << "\tW = " << W << "\tQp = " << Qp << "\tWp = " << Wp << endl;

}

// ------------ method called once each job just before starting event loop  ------------
	void 
QWCumuV3::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
	void 
QWCumuV3::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
	void 
QWCumuV3::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
	void 
QWCumuV3::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
	void 
QWCumuV3::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
	void 
QWCumuV3::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
QWCumuV3::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
	//The following says we do not know what parameters are allowed so do no validation
	// Please change this to state exactly what you do use, even if it is no parameters
	edm::ParameterSetDescription desc;
	desc.setUnknown();
	descriptions.addDefault(desc);

	//Specify that only 'tracks' is allowed
	//To use, remove the default given above and uncomment below
	//ParameterSetDescription desc;
	//desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
	//descriptions.addDefault(desc);
}

//////////////////////////////////////////


//define this as a plug-in
DEFINE_FWK_MODULE(QWCumuV3);
