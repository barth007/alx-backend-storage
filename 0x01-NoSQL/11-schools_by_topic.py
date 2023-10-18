#!/usr/bin/env python3
"""
This scripts checks if a particular topic is present in a collection
and returns a list of it
"""


def schools_by_topic(mongo_collection, topic):
    """
    checks if a topic is present and returns a list of them
    """

    result = mongo_collection.find({'topics': {'$in': [topic]}})
    return result


if __name__ == "__main__":
    schools_by_topic(mongo_collection, topic)
