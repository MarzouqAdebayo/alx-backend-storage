#!/usr/bin/env python3
"""Module '11-schools_by_topic.py' contains function schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic."""
    topic_filter = {
        "topics": {
            "$elemMatch": {
                "$eq": topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
