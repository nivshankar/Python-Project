<div align="center">

# -- ! Sales Data Analyzer ! --
### *Interactive Menu-Driven Console Tool for Sales Data Exploration, Cleaning & Visualization*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Operations-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"A menu of options is only as useful as the data behind it — this tool gives sales data both."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🗂️ Part A — Data Management & Exploration](#️-part-a--data-management--exploration)
- [📊 Part B — Statistics & Visualization](#-part-b--statistics--visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Sales Data Analyzer** is an object-oriented, menu-driven Python console application that turns a raw sales CSV into an interactive data-exploration toolkit. Built around a `SalesDataAnalyzer` class, the program lets a user load a dataset and then navigate a nested system of menus to explore, clean, transform, analyze, and visualize it — entirely from the terminal.

This project is designed to:
- Strengthen understanding of object-oriented Python design (classes, state, encapsulation)
- Practice building nested, menu-driven CLI programs with `while` loops and `if-elif` branching
- Apply pandas and NumPy for data exploration, cleaning, and aggregation
- Generate a wide range of matplotlib/seaborn visualizations from user-selected columns

---

## 🎯 Problem Statement

> **Objective:** Build an interactive console tool that lets a user explore, clean, and visualize any sales dataset without writing code.

Given a sales dataset (`SalesID`, `Date`, `Product`, `Region`, `Sales`, `Profit`, `Year`), the program wraps all analysis capability inside a single class so the user can repeatedly load data, inspect it, handle missing values, run NumPy/pandas operations, compute statistics, and generate plots — all driven by simple numbered menu choices.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading | I/O | Loads any CSV path into the analyzer via `pandas.read_csv` |
| Data Exploration | Menu | Head, tail, columns, dtypes, and `info()` on demand |
| Missing Data Handling | Menu | View, mean-fill, drop, or custom-replace missing values |
| DataFrame Operations | Menu | NumPy arrays, math ops, combine/split, search/sort/filter, aggregation, pivot tables |
| Statistical Analysis | Analysis | Describe, std, variance, and percentiles for any column |
| Data Visualization | Menu | Bar, line, scatter, pie, histogram, stack, heatmap, and box plots |
| Save Visualization | I/O | Saves the most recently generated plot to disk |

The goal is to demonstrate a **fully interactive, class-based data-analysis console application**.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧱 **Object-Oriented Design** | All state and logic encapsulated in a `SalesDataAnalyzer` class |
| 🔁 **Nested Menu System** | Main menu branches into 6+ sub-menus, each looping until "Back" |
| 📥 **Flexible Data Loading** | Load any CSV path at runtime, with error handling |
| 🔍 **Data Exploration** | Head/tail preview, column list, dtypes, and full `info()` summary |
| 🧹 **Missing Data Toolkit** | Mean-fill, row-drop, or custom-value replacement for missing entries |
| 🔢 **NumPy Array Tools** | Column-to-array conversion, indexing, and slicing on demand |
| ➕ **Mathematical Operations** | Sum, mean, max, min, plus user-driven addition/multiplication on arrays |
| 🔗 **Combine & Split Data** | Concat/merge with another CSV, or group-split by any column |
| 🔎 **Search, Sort & Filter** | Exact-match search, ascending/descending sort, and value filtering |
| 📊 **Aggregate Functions** | Sum/mean/count/max/min, with optional group-by breakdown |
| 📐 **Pivot Tables** | Build a pivot table from any index/columns/values combination |
| 🎨 **8 Chart Types** | Bar, line, scatter, pie, histogram, stack plot, heatmap, and box plot |
| 💾 **Save to File** | Exports the last-rendered figure to a user-named image file |
| ⚠️ **Robust Error Handling** | Invalid columns, paths, and inputs are caught and reported gracefully |

---

## 🏗️ Project Structure

```
📦 sales-data-analyzer/
│
├── 📓 Sales_Data_Analysis.ipynb   ← Main Jupyter notebook (entry point)
├── 📄 sales_data.csv              ← Source dataset (expected in same directory)
│
└── 📄 README.md                   ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu          │  ← Load / Explore / DataFrame Ops /
│                               │    Missing Data / Stats / Visualize / Save / Exit
└────────────┬────────────────┘
             │
   ┌─────────┼─────────────┬───────────────┬─────────────┐
   ▼         ▼             ▼               ▼             ▼
┌───────┐ ┌─────────┐ ┌───────────┐ ┌──────────────┐ ┌──────────┐
│ Load  │ │ Explore │ │ DataFrame │ │ Missing Data │ │ Stats /  │
│ CSV   │ │ Data    │ │ Ops Menu  │ │ Menu         │ │ Visualize│
└───┬───┘ └────┬────┘ └─────┬─────┘ └──────┬───────┘ └────┬─────┘
    │          │            │              │              │
    ▼          ▼            ▼              ▼              ▼
┌─────────────────────────────────────────────────────────────┐
│           Print Results / Render Plot to Console/Screen      │
└────────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
                     Loop Back to Menu
                             │
                      (Choice: Exit) ✅
```

---

## 🗂️ Part A — Data Management & Exploration

### 📝 1. Loading the Dataset

The `load_data` method reads any CSV path into the class's internal DataFrame, with a try/except guard against bad paths.

**Logic:**
```python
def load_data(self, file_path):
    try:
        self.data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
    except Exception as e:
        print("Error loading dataset:", e)
```

---

### 🔍 2. Exploring the Data

> A sub-menu offering head/tail previews, column listing, dtype inspection, and a full `info()` summary.

**Logic:**
```python
print(self.data.head())
print(self.data.tail())
print(self.data.columns.tolist())
print(self.data.dtypes)
print(self.data.info())
```

---

### 🧹 3. Handling Missing Data

> Detects missing rows, then offers mean-fill, row-drop, or custom-value replacement.

**Logic:**
```python
missing_rows = self.data[self.data.isnull().any(axis=1)]

numeric_cols = self.data.select_dtypes(include=np.number).columns
for col in numeric_cols:
    self.data[col] = self.data[col].fillna(self.data[col].mean())

self.data = self.data.dropna()
self.data = self.data.fillna(value)
```

---

### 🔢 4. DataFrame Operations Menu

> A dedicated sub-menu covering NumPy arrays, math operations, combining/splitting data, search/sort/filter, aggregation, and pivot tables.

**Logic:**
```python
arr = self.data[column].to_numpy()
print("First 5 elements:", arr[:5])

group_col_data = pd.concat([self.data, other_df], ignore_index=True)
merged_data = pd.merge(self.data, other_df, on=key)

groups = self.data.groupby(column)

pivot = pd.pivot_table(self.data, index=index_col, columns=columns_col, values=values_col, aggfunc="sum")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧱 Class-Based State | `self.data` persists across every menu interaction |
| 🔁 Nested `while True` Menus | Each sub-menu loops until the user selects "Back" |
| 🔢 `to_numpy()` + slicing | Converting a column to an array and indexing into it |
| 🔗 `pd.concat()` / `pd.merge()` | Combining two datasets by stacking or key-based joining |
| 📐 `pd.pivot_table()` | Cross-tabulating one column against another with an aggregation |

---

## 📊 Part B — Statistics & Visualization

### 📐 5. Statistical Analysis

> Computes `describe()`, standard deviation, variance, and the 25th/50th/75th percentiles for any chosen numeric column.

**Logic:**
```python
print(self.data[column].describe())
print("Standard Deviation:", self.data[column].std())
print("Variance:", self.data[column].var())
print("25th Percentile:", self.data[column].quantile(0.25))
print("50th Percentile:", self.data[column].quantile(0.5))
print("75th Percentile:", self.data[column].quantile(0.75))
```

---

### 🎨 6. Data Visualization Menu

> An 8-option chart menu — Bar, Line, Scatter, Pie, Histogram, Stack Plot, Heatmap, and Box Plot — each built from user-chosen columns.

**Logic:**
```python
ax.bar(self.data[x_col], self.data[y_col])          # Bar Plot
ax.plot(self.data[x_col], self.data[y_col])          # Line Plot
ax.scatter(self.data[x_col], self.data[y_col])       # Scatter Plot
ax.pie(counts, labels=counts.index, autopct="%1.1f%%")  # Pie Chart
ax.hist(self.data[column], bins=10)                  # Histogram
ax.stackplot(self.data[x_col], *[self.data[c] for c in y_list], labels=y_list)  # Stack Plot
sns.heatmap(numeric_data.corr(), annot=True, ax=ax)  # Heatmap
sns.boxplot(y=self.data[column], ax=ax)              # Box Plot
```

---

### 💾 7. Saving a Visualization

> Persists the most recently rendered figure (`self.last_figure`) to a user-specified filename.

**Logic:**
```python
self.last_figure.savefig(filename)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 📐 `describe()` + quantiles | Full statistical summary of a numeric column |
| 🎨 8 Distinct Chart Types | One method covering the most common matplotlib/seaborn plots |
| 🖼️ `self.last_figure` | Tracks the latest figure object so it can be saved on demand |
| 🧮 `select_dtypes(include=np.number)` | Isolating numeric columns for correlation and heatmaps |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, aggregation, and pivoting |
| 🔢 **NumPy** | Latest | Array conversion and numeric operations |
| 📊 **Matplotlib** | Latest | Bar, line, scatter, pie, histogram, and stack plots |
| 🎨 **Seaborn** | Latest | Heatmap and box plot visualizations |
| 📓 **Jupyter Notebook** | Latest | Interactive execution environment |

---

## 📈 Results & Insights

Running the analyzer against `sales_data.csv` (150 records across `SalesID`, `Date`, `Product`, `Region`, `Sales`, `Profit`, and `Year`) enables:

- ✅ **Full Dataset Exploration** — Instant head/tail/dtype/info views without writing code
- 🧹 **Data Quality Checks** — Missing values identified and resolved through the chosen strategy
- 📊 **Region & Product Breakdown** — Aggregation and pivot tables reveal sales/profit by category
- 📈 **On-Demand Visualizations** — Any numeric or categorical column can be turned into 1 of 8 chart types
- 💾 **Reusable Outputs** — Generated charts can be saved directly as image files

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Combines OOP, pandas, NumPy, and visualization in one guided tool |
| 🔄 **Reusability** | Works with any CSV that has comparable numeric/categorical columns |
| 📚 **Educational** | Each menu option demonstrates a distinct pandas/NumPy/matplotlib concept |
| 🖥️ **No Hardcoded Columns** | All column names are supplied interactively by the user |
| ⚡ **All-in-One Toolkit** | Exploration, cleaning, analysis, and visualization in a single class |
| 🧪 **Extensible** | New chart types or DataFrame operations can be added as class methods |
| 📖 **Readable Code** | Clear method-per-feature structure keeps logic easy to follow |
| 🛡️ **Input Safety** | Invalid columns, choices, and file paths are caught and reported |

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

> *"Every dataset tells a story — analysis is how you learn to read it."*

**🎓 Role:** Data Analysis Enthusiast | Python Developer \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Data Visualization · Object-Oriented Programming

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Official Docs](https://pandas.pydata.org/docs/) — Official pandas reference
- 🔢 [NumPy Documentation](https://numpy.org/doc/) — Array operations reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Core plotting reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 25 July, 2026*

</div>
