#!/usr/bin/env python3
"""
This take an argument of List type and list all
document in a collection or empty if otherwise
"""


def list_all(mongo_collection):
    """
    This list all document in a collection
    """

    all_collections = []
    for doc in mongo_collection.find():
        all_collections.append(doc)

    if not all_collections:
        return all_collections
    return all_collections


if __name__ == "__main__":
    list_all(mongo_collection)
