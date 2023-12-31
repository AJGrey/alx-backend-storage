#!/usr/bin/env python3
""" A python function that changes the topics of all documents based on the name
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of all documents"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

