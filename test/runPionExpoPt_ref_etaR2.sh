#/bin/bash

echo $PWD
WORKDIR=$PWD
ls -l
source /afs/cern.ch/project/eos/installation/cms/etc/setup.sh
cd /afs/cern.ch/work/q/qwang/cleanroom2/CMSSW_5_3_20/src/QWAna/QWCumuV3/test
eval `scramv1 runtime -sh`
cp qwcumuv2_PionExpoPt_ref_etaR2_Gen.py $WORKDIR/cfg.py
cd $WORKDIR
cmsRun cfg.py
ls -l
NEW_UUID=$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | head -c 8)
cmsStage cumu.root /store/group/phys_heavyions/qwang/CumuV3/MC/PionExpoPt_ref_etaR2/cumu_$NEW_UUID.root
echo done transfter
