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
#include <algorithm>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h>
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HeavyIonEvent/interface/EvtPlane.h"
#include "TH1.h"
#include "TH2.h"
#include "TNtuple.h"
#include "TComplex.h"
#include <complex>


#include "QWAna/QWCumuV3/interface/QWCumuV3.h"


using namespace std;

//#ifdef QW_DEBUG
//
// constructors and destructor
//
QWCumuV3::QWCumuV3(const edm::ParameterSet& iConfig):
	trackEta_( iConfig.getUntrackedParameter<edm::InputTag>("trackEta") ),
	trackPhi_( iConfig.getUntrackedParameter<edm::InputTag>("trackPhi") ),
	trackWeight_( iConfig.getUntrackedParameter<edm::InputTag>("trackWeight") ),
	trackCharge_( iConfig.getUntrackedParameter<edm::InputTag>("trackCharge") ),
	vertexZ_( iConfig.getUntrackedParameter<edm::InputTag>("vertexZ") ),
	centralityTag_( iConfig.getUntrackedParameter<edm::InputTag>("centrality") )
{
	//now do what ever initialization is needed
	minvz_ = iConfig.getUntrackedParameter<double>("minvz", -15.);
	maxvz_ = iConfig.getUntrackedParameter<double>("maxvz", 15.);

	rfpmineta_ = iConfig.getUntrackedParameter<double>("rfpmineta", -2.4);
	rfpmaxeta_ = iConfig.getUntrackedParameter<double>("rfpmaxeta", 2.4);
	rfpminpt_ = iConfig.getUntrackedParameter<double>("rfpminpt", 0.3);
	rfpmaxpt_ = iConfig.getUntrackedParameter<double>("rfpmaxpt", 100);

	poimineta_ = iConfig.getUntrackedParameter<double>("poimineta", -2.4);
	poimaxeta_ = iConfig.getUntrackedParameter<double>("poimaxeta", 2.4);
	poiminpt_ = iConfig.getUntrackedParameter<double>("poiminpt", 0.3);
	poimaxpt_ = iConfig.getUntrackedParameter<double>("poimaxpt", 3.0);

	b2PartGap_ = iConfig.getUntrackedParameter<bool>("b2PartGap", true);
	dEtaGap_ = iConfig.getUntrackedParameter<double>("etaGap", 2.);

	cmode_ = iConfig.getUntrackedParameter<int>("cmode", 1);
	nvtx_ = iConfig.getUntrackedParameter<int>("nvtx", 100);

	for ( int n = 1; n < 7; n++ ) {
		q[n] = correlations::QVector(0, 0, true);
	}

	//
	//cout << __LINE__ << "\t" << tracks_.label().c_str() << "\t|" << tracks_.instance() << "\t|" << tracks_.process() << endl;
	//
	edm::Service<TFileService> fs;

	trV = fs->make<TTree>("trV", "trV");
	trV->Branch("Noff", &gNoff, "Noff/I");
	trV->Branch("Mult", &gMult, "Mult/I");

	trV->Branch("wQGap22", &wQGap[2], "wQGap22/D");
	trV->Branch("wQpGap22", wQpGap[2], "wQpGap22[24]/D");
	trV->Branch("wQetaGap22", wQetaGap[2], "wQetaGap22[24]/D");
	trV->Branch("wQcGap22", wQcGap[2], "wQcGap22[2]/D");


	for ( int n = 2; n < 7; n++ ) {
		trV->Branch(Form("rQGap%i%i", n, 2), &rQGap[n], Form("rQGap%i%i/D", n, 2));
		trV->Branch(Form("rQpGap%i%i", n, 2), rQpGap[n], Form("rQpGap%i%i[24]/D", n, 2));
		trV->Branch(Form("rQetaGap%i%i", n, 2), rQetaGap[n], Form("rQetaGap%i%i[24]/D", n, 2));
		trV->Branch(Form("rQcGap%i%i", n, 2), rQcGap[n], Form("rQcGap%i%i[2]/D", n, 2));
	}

	for ( int np = 0; np < 4; np++ ) {
		for ( int n = 2; n < 7; n++ ) {
			trV->Branch(Form("rQ%i%i", n, 2+2*np), &rQ[n][np], Form("rQ%i%i/D", n, 2+2*np));
			trV->Branch(Form("rX%i%i", n, 2+2*np), &rX[n][np], Form("rX%i%i/D", n, 2+2*np));
			trV->Branch(Form("rQ%i%ic", n, 2+2*np), rQc[n][np], Form("rQ%i%ic[2]/D", n, 2+2*np));
			trV->Branch(Form("rQ%i%ip", n, 2+2*np), rQp[n][np], Form("rQ%i%ip[24]/D", n, 2+2*np));
			trV->Branch(Form("rQ%i%ieta", n, 2+2*np), rQeta[n][np], Form("rQ%i%ieta[24]/D", n, 2+2*np));
		}

		int n = 2;
		trV->Branch(Form("wQ%i%i", n, 2+2*np), &wQ[n][np], Form("wQ%i%i/D", n, 2+2*np));
		trV->Branch(Form("wX%i%i", n, 2+2*np), &wX[n][np], Form("wX%i%i/D", n, 2+2*np));
		trV->Branch(Form("wQ%i%ic", n, 2+2*np), wQc[n][np], Form("wQ%i%ic[2]/D", n, 2+2*np));
		trV->Branch(Form("wQ%i%ip", n, 2+2*np), wQp[n][np], Form("wQ%i%ip[24]/D", n, 2+2*np));
		trV->Branch(Form("wQ%i%ieta", n, 2+2*np), wQeta[n][np], Form("wQ%i%ieta[24]/D", n, 2+2*np));
	}

	initQ();
}


