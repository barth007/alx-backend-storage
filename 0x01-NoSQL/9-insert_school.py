#!/usr/bin/env python3
"""
This script inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    it inserts a new document in a collection
    """

    item = kwargs
    mongo_collection.insert_one(item)
    return mongo_collection.inserted_id


if __name__ == "__main__":
    insert_school(mongo_collection, **kwargs)
