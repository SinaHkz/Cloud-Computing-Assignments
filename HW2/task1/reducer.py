#!/usr/bin/env python3
import sys

current_id = None
sum_value = 0.0
count = 0

# iterate over the lines from standard input whcih is the output of the mapper
# The output of the mapper is written on hdfs and 
# get sorted by client_id in shuffle phase before it is passed to the reducer
for line in sys.stdin:
    # extract the client_id and feature_value from the line
    client_id, val_count = line.strip().split('\t')
    val, cnt = val_count.split(',')
    val = float(val)
    cnt = int(cnt)

    # if the client_id is the same as the current_id,
    # add the feature_value and count to the sum and count
    # otherwise, print the current_id and sum_value, and reset the sum and count
    if client_id == current_id:
        sum_value += val
        count += cnt
    else:
        if current_id:
            print(f"{current_id}\t{sum_value}\t{count}") # write the result of the previous client_id
        current_id = client_id
        sum_value = val
        count = cnt

if current_id:
    print(f"{current_id}\t{sum_value}\t{count}")
