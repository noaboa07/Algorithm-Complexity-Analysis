import random
import math
import time
import pickle
import os

# ----------------- Utility Functions ------------------

# Generate n unique random points in 2D space

def generate_points(n):
    points = set()
    while len(points) < n:
        x = random.randint(0, 1000000)
        y = random.randint(0, 1000000)
        points.add((x, y))
    return list(points)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# ----------------- Closest Pair Algorithms ------------------

def brute_force_closest_pair(points):
    min_dist = float('inf')
    pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return pair, min_dist

# Merge Sort for sorting points by x or y coordinate
def merge_sort(arr, coord='x'):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], coord)
    right = merge_sort(arr[mid:], coord)
    return merge(left, right, coord)

def merge(left, right, coord):
    merged = []
    i = j = 0
    key = 0 if coord == 'x' else 1
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Divide and Conquer Closest Pair

def divide_and_conquer_closest_pair(points):
    Px = merge_sort(points.copy(), 'x')
    Py = merge_sort(points.copy(), 'y')
    return _closest_pair(Px, Py)

def _closest_pair(Px, Py):
    if len(Px) <= 3:
        return brute_force_closest_pair(Px)
    mid = len(Px) // 2
    Qx = Px[:mid]
    Rx = Px[mid:]
    midpoint = Px[mid][0]
    Qy = [p for p in Py if p[0] <= midpoint]
    Ry = [p for p in Py if p[0] > midpoint]
    (p1, q1), d1 = _closest_pair(Qx, Qy)
    (p2, q2), d2 = _closest_pair(Rx, Ry)
    delta = min(d1, d2)
    min_pair = (p1, q1) if d1 < d2 else (p2, q2)
    strip = [p for p in Py if abs(p[0] - midpoint) < delta]
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 16, len(strip))):
            dist = distance(strip[i], strip[j])
            if dist < delta:
                delta = dist
                min_pair = (strip[i], strip[j])
    return min_pair, delta

# ----------------- Safe Experiment Runner ------------------

def run_experiments_safe(m=10):
    save_file = "experiment_results.pkl"

    # Safe alternate range
    n_values = list(range(10000, 55001, 5000))

    # Try to load previous results since i lost all my previous progress and it wouldnt save 
    if os.path.exists(save_file):
        with open(save_file, "rb") as f:
            results = pickle.load(f)
        print("Loaded saved progress.")
    else:
        results = {'n': [], 'ALG1_avg': [], 'ALG2_avg': []}

    for n in n_values:
        if n in results['n']:
            print(f"Skipping n = {n} (already done)")
            continue

        print(f"Running n = {n}...")
        alg1_times = []
        alg2_times = []

        for i in range(m):
            print(f"   Iteration {i+1}/{m}")
            points = generate_points(n)

            # ALG1
            start = time.time()
            brute_force_closest_pair(points)
            alg1_times.append(time.time() - start)

            # ALG2
            start = time.time()
            divide_and_conquer_closest_pair(points)
            alg2_times.append(time.time() - start)

        avg1 = sum(alg1_times) / m
        avg2 = sum(alg2_times) / m
        results['n'].append(n)
        results['ALG1_avg'].append(avg1)
        results['ALG2_avg'].append(avg2)

        # Save after every `n` so we don't lose progress
        with open(save_file, "wb") as f:
            pickle.dump(results, f)
        print(f"Saved progress after n = {n}")

    print("✅ All experiments complete and saved.")
    return results

# ----------------- Run ------------------

if __name__ == "__main__":
    run_experiments_safe()
