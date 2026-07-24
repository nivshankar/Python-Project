<div align="center">

# -- ! COVID-19 Data Analysis ! --
### *Exploratory Data Analysis & Visualization of Global COVID-19 Trends*

[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizations-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"Behind every data point is a story — behind every trend is a truth worth understanding."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📓 Notebook Walkthrough](#-notebook-walkthrough)
- [🗂️ Dataset — covid_data.csv](#️-dataset--covid_datacsv)
- [📊 Visualizations](#-visualizations)
- [📈 Key Results & Insights](#-key-results--insights)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **COVID-19 Data Analysis** project is a focused Exploratory Data Analysis (EDA) Jupyter Notebook that loads, cleans, aggregates, and visualizes global COVID-19 data across 10 countries for the month of January 2021. Using **Pandas**, **Matplotlib**, and **Seaborn**, it delivers a complete analytical pipeline — from raw CSV ingestion to publication-quality charts — in a clean, single-cell notebook.

This project is designed to:
- Apply real-world EDA techniques on a public health dataset
- Demonstrate Pandas `groupby`, `describe`, and `isnull` for quick data profiling
- Build meaningful, insight-driven visualizations using Seaborn and Matplotlib
- Uncover cross-country patterns, time-based trends, and metric correlations in COVID-19 data

---

## 🎯 Problem Statement

> **Objective:** Perform a comprehensive exploratory analysis of COVID-19 case data across multiple countries, aggregate key metrics, identify the most affected country, and visualize trends and correlations to surface actionable insights.

| 📂 Step | 📄 Type | 🔍 Description |
|---------|---------|----------------|
| Data Loading | Input | Read `covid_data.csv`; parse `Date` column as `datetime` |
| Data Inspection | Exploration | `head()`, `info()`, `describe()`, `isnull().sum()` |
| Country Aggregation | Analysis | `groupby("Country")` summing Confirmed, Recovered, Deaths |
| Bar Chart | Visualization | Total confirmed cases ranked by country |
| Time-Series Line Plot | Visualization | Confirmed, Recovered, Deaths trends for the top country |
| Correlation Heatmap | Visualization | Pearson correlation matrix across all 4 numeric metrics |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📁 **CSV Data Ingestion** | Loads `covid_data.csv` using `pd.read_csv()` |
| 📅 **Date Parsing** | Converts `Date` column to `datetime64` via `pd.to_datetime()` |
| 🔍 **Data Profiling** | `head()`, `info()`, `describe()`, and `isnull().sum()` in one pass |
| 🌍 **10-Country Dataset** | Covers Brazil, China, France, Germany, India, Italy, Russia, Spain, UK, USA |
| 📆 **January 2021 Coverage** | 300 records spanning 2021-01-01 to 2021-01-30 (30 days × 10 countries) |
| 📊 **Country-Level Aggregation** | `groupby("Country")` summing Confirmed, Recovered, Deaths |
| 🏆 **Auto Top-Country Detection** | Identifies the top country by confirmed cases automatically for trend analysis |
| 📈 **3 Visualizations** | Seaborn bar plot, Seaborn multi-line time-series, Seaborn heatmap |
| 🔗 **Correlation Matrix** | Pearson correlation across Confirmed, Recovered, Deaths, and Active |
| ✅ **Zero Missing Values** | Dataset is clean — `isnull().sum()` confirms 0 nulls across all 6 columns |

---

## 🏗️ Project Structure

```
📦 covid19-analysis/
│
├── 📓 covid19_analysis.ipynb    ← Jupyter Notebook (main analysis file)
├── 🗂️ covid_data.csv            ← COVID-19 dataset (300 records, 10 countries)
│
└── 📄 README.md                 ← Project documentation
```

> **How to run:**
> ```bash
> pip install pandas matplotlib seaborn notebook
> jupyter notebook covid19_analysis.ipynb
> ```
> Ensure `covid_data.csv` is in the same directory as the notebook before running.

---

## 🔄 Project Workflow

```
covid_data.csv
      │
      ▼  pd.read_csv() + pd.to_datetime()
  DataFrame (300 rows × 6 columns)
      │
      ├──▶  Data Inspection
      │     head() · info() · describe() · isnull().sum()
      │
      ├──▶  Country Aggregation
      │     groupby("Country")[["Confirmed","Recovered","Deaths"]].sum()
      │     → country_totals DataFrame (10 rows × 3 columns)
      │
      ├──▶  Chart 1: Bar Plot
      │     Total Confirmed Cases by Country (Seaborn barplot)
      │
      ├──▶  Auto Top-Country Detection
      │     top_country = country_totals.index[0]
      │     top_country_data = df[df["Country"] == top_country]
      │
      ├──▶  Chart 2: Multi-Line Time-Series
      │     Confirmed / Recovered / Deaths trends over Jan 2021 (Seaborn lineplot)
      │
      └──▶  Chart 3: Correlation Heatmap
            df[["Confirmed","Recovered","Deaths","Active"]].corr()
            → Seaborn heatmap (coolwarm palette, annotated)
```

---

## 📓 Notebook Walkthrough

The notebook contains a single primary code cell that executes the entire analysis pipeline from top to bottom. Here is a step-by-step breakdown:

**Step 1 — Import Libraries**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Imports the three required libraries: Pandas for data handling, Matplotlib as the base plotting engine, and Seaborn for high-level statistical charts.

---

**Step 2 — Load & Parse Data**
```python
df = pd.read_csv("covid_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
```
Reads the CSV into a DataFrame and converts the `Date` column from a string to `datetime64[us]` format, enabling time-series operations and correct x-axis rendering.

---

**Step 3 — Data Inspection**
```python
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
```
Runs a four-part profile of the dataset:
- `head()` — previews the first 5 rows
- `info()` — shows column names, non-null counts, and data types
- `describe()` — generates count, mean, min, max, std, and percentiles for all numeric columns
- `isnull().sum()` — confirms zero missing values across all 6 columns

---

**Step 4 — Country-Level Aggregation**
```python
country_totals = df.groupby("Country")[["Confirmed", "Recovered", "Deaths"]].sum()
print(country_totals)
```
Groups the 300 records by `Country` and sums the three key metrics across all dates, producing a 10-row summary table — one row per country.

---

**Step 5 — Bar Chart: Confirmed Cases by Country**
```python
sns.barplot(x=country_totals.index, y=country_totals["Confirmed"])
plt.title("Total Confirmed Cases by Country")
```
Plots the aggregated confirmed totals per country as a Seaborn bar chart, sorted alphabetically. X-axis labels are rotated 45° for readability.

---

**Step 6 — Auto Top-Country Detection & Filtering**
```python
top_country = country_totals.index[0]
top_country_data = df[df["Country"] == top_country]
```
Automatically identifies the first country in the sorted aggregation index and filters all 30 records for that country to feed into the time-series chart.

---

**Step 7 — Multi-Line Time-Series Chart**
```python
sns.lineplot(x="Date", y="Confirmed", data=top_country_data, label="Confirmed")
sns.lineplot(x="Date", y="Recovered", data=top_country_data, label="Recovered")
sns.lineplot(x="Date", y="Deaths", data=top_country_data, label="Deaths")
plt.title(f"Trend Over Time for {top_country}")
```
Plots Confirmed, Recovered, and Deaths as three overlaid lines across all 30 days of January 2021 for the top country, with a legend and rotated date labels.

---

**Step 8 — Correlation Heatmap**
```python
correlation = df[["Confirmed", "Recovered", "Deaths", "Active"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Between COVID-19 Metrics")
```
Computes the Pearson correlation matrix across all four numeric columns and renders it as an annotated `coolwarm` heatmap, revealing how strongly each metric relates to the others.

---

## 🗂️ Dataset — covid_data.csv

| Column | Type | Description |
|--------|------|-------------|
| `Date` | `datetime64[us]` | Date of the record (2021-01-01 to 2021-01-30) |
| `Country` | `str` | One of 10 countries |
| `Confirmed` | `int64` | Daily confirmed COVID-19 cases |
| `Recovered` | `int64` | Daily recovered cases |
| `Deaths` | `int64` | Daily deaths |
| `Active` | `int64` | Active cases (Confirmed − Recovered − Deaths) |

**Dataset Summary:**

| Metric | Value |
|--------|-------|
| Total Records | 300 rows |
| Date Range | 2021-01-01 to 2021-01-30 |
| Countries Covered | 10 |
| Missing Values | 0 (all columns fully populated) |
| Memory Usage | 14.2 KB |

**Countries included:** Brazil · China · France · Germany · India · Italy · Russia · Spain · UK · USA

**Descriptive Statistics (from `describe()` output):**

| Metric | Confirmed | Recovered | Deaths | Active |
|--------|-----------|-----------|--------|--------|
| Mean | 2,501.69 | 2,069.26 | 124.41 | 941.67 |
| Min | 661 | 492 | 27 | 0 |
| Max | 5,237 | 3,528 | 198 | 3,665 |
| Std Dev | 1,629.48 | 958.51 | 50.05 | 1,094.13 |

**Country-Level Totals (from `groupby` aggregation):**

| Country | Confirmed | Recovered | Deaths |
|---------|-----------|-----------|--------|
| Brazil | 25,203 | 74,619 | 5,131 |
| China | 28,751 | 72,812 | 1,064 |
| France | 57,253 | 101,777 | 1,169 |
| Germany | 145,331 | 88,577 | 3,470 |
| India | 139,379 | 32,782 | 4,921 |
| Italy | 63,573 | 19,680 | 3,190 |
| Russia | 39,525 | 56,467 | 4,346 |
| Spain | 151,358 | 100,922 | 3,806 |
| UK | 74,663 | 28,829 | 5,627 |
| USA | 25,472 | 44,314 | 4,600 |

---

## 📊 Visualizations

The notebook produces three charts, each targeting a distinct analytical question:

---

### 1. Seaborn Bar Plot — Total Confirmed Cases by Country

```python
sns.barplot(x=country_totals.index, y=country_totals["Confirmed"])
plt.title("Total Confirmed Cases by Country")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
```

Displays the total cumulative confirmed cases for each of the 10 countries across January 2021. Countries are sorted alphabetically along the x-axis with labels rotated 45° for readability.

**Answers:** *Which countries reported the highest total confirmed COVID-19 cases in January 2021?*

---

### 2. Seaborn Multi-Line Time-Series — Trend Over Time for Top Country

```python
sns.lineplot(x="Date", y="Confirmed", data=top_country_data, label="Confirmed")
sns.lineplot(x="Date", y="Recovered", data=top_country_data, label="Recovered")
sns.lineplot(x="Date", y="Deaths",    data=top_country_data, label="Deaths")
plt.title(f"Trend Over Time for {top_country}")
```

Overlays three line plots — Confirmed, Recovered, and Deaths — across all 30 days of January 2021 for the automatically detected top country (alphabetically first in the aggregated totals). The legend clearly labels each line.

**Answers:** *How did Confirmed, Recovered, and Death counts evolve day-by-day for the top country?*

---

### 3. Seaborn Heatmap — Correlation Between COVID-19 Metrics

```python
correlation = df[["Confirmed", "Recovered", "Deaths", "Active"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Between COVID-19 Metrics")
```

Computes the Pearson correlation matrix across all four numeric columns and renders it as an 4×4 annotated heatmap with `coolwarm` palette. Values near +1 indicate strong positive correlation; values near -1 indicate strong negative correlation.

**Answers:** *How strongly do Confirmed, Recovered, Deaths, and Active cases correlate with each other?*

---

## 📈 Key Results & Insights

Based on the notebook output for the January 2021 dataset:

| Insight | Value |
|---------|-------|
| 📊 Total Records | 300 entries across 10 countries and 30 days |
| ✅ Data Quality | Zero missing values — no cleaning required |
| 🏆 Highest Confirmed (Total) | **Spain** — 151,358 confirmed cases |
| 💀 Highest Deaths (Total) | **UK** — 5,627 deaths |
| 💚 Highest Recovered (Total) | **France** — 101,777 recoveries |
| 📉 Lowest Confirmed (Total) | **Brazil** — 25,203 confirmed cases |
| 📅 Average Daily Confirmed | 2,501.69 cases per record |
| ⏱️ Average Daily Deaths | 124.41 deaths per record |
| 🔢 Max Single-Day Confirmed | 5,237 cases |
| 🔢 Max Single-Day Deaths | 198 deaths |
| 🔗 Strongest Correlation | Confirmed ↔ Deaths (expected positive relationship) |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.13+ | Core programming language |
| 📓 **Jupyter Notebook** | Latest | Interactive development and execution environment |
| 🐼 **Pandas** | 2.0+ | CSV loading, datetime parsing, groupby aggregation, describe |
| 📊 **Matplotlib** | 3.7+ | Base plotting engine, figure sizing, axis labeling |
| 🎨 **Seaborn** | 0.12+ | `barplot`, `lineplot`, `heatmap` with `coolwarm` palette |
| 📅 **pd.to_datetime** | Pandas | Parses `Date` column from string to `datetime64[us]` |
| 🔗 **df.corr()** | Pandas | Computes Pearson correlation matrix across numeric columns |
| 📐 **groupby().sum()** | Pandas | Aggregates Confirmed, Recovered, Deaths by Country |

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Complete EDA Pipeline** | Covers load → inspect → aggregate → visualize in a clean linear flow |
| 🌍 **Multi-Country Coverage** | Simultaneous analysis of 10 major countries enables direct comparison |
| 📅 **Time-Series Ready** | `pd.to_datetime()` enables accurate date-axis rendering and temporal analysis |
| 🏆 **Auto Top-Country Logic** | Dynamically detects the top country — no hardcoded values |
| 🔗 **Correlation Insight** | Heatmap exposes relationships between all four COVID metrics simultaneously |
| ✅ **Clean Dataset** | Zero missing values means no imputation step required — analysis is immediate |
| 📊 **3 Distinct Chart Types** | Bar, multi-line, and heatmap each answer a fundamentally different analytical question |
| ⚡ **Single-Cell Execution** | Entire pipeline runs in one cell — fast, reproducible, and easy to share |
| 🧪 **Extensible** | New countries, date ranges, or chart types can be added with minimal code changes |
| 📓 **Notebook Format** | Each step is visible, executable, and accompanied by printed output for verification |

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

> *"Every pandemic leaves data behind — the analyst's job is to make that data speak."*

**🎓 Role:** Junior Python Developer | Data Analytics Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Pandas · Matplotlib · Seaborn · EDA · Data Visualization · Jupyter Notebooks

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame operations, groupby, datetime parsing
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) — Figure layout, axis formatting, and tight_layout
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — barplot, lineplot, heatmap references
- 🌍 [Our World in Data — COVID-19](https://ourworldindata.org/coronavirus) — COVID-19 data and research reference
- 📈 [Real Python — Pandas EDA](https://realpython.com/pandas-python-explore-dataset/) — Exploratory data analysis guide
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data science courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
