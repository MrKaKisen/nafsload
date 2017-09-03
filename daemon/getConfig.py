# nafsload (c) Vilhelm Prytz 2017
# getConfig
# functions for parsing configuration files

import ConfigParser

# this thing with parsing configs using objects is kinda "sloopy". I'll re-do it sometime :)

configDir =
limitsConfigDir =
actionsConfigDir =

class Config(object):
    import ConfigParser

    def __init__(self, configFile):
        parser = ConfigParser.ConfigParser()
        parser.read(configFile)

        try:
            # main section
            self.checkInterval = parser.get("nafsload", "checkInterval")
            self.debugMode = parser.getboolean("nafsload", "debug")

            # email section
            self.email_server = parser.get("email", "server")
            self.email_port = parser.get("email", "port")
            self.email_username = parser.get("email", "username")
            self.email_password = parser.get("email", "password")


        except ConfigParser.MissingSectionHeaderError or ConfigParser.ParsingError:
            log("FATAL", "Could not read config. Please check your config if it's setup properly.")
            quit(1)

class LimitsConfig(object):
    import ConfigParser

    def __init__(self, configFile):
        parser = ConfigParser.ConfigParser()
        parser.read(configFile)

        self.limits = []
        self.limitsActions = []

        for section in parser.sections():
            try:
                self.limits.append(section)
                self.limitsActions.append(parser.get(section, "Actions"))
            except ConfigParser.MissingSectionHeaderError or ConfigParser.ParsingError:
                log("FATAL", "error occured reading limits config.")
                quit(1)


class ActionsConfig(object):
    import ConfigParser

    def __init__(self, configFile):
        parser = ConfigParser.ConfigParser()
        parser.read(configFile)

        self.actions = []
        self.actionsCommand = []

        for section in parser.sections():
            try:
                self.actions.append(section)
                self.actionsCommand.append(parser.get(section, "command"))
            except ConfigParser.MissingSectionHeaderError or ConfigParser.ParsingError:
                log("FATAL", "error occured reading actions config.")
                quit(1)


def getConfigs():
    config = Config(configDir)
    limitsConfig = LimitsConfig(limitsConfigDir)
    actionsConfig = ActionsConfig(actionsConfigDir)

    return config, limitsConfig, actionsConfig
