<div align="center">

# -- ! Numpy Analyzer ! --
### *Interactive Console-Based NumPy Array Analysis Tool*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![OOP](https://img.shields.io/badge/OOP-Class%20Based-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)

<br/>

> *"Data is the new oil — NumPy is the refinery that shapes it into something powerful."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 OOP Design — DataAnalytics Class](#-oop-design--dataanalytics-class)
- [⚙️ Core Modules & Operations](#️-core-modules--operations)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Output](#-results--output)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Numpy Analyzer** is a comprehensive, menu-driven Python console application built around a single **OOP class** — `DataAnalytics` — that encapsulates all array operations using the **NumPy** library. It supports 1D, 2D, and 3D array creation, and provides six major categories of operations: indexing/slicing, mathematical ops, combining/splitting, search/sort/filter, and statistical aggregations.

This project is designed to:
- Demonstrate practical NumPy usage through an interactive CLI
- Apply Object-Oriented Programming with a clean single-class design
- Practice real-world array manipulation — the kind used in data science and analytics
- Build intuition for NumPy's axis-based operations, boolean filtering, and reshaping

---

## 🎯 Problem Statement

> **Objective:** Build a single-entry console tool that allows users to create NumPy arrays of any dimension and perform a full suite of analysis operations interactively.

| 📂 Module | 📄 Type | 🔍 Description |
|-----------|---------|----------------|
| Create Array | Input | 1D, 2D, or 3D NumPy array from user-entered elements |
| Indexing / Slicing | Access | Element access by index; row+column slicing |
| Mathematical Ops | Computation | Element-wise add, subtract, multiply, divide on same-shape arrays |
| Combine / Split | Restructure | `np.vstack` to combine; `np.vsplit` to divide into equal parts |
| Search / Sort / Filter | Analysis | Element search by value, axis-based sort, boolean filter conditions |
| Aggregation & Stats | Statistics | Sum, mean, max, min, std deviation, variance — entire or axis-wise |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧱 **OOP Architecture** | Entire logic encapsulated in the `DataAnalytics` class |
| 🔢 **3 Array Dimensions** | Supports 1D, 2D, and 3D NumPy array creation |
| 🔁 **Persistent Main Menu** | Program loops with `while True` until user selects Exit |
| ↩️ **Sub-menu Navigation** | Every operation has a dedicated sub-menu with Back option |
| 🔪 **Indexing & Slicing** | Dimension-aware: 1D index, 2D row+col, 3D depth+row+col |
| ➕ **Element-wise Math** | Add, subtract, multiply, divide two same-shaped arrays |
| 🔗 **Combine & Split** | `vstack` for vertical combine; `vsplit` for equal row-splits |
| 🔍 **Search by Value** | Returns all `[row, column]` positions where value appears |
| 📊 **Axis-Aware Sort** | Sort row-wise (axis=1) or column-wise (axis=0) |
| 🎯 **Boolean Filter** | Filter elements greater than, less than, or equal to a value |
| 📈 **6 Aggregations** | Sum, Mean, Max, Min, Std Dev, Variance with axis control |
| ⚠️ **Input Validation** | Invalid dimensions, wrong element counts, and bad types are caught |
| 🚫 **Array Size Guard** | Max 30 elements enforced to keep interactive use manageable |

---

## 🏗️ Project Structure

```
📦 numpy-analyzer/
│
├── 📄 Numpy_Analyzer.py    ← Single-file script (entry point + DataAnalytics class)
│
└── 📄 README.md            ← Project documentation
```

> **How to run:**
> ```bash
> pip install numpy
> python Numpy_Analyzer.py
> ```

---

## 🔄 Project Workflow

```
Program Start  →  main()  →  DataAnalytics object created
                                        │
                          ┌─────────────▼─────────────┐
                          │      Display Main Menu     │  ← 7 options
                          └─────────────┬─────────────┘
                                        │
        ┌────────────────┬──────────────┼──────────────┬────────────────┐
        ▼                ▼             ▼               ▼                ▼
  ┌───────────┐   ┌───────────┐  ┌──────────┐  ┌──────────┐   ┌──────────────┐
  │ Choice 1  │   │ Choice 2  │  │ Choice 3 │  │ Choice 4 │   │  Choice 5/6  │
  │  Create   │   │  Index /  │  │  Math    │  │ Combine/ │   │ Search/Sort/ │
  │  Array    │   │  Slice    │  │  Ops     │  │  Split   │   │ Filter/Stats │
  └─────┬─────┘   └─────┬─────┘  └────┬─────┘  └────┬─────┘   └──────┬───────┘
        │               │             │              │                 │
        ▼               ▼             ▼              ▼                 ▼
  ┌──────────────────────────────────────────────────────────────────────────┐
  │       self.array updated → Operation performed → Output printed          │
  └──────────────────────────────────┬───────────────────────────────────────┘
                                     │
                            Back to Main Menu
                                     │
                              (Choice 7) Exit ✅
```

---

## 🧱 OOP Design — DataAnalytics Class

### 📐 Class Overview

```
DataAnalytics
│
├── Attributes
│   ├── self.array          ← Active NumPy array (shared across all operations)
│   ├── self.arr1d / arr2d / arr3d  ← Boolean flags tracking current dimension
│   ├── self.row, self.col, self.depth  ← Shape metadata
│   └── self.__arrstr / __arrlist   ← Private parsing helpers
│
└── Methods
    ├── CreateOneDArray()           ← 1D array, size 3–30
    ├── CreateTwoDArray()           ← 2D array, rows×cols ≤ 30
    ├── CreateThreeDArray()         ← 3D array, depth×row×col ≤ 30
    ├── Indexing_Slicing()          ← Dimension-aware index + slice
    ├── MathematicalOperation()     ← Element-wise +, −, ×, ÷ with second array
    ├── Combining_Spliting()        ← np.vstack + np.vsplit
    ├── SearchSortFilter()          ← np.where, np.sort, boolean mask
    └── AggregationStatistics()     ← np.sum/mean/max/min/std/var with axis
```

### 🔐 Encapsulation

| Attribute | Modifier | Purpose |
|-----------|----------|---------|
| `self.array` | Public | Shared active array accessed by all methods |
| `self.arr1d/2d/3d` | Public | Dimension flags drive dimension-aware logic |
| `self.__arrstr` | Private (name-mangled) | Raw input string — not exposed outside class |
| `self.__arrlist` | Private (name-mangled) | Split element list — internal parsing only |

---

## ⚙️ Core Modules & Operations

### 1️⃣ Create a NumPy Array
- Choose dimension: 1, 2, or 3
- Enter elements space-separated; count must exactly match the required size
- Array stored as `self.array` via `np.array(...).reshape(...)` and reused by all subsequent operations
- Size guard: 1D max 30 elements; 2D/3D max 30 total elements

### 2️⃣ Indexing & Slicing
- **1D Indexing:** Enter a single index → returns `array[i]`
- **2D Indexing:** Enter `row,col` comma-separated → returns `array[a,b]`
- **3D Indexing:** Enter `depth,row,col` → returns `array[a,b,c]`
- **Slicing:** Enter `start:end` for rows and columns separately → returns sub-array

### 3️⃣ Mathematical Operations
- User enters a **second array of the same shape** as the stored array
- Operations: `np.add`, `np.subtract`, `np.multiply`, `np.divide`
- Shows Original Array, Second Array, and Result Array

### 4️⃣ Combine or Split Arrays
- **Combining:** Enter second same-shaped array → `np.vstack(array1, array2)`
- **Splitting:** Enter number of parts → `np.vsplit(array, n)` — splits combined/active array vertically

### 5️⃣ Search, Sort & Filter Arrays
- **Search:** Enter a value → uses `np.where()` to return all `[row, col]` positions
- **Sort:** Choose row-wise (`axis=1`) or column-wise (`axis=0`) → `np.sort()`
- **Filter:** Choose Greater / Less / Equal + threshold → boolean mask `array[array > val]`

### 6️⃣ Aggregations & Statistics
All six operations support **axis selection** for 2D/3D arrays:

| Stat | NumPy Function | Axis Options |
|------|---------------|--------------|
| Sum | `np.sum()` | Entire / Row-wise / Column-wise |
| Mean | `np.mean()` | Entire / Row-wise / Column-wise |
| Maximum | `np.max()` | Entire / Row-wise / Column-wise |
| Minimum | `np.min()` | Entire / Row-wise / Column-wise |
| Std Dev | `np.std()` | Entire / Row-wise / Column-wise |
| Variance | `np.var()` | Entire / Row-wise / Column-wise |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language |
| 🔢 **NumPy** | 1.24+ | Array creation, reshaping, math, sort, search, stats |
| 🧱 **OOP / Class** | Built-in | `DataAnalytics` class encapsulates all logic |
| 🔀 **match-case** | Python 3.10+ | Structural pattern matching for all menu choices |
| 🔁 **while True** | Built-in | Persistent menus with break-on-back navigation |
| 🔍 **np.where()** | NumPy | Element search returning index positions |
| 📊 **np.sort()** | NumPy | Axis-based array sorting |
| 🎯 **Boolean Mask** | NumPy | `array[array > val]` for filtering |
| 🔗 **np.vstack/vsplit** | NumPy | Vertical array combining and splitting |

---

## 📈 Results & Output

---

### ▶️ Main Menu & Input Validation

<img src="Image 1.png">

> *Welcome screen with 7-option main menu. Invalid string input "k" caught — "Enter choice as an option number." displayed. User then selects option 1.*

---

### 🔢 Creating a 2D Array

<img src="Image 2.png">

> *Invalid dimension 6 rejected. Then dimension 2 selected — 6 rows × 4 columns (24 elements) entered. "2D Array created successfully" confirmed.*

<img src="Image 3.png">

> *The created 6×4 array displayed. User then selects option 2 (Indexing or Slicing) and chooses Indexing sub-option.*

---

### 🔪 Indexing & Slicing

<img src="Image 4.png">

> *Indexing: element at row 3, column 3 → value 55. Slicing: rows 0:4, columns 1:3 → 4×2 sub-array `[[15,4],[32,29],[14,87],[12,76]]`.*

---

### ➕ Mathematical Operations — Addition & Division

<img src="Image 6.png">

> *Addition of two 6×4 arrays: Original + Second Array = Result array shown element-wise.*

<img src="Image 8.png">

> *Division of the stored array by a new 6×4 array — floating-point result array displayed.*

---

### 🔗 Combining Arrays

<img src="Image 10.png">

> *Two 6×4 arrays combined using `np.vstack` — resulting 12×4 combined array displayed.*

---

### ✂️ Splitting Arrays

<img src="Image 11.png">

> *Combined 12×4 array split into 3 equal parts using `np.vsplit` — each 4×4 sub-array shown. Invalid choice 33 caught with "Choose valid option" message.*

---

### 🔍 Search & Sort

<img src="Image 12.png">

> *Searching for element 28 — found at positions `[(4, 3), (11, 2)]`. Sort sub-menu shown, option 2 (Sort Array) selected.*

<img src="Image 13.png">

> *Array sorted column-wise (axis=0) — all columns sorted independently in ascending order.*

---

### 🎯 Filter Array

<img src="Image 15.png">

> *Filter condition: elements greater than 20. All matching elements extracted as a 1D boolean-masked result array.*

---

### 📈 Aggregation — Row-wise Sum & Standard Deviation

<img src="Image 17.png">

> *Sum computed row-wise (axis=1) — each row's total displayed as `[196, 115, 291, 213, 49, 177, 216, 226, 278, 249, 128, 145]`.*

<img src="Image 18.png">

> *Standard deviation computed over the entire array: **31.558**.*

---

### 🚪 Exit

<img src="Image 19.png">

> *User selects option 7 from main menu. Program prints "Thank you for using Numpy Analyzer...." and exits cleanly.*

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **NumPy-Focused** | Directly demonstrates array creation, reshaping, math, sort, search, and stats |
| 🧱 **Clean OOP Design** | Single `DataAnalytics` class keeps all logic organized and self-contained |
| 🔢 **Multi-Dimensional** | Supports 1D, 2D, and 3D arrays with dimension-aware operation logic |
| 📊 **Axis-Aware Stats** | Aggregations can target entire array, rows, or columns independently |
| 🎯 **Boolean Filtering** | Intuitive Greater/Less/Equal filter using NumPy boolean masks |
| ⚠️ **Robust Validation** | Invalid inputs, wrong element counts, and out-of-range indices handled gracefully |
| 🚫 **Size Guard** | 30-element cap prevents unwieldy array sizes in CLI |
| 🔁 **Persistent State** | `self.array` persists across operations — create once, analyze many times |
| 🧪 **Extensible** | New operations can be added as methods to `DataAnalytics` without touching `main()` |

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

> *"Every array tells a story — NumPy just helps you read it."*

**🎓 Role:** Junior Python Developer | Data Analytics Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · NumPy · OOP · CLI Applications · Data Analysis · Array Operations

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔢 [NumPy Official Docs](https://numpy.org/doc/) — NumPy array operations and API reference
- 📊 [Real Python — NumPy](https://realpython.com/numpy-array-programming/) — NumPy array programming guide
- 🔪 [NumPy Indexing Guide](https://numpy.org/doc/stable/user/basics.indexing.html) — Indexing and slicing reference
- 📈 [GeeksForGeeks — NumPy](https://www.geeksforgeeks.org/numpy-tutorial/) — NumPy tutorials and examples
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data science courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 12 July, 2026*

</div>
