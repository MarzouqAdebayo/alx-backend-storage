#!/usr/bin/env python3
"""Module '101-students.py' contains function top_students """


def top_students(mongo_collection):
    """Compute the average score of each student"""
    pipeline = [
        {"$project": {
            "_id": 1,
            "name": 1,
            "averageScore": {
                "$avg": "$topics.score"
            }
        }},
        {"$sort": {"averageScore": -1}},
    ]
    result = mongo_collection.aggregate(pipeline)
    return result
