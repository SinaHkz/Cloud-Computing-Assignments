import subprocess
import ray

# Start Ray
ray.init(address="auto")

# Fetch Zen of Python
zen_of_python = subprocess.check_output(["python", "-c", "import this"])
corpus = zen_of_python.split()

# Partition data into chunks
num_partitions = 3
chunk = len(corpus) // num_partitions
partitions = [
    corpus[i * chunk: (i + 1) * chunk] for i in range(num_partitions)
]

# --- Map Phase ---

def map_function(document):
    for word in document.lower().split():
        yield word.encode("utf-8"), 1

@ray.remote
def apply_map(corpus_partition, num_partitions=3):
    map_results = [[] for _ in range(num_partitions)]
    for word in corpus_partition:
        for result in map_function(word.decode("utf-8")):
            first_letter = result[0].decode("utf-8")[0]
            word_index = ord(first_letter) % num_partitions
            map_results[word_index].append(result)
    return map_results

# Launch map tasks in parallel
map_tasks = [
    apply_map.options(num_returns=num_partitions).remote(part, num_partitions)
    for part in partitions
]

# Transpose the results: group outputs by reducer
partitions_for_reduce = [[] for _ in range(num_partitions)]
for i in range(num_partitions):
    results = ray.get(map_tasks[i])
    for j in range(num_partitions):
        partitions_for_reduce[j].append(results[j])

# --- Reduce Phase ---

@ray.remote
def apply_reduce(*mapper_outputs):
    reduced = dict()
    for output in mapper_outputs:
        for key, val in output:
            reduced[key] = reduced.get(key, 0) + val
    return reduced

# Launch reduce tasks
reduce_tasks = [
    apply_reduce.remote(*partitions_for_reduce[i])
    for i in range(num_partitions)
]

# Collect and aggregate final counts
final_counts = {k: v for result in ray.get(reduce_tasks) for k, v in result.items()}

for word, count in sorted(final_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{word.decode('utf-8')}: {count}")
