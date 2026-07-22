<div align="center">

# -- ! Sales Data Analyzer ! --
### *OOP-Based Interactive Sales Data Analysis & Visualization Tool*

[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizations-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"Data speaks louder than assumptions — analyze it, visualize it, and let the insights lead the way."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 OOP Design — SalesDataAnalyzer Class](#-oop-design--salesdataanalyzer-class)
- [📋 Main Menu — Program Navigation](#-main-menu--program-navigation)
- [⚙️ Core Modules & Operations](#️-core-modules--operations)
- [📊 Visualizations](#-visualizations)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Sales Data Analyzer** is a comprehensive, menu-driven Jupyter Notebook project built around a single OOP class — `SalesDataAnalyzer` — that uses **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn** to load, explore, clean, analyze, and visualize any CSV-based sales dataset interactively.

Unlike a fixed-dataset project, this tool is designed to work with **any CSV file** — the user specifies the file path at runtime, making it a reusable general-purpose data analysis engine. The `main()` function drives an 8-option interactive menu inside the notebook, and a dedicated `dataframe_operations_menu()` provides a further 10-option sub-menu for advanced DataFrame operations.

This project is designed to:
- Apply OOP design to a real-world data analytics workflow
- Cover the complete data analysis pipeline: load → explore → clean → analyze → visualize → save
- Demonstrate advanced Pandas operations including groupby, pivot tables, merge, reindexing, and transform
- Build 9 distinct Matplotlib and Seaborn visualizations covering every common chart type
- Practice NumPy array operations on real DataFrame columns

---

## 🎯 Problem Statement

> **Objective:** Build a class-based, interactive data analysis tool in a Jupyter Notebook that can load any CSV sales dataset and provide a complete suite of exploration, cleaning, computation, and visualization operations through a menu-driven interface.

| 📂 Module | 📄 Type | 🔍 Description |
|-----------|---------|----------------|
| Load Dataset | Input | Load any CSV file by path with full error handling |
| Explore Data | Inspection | View head/tail, column names, data types, and `.info()` / `.describe()` |
| DataFrame Operations | Manipulation | NumPy arrays, math ops, combine, split, search, sort, filter, groupby, pivot, reindex |
| Handle Missing Data | Cleaning | View, fill with mean, drop rows, or replace with custom value |
| Descriptive Statistics | Analysis | `describe()` + std dev, variance, and percentiles for any column |
| Data Visualization | Charts | 9 chart types: bar, line, scatter, pie, histogram, stack, subplots, heatmap, box plot |
| Save Visualization | Export | Save the last rendered chart to a file (PNG, PDF, etc.) |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧱 **OOP Architecture** | All logic encapsulated in `SalesDataAnalyzer` + standalone `dataframe_operations_menu()` |
| 📁 **Any CSV Support** | Accepts any CSV file path at runtime — not tied to a specific dataset |
| 🔁 **Dual Menu System** | Main 8-option menu + 10-option DataFrame operations sub-menu |
| ✅ **Layered Error Handling** | `FileNotFoundError`, `EmptyDataError`, invalid column names, and invalid operators all caught |
| 🔒 **Data Guard** | `_check_data()` private method blocks all operations if no dataset is loaded |
| 🔍 **Flexible Search** | Search any column by exact value match using string casting |
| 📊 **Bidirectional Sort** | Sort any column ascending or descending on demand |
| 🎯 **5-Operator Filter** | Filter by `==`, `>`, `<`, `>=`, `<=` on any numeric or string column |
| 🧮 **NumPy Integration** | Columns converted to NumPy arrays for indexing, slicing, and element-wise math |
| 🔗 **3 Combine Methods** | `pd.concat`, `pd.merge` (on a key), and `DataFrame.join` |
| ✂️ **GroupBy Split** | Split the entire DataFrame into sub-DataFrames by any column's unique values |
| 📐 **Pivot Tables** | `pd.pivot_table` with user-chosen index, values, and aggregation function |
| 🔄 **GroupBy Transform** | Adds a group-mean column via `groupby().transform("mean")` |
| 🔢 **Reindex** | Resets index to start from 1 and labels it `S.No` |
| 📈 **9 Chart Types** | Bar, line, scatter, pie, histogram, stack plot, subplots, seaborn heatmap, seaborn box plot |
| 💾 **Save Last Plot** | `save_visualization(filename)` saves the most recently generated figure to disk |

---

## 🏗️ Project Structure

```
📦 sales-data-analyzer/
│
├── 📓 Sales_Data_Analyzer.ipynb    ← Jupyter Notebook (single-cell program)
├── 🗂️ your_dataset.csv             ← Any CSV sales dataset (user-supplied at runtime)
│
└── 📄 README.md                    ← Project documentation
```

> **How to run:**
> ```bash
> pip install numpy pandas matplotlib seaborn notebook
> jupyter notebook Sales_Data_Analyzer.ipynb
> ```
> Then run the single cell. When prompted, enter the path to your CSV file.

---

## 🔄 Project Workflow

```
Notebook Cell Executed  →  main() called  →  SalesDataAnalyzer() created
                                                        │
                                         ┌──────────────▼──────────────┐
                                         │       Main Menu (8 options)  │
                                         └──────────────┬──────────────┘
                                                        │
        ┌──────────────┬──────────────┬─────────────────┼──────────────┬──────────────┐
        ▼              ▼              ▼                  ▼              ▼              ▼
  ┌──────────┐  ┌───────────┐  ┌──────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
  │  Load    │  │  Explore  │  │  DataFrame   │  │  Handle  │  │  Stats   │  │ Visualize│
  │ Dataset  │  │   Data    │  │  Operations  │  │ Missing  │  │ Analysis │  │  & Save  │
  └────┬─────┘  └─────┬─────┘  └──────┬───────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
       │              │               │                │              │              │
       ▼              ▼               ▼                ▼              ▼              ▼
  load_data()   explore_data()  10-option sub-menu  clean_data()  statistical_  visualize_data()
                                (NumPy / math /                   analysis()    save_visualization()
                                 combine / split /
                                 search / agg /
                                 pivot / groupby /
                                 reindex)
                                                        │
                                                 (Option 8) Exit ✅
```

---

## 🧱 OOP Design — SalesDataAnalyzer Class

### 📐 Class & Function Overview

```
SalesDataAnalyzer
│
├── Instance Attributes (__init__)
│   ├── self.data        ← Active Pandas DataFrame (None until loaded)
│   └── self.last_fig    ← Stores the most recently rendered matplotlib figure
│
├── Private Methods
│   └── _check_data()    ← Returns False and prints error if self.data is None
│
└── Public Methods
    ├── load_data(file_path)          ← pd.read_csv with FileNotFoundError / EmptyDataError handling
    ├── explore_data()                ← Sub-menu: head, tail, columns, dtypes, info, describe
    ├── clean_data()                  ← Sub-menu: view missing, fill mean, drop rows, replace value
    ├── mathematical_operations()     ← Converts column to NumPy; indexing, slicing, element-wise ops
    ├── combine_data(other_df)        ← concat / merge (on key) / join
    ├── split_data()                  ← groupby column → dict of sub-DataFrames
    ├── search_sort_filter()          ← Sub-menu: exact search, sort asc/desc, 5-operator filter
    ├── aggregate_functions()         ← Sum, mean, count, min, max on chosen column
    ├── statistical_analysis()        ← describe() + std, var, Q1, Q2, Q3 percentiles
    ├── create_pivot_table()          ← pd.pivot_table with user-defined index, values, aggfunc
    ├── groupby_transform()           ← groupby + transform("mean") → new column added
    ├── reindex_data()                ← reset_index → start from 1 → label "S.No"
    ├── visualize_data()              ← 9-chart sub-menu; stores fig in self.last_fig
    └── save_visualization(filename)  ← self.last_fig.savefig(filename)

standalone function:
└── dataframe_operations_menu(analyzer)  ← 10-option sub-menu wiring DataFrame methods
```

### 🔐 Encapsulation & Validation

| Rule | Behaviour |
|------|-----------|
| No dataset loaded | `_check_data()` blocks all methods and prints a clear prompt to load first |
| File not found | `load_data()` catches `FileNotFoundError` with a descriptive message |
| Empty CSV | `load_data()` catches `pd.errors.EmptyDataError` |
| Invalid column name | Every method validates column input against `self.data.columns` before proceeding |
| Invalid operator in filter | `match/case` catches unsupported operators and prompts again |
| Invalid combine method | `match/case` in `combine_data()` catches anything other than concat/merge/join |
| No figure to save | `save_visualization()` checks `self.last_fig` before attempting to save |
| Insufficient numeric columns | Heatmap and subplots require at least 2 numeric columns — checked before rendering |

---

## 📋 Main Menu — Program Navigation

```
=====================================================================================
              Data Analysis & Visualization Program
=====================================================================================
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
```

### Option 3 — DataFrame Operations Sub-Menu

```
=====================================================================================
Perform DataFrame Operations
1.  NumPy Array Creation, Indexing & Slicing
2.  Mathematical Operations
3.  Combine DataFrames
4.  Split DataFrame
5.  Search, Sort, Filter
6.  Aggregate Functions
7.  Create Pivot Table
8.  Groupby & Transform
9.  Reindex Data
10. Back to Main Menu
```

---

## ⚙️ Core Modules & Operations

### 1️⃣ Load Dataset
Accepts any CSV file path. Uses `pd.read_csv()` wrapped in a `try/except` block that handles `FileNotFoundError`, `EmptyDataError`, and any unexpected exceptions.

---

### 2️⃣ Explore Data
Interactive sub-menu offering 5 inspection operations:

| Option | Operation | Pandas Method |
|--------|-----------|---------------|
| 1 | First 5 rows | `df.head()` |
| 2 | Last 5 rows | `df.tail()` |
| 3 | Column names | `list(df.columns)` |
| 4 | Data types | `df.dtypes` |
| 5 | Full info + summary | `df.info()` + `df.describe(include="all")` |

---

### 3️⃣ DataFrame Operations

**NumPy Array & Math Operations:**
Converts any numeric column to a NumPy array via `.to_numpy()`. Demonstrates:
- `arr[0]` — element indexing
- `arr[2:6]` — slicing
- `arr[:10] + 10` — element-wise addition
- `arr[:10] * 2` — element-wise multiplication
- `np.sqrt(np.abs(arr[:10]))` — square root with absolute value

**Combine DataFrames** — three methods:

| Method | Behaviour |
|--------|-----------|
| `concat` | `pd.concat([df1, df2], ignore_index=True)` — vertical stacking |
| `merge` | `pd.merge(df1, df2, on=key, how="outer")` — key-based join |
| `join` | `df.join(other.set_index(col0), rsuffix="_other")` — index join |

**Split DataFrame:**
Groups the DataFrame by a user-chosen column using `groupby()` and returns a dictionary of sub-DataFrames — one per unique value. Prints each group's head.

**Search, Sort, Filter:**

| Operation | Logic |
|-----------|-------|
| Search | `df[df[col].astype(str) == value]` — string cast for type-safe exact match |
| Sort | `df.sort_values(by=col, ascending=True/False)` |
| Filter | `df[df[col] op value]` with `==`, `>`, `<`, `>=`, `<=` — auto-casts to float |

**Aggregate Functions:**
On a user-chosen numeric column: `sum`, `mean`, `count`, `min`, `max`.

**Create Pivot Table:**
`pd.pivot_table(df, index=index_col, values=values_col, aggfunc=agg_func)` with `sum`, `mean`, or `count`.

**GroupBy & Transform:**
`groupby(group_col)[value_col].transform("mean")` — adds a new `{col}_group_mean` column to the DataFrame in place.

**Reindex:**
`reset_index(drop=True)` → increments index by 1 → assigns `"S.No"` as the index name. Produces human-readable 1-based indexing.

---

### 4️⃣ Handle Missing Data
Interactive sub-menu with 4 strategies:

| Option | Strategy | Method |
|--------|----------|--------|
| 1 | View rows with missing values | `df[df.isnull().any(axis=1)]` |
| 2 | Fill numeric NaN with column mean | `df[numeric_cols].fillna(df[numeric_cols].mean())` |
| 3 | Drop all rows with any NaN | `df.dropna()` — reports how many rows were removed |
| 4 | Replace all NaN with custom value | `df.fillna(user_value)` |

---

### 5️⃣ Descriptive Statistics
Runs `df[numeric_cols].describe()` for the full summary table, then for a chosen column adds:
- Standard Deviation — `df[col].std()`
- Variance — `df[col].var()`
- 25th Percentile (Q1) — `df[col].quantile(0.25)`
- 50th Percentile (Median) — `df[col].quantile(0.50)`
- 75th Percentile (Q3) — `df[col].quantile(0.75)`

---

## 📊 Visualizations

The notebook provides 9 chart types, all accessible from the Data Visualization sub-menu. Every chart stores the current figure in `self.last_fig` for later saving.

### 1. Bar Plot
```python
grouped = df.groupby(x_col)[y_col].sum()
plt.bar(grouped.index.astype(str), grouped.values)
```
Groups data by a categorical column, sums a numeric column, and plots aggregated bars. Answers: *Which category has the highest total value?*

---

### 2. Line Plot
```python
plt.plot(df.index, df[y_col])
```
Plots a numeric column against the row index — ideal for showing value trends across records. Answers: *How does a metric trend across the dataset?*

---

### 3. Scatter Plot
```python
plt.scatter(df[x_col], df[y_col])
```
Plots one numeric column against another to reveal correlations or clusters. Answers: *Is there a relationship between two numeric variables?*

---

### 4. Pie Chart
```python
grouped = df.groupby(cat_col)[val_col].sum()
plt.pie(grouped.values, labels=grouped.index.astype(str), autopct="%1.1f%%")
```
Shows proportional contribution of each category to a total numeric value. Answers: *What share of the total does each category hold?*

---

### 5. Histogram
```python
plt.hist(df[col].dropna(), bins=10)
```
Shows the frequency distribution of a single numeric column across 10 bins. Answers: *How is this variable distributed?*

---

### 6. Stack Plot
```python
pivoted = df.pivot_table(index=df.index, columns=cat_col, values=val_col, aggfunc="sum").fillna(0)
plt.stackplot(pivoted.index, [pivoted[c] for c in pivoted.columns], labels=pivoted.columns)
```
Stacked area chart showing how each category's contribution builds up to a cumulative total. Answers: *How do multiple categories stack against each other over records?*

---

### 7. Subplots (4-Panel Dashboard)
```python
plt.figure(figsize=(10, 8))
plt.subplot(2,2,1)  # Histogram of first numeric col
plt.subplot(2,2,2)  # Line plot of first numeric col
plt.subplot(2,2,3)  # Scatter: first vs last numeric col
plt.subplot(2,2,4)  # Box plot of all numeric cols
```
A 2×2 multi-panel dashboard combining histogram, line plot, scatter, and box plot in one figure. Requires at least 2 numeric columns.

---

### 8. Seaborn Heatmap
```python
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
```
Displays the Pearson correlation matrix of all numeric columns with annotated values. Requires at least 2 numeric columns. Answers: *Which pairs of numeric variables are most strongly correlated?*

---

### 9. Seaborn Box Plot
```python
sns.boxplot(x=cat_col, y=col, data=df)   # grouped
sns.boxplot(y=col, data=df)              # single
```
Shows distribution, median, IQR, and outliers for a numeric column, optionally grouped by a categorical column. Answers: *What is the spread and outlier profile of this variable?*

---

### 💾 Save Visualization
```python
analyzer.save_visualization("my_chart.png")
```
Saves `self.last_fig` (the most recently created chart) to any filename. Supports all Matplotlib-supported formats: `.png`, `.pdf`, `.svg`, `.jpg`.

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.13+ | Core programming language |
| 📓 **Jupyter Notebook** | Latest | Interactive development and execution environment |
| 🐼 **Pandas** | 2.0+ | CSV loading, DataFrame operations, groupby, merge, pivot, reindex |
| 🔢 **NumPy** | 1.24+ | Array conversion, indexing, slicing, element-wise math, `np.sqrt` |
| 📊 **Matplotlib** | 3.7+ | Bar, line, scatter, pie, histogram, stack plot, subplots |
| 🎨 **Seaborn** | 0.12+ | Correlation heatmap (`coolwarm`) and grouped/single box plot |
| 🧱 **OOP / Class** | Built-in | `SalesDataAnalyzer` encapsulates all data + methods |
| 🔀 **match-case** | Python 3.10+ | Structural pattern matching for all menus and operators |
| 🔁 **while True** | Built-in | Persistent menus with `break`-on-back navigation |

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Full Pipeline** | Covers every stage: load → explore → clean → analyse → visualize → export |
| 🧱 **Clean OOP Design** | `SalesDataAnalyzer` class keeps all state and logic in one place |
| 📁 **Dataset Agnostic** | Works with any CSV file — not hardcoded to a specific dataset |
| 🔒 **Defensive Programming** | `_check_data()` guard + column validation + operator validation at every step |
| 🔗 **3 Combine Strategies** | `concat`, `merge`, and `join` give full flexibility for combining data sources |
| 📐 **Advanced Pandas** | Pivot tables, groupby/transform, and reindexing go beyond basic DataFrame usage |
| 📊 **9 Chart Types** | Every common business chart type covered in a single interactive menu |
| 💾 **Plot Export** | `save_visualization()` exports any chart to file without leaving the notebook |
| 🧮 **NumPy on Real Data** | Array operations applied directly to DataFrame columns — bridges Pandas and NumPy |
| 🧪 **Extensible** | New analysis methods or chart types can be added to the class with no refactoring |
| 📓 **Single Cell Design** | Entire program runs from one notebook cell — clean, self-contained, and portable |

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

> *"Good analysis doesn't just show what happened — it reveals why, and what comes next."*

**🎓 Role:** Junior Python Developer | Data Analytics Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Pandas · NumPy · Matplotlib · Seaborn · OOP · Jupyter Notebooks · Data Analysis · Data Visualization

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame operations, groupby, pivot tables, merge, reindex
- 🔢 [NumPy Documentation](https://numpy.org/doc/) — Array arithmetic, indexing, slicing, and math functions
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) — Chart creation, subplots, and figure saving
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical data visualization, heatmaps, and box plots
- 📓 [Jupyter Notebook Docs](https://jupyter-notebook.readthedocs.io/) — Notebook usage and best practices
- 📈 [Real Python — Pandas](https://realpython.com/pandas-python-explore-dataset/) — Exploratory data analysis with Pandas
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data science courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