QWCumuV3::~QWCumuV3()
{

	// do anything here that needs to be done at desctruction time
	// (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

void
QWCumuV3::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
//	analyzeData(iEvent, iSetup);

	Handle<std::vector<double> >	hEta;
	Handle<std::vector<double> >	hPhi;
	Handle<std::vector<double> >	hPt;
	Handle<std::vector<double> >	hWeight;
	Handle<std::vector<double> >	hCharge;
	Handle<std::vector<double> >	hVz;

	iEvent.getByLabel(trackEta_,	hEta);
	iEvent.getByLabel(trackPhi_,	hPhi);
	iEvent.getByLabel(trackPt_,	hPt);
	iEvent.getByLabel(trackWeight_, hWeight);
	iEvent.getByLabel(trackCharge_, hCharge);
	iEvent.getByLabel(vertexZ_, 	hVz);

	unsigned int sz = hEta->size();
	if ( sz == 0 ) return;

	std::vector<int>	RFP;
	RFP.reserve(sz);
	for ( int i = 0; i < sz; i++ ) {
		if ( hEta[i] < rfpmaxeta_ and hEta[i] > rfpmineta_
		and hPt[i] < rfpmaxpt_ and hPt[i] > rfpminpt_ ) {
			RFP[i] = 1;
		} else {
			RFP[i] = 0;
		}
	}

	for ( int n = 0; n < 7; n++ ) {
		rQGap[n] = 0;
		wQGap[n] = 0;
		rQcGap[n][0] = 0;
		wQcGap[n][0] = 0;
		rQcGap[n][1] = 0;
		wQcGap[n][1] = 0;

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
		for ( int j = 0; j < 24; j++ ) {
			rQpGap[n][j] = 0;
			wQpGap[n][j] = 0;
			rQetaGap[n][j] = 0;
			wQetaGap[n][j] = 0;
		}
	}

	for ( int i = 0; i < sz; i++ ) {
		if ( RFP[i] != 1 ) continue;
		for ( int n = 1; n < 7; n++ ) {
			q[n].fill(hPhi[i], hWeight[i]);
		}
	}
	if ( b2PartGap_ ) {
		for ( int i = 0; i < sz; i++ ) {
			if ( RFP[i] != 1 ) continue;
			for ( int n = 1; n < 7; n++ ) {
				// ref 2part gap
				for ( int j = i+1; j < sz; j++ ) {
					if ( RFP[j] != 1 ) continue;
					if ( fabs(hEta[i] - hEta[j]) < dEtaGap_ ) continue;
					rQGap[n] += cos( n*( hPhi[j] - hPhi[i] ) ) * hWeight[i] * hWeight[j];
					wQGap[n] += hWeight[i] * hWeight[j];
				}
			}
		}
		for ( int i = 0; i < sz; i++ ) {
			if ( RFP[i] != 1 ) continue;
			for ( int n = 1; n < 7; n++ ) {
				for ( int j = 0; j < sz; j++ ) {
					if ( j == i ) continue;
					if ( fabs(hEta[i] - hEta[j]) < dEtaGap_ ) continue;
					if ( hEta[j] < rfpmineta_ or hEta[j] > rfpmaxeta_ ) continue;
					if ( hPt[j] < poiptmin_ or hPt[j] > poiptmax_ ) continue;
					int ipt = 0;
					while ( hPt[j] > ptbins[ipt+1] ) ipt++;
					rQpGap[n][ipt] += cos( n*( hPhi[j] - hPhi[i] ) ) * hWeight[i] * hWeight[j];
					wQpGap[n][ipt] += hWeight[i] * hWeight[j];
				}
				for ( int j = 0; j < sz; j++ ) {
					if ( j == i ) continue;
					if ( fabs(hEta[i] - hEta[j]) < dEtaGap_ ) continue;
					if ( hEta[j] < -2.4 or hEta[j] > 2.4 ) continue;
					if ( hPt[j] < rfpptmin_ or hPt[j] > rfpptmax_ ) continue;
					int ieta = 0;
					while ( hEta[j] > etabins[ieta+1] ) ieta++;
					rQetaGap[n][ieta] += cos( n*( hPhi[j] - hPhi[i] ) ) * hWeight[i] * hWeight[j];
					wQetaGap[n][ieta] += hWeight[i] * hWeight[j];
				}
				for ( int j = 0; j < sz; j++ ) {
					if ( j == i ) continue;
					if ( RFP[j] != 1) continue;
					if ( fabs(hEta[i] - hEta[j]) < dEtaGap_ ) continue;

					if ( hCharge[j] < 0 ) {
						rQcGap[n][0] += cos( n*( hPhi[j] - hPhi[i] ) ) * hWeight[i] * hWeight[j];
						wQcGap[n][0] += hWeight[i] * hWeight[j];
					} else {
						rQcGap[n][1] += cos( n*( hPhi[j] - hPhi[i] ) ) * hWeight[i] * hWeight[j];
						wQcGap[n][1] += hWeight[i] * hWeight[j];
					}
				}
			}
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
			for ( int i = 0; i < sz; i++ ) {
				if ( !RFP[i] ) continue;
				correlations::QVector tq = q[n];
				tq.unfill(hPhi[i], hWeight[i]);
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
				qp += hWeight[i] * correlations::Complex( TMath::Cos(hPhi[i] * n) , TMath::Sin(hPhi[i] * n) ) * r.sum();
				wt += hWeight[i] * r.weight();
				delete cq;
			}
			rX[n][np] = qp.real();
			iX[n][np] = qp.imag();
			wX[n][np] = wt;

			// pt differential
			for ( int ipt = 0; ipt < nPtBins; ipt++ ) {
				qp = 0;
				wt = 0;
				for ( int i = 0; i < sz; i++ ) {
					if ( hEta[i] < poimineta_ or hEta[i] > poimaxeta_ ) continue;
					if ( hPt[i] < poiptmin_ or hPt[i] > poiptmax_ ) continue;
					if ( hPt[i] < ptbins[ipt] || hPt[i] > ptbins[ipt+1] ) continue;
					correlations::QVector tq = q[n];
					if ( RFP[i] ) tq.unfill(hPhi[i], hWeight[i]);
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
					qp += hWeight[i] * correlations::Complex( TMath::Cos(hPhi[i] * n) , TMath::Sin(hPhi[i] * n) ) * r.sum();
					wt += hWeight[i] * r.weight();
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
				for ( int i = 0; i < sz; i++ ) {
					if ( hPt[i] < rfpptmin_ or hPt[i] > rfpptmax_ ) continue;
					if ( hEta[i] < etabins[ieta] || hEta[i] > etabins[ieta+1] ) continue;
					correlations::QVector tq = q[n];
					if ( RFP[i] ) tq.unfill(hPhi[i], hWeight[i]);
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
					qp += hWeight[i] * correlations::Complex( TMath::Cos(hPhi[i] * n) , TMath::Sin(hPhi[i] * n) ) * r.sum();
					wt += hWeight[i] * r.weight();
					delete cq;
				}
				rQeta[n][np][ieta] = qp.real();
				iQeta[n][np][ieta] = qp.imag();
				wQeta[n][np][ieta] = wt;
			}

			// charge - differential
			for ( int i = 0; i < sz; i++ ) {
				qp = 0;
				wt = 0;
				if ( hCharge[i] > 0 || !RFP[i] ) continue;
				correlations::QVector tq = q[n];
				tq.unfill(hPhi[i], hWeight[i]);
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
				qp += hWeight[i] * correlations::Complex( TMath::Cos(hPhi[i] * n) , TMath::Sin(hPhi[i] * n) ) * r.sum();
				wt += hWeight[i] * r.weight();
				delete cq;
			}
			rQc[n][np][0] = qp.real();
			iQc[n][np][0] = qp.imag();
			wQc[n][np][0] = wt;

			// charge + differential
			qp = 0;
			wt = 0;
			for ( int i = 0; i < sz; i++ ) {
				if ( hCharge[i] < 0 || !RFP[i] ) continue;
				correlations::QVector tq = q[n];
				tq.unfill(hPhi[i], hWeight[i]);
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
				qp += hWeight[i] * correlations::Complex( TMath::Cos(hPhi[i] * n) , TMath::Sin(hPhi[i] * n) ) * r.sum();
				wt += hWeight[i] * r.weight();
				delete cq;
			}
			rQc[n][np][1] = qp.real();
			iQc[n][np][1] = qp.imag();
			wQc[n][np][1] = wt;
		}
	}

	gNoff = Noff;
	gMult = Mult;

//	t->RunId = iEvent.id().run();
//	t->EventId = iEvent.id().event();
	trV->Fill();
	doneQ();

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
