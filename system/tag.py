# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103,R0913

"""Tag Functions
The following functions give you access to interact with Ignition Tags."""

__all__ = [
    'browseTags',
    'read'
]


def browseTags(parentPath="", tagPath=None, tagType=None, dataType=None, udtParentType=None,
               recursive=False, sort="ASC"):
    """Returns an array of tags from a specific folder. The function supports filtering and
    recursion. Leave filters blank to return all tags.

    If called in the gateway scope, a Tag Provider must be specified.

    Args:
        parentPath (str): The parent folder path. Leave blank for the root folder. Note: you can
            specify the tag provider name in square brackets at the beginning of the parentPath
            string. Example: "[myTagProvider]MyTagsFolder". If the tag provider name is left off
            then the project default provider will be used.
        tagPath (str): Filters on a tag path. Use * as a wildcard for any number of characters and
            a ? for a single character.
        tagType (str): Filters on a tag type. Possible values are OPC, MEMORY, DB, QUERY, Folder,
            DERIVED and UDT_INST.
        dataType (): The data type of the tag. Not used for UDT instances or folders. Possible
            values are Int1, Int2, Int4, Int8, Float4, Float8, Boolean, String, and DateTime.
        udtParentType (str): The name of the parent UDT.
        recursive (bool): Recursively search for tags inside of folders. Note: It is highly
            recommended that recursive is set to false, as server timeouts are more likely to
            occur.
        sort (str): Sets the sort order, possible values are ASC and DESC. Sorting is done on the
            full path of the tag.

    Returns:
        list[BrowseTag]: An array of BrowseTag. BrowseTag has the following variables: name, path,
            fullPath, type, dataType, and the following functions: isFolder(), isUDT(), isOPC(),
            isMemory(), isExpression(), isQuery().
    """
    print(parentPath, tagPath, tagType, dataType, udtParentType, recursive, sort)


def read(tagPath):
    """Reads the value of the tag at the given tag path. Returns a qualified value object. You can
    read the value, quality, and timestamp from this object. If the tag path does not specify a tag
    property, then the Value property is assumed.

    You can also read the value of tag attributes by appending the attribute to the tagPath
    parameter. See the Tag Attributes page for a list of available attributes.

    Args:
        tagPath (str): Reads from the given tag path. If no property is specified in the path, the
            Value property is assumed.

    Returns:
        QualifiedValue: A qualified value. This object has three sub-members: value, quality, and
            timestamp.
    """
    print tagPath
