#include <correlations/Types.hh>
#include <correlations/Result.hh>
#include <correlations/QVector.hh>
#include <correlations/recursive/FromQVector.hh>
#include <correlations/recurrence/FromQVector.hh>
#include <correlations/closed/FromQVector.hh>
#include <TComplex.h>
#include <TH1.h>
#include <TH2.h>
#include <TTree.h>
#include <TNtupleD.h>
#include <TRandom3.h>
#include <TFile.h>
#include "QWConstV3.h"
#include <RecoHI/HiEvtPlaneAlgos/interface/HiEvtPlaneList.h>
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
//
// constants, enums and typedefs
//

//#define QW_DEBUG 1
//#define QW_PEREVENT 1

#define PRD(x) cout << "!!QW!! " << __LINE__ << " DEBUG OUTPUT " << (#x) << " = " << (x) << endl;
#define PR(x) cout << "!!QW!! " << __LINE__ << " DEBUG OUTPUT " << (#x) << endl;
//
// class declaration
//

///////////////// Class ////////////////////////////

class QWCumuV3 : public edm::EDAnalyzer {
	public:
		explicit QWCumuV3(const edm::ParameterSet&);
		~QWCumuV3();

		static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	private:
		virtual void beginJob() ;
		virtual void analyze(const edm::Event&, const edm::EventSetup&);
		void analyzeData(const edm::Event&, const edm::EventSetup&);
		void analyzeGen(const edm::Event&, const edm::EventSetup&);
		void analyzeEP(const edm::Event&, const edm::EventSetup&);
		virtual void endJob() ;

		virtual void beginRun(edm::Run const&, edm::EventSetup const&);
		virtual void endRun(edm::Run const&, edm::EventSetup const&);
		virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
		virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

	/////////////////////////////////////////////
		//TRandom3 * gRandom;
		// ----------member data ---------------------------

		edm::InputTag					trackEta_;
		edm::InputTag					trackPhi_;
		edm::InputTag					trackWeight_;
		edm::InputTag					vertexZ_;

		edm::InputTag					centralityTag_;

		double	minvz_, maxvz_;

		unsigned int	nvtx_;
	/////////////////////////////////////////////
		double	rfpmineta_, rfpmaxeta_;
		double	poimineta_, poimaxeta_;
		double	rfpptmin_, rfpptmax_;
		double	poiptmin_, poiptmax_;

		bool	b2PartGap_;
		double	dEtaGap_;

		int	cmode_;

		unsigned int	nvtx_;

	/////////////////////////////////////////////
		TTree * trV;

		int gNoff;
		int gMult;

		double rQGap[7];
		double wQGap[7];

		double rQpGap[7][24];
		double wQpGap[7][24];

		double rQetaGap[7][24];
		double wQetaGap[7][24];

		double rQcGap[7][2];
		double wQcGap[7][2];

		double rQ[7][4];
		double iQ[7][4];
		double wQ[7][4];

		double rX[7][4];
		double iX[7][4];
		double wX[7][4];

		double rQp[7][4][24];
		double iQp[7][4][24];
		double wQp[7][4][24];

		double rQeta[7][4][24];
		double iQeta[7][4][24];
		double wQeta[7][4][24];

		double rQc[7][4][2];
		double iQc[7][4][2];
		double wQc[7][4][2];

		correlations::HarmonicVector	hc[7];
		correlations::QVector		q[7];
		correlations::FromQVector	*cq[7];

		void initQ();
		void doneQ();
		void Sim();

		bool CaloMatch(const reco::Track&, const edm::Event&, unsigned int idx);
};



