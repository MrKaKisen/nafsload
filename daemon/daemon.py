# nafsload (c) Vilhelm Prytz 2017
# daemon
# main daemon file

# imports
import time
import os

# main daemon function
def runDaemon(config, limitsConfig, actionsConfig):
    stopDaemon = False

    while stopDaemon is False:

        currentLoad = os.getloadavg()[0]

        limitList = 0
        for limit in limitsConfig.limits:
            if int(currentLoad) >= int(limit):
                log("WARNING", "Load is over limit! (load " + currentLoad + " is over " + limit + ").")

                actionsPerform = limitsConfig.limitsActions[limitList].split()

                for action in actionsPerform:
                    actionsIteration = 0
                    for availableAction in actionsConfig.actions:
                        if action == availableAction:
                            actionsConfig.actionsCommand[actionsIteration]

                        actionsIteration = actionsIteration+1

            limitList = limitList+1


        time.sleep(int(config.checkInterval))
