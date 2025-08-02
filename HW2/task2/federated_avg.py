from pyspark import SparkContext
import random

# Init Spark context: the entry point for Spark applications, allows us to connect to a Spark cluster and create RDDs.
sc = SparkContext(appName="FederatedAveraging")

# input file path of HDFS outpuy
file_path = "/app/hadoop_output.txt"
output_log_path = "/app/output.txt"

lines = sc.textFile(file_path)

# This function convert each line into the mentioned format: (client_id, (sum, count))
def parse_line(line):
    parts = line.strip().split("\t")
    client_id = parts[0]
    feature_sum = float(parts[1])
    count = int(parts[2])
    return (client_id, (feature_sum, count))

client_data = lines.map(parse_line)

# Read features and counts as RDDs and setting a map: Transformation
# Calculate the global average bu summing all the feature sums and counts: Action
total_sum = client_data.map(lambda x: x[1][0]).sum()
total_count = client_data.map(lambda x: x[1][1]).sum()
global_average = total_sum / total_count

log_lines = []
log_lines.append(f"\nInitial Global Average: {global_average:.4f}\n")
print(f"\nInitial Global Average: {global_average:.4f}\n")

for round_num in range(1, 4):
    log_lines.append(f"--- Round {round_num} ---\n")
    print(f"--- Round {round_num} ---")

    # Calculate local averages
    local_averages = client_data.map(lambda x: (x[0], x[1][0] / x[1][1]))

    # Adding some noise to the local averages.
    updated_averages = local_averages.mapValues(lambda avg: avg + random.uniform(-1, 1))

    # Recalculate global average
    # map : Transformation & mean: Action
    # The map function is used to extract the updated averages, and the mean function calculates the average of these values.
    global_average = updated_averages.map(lambda x: x[1]).mean()

    for client_id, updated_avg in updated_averages.collect():
        line = f"{client_id} updated average: {updated_avg:.4f}"
        print(line)
        log_lines.append(line + "\n")
    
    log_lines.append(f"Global Average after Round {round_num}: {global_average:.4f}\n\n")
    print(f"Global Average after Round {round_num}: {global_average:.4f}\n")

sc.stop()

# Save log to file
with open(output_log_path, "w") as f:
    f.writelines(log_lines)
