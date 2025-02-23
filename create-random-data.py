import random
import time
import json

def createDatabase(size, maxNumber):
    t1 = time.perf_counter()
    filename = f'db{size}params.json' 
    numbers = random.choices(range(1, maxNumber + 1), k=size)

    try:
        with open(filename, "w") as f:
            json.dump(numbers, f)
    except IOError as e:
        print(f"File error: {e}")

    t2 = time.perf_counter()
    print(f'Generated {filename} in {t2 - t1:.4f} seconds')

for size in range(5000, 50001, 5000):
    createDatabase(size, 1000000)
