#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

#itertate over the rows in the CSV file
for row in reader:
    client_id = row[0] # extract the client_id 
    # ignore the header line
    if client_id == "client_id":
        continue
    feature_value = float(row[1]) # extract the feature_value
    print(f"{client_id}\t{feature_value},1") # print the client_id and feature_value as key-value pair in hdfs
