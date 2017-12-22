# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103

"""Security Functions
The following functions give you access to interact with the users and roles in the Gateway."""

__all__ = [
    'getRoles',
    'getUsername'
]


def getRoles():
    """Finds the roles that the currently logged in user has, returns them as a Python tuple of
    strings.

    Returns:
        tuple: A list of the roles (strings) that are assigned to the current user.
    """
    return ('Administrator', 'Developer')


def getUsername():
    """Returns the currently logged-in username.

    Returns:
        str: The current username.
    """
    return 'johdoe'
