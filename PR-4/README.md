<div align="center">

# -- ! Data Analyser & Transformer ! --
### *Interactive Console-Based Data Analysis, Filtering & Sorting Tool*

<br/>

> *"Data is only as useful as the tools that analyse it — build those tools, and you command the information."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📥 Part A — Data Input](#-part-a--data-input)
- [📊 Part B — Data Analysis & Operations](#-part-b--data-analysis--operations)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Data Analyser & Transformer** is a beginner-friendly, interactive Python console application that demonstrates core programming concepts such as **recursion**, **lambda functions**, **nested loops**, **list manipulation**, and **user-defined functions**. The program presents a menu-driven interface that runs continuously until the user chooses to exit.

This project is designed to:
- Strengthen understanding of 1D arrays and 2D matrices (lists of lists)
- Practice user input handling and menu-driven program design
- Apply recursive logic for mathematical computations (Factorial)
- Use lambda functions for clean, concise data filtering
- Implement sorting algorithms using Python's built-in sort utilities

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool to insert, analyse, filter, and sort 1D and 2D array data.

You are building a data analysis utility for students learning Python. The program must accept user choices from a menu and execute the corresponding task — whether inserting array data, summarising statistics, computing factorials, filtering by threshold, or sorting the data.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Input | Console Input | Accepts 1D arrays or 2D matrices from user or sample |
| Data Summary | Analysis | Displays count, min, max, sum, and average |
| Factorial Calculator | Recursion | Computes n! using a recursive function |
| Filter By Threshold | Lambda + Loop | Filters elements greater than or equal to a threshold |
| Sort Data | Built-in Sort | Sorts 1D arrays or 2D matrices in ascending or descending order |

The goal is to demonstrate **fundamental Python programming skills** — functions, recursion, lambdas, and nested loops — through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📐 **1D & 2D Support** | Handles both single-dimension arrays and multi-row matrices |
| 🧮 **Recursive Factorial** | Computes factorial of any integer using recursion |
| 📊 **Data Summary** | Reports total elements, min, max, sum, and average |
| 🔍 **Lambda Filtering** | Uses a lambda expression to filter values by threshold |
| 🔃 **Dual Sorting** | Supports both ascending and descending sort for 1D and 2D data |
| 🖥️ **CLI Interface** | Simple, clean text-based menu for user interaction |
| 🧪 **Sample Array** | Built-in sample 1D array for quick testing without manual input |

---

## 🏗️ Project Structure

```
📦 data-analyser-transformer/
│
├── 📄 DataAnalyser.py       ← Main Python script (entry point)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────────┐
│      Display Main Menu          │  ← 6 Options shown in a loop
└──────────────┬──────────────────┘
               │
   ┌───────────┼──────────────────────────┐
   ▼           ▼           ▼             ▼
┌───────┐  ┌───────┐  ┌─────────┐  ┌──────────┐
│ Insert│  │Summary│  │Factorial│  │Filter /  │
│ Array │  │ (2)   │  │  (3)    │  │Sort(4,5) │
│  (1)  │  └───┬───┘  └────┬────┘  └────┬─────┘
└───┬───┘      │           │            │
    │          ▼           ▼            ▼
    │    ┌──────────┐ ┌─────────┐ ┌──────────────┐
    │    │Count/Min/│ │ n*(n-1) │ │ Lambda Filter│
    │    │Max/Sum/  │ │ *...*1  │ │ / .sort()    │
    │    │  Avg     │ └─────────┘ └──────────────┘
    │    └──────────┘
    ▼
┌──────────────────┐
│ 1D Array or 2D   │
│ Matrix Input     │
│ (Sample/Manual)  │
└──────────────────┘
             │
             ▼
    Loop Back to Menu
             │
      (Choice: 6) Exit ✅
```

---

## 📥 Part A — Data Input

### 📝 1. What is Array Input?

The program supports two types of data structures: a **1D array** (a flat list of integers) and a **2D matrix** (a list of lists). The user selects the dimension and either enters values manually or uses a built-in sample array.

---

### 🗺️ 2. Input Modes — Overview

| Mode | Dimension | Method |
|------|-----------|--------|
| 1️⃣ | **1D Array — Sample** | Loads `[10, 3, 7, 32, 21, 76, 80, 110, 6, -7]` automatically |
| 2️⃣ | **1D Array — Manual** | User specifies size and enters each element |
| 3️⃣ | **2D Matrix — Manual** | User specifies rows × columns and fills each cell |

---

### 🔢 3. 1D Array Input

> User selects size and enters each element one by one, indexed from `a[0]`.

**Logic:**
```python
size = int(input("Enter array size: "))
for i in range(size):
    ele = int(input(f"a[{i}] : "))
    input_array_1D.append(ele)
```

**Sample Output:**
```
Enter array size: 4
a[0] : 10
a[1] : -3
a[2] : 22
a[3] : 7
The following is the input array: [10, -3, 22, 7]
```

---

### 🏢 4. 2D Matrix Input

> User defines row and column count, then fills each cell using nested index notation `a[row][col]`.

**Logic:**
```python
for r in range(row):
    row_ele = []
    for c in range(col):
        ele = int(input(f"a[{r}][{c}] : "))
        row_ele.append(ele)
    matrix.append(row_ele)
```

**Sample Output (3×3 matrix):**
```
a[0][0] : 2    a[0][1] : 7    a[0][2] : 9
a[1][0] : -4   a[1][1] : 5    a[1][2] : 18
a[2][0] : 15   a[2][1] : -3   a[2][2] : -8

The following is the input Matrix:
2   7   9
-4  5   18
15  -3  -8
```

---

## 📊 Part B — Data Analysis & Operations

### 📈 5. Data Summary (Option 2)

> Computes and displays five key statistics for the loaded array or matrix.

**Key Concepts Used:**

| Statistic | 1D Method | 2D Method |
|-----------|-----------|-----------|
| Total Elements | `len(Array_1d)` | `len(matrix) * len(matrix[0])` |
| Minimum | `min(Array_1d)` | Custom `Min_2D()` function |
| Maximum | `max(Array_1d)` | Custom `Max_2D()` function |
| Sum | `sum(Array_1d)` | Custom `Sum_2D()` function |
| Average | `sum / len` | Custom `Avg_2D()` function |

**Sample Output (1D):**
```
Data Summary:
Total elements: 9
Minimum value : -190
Maximum value : 735
Sum of all values : 609
Average value: 67.67
```

**Sample Output (2D):**
```
Data Summary:
Total elements: 9
Minimum value : -8
Maximum value : 18
Sum of all values : 41
Average value: 4.56
```

---

### 🧮 6. Factorial Calculator — Recursion (Option 3)

> Computes n! using a recursive function that calls itself until the base case is reached.

**Logic:**
```python
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔁 **Recursion** | Function calls itself with `n - 1` until `n <= 1` |
| 🛑 **Base Case** | Returns `1` when `n <= 1` to stop recursion |
| ✖️ **Multiplication** | Each call multiplies `n` by the result of `fact(n-1)` |
| 📐 **Formula** | `fact(n) = n × (n-1) × (n-2) × ... × 2 × 1` |

**Sample Output:**
```
Enter a number to calculate it's factorial: 8
The Factorial of 8 is 40320
```

---

### 🔍 7. Filter Data By Threshold (Option 4)

> Uses a **lambda function** to filter and return all elements greater than or equal to a user-defined threshold value. Works for both 1D arrays and 2D matrices.

**Logic:**
```python
threshold = int(input("Enter a threshold value: "))
filter = lambda x: x >= threshold
filtered = []

for ele in Array_1d:          # For 1D
    if filter(ele):
        filtered.append(ele)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔍 **Lambda** | `lambda x: x >= threshold` defines an inline filter condition |
| 🔁 **Iteration** | Loops through all elements (flat or nested) |
| 📋 **List Building** | Appends qualifying elements to a new list |

**Sample Output (1D, threshold = 56):**
```
Elements greater than or equal to 56:
[82, 735]
```

**Sample Output (2D, threshold = 10):**
```
Elements greater than or equal to 10:
[18, 15]
```

---

### 🔃 8. Sort Data (Option 5)

> Sorts the loaded 1D array or 2D matrix in the user's chosen direction using Python's built-in sort utilities.

**Logic:**
```python
# 1D Ascending
Array_1d.sort()

# 1D Descending
Array_1d.sort(reverse=True)

# 2D Ascending
sorted_2d = sorted(matrix)

# 2D Descending
sorted_2d = sorted(matrix, reverse=True)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔃 `.sort()` | In-place sort for 1D arrays (modifies original list) |
| 📋 `sorted()` | Returns a new sorted list for 2D matrices |
| ↕️ `reverse=True` | Switches sort direction to descending |

**Sample Output (1D Ascending):**
```
Sorted array in ascending: [-190, -45, 3, 4, 6, 6, 8, 82, 735]
```

**Sample Output (2D Descending):**
```
Sorted matrix using sorted method: [[15, -3, -8], [2, 7, 9], [-4, 5, 18]]
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language |
| 🔁 **While Loop** | Built-in | Infinite menu loop control |
| 🔂 **For Loop** | Built-in | Array traversal and matrix iteration |
| 🧮 **Recursion** | Built-in | Factorial computation via self-calling function |
| 🔍 **Lambda** | Built-in | Inline filter condition for threshold comparison |
| 🔃 **sort / sorted** | Built-in | Ascending and descending sort operations |
| 🗂️ **match-case** | Python 3.10+ | Structured menu branching (structural pattern matching) |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |
| 📐 **f-strings** | Python 3.6+ | Formatted string output |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **1D & 2D Data Entry** — Flexible input supporting sample arrays and manual matrix entry
- 📊 **Statistical Summary** — Instant count, min, max, sum, and average for any loaded dataset
- 🧮 **Recursive Factorial** — Accurate computation of n! via clean recursive logic
- 🔍 **Threshold Filtering** — Lambda-powered filtering returns only qualifying elements
- 🔃 **Bidirectional Sorting** — Both ascending and descending sort available for 1D and 2D data
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core concepts — recursion, lambdas, loops, and I/O — in one project |
| 🔄 **Reusability** | Helper functions (`Max_2D`, `Min_2D`, `Sum_2D`, `Avg_2D`) are modular and reusable |
| 📚 **Educational** | Each feature reinforces a distinct Python concept with real outputs |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add new operations (median, standard deviation, matrix transpose, etc.) |
| 📖 **Readable Code** | Clear `match-case` and function-based structure makes logic easy to follow |
| 🛡️ **Dimension Guard** | Program validates array dimension input and prompts again on invalid entries |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Neev Shankar

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/)

> *"Every dataset has a story — write the code that tells it."*

**🎓 Role:** First-Year Engineering Student | Python Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Arrays · Recursion · Lambda Functions · CLI Applications · Data Analysis

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔁 [Real Python — Recursion](https://realpython.com/python-thinking-recursively/) — In-depth recursion tutorials
- 📐 [GeeksForGeeks — Lists & Arrays](https://www.geeksforgeeks.org/python-list/) — Python list and array examples
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 🔍 [Python Lambda Guide](https://realpython.com/python-lambda/) — Lambda function deep dive
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 06 June, 2026*

</div>
