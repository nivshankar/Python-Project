<div align="center">

# -- ! World Happiness Analysis ! --
### *Exploratory Data Analysis & Visualization of Global Happiness Trends (2018–2023)*

[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizations-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"Happiness is not a random outcome — it is a measurable pattern shaped by wealth, support, freedom, and community."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📓 Notebook Walkthrough](#-notebook-walkthrough)
- [🗂️ Dataset — happiness_data.csv](#️-dataset--happiness_datacsv)
- [📊 Visualizations](#-visualizations)
- [📈 Key Results & Insights](#-key-results--insights)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **World Happiness Analysis** project is a focused Exploratory Data Analysis (EDA) Jupyter Notebook that loads, inspects, filters, aggregates, and visualizes global happiness data across multiple countries and regions spanning **2018 to 2023**. Using **Pandas**, **Matplotlib**, and **Seaborn**, it delivers a complete analytical pipeline — from raw CSV ingestion through to four publication-quality charts — executed within a clean, single-cell notebook.

This project is designed to:
- Apply real-world EDA techniques on a social science dataset
- Practice Pandas operations including `groupby`, `sort_values`, `describe`, and latest-year filtering
- Build four meaningful Seaborn visualizations covering rankings, relationships, correlations, and regional comparisons
- Uncover what factors — GDP, social support, life expectancy, freedom, and generosity — drive national happiness scores

---

## 🎯 Problem Statement

> **Objective:** Perform a comprehensive exploratory analysis of global happiness data, identify the happiest countries and regions, examine the relationship between economic and social factors and happiness, and visualize cross-factor correlations to surface what drives national wellbeing.

| 📂 Step | 📄 Type | 🔍 Description |
|---------|---------|----------------|
| Data Loading | Input | Read `happiness_data.csv` into a Pandas DataFrame |
| Data Inspection | Exploration | `head()`, `info()`, `describe()`, `isnull().sum()` |
| Latest-Year Filtering | Transformation | Filter to the most recent year using `df["Year"].max()` |
| Top 10 Ranking | Analysis | Sort by `HappinessScore` descending, take top 10 countries |
| GDP vs Happiness | Analysis | Scatter plot coloured by Region showing economic relationship |
| Correlation Matrix | Analysis | Pearson correlation across 6 happiness-factor columns |
| Regional Aggregation | Analysis | `groupby("Region")` mean happiness, sorted descending |
| 4 Visualizations | Output | Horizontal bar, scatter, heatmap, vertical bar by region |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📁 **CSV Data Ingestion** | Loads `happiness_data.csv` using `pd.read_csv()` |
| 📅 **Dynamic Latest-Year Filter** | Auto-detects the most recent year via `df["Year"].max()` — no hardcoding |
| 🔍 **Data Profiling** | `head()`, `info()`, `describe()`, and `isnull().sum()` in one pass |
| 🌍 **Multi-Country, Multi-Year** | 300 records spanning 6 years (2018–2023) across multiple countries and regions |
| 🏆 **Top 10 Happiest Countries** | Dynamic ranking of the top 10 countries in the latest year by Happiness Score |
| 💰 **GDP vs Happiness Scatter** | Region-coloured scatter plot revealing the economic dimension of happiness |
| 🔗 **6-Factor Correlation Matrix** | Pearson correlation across HappinessScore, GDPPerCapita, SocialSupport, LifeExpectancy, Freedom, Generosity |
| 🌏 **Regional Comparison** | `groupby("Region")` mean scores sorted to rank regions by average happiness |
| ✅ **Zero Missing Values** | Dataset is fully clean — `isnull().sum()` confirms 0 nulls across all 9 columns |
| 🎨 **YlGnBu Heatmap Palette** | Heatmap rendered in `YlGnBu` for intuitive value-intensity reading |

---

## 🏗️ Project Structure

```
📦 happiness-analysis/
│
├── 📓 happiness_analysis.ipynb    ← Jupyter Notebook (main analysis file)
├── 🗂️ happiness_data.csv          ← World happiness dataset (300 records, 2018–2023)
│
└── 📄 README.md                   ← Project documentation
```

> **How to run:**
> ```bash
> pip install pandas matplotlib seaborn notebook
> jupyter notebook happiness_analysis.ipynb
> ```
> Ensure `happiness_data.csv` is in the same directory as the notebook before running.

---

## 🔄 Project Workflow

```
happiness_data.csv
       │
       ▼  pd.read_csv()
   DataFrame (300 rows × 9 columns)
       │
       ├──▶  Data Inspection
       │     head() · info() · describe() · isnull().sum()
       │
       ├──▶  Latest-Year Filtering
       │     latest_year = df["Year"].max()
       │     latest_data = df[df["Year"] == latest_year]
       │
       ├──▶  Top 10 Ranking
       │     top10 = latest_data.sort_values("HappinessScore", ascending=False).head(10)
       │
       ├──▶  Chart 1: Horizontal Bar Plot
       │     Top 10 Happiest Countries in {latest_year} (Seaborn barplot)
       │
       ├──▶  Chart 2: Scatter Plot
       │     GDP per Capita vs Happiness Score, coloured by Region (Seaborn scatterplot)
       │
       ├──▶  Chart 3: Correlation Heatmap
       │     6-factor Pearson correlation matrix (Seaborn heatmap, YlGnBu)
       │
       ├──▶  Regional Aggregation
       │     region_avg = latest_data.groupby("Region")["HappinessScore"].mean()
       │                             .sort_values(ascending=False)
       │
       └──▶  Chart 4: Regional Bar Plot
             Average Happiness Score by Region (Seaborn barplot)
```

---

## 📓 Notebook Walkthrough

The notebook executes its entire analysis pipeline in a single primary code cell. Here is a step-by-step breakdown of every operation:

---

**Step 1 — Import Libraries**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Imports Pandas for data handling, Matplotlib as the base plotting engine, and Seaborn for statistical chart rendering.

---

**Step 2 — Load Data**
```python
df = pd.read_csv("happiness_data.csv")
```
Reads the happiness dataset into a DataFrame. Unlike the COVID project, no date parsing is needed here — the `Year` column is stored as `int64`.

---

**Step 3 — Data Inspection**
```python
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
```
Runs a four-part profile of the dataset:
- `head()` — previews the first 5 rows including Country, Region, Year, HappinessScore, and all 5 factor columns
- `info()` — shows 9 columns, 300 non-null entries, dtypes (`str` × 2, `int64` × 1, `float64` × 6), and 21.2 KB memory usage
- `describe()` — generates count, mean, std, min/max, and percentiles for all numeric columns
- `isnull().sum()` — confirms zero missing values across all 9 columns

---

**Step 4 — Dynamic Latest-Year Filtering**
```python
latest_year = df["Year"].max()
latest_data = df[df["Year"] == latest_year]
```
Automatically detects the most recent year in the dataset (`2023`) and filters all records for that year into `latest_data`. This makes the analysis self-updating — if newer data is added to the CSV, the notebook adapts without any code changes.

---

**Step 5 — Top 10 Ranking**
```python
top10 = latest_data.sort_values("HappinessScore", ascending=False).head(10)
```
Sorts the latest-year data by `HappinessScore` in descending order and takes the top 10 countries, ready for the horizontal bar chart.

---

**Step 6 — Chart 1: Top 10 Happiest Countries**
```python
sns.barplot(x="HappinessScore", y="Country", data=top10)
plt.title(f"Top 10 Happiest Countries in {latest_year}")
plt.xlabel("Happiness Score")
plt.ylabel("Country")
```
Renders a horizontal Seaborn bar chart with `HappinessScore` on the x-axis and country names on the y-axis. The dynamic title reflects whatever `latest_year` resolves to.

---

**Step 7 — Chart 2: GDP per Capita vs Happiness Score**
```python
sns.scatterplot(x="GDPPerCapita", y="HappinessScore", data=latest_data, hue="Region")
plt.title("GDP per Capita vs Happiness Score")
```
Plots each country's GDP per Capita against its Happiness Score, with each point coloured by `Region`. The `hue` parameter automatically assigns distinct colours and generates a legend — revealing whether wealthier regions also tend to be happier.

---

**Step 8 — Chart 3: Correlation Heatmap**
```python
correlation = latest_data[["HappinessScore", "GDPPerCapita", "SocialSupport",
                            "LifeExpectancy", "Freedom", "Generosity"]].corr()
sns.heatmap(correlation, annot=True, cmap="YlGnBu")
plt.title("Correlation Between Happiness Factors")
```
Computes the Pearson correlation matrix across all 6 key columns and renders it as an annotated 6×6 heatmap with the `YlGnBu` palette. Stronger positive correlations appear in deeper blue tones.

---

**Step 9 — Regional Aggregation**
```python
region_avg = latest_data.groupby("Region")["HappinessScore"].mean().sort_values(ascending=False)
```
Groups the latest-year data by `Region`, computes the mean `HappinessScore` for each, and sorts descending — ranking regions from happiest to least happy.

---

**Step 10 — Chart 4: Average Happiness Score by Region**
```python
sns.barplot(x=region_avg.index, y=region_avg.values)
plt.xticks(rotation=45)
plt.title("Average Happiness Score by Region")
plt.xlabel("Region")
plt.ylabel("Average Happiness Score")
```
Renders a vertical Seaborn bar chart of average happiness by region, with x-axis labels rotated 45° for readability. This allows direct regional comparison alongside the country-level ranking from Chart 1.

---

## 🗂️ Dataset — happiness_data.csv

| Column | Type | Description |
|--------|------|-------------|
| `Country` | `str` | Name of the country |
| `Region` | `str` | Geographic / geopolitical region |
| `Year` | `int64` | Year of the survey (2018–2023) |
| `HappinessScore` | `float64` | Overall happiness score (scale: 0–10) |
| `GDPPerCapita` | `float64` | GDP per capita contribution to happiness |
| `SocialSupport` | `float64` | Social support score |
| `LifeExpectancy` | `float64` | Healthy life expectancy contribution |
| `Freedom` | `float64` | Freedom to make life choices score |
| `Generosity` | `float64` | Generosity contribution score |

**Dataset Summary:**

| Metric | Value |
|--------|-------|
| Total Records | 300 rows |
| Year Range | 2018 to 2023 |
| Missing Values | 0 (all 9 columns fully populated) |
| Memory Usage | 21.2 KB |
| Data Types | `str` × 2, `int64` × 1, `float64` × 6 |

**Sample Data (first 5 rows — Finland):**

```
Country   Region   Year  HappinessScore  GDPPerCapita  SocialSupport  LifeExpectancy  Freedom  Generosity
Finland   Europe   2018  4.420           0.750         1.060          0.474           0.697    0.158
Finland   Europe   2019  4.753           0.741         0.889          0.674           0.337    0.399
Finland   Europe   2020  4.523           0.769         1.405          0.712           0.310    0.373
Finland   Europe   2021  4.553           0.757         1.535          0.702           0.551    0.353
Finland   Europe   2022  4.691           0.771         0.969          0.558           0.581    0.466
```

**Descriptive Statistics (from `describe()` output):**

| Metric | HappinessScore | GDPPerCapita | SocialSupport | LifeExpectancy | Freedom | Generosity |
|--------|---------------|--------------|---------------|----------------|---------|------------|
| Mean | 5.955 | 1.195 | 1.048 | 0.686 | 0.436 | 0.255 |
| Std | 1.097 | 0.407 | 0.317 | 0.224 | 0.143 | 0.145 |
| Min | 3.817 | 0.479 | 0.506 | 0.300 | 0.201 | 0.001 |
| Max | 7.907 | 2.057 | 1.595 | 1.088 | 0.697 | 0.500 |
| 25th % | 4.967 | 0.849 | 0.789 | 0.485 | 0.314 | 0.140 |
| 50th % | 6.174 | 1.131 | 1.031 | 0.699 | 0.419 | 0.264 |
| 75th % | 6.848 | 1.516 | 1.325 | 0.889 | 0.563 | 0.377 |

---

## 📊 Visualizations

The notebook produces four charts, each answering a distinct analytical question:

---

### 1. Seaborn Horizontal Bar Plot — Top 10 Happiest Countries

```python
sns.barplot(x="HappinessScore", y="Country", data=top10)
plt.title(f"Top 10 Happiest Countries in {latest_year}")
```

Displays the top 10 countries ranked by Happiness Score in the most recent year of the dataset. Countries are ordered from highest to lowest, displayed horizontally for easy label readability.

**Answers:** *Which countries rank as the happiest in the world in the latest year?*

---

### 2. Seaborn Scatter Plot — GDP per Capita vs Happiness Score

```python
sns.scatterplot(x="GDPPerCapita", y="HappinessScore", data=latest_data, hue="Region")
plt.title("GDP per Capita vs Happiness Score")
```

Plots every country's GDP per Capita against its Happiness Score for the latest year, with each point colour-coded by Region. The `hue="Region"` parameter automatically creates a colour legend revealing regional clustering patterns.

**Answers:** *Is there a relationship between a country's economic output and its people's happiness? Do wealthier regions cluster at higher happiness scores?*

---

### 3. Seaborn Heatmap — Correlation Between Happiness Factors

```python
correlation = latest_data[["HappinessScore", "GDPPerCapita", "SocialSupport",
                            "LifeExpectancy", "Freedom", "Generosity"]].corr()
sns.heatmap(correlation, annot=True, cmap="YlGnBu")
plt.title("Correlation Between Happiness Factors")
```

Computes a 6×6 Pearson correlation matrix and renders it as an annotated heatmap with the `YlGnBu` palette. Each cell shows the exact correlation coefficient; deeper blue indicates stronger positive correlation.

**Answers:** *Which factors correlate most strongly with Happiness Score? How do GDP, Social Support, Life Expectancy, Freedom, and Generosity relate to each other?*

---

### 4. Seaborn Vertical Bar Plot — Average Happiness Score by Region

```python
region_avg = latest_data.groupby("Region")["HappinessScore"].mean().sort_values(ascending=False)
sns.barplot(x=region_avg.index, y=region_avg.values)
plt.title("Average Happiness Score by Region")
```

Aggregates all countries in the latest year by their Region, computes the mean Happiness Score per region, sorts descending, and plots as a vertical bar chart with rotated x-axis labels.

**Answers:** *Which global regions are the happiest on average? How large is the happiness gap between regions?*

---

## 📈 Key Results & Insights

Based on the notebook's printed output for the full 300-record dataset:

| Insight | Value |
|---------|-------|
| 📊 Total Records | 300 entries across multiple countries and 6 years (2018–2023) |
| ✅ Data Quality | Zero missing values — no cleaning required |
| 🏆 Highest Happiness Score (Ever) | **7.907** — maximum across all 300 records |
| 📉 Lowest Happiness Score (Ever) | **3.817** — minimum across all 300 records |
| 📆 Latest Year Analysed | **2023** (auto-detected via `df["Year"].max()`) |
| 💰 Average GDP per Capita | **1.195** across all records |
| 💰 Highest GDP per Capita | **2.057** |
| 💚 Average Social Support | **1.048** |
| 🏃 Average Freedom Score | **0.436** |
| 🤝 Average Generosity | **0.255** (lowest average factor) |
| 🌍 Mean Happiness Score (All) | **5.955** |
| 📐 Std Dev of Happiness | **1.097** — moderate spread across countries |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.13+ | Core programming language |
| 📓 **Jupyter Notebook** | Latest | Interactive development and execution environment |
| 🐼 **Pandas** | 2.0+ | CSV loading, groupby aggregation, sort, describe, filtering |
| 📊 **Matplotlib** | 3.7+ | Base plotting engine, figure sizing, axis formatting |
| 🎨 **Seaborn** | 0.12+ | `barplot`, `scatterplot`, `heatmap` (YlGnBu palette) |
| 🔗 **df.corr()** | Pandas | Pearson correlation matrix across 6 happiness factor columns |
| 📐 **groupby().mean()** | Pandas | Regional average happiness score computation |
| 🔍 **sort_values()** | Pandas | Country ranking and regional sorting |

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Complete EDA Pipeline** | Covers load → inspect → filter → rank → aggregate → visualize in a linear flow |
| 📅 **Dynamic Year Detection** | `df["Year"].max()` auto-selects the latest year — zero hardcoding |
| 🌍 **Multi-Year Coverage** | 6 years of data (2018–2023) enables both longitudinal and snapshot analysis |
| 🎨 **Region-Coloured Scatter** | `hue="Region"` in scatter plot reveals geographic clustering without extra code |
| 🔗 **6-Factor Correlation** | Heatmap exposes relationships between all key happiness drivers simultaneously |
| 🌏 **Regional Aggregation** | `groupby("Region")` adds a second layer of analysis beyond individual country ranking |
| ✅ **Clean Dataset** | Zero missing values means analysis begins immediately with no preprocessing step |
| 📊 **4 Distinct Chart Types** | Horizontal bar, scatter, heatmap, and vertical bar each answer a different question |
| ⚡ **Single-Cell Execution** | Entire pipeline runs in one cell — fast, reproducible, and easy to share |
| 🧪 **Extensible** | New years, countries, factors, or chart types can be added with minimal code changes |

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

> *"Happiness may be subjective — but its patterns are measurable, and the data never lies."*

**🎓 Role:** Junior Python Developer | Data Analytics Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Pandas · Matplotlib · Seaborn · EDA · Data Visualization · Jupyter Notebooks

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame operations, groupby, sort, filtering
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/contents.html) — Figure layout, axis formatting, and tight_layout
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — barplot, scatterplot, heatmap references
- 🌍 [World Happiness Report](https://worldhappiness.report/) — Original source of happiness index data and methodology
- 📈 [Real Python — Pandas EDA](https://realpython.com/pandas-python-explore-dataset/) — Exploratory data analysis guide
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and data science courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
