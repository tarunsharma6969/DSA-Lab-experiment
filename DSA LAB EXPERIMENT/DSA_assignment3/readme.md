# Data Structures Assignment 3 – Sorting Algorithms Benchmark

## Course:
ETCCDS202 – Data Structures

## Assignment:
Unit 3 – Sorting Algorithms (Insertion Sort, Merge Sort, Quick Sort + Benchmarking)

---

# Objective
This assignment implements and compares three major sorting algorithms:

- Insertion Sort
- Merge Sort
- Quick Sort

The project benchmarks their performance on different dataset types and sizes to compare theoretical complexity with practical execution.

---

# Algorithms Implemented

## 1. Insertion Sort
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)
- Stable: Yes
- In-Place: Yes

## 2. Merge Sort
- Best/Average/Worst Case: O(n log n)
- Stable: Yes
- In-Place: No
- Extra Space: O(n)

## 3. Quick Sort
- Best/Average Case: O(n log n)
- Worst Case: O(n²)
- Stable: No
- In-Place: Yes

---

# Dataset Types Used
The algorithms were tested on:

- Random Data
- Sorted Data
- Reverse Sorted Data

---

# Dataset Sizes
- 1000
- 5000
- 10000

---

# Features
- Automatic dataset generation
- Performance timing using `time.perf_counter()`
- Comparison across multiple input patterns
- Demonstrates worst-case and best-case scenarios
- Theory vs Practical performance analysis

---

# Key Observations

## Insertion Sort:
- Performs well on nearly sorted data
- Very slow on large random/reverse datasets

## Merge Sort:
- Consistent and reliable performance
- Stable sorting
- Requires additional memory

## Quick Sort:
- Usually fastest in practice
- Can degrade on bad pivot selection
- Improved using middle pivot strategy

---

# Files Included
```bash
assignment3_sorting.py
README.md