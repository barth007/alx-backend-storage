#!/usr/bin/env python3
"""
This scipt changes all topics of a collection document
base on their names
"""


def update_topics(mongo_collection, name, topics):
    """
    This updates a collection document based on their name
    """

    result = mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
        )
    return result


if __name__ == "__main__":
    update_topics(mongo_collection, name, topics)
