# nafsload (c) Vilhelm Prytz 2017
# __main__
# main file

from getConfig import *
from daemon import runDaemon

config, limitsConfig, actionsConfig = getConfig()

runDaemon(config, limitsConfig, actionsConfig)
