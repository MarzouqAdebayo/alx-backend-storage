#!/usr/bin/env python3
"""Module '12-log_stats.py' contains function print_nginx_request logs """
from pymongo import MongoClient


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
    pipeline = [
        {"$group": {"_id": "$ip", "total_requests": {"$sum": 1}}},
        {"$sort": {"total_requests": -1}},
        {"$limit": 10},
    ]
    request_logs = nginx_collection.aggregate(pipeline)
    for request_log in request_logs:
        ip_address = request_log.get("_id")
        request_count_from_ip_address = request_log.get("total_requests")
        print("\t{}: {}".format(ip_address, request_count_from_ip_address))


def run():
    """Provides some stats about Nginx logs stored in MongoDB."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    print_nginx_request_logs(client.logs.nginx)


if __name__ == "__main__":
    run()
