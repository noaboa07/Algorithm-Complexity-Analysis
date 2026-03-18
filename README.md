# Algorithm Complexity Analysis: Closest Pair of Points
### Empirical Performance & Optimization Study | Noah Russell

This project explores the practical performance differences between two fundamental algorithmic approaches to the **Closest Pair of Points** problem in 2D space. By comparing a naive approach against a recursive optimization, this study validates theoretical Big-O complexity through empirical execution data.

---

## 🧠 Algorithms Implemented

### 1. Brute-Force (Θ(n²))
A baseline implementation that computes the Euclidean distance between every possible pair of points. While simple, the computational cost grows quadratically as $n$ increases, making it inefficient for large-scale geospatial data.



### 2. Divide & Conquer (Θ(n log n))
An optimized recursive approach that partitions the plane into halves, solves for each sub-problem, and efficiently processes the "strip" near the partition line. This implementation significantly reduces the search space, aligning with the theoretical $n \log n$ efficiency required for high-performance systems.



---

## 📊 Experimental Methodology
* **Data Generation:** Automated generation of $n$ unique random points in a $1,000,000 \times 1,000,000$ coordinate plane.
* **Logging & Persistence:** Utilized `pickle` for safe experiment state persistence, allowing for large-scale data collection across multiple hardware sessions without data loss.
* **Verification:** Empirical runtimes (ms) were captured using the `time` library and benchmarked against predicted theoretical curves using calculated constants ($c_1, c_2$).

---

## 📈 Key Findings
The results clearly demonstrate the "crossover point" where the $\Theta(n \log n)$ optimization begins to drastically outperform the brute-force method. This project provides a real-world validation of how algorithmic scaling directly impacts system latency and resource consumption in production environments.

---
**Noah Russell** | Master of Science in AI (May 2026)
[LinkedIn](https://www.linkedin.com/in/your-profile) | [Email](mailto:noahrussell2004@gmail.com)
