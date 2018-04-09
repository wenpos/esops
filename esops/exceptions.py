class EsopsException(Exception):
    """
    Base class for all exceptions raised by esops which are not Elasticsearch
    exceptions.
    """


class FailedExecution(EsopsException):
    """
        Exception raised when an action fails to execute for some reason.
    """

class ConfigurationError(EsopsException):
    """
    Exception raised when a misconfiguration is detected
    """

class MissingArgument(EsopsException):
    """
    Exception raised when a needed argument is not passed.
    """