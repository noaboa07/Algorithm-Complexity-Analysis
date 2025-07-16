import pickle
import math
import matplotlib.pyplot as plt

# --------------------- Load Saved Experiment Data ---------------------
with open("experiment_results.pkl", "rb") as f:
    results = pickle.load(f)

n_values = results['n']
alg1_avg = results['ALG1_avg']  # Brute-force
alg2_avg = results['ALG2_avg']  # Divide & Conquer

# --------------------- Table Generators ---------------------

def generate_table_alg1(n_vals, empirical_rts):
    print("Table for ALG1 (Brute-Force, Θ(n²))")
    theoretical = [n**2 for n in n_vals]
    ratios = [empirical / t for empirical, t in zip(empirical_rts, theoretical)]
    c1 = max(ratios)
    predicted = [c1 * t for t in theoretical]

    print(f"{'n':>8} | {'n^2':>15} | {'EmpiricalRT(ms)':>15} | {'Ratio':>10} | {'PredictedRT(ms)':>15}")
    print("-" * 75)
    for i in range(len(n_vals)):
        print(f"{n_vals[i]:>8} | {theoretical[i]:>15} | {empirical_rts[i]*1000:>15.3f} | {ratios[i]:>10.2e} | {predicted[i]*1000:>15.3f}")
    print(f"\nEstimated constant c1 = {c1:.2e}")
    return theoretical, predicted, c1

def generate_table_alg2(n_vals, empirical_rts):
    print("\nTable for ALG2 (Divide & Conquer, Θ(n log₂ n))")
    theoretical = [n * math.log2(n) for n in n_vals]
    ratios = [empirical / t for empirical, t in zip(empirical_rts, theoretical)]
    c2 = max(ratios)
    predicted = [c2 * t for t in theoretical]

    print(f"{'n':>8} | {'n·log₂n':>15} | {'EmpiricalRT(ms)':>15} | {'Ratio':>10} | {'PredictedRT(ms)':>15}")
    print("-" * 75)
    for i in range(len(n_vals)):
        print(f"{n_vals[i]:>8} | {theoretical[i]:>15.2f} | {empirical_rts[i]*1000:>15.3f} | {ratios[i]:>10.2e} | {predicted[i]*1000:>15.3f}")
    print(f"\nEstimated constant c2 = {c2:.2e}")
    return theoretical, predicted, c2

# --------------------- Graph Plots ---------------------

def plot_alg1_vs_alg2(n, alg1, alg2):
    plt.figure(figsize=(10, 6))
    plt.plot(n, [t * 1000 for t in alg1], marker='o', label='ALG1: Brute Force')
    plt.plot(n, [t * 1000 for t in alg2], marker='s', label='ALG2: Divide & Conquer')
    plt.title('Graph 1: Empirical Runtime Comparison')
    plt.xlabel('Input Size n')
    plt.ylabel('Average Runtime (ms)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_empirical_vs_predicted(n, empirical, predicted, title, label):
    plt.figure(figsize=(10, 6))
    plt.plot(n, [t * 1000 for t in empirical], marker='o', label=f'{label}: EmpiricalRT')
    plt.plot(n, [t * 1000 for t in predicted], marker='s', label=f'{label}: PredictedRT')
    plt.title(title)
    plt.xlabel('Input Size n')
    plt.ylabel('Runtime (ms)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# --------------------- Execute ---------------------

print("== Generating Tables and Graphs ==")
alg1_theo, alg1_pred, c1 = generate_table_alg1(n_values, alg1_avg)
alg2_theo, alg2_pred, c2 = generate_table_alg2(n_values, alg2_avg)

# Graph 1: Empirical Runtime Comparison
plot_alg1_vs_alg2(n_values, alg1_avg, alg2_avg)

# Graphs 2 and 3: Empirical vs Predicted
plot_empirical_vs_predicted(n_values, alg1_avg, alg1_pred, "ALG1: Empirical vs Predicted", "Brute Force")
plot_empirical_vs_predicted(n_values, alg2_avg, alg2_pred, "ALG2: Empirical vs Predicted", "Divide & Conquer")
