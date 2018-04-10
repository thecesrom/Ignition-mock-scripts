# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103

"""Utility Functions
The following functions give you access to view various Gateway and Client data, as well as interact
with other various systems."""

__all__ = [
    'getGatewayAddress',
    'getProjectName',
    'setLocale',
    'translate'
]


def getGatewayAddress():
    """Returns the address of the gateway that the client is currently communicating with.

    Returns:
        str: The address of the Gateway that the client is communicating with.
    """
    return 'http://localhost:8088/main'


def getProjectName():
    """Returns the name of the project that is currently being run.

    Returns:
        str: The name of the currently running project.
    """
    return 'MyProject'


def jsonDecode(jsonString):
    """Takes a json String and converts it into a Python object such as a list or a dict. If the
    input is not valid json, a string is returned.

    Args:
        jsonString (str): The JSON string to decode into a Python object.

    Returns:
        object: The decoded Python object.
    """
    print(jsonString)
    return object


def setLocale(locale):
    """Sets the user's current Locale. Any valid Java locale code (case-insensitive) can be used as
    a parameter, including ones that have not yet been added to the Translation Manager. An invalid
    locale code will cause an Illegal Argument Exception.

    Args:
        locale (str): A locale code, such as 'en_US' for US English.
    """
    print locale


def translate(term):
    """This function allows you to retrieve the global translation of a term from the translation
    database using the current locale.

    Args:
        term (str): The term to look up.

    Returns:
        str: The translated term.
    """
    return term
