#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK
# -*- coding: utf-8 -*-

# Copyright 2019-2020 CERN and copyright holders of ALICE O2.
# See https://alice-o2.web.cern.ch/copyright for details of the copyright holders.
# All rights not expressly granted are reserved.
#
# This software is distributed under the terms of the GNU General Public
# License v3 (GPL Version 3), copied verbatim in the file "COPYING".
#
# In applying this license CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

# \Author: ionut.cristian.arsene@cern.ch
# \Interface:  cevat.batuhan.tolon@cern.ch

# Orginal Task: https://github.com/AliceO2Group/O2Physics/blob/master/PWGDQ/Tasks/dqFlow.cxx

# run template: `python3 runDQFlow.py <config.json> --task-name:<configurable|processFunc> parameter ...`
# parameter can be multiple like this:
# --analysis-qvector:cfgBarrelTrackCuts jpsiPID1 jpsiPID2

import sys
import logging
import logging.config
import os
from extramodules.dqTranscations import aodFileChecker, jsonTypeChecker, mainTaskChecker, trackPropagationChecker
from extramodules.configSetter import SetArgsToArgumentParser, commonDepsToRun, dispInterfaceMode, dispO2HelpMessage, setConfigs, setConverters, debugSettings, dispArgs, setProcessDummy, setSwitch
from extramodules.pycacheRemover import runPycacheRemover
from extramodules.utils import dumpJson, loadJson


def main():
    
    # Setting arguments for CLI
    parsedJsonFile = "configs/configFlowDataRun3.json"
    setArgsToArgumentParser = SetArgsToArgumentParser(parsedJsonFile, ["timestamp-task", "tof-event-time", "bc-selection-task", "tof-pid-beta"])
    args = setArgsToArgumentParser.parseArgs()
    dummyHasTasks = setArgsToArgumentParser.dummyHasTasks
    processFuncs = setArgsToArgumentParser.processFuncs
    allArgs = vars(args) # for get args
    
    # All Dependencies
    commonDeps = ["o2-analysis-timestamp", "o2-analysis-event-selection", "o2-analysis-multiplicity-table", "o2-analysis-centrality-table", "o2-analysis-trackselection", "o2-analysis-trackextension", "o2-analysis-pid-tof-base", "o2-analysis-pid-tof-full", "o2-analysis-pid-tof-beta", "o2-analysis-pid-tpc-full"]
    #commonDeps = ["o2-analysis-timestamp", "o2-analysis-event-selection", "o2-analysis-multiplicity-table", "o2-analysis-centrality-table"]
    #barrelDeps = ["o2-analysis-trackselection", "o2-analysis-trackextension", "o2-analysis-pid-tof-base", "o2-analysis-pid-tof-full", "o2-analysis-pid-tof-beta", "o2-analysis-pid-tpc-full"]
    #muonDeps = ["o2-analysis-fwdtrackextension"]
    
    # Debug Settings
    debugSettings(args.debug, args.logFile, fileName = "dqFlow.log")
    
    # if cliMode true, Overrider mode else additional mode
    cliMode = args.override
    
    # Basic validations
    jsonTypeChecker(args.cfgFileName)
    jsonTypeChecker(parsedJsonFile)
    
    # Load the configuration file provided as the first parameter
    config = loadJson(args.cfgFileName)
    
    taskNameInConfig = "analysis-qvector"
    taskNameInCommandLine = "o2-analysis-dq-flow"
    
    mainTaskChecker(config, taskNameInConfig)
    
    # Interface Mode message
    dispInterfaceMode(cliMode)
    
    # Set arguments to config json file
    setConfigs(allArgs, config, cliMode)
    
    # process function automation based on cliMode
    setSwitch(config, processFuncs, allArgs, cliMode)
    
    # Transactions
    aodFileChecker(allArgs["internal_dpl_aod_reader:aod_file"])
    #trackPropagationChecker(args.add_track_prop, barrelDeps)
    trackPropagationChecker(args.add_track_prop, commonDeps)
    setProcessDummy(config, dummyHasTasks) # dummy automizer
    
    # Write the updated configuration file into a temporary file
    updatedConfigFileName = "tempConfigDQFlow.json"
    
    dumpJson(updatedConfigFileName, config)
    
    # Check which dependencies need to be run
    depsToRun = commonDepsToRun(commonDeps)
    """
    for processFunc in processFuncs[taskNameInConfig]:
        if processFunc not in config[taskNameInConfig].keys():
            continue
        if config[taskNameInConfig][processFunc] == "true":
            if "processBarrel" in processFunc:
                for dep in barrelDeps:
                    depsToRun[dep] = 1
            if "processForward" in processFunc:
                for dep in muonDeps:
                    depsToRun[dep] = 1
    """
    
    commandToRun = f"{taskNameInCommandLine} --configuration json://{updatedConfigFileName} --severity error --shm-segment-size 12000000000 -b"
    for dep in depsToRun.keys():
        commandToRun += " | " + dep + " --configuration json://" + updatedConfigFileName + " -b"
        logging.debug("%s added your workflow", dep)
    
    commandToRun = setConverters(allArgs, updatedConfigFileName, commandToRun)
    
    dispO2HelpMessage(args.helpO2, commandToRun)
    
    print("====================================================================================================================")
    logging.info("Command to run:")
    logging.info(commandToRun)
    print("====================================================================================================================")
    logging.info("Deps to run:")
    logging.info(depsToRun.keys())
    print("====================================================================================================================")
    dispArgs(allArgs) # Display all args
    os.system(commandToRun) # Execute O2 generated commands
    runPycacheRemover() # Run pycacheRemover


if __name__ == '__main__':
    sys.exit(main())
