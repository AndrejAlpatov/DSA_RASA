"""
This module comprise functions to operate with MongoDB
"""


from .file_for_internal_usage import client_mongoDB


# Get date bank access and then collections from DB
def data_bank_access(collections_names_in):
    """
    A function to return any collections from MongoDB

    Args:
        collections_names_in(list): A list with collection names as strings

    Returns:
        Collections from MongoDB, which names were passed as a parameter
    """

    # get Database
    client = client_mongoDB
    database = client.get_database("MensaSkill")

    # get all collections from DB
    all_collections_list = []
    collections_to_be_returned = []

    # Get names of all collections in DB
    collections_names = database.list_collection_names()

    # add names of collections to the list
    for collection_name in collections_names:
        all_collections_list.append(database[collection_name])

    # if the passed collection name exist, collection will be returned
    for collection_name_in in collections_names_in:
        if collection_name_in in collections_names:
            collections_to_be_returned.append(database[collection_name_in])

    return collections_to_be_returned
