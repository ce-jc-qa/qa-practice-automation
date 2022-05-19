import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('/Users/jpayos/PycharmProjects/BackendAutomation/utilities/properties.ini')
    return config


def getPassword():
    return "Vios021628$$"
