# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103,C0111,R0201

"""Database Functions
The following functions give you access to view and modify data in the database."""

__all__ = [
    'createSProcCall',
    'execSProcCall'
]

# Type codes
# These are codes defined by the JDBC specification.
BIT = -7
REAL = 7
LONGVARCHAR = -1
LONGVARBINARY = -4
BLOB = 2004
TINYINT = -6
DOUBLE = 8
DATE = 91
NULL = 0
CLOB = 2005
SMALLINT = 5
NUMERIC = 2
TIME = 92
OTHER = 1111
JAVA_OBJECT = 2000
INTEGER = 4
DECIMAL = 3
TIMESTAMP = 93
SQLXML = 2009
DATALINK = 70
BIGINT = -5
CHAR = 1
BINARY = -2
NCLOB = 2011
BOOLEAN = 16
FLOAT = 6
VARCHAR = 12
VARBINARY = -3
ARRAY = 2003
ROWID = -8
NCHAR = -15
NVARCHAR = -9
LONGNVARCHAR = -16


class _SProcCall(object):
    def __init__(self):
        pass

    def getResultSet(self):
        """Returns a dataset that is the resulting data of the stored procedure, if any.

        Returns:
            Dataset: The dataset that is the resulting data of the stored procedure, if any.
        """
        pass

    def getUpdateCount(self):
        """Returns the number of rows modified by the stored procedure, or -1 if not applicable.

        Returns:
             int: The number of rows modified by the stored procedure, or -1 if not applicable.
        """
        return 1

    def getReturnValue(self):
        """Returns the return value, if registerReturnParam had been called.

        Returns:
             int: The return value, if registerReturnParam had been called.
        """
        return 0

    def getOutParamValue(self, param):
        """Returns the value of the previously registered out-parameter.

        Args:
            param: Index (int) or name (str) of the previously registered out-parameter.

        Returns:
            value: The value of the previously registered out-parameter.
        """
        print param
        return 0

    def registerInParam(self, param, typeCode, value):
        """Registers an in parameter for the stored procedure.

        Args:
            param (object): Index (int starting at 1, not 0), or name (str).
            typeCode (int): Type code constant.
            value (object): Value of type `typeCode`.
        """
        print(param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        """Registers an out parameter for the stored procedure.

        Args:
            param (object): Index (int starting at 1, not 0), or name (str).
            typeCode (int): Type code constant.
        """
        print(param, typeCode)

    def registerReturnParam(self, typeCode):
        """Use this function to specify the datatype of the returned value.

        Args:
            typeCode (int): Type code constant.
        """
        print typeCode


def createSProcCall(procedureName, database=None, tx=None, skipAudit=None):
    """Creates an SProcCall object, which is a stored procedure call context.

    Args:
        procedureName (str): The named of the stored procedure to call.
        database (Optional[str]): The name of the database connection to execute against. If omitted
            or "", the project's default database connection will be used.
        tx ((Optional[str]): A transaction identifier. If omitted, the call will be executed in its
            own transaction.
        skipAudit ((Optional[bool]): A flag which, if set to true, will cause the procedure call to
            skip the audit system. Useful for some queries that have fields which won't fit into the
            audit log.

    Returns:
        SProcCall: A stored procedure call context, which can be configured and then used as the
            argument to system.db.execSProcCall.
    """
    print(procedureName, database, tx, skipAudit)
    return _SProcCall()


def execSProcCall(callContext):
    """Executes a stored procedure call. The one parameter to this function is an SProcCall - a
    stored procedure call context. See the description of system.db.createSProcCall for more
    information and examples.

    Args:
        callContext (SProcCall): A stored procedure call context, with any input, output, and/or
            return value parameters correctly configured. Use system.db.createSProcCall to create a
            call context.
    """
    print callContext
