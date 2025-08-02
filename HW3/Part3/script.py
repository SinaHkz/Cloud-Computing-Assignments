import requests
import time
import random
import string
import threading

def generate_random_string(length=10000):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def cpu_stress(n=50000):
    # Simulate CPU work with floating-point calculations
    x = 0.0
    for i in range(n):
        x += (i ** 0.5) / (i + 1)
    return x

def send_requests(duration=60, url="http://127.0.0.1:8080/function/to-uppercase"):
    end_time = time.time() + duration
    with open("function_results.txt", "a") as file:
        while time.time() < end_time:
            _ = cpu_stress()  # CPU stress before each request
            data = generate_random_string()
            try:
                response = requests.post(url, data=data)
                file.write(response.text + "\n")
            except Exception as e:
                file.write(f"Error: {e}\n")

# Start multiple threads to simulate load
threads = []
for _ in range(3):  # Adjust thread count based on your CPU cores
    t = threading.Thread(target=send_requests)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
