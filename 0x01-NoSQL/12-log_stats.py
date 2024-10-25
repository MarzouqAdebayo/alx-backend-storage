#!/usr/bin/env python3
"""Module '12-log_stats.py' contains function print_nginx_request logs """


def print_nginx_request_logs(nginx_collection):
    """Prints stats about Nginx request logs."""
    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    pipeline = [{"$group": {"_id": "$method", "count": {"$sum": 1}}}]
    result = {
        item["_id"]: item["count"]
        for item in list(nginx_collection.aggregate(pipeline))
    }
    for method in methods:
        if method in result.keys():
            print("\tmethod {}: {}".format(method, result[method]))
        else:
            print("\tmethod {}: {}".format(method, 0))
    status_checks_count = len(
        list(nginx_collection.find({"method": "GET", "path": "/status"}))
    )
    print("{} status check".format(status_checks_count))
