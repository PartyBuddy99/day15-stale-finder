import json
import os
import sys
import boto3
from datetime import datetime, timedelta, timezone

def main():
    days = int(sys.argv[1])
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    session = boto3.Session(profile_name='devops-learner')
    s3 = session.client("s3")

    with open("config.json") as json_file:
        config = json.load(json_file)
        bucket_name = config["bucket"]
        response = s3.list_objects(Bucket=bucket_name)
        for obj in response["Contents"]:
            if obj["LastModified"] < cutoff:
                print("Filename:", obj["Key"], ",FileSize:", obj["Size"], ",Last-modified:",obj["LastModified"])

if __name__ == "__main__":
    main()