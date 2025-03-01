# Tutorial Part

- [Tutorial Part](#tutorial-part)
  - [Download Datas For Tutorials](#download-datas-for-tutorials)
  - [Workflows In Tutorials](#workflows-in-tutorials)
  - [Skimmed Datas In Tutorials](#skimmed-datas-in-tutorials)
  - [Pre-Made JSON configuration Files In Tutorials](#pre-made-json-configuration-files-in-tutorials)
  - [MC Part](#mc-part)
    - [Run tableMakerMC on LHC21i3d2 (jpsi to MuMu pp Run3Simulation)](#run-tablemakermc-on-lhc21i3d2-jpsi-to-mumu-pp-run3simulation)
    - [Run dqEfficiency on MC (LHC21i3d2 pp Run3Simulation)](#run-dqefficiency-on-mc-lhc21i3d2-pp-run3simulation)
    - [Run tablemakerMC on LHC21i3b (Prompt jpsi to dielectron pp Run3Simulation)](#run-tablemakermc-on-lhc21i3b-prompt-jpsi-to-dielectron-pp-run3simulation)
    - [Run dqEfficiency on MC (LHC21i3b pp Run3Simulation)](#run-dqefficiency-on-mc-lhc21i3b-pp-run3simulation)
    - [Run tablemakerMC on LHC21i3f2 (Non-Prompt jpsi to dielectron pp Run3Simulation)](#run-tablemakermc-on-lhc21i3f2-non-prompt-jpsi-to-dielectron-pp-run3simulation)
    - [Run dqEfficiency on LHC21i3f2 (LHC21i3f2 pp Run3Simulation)](#run-dqefficiency-on-lhc21i3f2-lhc21i3f2-pp-run3simulation)
  - [Data Part](#data-part)
    - [Run tableMaker on LHC15o (LHC15o PbPb Run2Data)](#run-tablemaker-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run tableReader on LHC15o (LHC15o PbPb Run2Data)](#run-tablereader-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run tableMaker on LHC15o With Generic Flow Analysis (LHC15o PbPb Run2Data)](#run-tablemaker-on-lhc15o-with-generic-flow-analysis-lhc15o-pbpb-run2data)
    - [Run tableReader on LHC15o with Generic Flow Analysis (LHC15o PbPb Run2Data)](#run-tablereader-on-lhc15o-with-generic-flow-analysis-lhc15o-pbpb-run2data)
    - [Run dqFlow on LHC15o (LHC15o PbPb Run2Data)](#run-dqflow-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run v0Selector on LHC15o (LHC15o PbPb Run2Data)](#run-v0selector-on-lhc15o-lhc15o-pbpb-run2data)
    - [Run tableMaker on LHC22c (LHC22c pp Run3Data)](#run-tablemaker-on-lhc22c-lhc22c-pp-run3data)
    - [Run tableReader on Data (LHC22c pp Run3Data)](#run-tablereader-on-data-lhc22c-pp-run3data)
    - [Run filterPP on fwdprompt(From Hands-on-Session II)](#run-filterpp-on-fwdpromptfrom-hands-on-session-ii)
  - [Special Part : Dilepton Analysis For Non-Standart Existing Workflows in DQ](#special-part--dilepton-analysis-for-non-standart-existing-workflows-in-dq)
    - [MC : Dilepton Track Analysis (On Bc Simulation)](#mc--dilepton-track-analysis-on-bc-simulation)
    - [Data : Dilepton Hadron Analysis (On PbPb Data LHC15o)](#data--dilepton-hadron-analysis-on-pbpb-data-lhc15o)
  - [Special Part : run tableMaker and tableReader at the same time](#special-part--run-tablemaker-and-tablereader-at-the-same-time)


Firstly, clone repository in your workspace

`git clone https://github.com/ctolon/PythonInterfaceOOP.git`

Before you start, you need to do the installations in the readme file

**P.S.** Don't forget to install the O2 enviroment before running the scripts

Ex. `alienv enter O2Physics/latest,QualityControl/latest`

Assuming you have installed the argcomplete package, don't forget to source the bash script again in your O2 enviroment.

`cd ~/PythonInterfaceOOP/PythonInterfaceOOP`

`source argcomplete.sh`

If you don't have time to read the documentation follow these steps:

For **Linux** Based System:

* `alienv enter O2Physics/latest,QualityControl/latest` (Load Your alienv, if you want you can install lxplus version without using QC)
* `pip install argcomplete` and `pip3 install argcomplete`
* `source argcomplete.sh`

For **MacOS** Based System:

* `brew install bash`
* `alienv enter O2Physics/latest,QualityControl/latest` (Load Your alienv, if you want you can install lxplus version without using QC)
* `pip install argcomplete` and `pip3 install argcomplete`
* `exec bash` (temporary bash shell)
* `source argcomplete.sh`

if not works:

* `sudo chsh -s /bin/bash <username>`
* `source argcomplete.sh`

if you used the command `sudo chsh -s /bin/bash <username>` after you are done with the scripts (It converts your system shell zsh to bash):

* `sudo chsh -s /bin/zsh <username>` (It converts your system shell bash to zsh)


if you used the command `exec bash` you don't need to do anything.

## Download Datas For Tutorials

You can Found MC Datas, pre-made JSON config files and DQ Skimmed datas for tutorial at: [Click Here](https://cernbox.cern.ch/index.php/s/XWOFJVaBxiIw0Ft) password: DQ

Create a new folder in pythonInterfaceOOP directory with `mkdir Datas` and move the downloaded datas here.

You can found Real Data for pp at : [Click Here](https://alimonitor.cern.ch/catalogue/index.jsp?path=%2Falice%2Fdata%2F2022%2FLHC22c%2F517616%2Fapass1#/alice/data/2022/LHC22c/517616/apass1)

You can found Real Data for PbPb at : [Click Here](https://alimonitor.cern.ch/prod/jobs.jsp?t=20117&outputdir=PWGZZ/Run3_Conversion/242_20211215-1006_child_2$)

or [Click Here](https://cernbox.cern.ch/index.php/s/6KLIdQdAlNXj5n1)

**P.S:** Dont forget the change name of AO2D.root files for interface and Move this datas to you previously create Datas Folder.

For PbPb Data : AO2D.root to AO2D_PbPbDataRun2_LHC15o.root

For pp Data : AO2D.root to AO2D_ppDataRun3_LHC22c.root

If you downloaded these datasets, you can start.

## Workflows In Tutorials

<details><summary>For MC:</summary>

Workflow | Dataset | Skimmed | Process | Type | Col Syst
--- | --- | --- | --- | --- | --- |
`tableMakerMC` | `LHC21i3d2` | `No` | `MuonOnlyWithCov`<br>`OnlyBCs` | J/ψ → μ<sup>+</sup> μ<sup>−</sup> | `pp`
`dqEfficiency` | `LHC21i3d2` | `Yes`  | `DecayToMuMu` | J/ψ → μ<sup>+</sup> μ<sup>−</sup> | `pp`
`tableMakerMC` | `LHC21i3b` | `No` | `BarrelOnly`<br>`OnlyBCs` | J/ψ → e<sup>+</sup> e<sup>−</sup> | `pp`
`dqEfficiency` | `LHC21i3b` | `Yes` | `DecayToEE` | J/ψ → e<sup>+</sup> e<sup>−</sup>  | `pp`
`tableMakerMC` | `LHC21i3f2` | `No` | `BarrelOnly`<br>`OnlyBCs` | h<sub>B</sub> →  J/ψ + *X*, J/ψ → e<sup>+</sup> e<sup>−</sup>  | `pp`
`dqEfficiency` | `LHC21i3f2` | `Yes` | `DecayToEE` | h<sub>B</sub> →  J/ψ + *X*, J/ψ → e<sup>+</sup> e<sup>−</sup>  | `pp`
</details>

<details><summary>For Data:</summary>

Workflow | Dataset | Skimmed | Process | Selection | Col Syst
--- | --- | --- | --- | --- | --- |
`tableMaker` | `LHC15o` | `No` | `BarrelOnlyWithCent`<br>`OnlyBCs` | J/ψ → e<sup>+</sup> e<sup>−</sup> | `PbPb`
`tableReader`  | `LHC15o` | `Yes`  | `DecayToEE` | J/ψ → e<sup>+</sup> e<sup>−</sup> | `PbPb`
`tableMaker` | `LHC15o` | `No` | `FullWithCent`<br>`BarrelOnlyWithQvector`<br>`OnlyBCs` | J/ψ → e<sup>+</sup> e<sup>−</sup> | `PbPb`
`tableReader` | `LHC15o` | `Yes`  | `VnDecayToEE` | J/ψ → e<sup>+</sup> e<sup>−</sup> | `PbPb`
`dqFlow` | `LHC15o` | `No` | - | - | `PbPb`
`v0Selector` | `LHC15o` | `No`  | - | - | `PbPb`
`tableMaker` | `LHC22c` | `No` | `MuonOnlyWithCov`<br>`OnlyBCs` | J/ψ → μ<sup>+</sup> μ<sup>−</sup> | `pp`
`tableReader` | `LHC22c` | `Yes`  | `DecayToMuMuVertexing` | J/ψ → μ<sup>+</sup> μ<sup>−</sup> | `pp`
`filterPP` | `fwdprompt` | `No`  | `eventSelection` <br> `barrelTrackSelection`  <br> `muonSelection` | All Events | `pp`
</details>

<details><summary>For Dileptons:</summary>

Workflow | Dataset | Process | Type | Col Syst
--- | --- | --- | --- | --- |
`dqEfficiency` | `AO2D_Bc100` | `DecayToMuMuVertexing`<br>`dileptonTrackDimuonMuonSelection`  | B<sub>c</sub> → J/ψ → (μ<sup>+</sup> μ<sup>−</sup>) + μ | `pp`
`tableReader`  | `LHC15o` | `DecayToEE`<br>`dileptonHadron` | `dileptonhadron` | `PbPb`
</details>



<details><summary>TO BE ADDED IN TUTORIALS (Not Prepared Yet):</summary>

Workflow | Dataset | Process | Type | Col Syst
--- | --- | --- | --- | --- |
`dqEfficiency` | `AO2D_Bplus` | `DecayToMuMuVertexing`<br>`dileptonTrackDimuonMuonSelection`  |B<sup>+</sup> → J/ψ + K, → J/ψ → e<sup>+</sup> e<sup>−</sup> | `pp`
</details>

## Skimmed Datas In Tutorials

<details><summary>Reduced DQ skimmed data list created with tableMaker/tableMakerMC:</summary>

Data | Dataset | Used Workflow | Selected Processes (from tableMaker) |
--- | --- | --- | --- |
`reducedAod_ppMC_LHC21i3d2.root` | `LHC21i3d2` | `tableMakerMC` | `MuonOnlyWithCov`<br>`OnlyBCs`
`reducedAod_ppMC_LHC21i3b.root` | `LHC21i3b` | `tableMakerMC` | `BarrelOnly`<br>`OnlyBCs`
`reducedAod_ppMC_LHC21i3f2.root` | `LHC21i3f2` | `tableMakerMC` | `BarrelOnly`<br>`OnlyBCs`
`reducedAod_ppMC_Bc100.root` | `Bc100` | `tableMakerMC` | `MuonOnlyWithCov`<br>`OnlyBCs`
`reducedAod_PbPbData_LHC15o.root` | `LHC15o` | `tableMaker` | `BarrelOnlyWithCent`<br>`OnlyBCs`
`reducedAod_PbPbData_LHC15o_Flow.root` | `LHC15o` | `tableMaker` | `FullWithCent`<br>`BarrelOnlyWithQvector`<br>`OnlyBCs`
`reducedAod_PbPbData_LHC15o_dileptonHadron.root` | `LHC15o` | `tableMaker` | `BarrelOnly`<br>`OnlyBCs`
`reducedAod_ppData_LHC22c.root` | `LHC22c` | `tableMaker` | `MuonOnlyWithCov`<br>`OnlyBCs`
</details>

<details><summary>Reduced DQ Dileptons skimmed data list For Dilepton Analysis (dilepton-track and dilepton-hadron) created with tableReader/dqEfficiency:</summary>

Data | Dataset | Used Workflow | Selected Processes (from tableMaker) |
--- | --- | --- | --- |
`dileptonAOD_ppMC_BC100.root` | `Bc100` | `dqEfficiency` | `MuonOnlyWithCov`<br>`OnlyBCs`
`dileptonAOD_PbPbData_LHC15o_dileptonHadron.root` | `LHC15o` | `tableReader` | `BarrelOnly`<br>`OnlyBCs`
</details>

## Pre-Made JSON configuration Files In Tutorials

Config JSON list created with Scripts.

<details><summary>Common JSON configs</summary>

Config | For | Description
--- | --- | --- |
`configAnalysis_LHC21i3b_MC.json` | `MCRun3` | Run dqEfficiency on LHC21i3b Simulation → reducedAod_ppMC_LHC21i3b.root
`configAnalysis_LHC21i3d2_MC.json` | `MCRun3` | Run dqEfficiency on LHC21i3d2 Simulation → reducedAod_ppMC_LHC21i3d2.root
`configAnalysis_LHC21i3f2_MC.json` | `MCRun3` | Run dqEfficiency on LHC21i3f2 Simulation → reducedAod_ppMC_LHC21i3f2.root
`ConfigAnalysis_LHC15o_Data.json` | `DataRun2` | Run tableReader on LHC15o Data without flow → reducedAod_PbPbData_LHC15o.root
`ConfigAnalysis_LHC15o_Flow_Data.json` | `DataRun2` | Run tableReader on LHC15o Data for Flow Analysis → reducedAod_PbPbData_LHC15o_Flow.root
`ConfigAnalysis_LHC22c_Data.json` | `DataRun3` | Run tableReader on LHC22c Data → reducedAod_PbPbData_LHC15o.root
`configTableMaker_LHC21i3b_MCRun3.json` | `MCRun3` | Run tableMakerMC on LHC21i3b Simulation → AO2D_ppMCRun3_LHC21i3b.root
`configTableMaker_LHC21i3d2_MCRun3.json` | `MCRun3` | Run tableMakerMC on LHC21i3d2 Simulation → AO2D_ppMCRun3_LHC21i3d2.root
`configTableMaker_LHC21i3f2_MCRun3.json` | `MCRun3` | Run tableMakerMC on LHC21i3f2 Simulation → AO2D_ppMCRun3_LHC21i3f2.root
`ConfigTableMaker_LHC15o_DataRun2.json` | `DataRun2` | Run tableMaker on LHC15o without Flow → AO2D_PbPbDataRun2_LHC15o.root
`ConfigTableMaker_LHC15o_Flow_DataRun2.json` | `DataRun2` | Run tableMaker on LHC15o For Flow Analysis → AO2D_PbPbDataRun2_LHC15o.root
`ConfigTableMaker_LHC22c_DataRun3.json` | `DataRun3` | Run tableMaker on LHC22c Data → AO2D_ppDataRun3_LHC22c.root
`configV0Selector_LHC15o_DataRun2.json` | `DataRun2` | Run v0Selector on LHC15o Data → AO2D_PbPbDataRun2_LHC15o.root
</details>

<details><summary>JSON configs for Single Workflows</summary>

Config | For | Description
--- | --- | --- |
`configFilterPP_fwdprompt_Run3.json` | `MCRun3` | Run filterPP on fwdprompt → AO2D_fwdprompt.root
`configFlow_LHC15o_DataRun2.json` | `DataRun2` | Run dqFlow on LHC15o Data  → AO2D_PbPbDataRun2_LHC15o.root
`configV0Selector_LHC15o_DataRun2.json` | `DataRun2` | Run v0Selector on LHC15o Data → AO2D_PbPbDataRun2_LHC15o.root
</details>

JSON configs for dilepton-hadron and dilepton-track analysis:
<details><summary>
JSON configs for dilepton-hadron and dilepton-track analysis:</summary>

Config | For | Description
--- | --- | --- |
`configTableMaker_Bc100_MCRun3.json` | `MCRun3` | Run tableMakerMC on Bc100 Simulation for prepare dilepton-track analysis → AO2D_Bc100.root
`configAnalysis_Bc100_MC.json` | `MCRun3` | Run dqEfficiency on Bc100 Simulation for prepare skimmed dileptons output → reducedAod_ppMC_Bc100.root
`configAnalysisDilepton_Bc100_MC.json` | `MCRun3` | Run dqEfficiency on Bc100 Simulation for dilepton analysis → dileptonAOD_ppMC_BC100.root
`configTableMaker_LHC15o_DileptonHadron_DataRun2.json` | `DataRun2` | Run tableMaker on LHC15o Data for prepare dilepton-hadron analysis → AO2D_PbPbDataRun2_LHC15o.root
`configAnalysis_LHC15o_dileptonHadron_Data.json` | `DataRun2` | Run tableReader on LHC15o Data for prepare skimmed dileptons output → reducedAod_PbPbData_LHC15o_dileptonHadron.root
`configAnalysisDilepton_LHC15o_dileptonHadron_Data.json` | `DataRun2` | Run tableReader on LHC15o Data for dilepton analysis → reducedAod_PbPbData_LHC15o_dileptonHadron.root
</details>

P.S. Root files are inputs for JSON configs

## MC Part

**VERY IMPORTANT:** For this section, you need convert runOverMC variable to True in python scripts (runAnalysis.py and runTableMaker.py).

### Run tableMakerMC on LHC21i3d2 (jpsi to MuMu pp Run3Simulation)

Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerMCRun3.json --internal-dpl-aod-reader:aod-file Datas/AO2D_ppMCRun3_LHC21i3d2.root --table-maker-m-c:processMuonOnlyWithCov true --event-selection-task:syst pp --table-maker-m-c:cfgMuonCuts muonQualityCuts muonTightQualityCutsForTests --table-maker-m-c:cfgMCsignals muFromJpsi Jpsi muon --add_track_prop --logFile

```

 ### Run dqEfficiency on MC (LHC21i3d2 pp Run3Simulation)

You need to produce reducedAod.root file with tableMakerMC in previous step.

Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisMC.json --internal-dpl-aod-reader:aod-file reducedAod.root --analysis-track-selection:processSkimmed false --analysis-muon-selection:processSkimmed true --analysis-same-event-pairing:processDecayToMuMuVertexingSkimmed true --analysis-event-selection:cfgQA true --analysis-muon-selection:cfgQA true --analysis-same-event-pairing:cfgMuonCuts muonQualityCuts muonTightQualityCutsForTests --analysis-muon-selection:cfgMuonCuts muonQualityCuts muonTightQualityCutsForTests --analysis-muon-selection:cfgMuonMCSignals muFromJpsi --analysis-same-event-pairing:cfgBarrelMCRecSignals mumuFromJpsi dimuon --analysis-same-event-pairing:cfgBarrelMCGenSignals jpsi --logFile
```

### Run tablemakerMC on LHC21i3b (Prompt jpsi to dielectron pp Run3Simulation)

Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerMCRun3.json --internal-dpl-aod-reader:aod-file Datas/AO2D_ppMCRun3_LHC21i3b.root --table-maker-m-c:processBarrelOnly true --event-selection-task:syst pp --table-maker-m-c:cfgBarrelTrackCuts jpsiO2MCdebugCuts jpsiO2MCdebugCuts2 jpsiO2MCdebugCuts3 jpsiO2MCdebugCuts4 --table-maker-m-c:cfgMCsignals electronPrimary eFromJpsi Jpsi LMeeLF LMeeLFQ --logFile
```

 ### Run dqEfficiency on MC (LHC21i3b pp Run3Simulation)

You need to produce reducedAod.root file with tableMakerMC in previous step.

Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisMC.json --internal-dpl-aod-reader:aod-file reducedAod.root --analysis-track-selection:processSkimmed true --analysis-muon-selection:processSkimmed false --analysis-same-event-pairing:processDecayToEESkimmed true --analysis-track-selection:cfgQA true --analysis-same-event-pairing:cfgBarrelMCGenSignals Jpsi --analysis-same-event-pairing:cfgBarrelMCRecSignals eeFromJpsi dielectron --analysis-track-selection:cfgTrackCuts jpsiO2MCdebugCuts --analysis-track-selection:cfgTrackMCSignals eFromJpsi eFromNonpromptJpsi --logFile
```

### Run tablemakerMC on LHC21i3f2 (Non-Prompt jpsi to dielectron pp Run3Simulation)

Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerMCRun3.json --internal-dpl-aod-reader:aod-file Datas/AO2D_ppMCRun3_LHC21i3f2.root --table-maker-m-c:processBarrelOnly true --event-selection-task:syst pp --table-maker-m-c:cfgBarrelTrackCuts jpsiO2MCdebugCuts --table-maker-m-c:cfgMCsignals electronPrimary eFromJpsi eFromNonpromptJpsi eFromLMeeLF LMeeLF Jpsi everythingFromBeauty --debug debug --logFile
```

 ### Run dqEfficiency on LHC21i3f2 (LHC21i3f2 pp Run3Simulation)

You need to produce reducedAod.root file with tableMakerMC in previous step.

Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisMC.json --internal-dpl-aod-reader:aod-file reducedAod.root  --analysis-track-selection:processSkimmed true --analysis-muon-selection:processSkimmed false --analysis-same-event-pairing:processDecayToEESkimmed true --analysis-track-selection:cfgQA true --analysis-same-event-pairing:cfgBarrelMCGenSignals Jpsi nonPromptJpsi --analysis-same-event-pairing:cfgBarrelMCRecSignals eeFromJpsi dielectron --analysis-track-selection:cfgTrackCuts jpsiO2MCdebugCuts --analysis-same-event-pairing:cfgTrackCuts jpsiO2MCdebugCuts --analysis-track-selection:cfgTrackMCSignals eFromJpsi eFromNonpromptJpsi --debug debug --logFile
```

## Data Part

**VERY IMPORTANT:** For this section, you need convert runOverMC variable is False in python scripts (runAnalysis.py and runTableMaker.py).
### Run tableMaker on LHC15o (LHC15o PbPb Run2Data)

Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerDataRun2.json --internal-dpl-aod-reader:aod-file Datas/AO2D_PbPbDataRun2_LHC15o.root --table-maker:processBarrelOnlyWithCent true --event-selection-task:syst PbPb --table-maker:cfgQA true --centrality-table:estRun2V0M 1 --table-maker:cfgBarrelTrackCuts jpsiPID1 jpsiPID2 --add_fdd_conv --logFile
```

### Run tableReader on LHC15o (LHC15o PbPb Run2Data)

You need to produce reducedAod.root file with tableMaker in previous step.

Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisData.json --internal-dpl-aod-reader:aod-file reducedAod.root --analysis-track-selection:processSkimmed true --analysis-muon-selection:processSkimmed false --analysis-same-event-pairing:processDecayToEESkimmed true --analysis-track-selection:cfgQA true --analysis-track-selection:cfgTrackCuts jpsiPID1 jpsiPID2 --analysis-same-event-pairing:cfgTrackCuts jpsiPID1 jpsiPID2 --logFile

```

### Run tableMaker on LHC15o With Generic Flow Analysis (LHC15o PbPb Run2Data)

Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerDataRun2.json --internal-dpl-aod-reader:aod-file Datas/AO2D_PbPbDataRun2_LHC15o.root --table-maker:processFullWithCent true --table-maker:processBarrelOnlyWithQvector true --event-selection-task:syst PbPb --table-maker:cfgQA true --centrality-table:estRun2V0M 1 --table-maker:cfgBarrelTrackCuts jpsiPID1 jpsiPID2 --analysis-qvector:cfgBarrelTrackCuts jpsiPID1 jpsiPID2 --add_fdd_conv --logFile
```

### Run tableReader on LHC15o with Generic Flow Analysis (LHC15o PbPb Run2Data)

You need to produce reducedAod.root file with tableMaker in previous step.

Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisData.json --internal-dpl-aod-reader:aod-file reducedAod.root --analysis-track-selection:processSkimmed true --analysis-muon-selection:processSkimmed false --analysis-same-event-pairing:processVnDecayToEE true --analysis-track-selection:cfgQA true --analysis-track-selection:cfgTrackCuts jpsiPID1 jpsiPID2 --analysis-same-event-pairing:cfgTrackCuts jpsiPID1 jpsiPID2 --debug debug --logFile
```

### Run dqFlow on LHC15o (LHC15o PbPb Run2Data)

Command To Run:

```ruby
python3 runDQFlow.py configs/configFlowDataRun2.json --internal-dpl-aod-reader:aod-file Datas/AO2D_PbPbDataRun2_LHC15o.root --event-selection-task:syst PbPb --analysis-qvector:cfgQA true --centrality-table:estRun2V0M 1 --analysis-qvector:cfgBarrelTrackCuts jpsiPID1 jpsiPID2 --analysis-qvector:cfgMuonCuts muonQualityCuts muonTightQualityCutsForTests --add_fdd_conv
```
### Run v0Selector on LHC15o (LHC15o PbPb Run2Data)

Command To Run:

```ruby
python3 runV0selector.py configs/configV0SelectorDataRun2.json --internal-dpl-aod-reader:aod-file Datas/AO2D_PbPbDataRun2_LHC15o.root --add_fdd_conv --add_weakdecay_ind
```

### Run tableMaker on LHC22c (LHC22c pp Run3Data)

Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerDataRun3.json --internal-dpl-aod-reader:aod-file Datas/AO2D_ppDataRun3_LHC22c.root --table-maker:processMuonOnlyWithCov true --table-maker:processBarrelOnlyWithCov true --event-selection-task:syst pp --table-maker:cfgQA true --table-maker:cfgMuonCuts muonQualityCuts muonTightQualityCutsForTests --table-maker:cfgBarrelTrackCuts jpsiPID1 jpsiPID2 jpsiO2MCdebugCuts --add_track_prop --logFile

```

### Run tableReader on Data (LHC22c pp Run3Data)

You need to produce reducedAod.root file with tableMaker in previous step.

Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisData.json --internal-dpl-aod-reader:aod-file reducedAod.root --analysis-track-selection:processSkimmed true --analysis-muon-selection:processSkimmed true --analysis-same-event-pairing:processDecayToEESkimmed true --analysis-same-event-pairing:processDecayToMuMuVertexingSkimmed true --analysis-track-selection:cfgQA true --analysis-muon-selection:cfgQA true --analysis-muon-selection:cfgMuonCuts muonQualityCuts muonTightQualityCutsForTests --analysis-track-selection:cfgTrackCuts jpsiPID1 jpsiPID2 jpsiO2MCdebugCuts --analysis-same-event-pairing:cfgMuonCuts muonQualityCuts muonTightQualityCutsForTests --analysis-same-event-pairing:cfgTrackCuts jpsiPID1 jpsiPID2 jpsiO2MCdebugCuts --analysis-same-event-pairing:cfgAddSEPHistogram barrel dimuon vertexing-forward vertexing --logFile
```

**IMPORTANT NOTE:** Here we used the cfgAddSEPHistogram argument (`--analysis:same-event-paring:cfgAddSEPHistogram barrel dimuon vertexing-forward vertexing`) to define same event pairing histograms. This is because by default, dielectron decay histograms for same event pairing are defined in the configAnalysisData.json config file, and since we are doing dimuon analysis here, we have to also add muon histogram groups to histogram configurations with the configuration for dimuon.

### Run filterPP on fwdprompt(From Hands-on-Session II)

Command To Run:

```ruby
python3 runFilterPP.py configs/configFilterPPDataRun3.json --internal-dpl-aod-reader:aod-file Datas/AO2D_fwdprompt.root --event-selection-task:syst pp --d-q-barrel-track-selection:cfgBarrelTrackCuts jpsiO2MCdebugCuts jpsiPID2 --d-q-filter-p-p-task:cfgBarrelSels jpsiO2MCdebugCuts:pairNoCut:1 jpsiPID2::1 --d-q-muons-selection:cfgMuonsCuts muonLowPt muonHighPt muonLowPt --d-q-filter-p-p-task:cfgMuonSels muonLowPt::1 muonHighPt::1 muonLowPt:pairUpsilon:1 --d-q-filter-p-p-task:cfgWithQA true --logFile
```

P.S. Cuts Needs to optimized.

## Special Part : Dilepton Analysis For Non-Standart Existing Workflows in DQ

This section includes analysis with non-standard workflows in DQ workflows. These analyzes are carried out in 3 stages:

1. DQ skimmed data is created with TableMaker/tableMakerMC (input: AO2D.root, output: AnalysisResults.root)

2. DQ skimmed extra dilepton tables are created with tableReader/dqEfficiency and with this way new DQ skimmed data with extra dilepton tables are created on dileptonAod.root, Normally reducedAod.root that does not contains dilepton tables (input : reducedAod.root, output: AnalysisResults.root and dileptonAod.root)

3. With tableReader/dqEfficiency, analysis is performed on DQ skimmed dilepton data created earlier (input: dileptonAod.root and output: AnalysisResults.root)

### MC : Dilepton Track Analysis (On Bc Simulation)

**VERY IMPORTANT:** For this section, you need convert runOverMC variable to True in python scripts (runAnalysis.py and runTableMaker.py).

First Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerMCRun3.json --internal-dpl-aod-reader:aod-file Datas/AO2D_Bc100.root --table-maker-m-c:processMuonOnlyWithCov true --event-selection-task:syst pp --table-maker-m-c:cfgMCsignals Jpsi Bc anyBeautyHadron --table-maker-m-c:cfgMuonCuts matchedGlobal --table-maker-m-c:cfgMuonLowPt 0.0 --logFile
```

Second Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisMC.json --internal-dpl-aod-reader:aod-file reducedAod.root --analysis-track-selection:processSkimmed false --analysis-muon-selection:processSkimmed true --analysis-same-event-pairing:processDecayToMuMuVertexing true --analysis-muon-selection:cfgQA true --analysis-muon-selection:cfgMuonCuts matchedGlobal --analysis-same-event-pairing:cfgMuonCuts matchedGlobal --analysis-muon-selection:cfgMuonMCSignals muon muFromJpsi muFromBc dimuon --analysis-same-event-pairing:cfgBarrelMCGenSignals Jpsi --analysis-same-event-pairing:cfgBarrelMCRecSignals mumuFromJpsi --logFile --writer true
```

Note: We defined --writer argument as true for producing extra dilepton tables into dileptonAod.root from reducedAod.root. 

Third Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisMC.json --internal-dpl-aod-reader:aod-file dileptonAOD.root --analysis-muon-selection:processSkimmed true --analysis-track-selection:processSkimmed false --analysis-dilepton-track:processDimuonMuonSkimmed true --analysis-same-event-pairing:processDecayToMuMuVertexingSkimmed true --analysis-muon-selection:cfgMuonCuts matchedGlobal --analysis-muon-selection:cfgMuonMCSignals muon muFromJpsi muFromBc dimuon --analysis-dilepton-track:cfgBarrelMCRecSignals mumuFromJpsiFromBc mumumuFromBc --analysis-dilepton-track:cfgBarrelMCGenSignals Jpsi --analysis-same-event-pairing:cfgBarrelMCRecSignals mumuFromJpsi dimuon --analysis-same-event-pairing:cfgMuonCuts matchedGlobal --logFile
```

Note: We defined --reader argument for reading dilepton tables from dileptonAOD.

### Data : Dilepton Hadron Analysis (On PbPb Data LHC15o)

**VERY IMPORTANT:** For this section, you need convert runOverMC variable to False in python scripts (runAnalysis.py and runTableMaker.py).

First Command To Run:

```ruby
python3 runTableMaker.py configs/configTableMakerDataRun2.json -runData --aod Datas/AO2D_PbPbDataRun2_LHC15o.root --process OnlyBCs BarrelOnly --syst PbPb --cfgWithQA true --est Run2V0M --cfgBarrelTrackCuts jpsiPID1 jpsiPID2 --add_fdd_conv --debug debug --logFile
```

Second Command To Run:

```ruby
python3 runTableReader.py configs/configAnalysisData.json --aod reducedAod.root --analysis eventSelection trackSelection sameEventPairing --process DecayToEE --cfgQA true --cfgTrackCuts jpsiPID1 jpsiPID2 --debug debug --logFile --writer configs/writerConfiguration_dileptons.json
```

Third Command To Run:

```ruby
python3 runTableReader.py configs/configAnalysisData.json --aod dileptonAOD.root --analysis eventSelection trackSelection sameEventPairing dileptonHadron --process DecayToEE --cfgQA true --cfgTrackCuts jpsiPID1 jpsiPID2 --debug debug --logFile
```

## Special Part : run tableMaker and tableReader at the same time

Command To Run:

```ruby
python3 runAnalysis.py configs/configAnalysisData.json --analysis-same-event-pairing:processDecayToEESkimmed true -runParallel;python3 runTableMaker.py configs/configTableMakerDataRun3.json --internal-dpl-aod-reader:aod-file Datas/AO2D_ppDataRun3_LHC22c.root --table-maker:processBarrelOnly true -runParallel --add_track_prop
```

To run the tablemaker and the tablereader at the same time, you must first configure the tableReader with the runAnalysis.py script. then after adding the -runParallel argument `;` (it called as semi-colon) is put. Then the tableMaker is configured and the path of the AOD file must be given in the tableMaker script (again, given the -runParallel argument, don't forget for both scripts). Same goes for MC (for tableMakerMC and dqEfficiency, you need change runOverMC variables to False)

This way it produces analysis results for both tableReader and tableMaker in AnalysisResults.root, and you get reducedAod.root (it contains reduced tables from DQ data model)


[← Go back to Instructions For Python Scripts](5_InstructionsForPythonScripts.md) | [↑ Go to the Table of Content ↑](../README.md#table-of-contents) | [Continue to Developer Guide →](7_DeveloperGuide.md)
