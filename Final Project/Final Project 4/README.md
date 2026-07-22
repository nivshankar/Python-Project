<div align="center">

# -- ! Air Quality Analysis ! --
### *Exploratory Data Analysis & Visualization of City-Wise Air Quality Data*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"You can't manage what you don't measure — and you can't fix the air until you see what's in it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Preparation](#-part-a--data-preparation)
- [📊 Part B — Exploratory Analysis](#-part-b--exploratory-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Air Quality Analysis** is a data-analysis and visualization project built using **pandas**, **matplotlib**, and **seaborn** to explore a city-wise air quality dataset. The notebook loads pollutant and weather readings over time, ranks cities by average AQI, tracks trends for the worst-affected city, and studies relationships between weather and pollutant levels.

This project is designed to:
- Strengthen understanding of time-series parsing and grouped aggregation with pandas
- Practice exploratory data analysis (EDA) on environmental data
- Apply statistical visualization techniques with seaborn and matplotlib
- Uncover relationships between weather conditions and pollutant concentrations

---

## 🎯 Problem Statement

> **Objective:** Analyze city-level air quality data to identify pollution hotspots, trends, and contributing factors.

Given a dataset of daily air quality readings containing pollutant levels (PM2.5, PM10, NO2, SO2, CO, O3), AQI, temperature, and humidity across multiple cities, the notebook parses dates, ranks cities by average AQI, visualizes the AQI trend for the worst-performing city, and examines correlations between pollutants and weather variables.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Inspection | Analysis | Reads CSV, parses dates, inspects structure and summary stats |
| City-Wise AQI Ranking | Analysis | Groups data by city and computes average AQI |
| AQI Trend Over Time | Visualization | Line plot of AQI for the most polluted city |
| Temperature vs PM2.5 | Visualization | Scatter plot of temperature against PM2.5 by city |
| Correlation Heatmap | Analysis | Relationships between pollutants, AQI, and weather |

The goal is to demonstrate a **complete, beginner-friendly EDA workflow** on a real-world environmental dataset.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads `air_quality_data.csv` into a pandas DataFrame |
| 📅 **Date Parsing** | Converts the `Date` column to proper datetime format |
| 🔍 **Data Inspection** | Displays head, info, describe, and null-value summary |
| 🏙️ **City-Wise Grouping** | Computes and ranks average AQI per city |
| 📈 **AQI Trend Line** | Time-series visualization for the worst-affected city |
| 🌡️ **Weather vs Pollution** | Scatter plot relating temperature to PM2.5 levels |
| 🧮 **Correlation Analysis** | Heatmap across all pollutant and weather features |
| 🖼️ **Figure Sizing & Labels** | Every plot titled, labeled, and rotation-adjusted for readability |

---

## 🏗️ Project Structure

```
📦 air-quality-analysis/
│
├── 📓 air_quality_analysis.ipynb    ← Main Jupyter notebook (entry point)
├── 📄 air_quality_data.csv          ← Source dataset (expected in same directory)
│
└── 📄 README.md                     ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset
      │
      ▼
┌─────────────────────────────┐
│  Parse Dates & Inspect Data  │
│  (head/info/describe/isnull) │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Group by City & Compute      │
│  Average AQI                  │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Identify Worst City &        │
│  Plot AQI Trend Over Time     │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Compare Temperature vs       │
│  PM2.5 Across Cities          │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Generate Correlation          │
│  Heatmap of All Factors       │
└────────────┬────────────────┘
             │
             ▼
        Insights Ready ✅
```

---

## 🧹 Part A — Data Preparation

### 📝 1. Loading & Inspecting the Data

The dataset is read directly from `air_quality_data.csv`, the `Date` column is converted to a proper datetime type, and a quick structural inspection follows.

**Logic:**
```python
df = pd.read_csv("air_quality_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

---

### 🏙️ 2. City-Wise Average AQI

> Groups the dataset by `City` and computes the mean AQI for each, sorted from worst to best.

**Logic:**
```python
city_avg_aqi = df.groupby("City")["AQI"].mean().sort_values(ascending=False)
```

---

## 📊 Part B — Exploratory Analysis

### 🔍 3. Average AQI by City

> Bar plot ranking every city by its average Air Quality Index.

**Logic:**
```python
sns.barplot(x=city_avg_aqi.index, y=city_avg_aqi.values)
plt.title("Average AQI by City")
```

---

### 📈 4. AQI Trend Over Time (Worst City)

> Line plot tracking how AQI changes over time for the city with the highest average AQI.

**Logic:**
```python
worst_city = city_avg_aqi.index[0]
worst_city_data = df[df["City"] == worst_city]

sns.lineplot(x="Date", y="AQI", data=worst_city_data)
plt.title("AQI Trend Over Time for " + worst_city)
```

---

### 🌡️ 5. Temperature vs PM2.5 Levels

> Scatter plot examining how temperature relates to PM2.5 concentration, colored by city.

**Logic:**
```python
sns.scatterplot(x="Temperature", y="PM2.5", data=df, hue="City")
plt.title("Temperature vs PM2.5 Levels")
```

---

### 🔗 6. Correlation Heatmap

> Heatmap of correlations between all pollutants, AQI, temperature, and humidity.

**Logic:**
```python
correlation = df[["PM2.5", "PM10", "NO2", "SO2", "CO", "O3", "AQI", "Temperature", "Humidity"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Between Air Quality Factors")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 📅 `pd.to_datetime()` | Parsing date strings into datetime objects |
| 📥 `pd.read_csv()` | Loading tabular data into a DataFrame |
| 🏙️ `groupby().mean()` | City-wise aggregation of AQI |
| 📈 `sns.lineplot()` | Time-series trend visualization |
| 🌡️ `sns.scatterplot()` | Bivariate relationship with categorical hue |
| 🔗 `df.corr()` + `sns.heatmap()` | Multi-feature correlation analysis |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, and aggregation |
| 📊 **Matplotlib** | Latest | Base plotting and figure control |
| 🎨 **Seaborn** | Latest | Statistical visualization on top of matplotlib |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment |

---

## 📈 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Parsed Time-Series Data** — Dates converted for proper chronological analysis
- 🏙️ **City Ranking** — Cities ordered from most to least polluted by average AQI
- 📈 **Pollution Trend** — Time-based AQI pattern revealed for the worst-affected city
- 🌡️ **Weather-Pollution Link** — Visual relationship between temperature and PM2.5
- 🔗 **Feature Correlations** — Heatmap highlighting which pollutants move together and with AQI

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core EDA concepts: parsing, grouping, and visualization in one notebook |
| 🔄 **Reusability** | Aggregation and plotting logic can be reused for other environmental datasets |
| 📚 **Educational** | Each plot reinforces a specific air-quality analysis question |
| 🖥️ **Minimal Dependencies** | Runs with pandas, matplotlib, and seaborn only |
| ⚡ **Self-Contained** | Single notebook, instantly runnable end-to-end |
| 🧪 **Extensible** | Easy to add new cities, pollutants, or forecasting models |
| 📖 **Readable Code** | Clear, linear structure from loading to insight |
| 🛡️ **Data Safety** | Structural checks run before any analysis or plotting |

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
**🛠️ Skills:** Python · Pandas · Data Visualization · Exploratory Data Analysis

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Pandas Official Docs](https://pandas.pydata.org/docs/) — Official pandas reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Core plotting reference
- 🌫️ [EPA — Air Quality Index Basics](https://www.airnow.gov/aqi/aqi-basics/) — Reference for AQI interpretation
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
