#!/usr/bin/env python3
"""
This script inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    it inserts a new document in a collection
    """

    item = dict(kwargs)
    mongo_collection.insert_one(item)
    return mongo_collection.inserted_id
