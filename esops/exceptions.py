class EsOesException(Exception):
    """
    Base class for all exceptions raised by esops which are not Elasticsearch
    exceptions.
    """


class FailedExecution(EsOesException):
    """
        Exception raised when an action fails to execute for some reason.
    """
