#!/usr/bin/ env python3
"""A python function to list all the document with a particular topic"""


import pymongo

def schools_by_topic(mongo_collection, topic):
    """returns a list contsining school with particular topic"""
    return mongo_collection.find({"topics": topic})

