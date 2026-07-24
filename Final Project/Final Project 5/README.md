<div align="center">

# -- ! Stock Market Analysis ! --
### *Exploratory Data Analysis & Visualization of Multi-Company Stock Data*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"The stock market is a device for transferring money from the impatient to the patient — data helps you see which one you are."*

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

The **Stock Market Analysis** is a data-analysis and visualization project built using **pandas**, **matplotlib**, and **seaborn** to explore historical stock price data across multiple companies. The notebook loads OHLCV (Open, High, Low, Close, Volume) records, plots closing-price trends per company, computes moving averages, compares trading volumes, and studies correlations between price and volume metrics.

This project is designed to:
- Strengthen understanding of time-series parsing and rolling-window calculations with pandas
- Practice exploratory data analysis (EDA) on financial market data
- Apply statistical visualization techniques with seaborn and matplotlib
- Uncover relationships between price metrics and trading volume

---

## 🎯 Problem Statement

> **Objective:** Analyze multi-company stock data to understand price trends, momentum, and trading activity.

Given a dataset of daily stock records containing Open, High, Low, Close, and Volume values for several companies, the notebook parses dates, plots closing-price trends for every company, calculates short- and long-term moving averages for one company, ranks companies by average trading volume, and examines correlations between price and volume metrics.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Inspection | Analysis | Reads CSV, parses dates, inspects structure and summary stats |
| Closing Price Trend | Visualization | Line plot of closing price over time for every company |
| Moving Averages | Analysis | 10-day and 50-day rolling averages for one company |
| Average Trading Volume | Visualization | Bar plot ranking companies by average volume |
| Correlation Heatmap | Analysis | Relationships between Open, High, Low, Close, and Volume |

The goal is to demonstrate a **complete, beginner-friendly EDA workflow** on real-world financial market data.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads `stock_data.csv` into a pandas DataFrame |
| 📅 **Date Parsing** | Converts the `Date` column to proper datetime format |
| 🔍 **Data Inspection** | Displays head, info, describe, and null-value summary |
| 📈 **Multi-Company Trend Line** | Overlaid closing-price plot for every company |
| 📉 **Rolling Moving Averages** | 10-day and 50-day moving averages computed and plotted |
| 🏢 **Volume Comparison** | Bar plot of average trading volume by company |
| 🧮 **Correlation Analysis** | Heatmap across Open, High, Low, Close, and Volume |
| 🖼️ **Figure Sizing & Labels** | Every plot titled, labeled, and rotation-adjusted for readability |

---

## 🏗️ Project Structure

```
📦 stock-market-analysis/
│
├── 📓 stock_market_analysis.ipynb    ← Main Jupyter notebook (entry point)
├── 📄 stock_data.csv                 ← Source dataset (expected in same directory)
│
└── 📄 README.md                      ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset
      │
      ▼
┌─────────────────────────────┐
│  Parse Dates & Inspect Data   │
│  (head/info/describe/isnull)  │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Plot Closing Price Trend     │
│  for Every Company             │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Compute 10 & 50 Day Moving    │
│  Averages for First Company    │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Rank Companies by Average     │
│  Trading Volume                 │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Generate Correlation          │
│  Heatmap of Price/Volume       │
└────────────┬────────────────┘
             │
             ▼
        Insights Ready ✅
```

---

## 🧹 Part A — Data Preparation

### 📝 1. Loading & Inspecting the Data

The dataset is read directly from `stock_data.csv`, the `Date` column is converted to a proper datetime type, and a quick structural inspection follows.

**Logic:**
```python
df = pd.read_csv("stock_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

---

### 🏢 2. Identifying Companies

> Extracts the unique list of companies present in the dataset for per-company plotting and analysis.

**Logic:**
```python
companies = df["Company"].unique()
```

---

## 📊 Part B — Exploratory Analysis

### 📈 3. Closing Price Trend by Company

> Overlaid line plot showing the closing-price trend over time for every company in the dataset.

**Logic:**
```python
for company in companies:
    company_data = df[df["Company"] == company]
    plt.plot(company_data["Date"], company_data["Close"], label=company)
plt.title("Closing Price Trend by Company")
plt.legend()
```

---

### 📉 4. Moving Averages (10-Day & 50-Day)

> Computes short-term and long-term rolling averages of the closing price for the first company and plots them alongside the raw price.

**Logic:**
```python
first_company_data["MA10"] = first_company_data["Close"].rolling(window=10).mean()
first_company_data["MA50"] = first_company_data["Close"].rolling(window=50).mean()

plt.plot(first_company_data["Date"], first_company_data["Close"], label="Close Price")
plt.plot(first_company_data["Date"], first_company_data["MA10"], label="10 Day Moving Average")
plt.plot(first_company_data["Date"], first_company_data["MA50"], label="50 Day Moving Average")
plt.title("Moving Averages for " + first_company)
```

---

### 🏢 5. Average Trading Volume by Company

> Bar plot ranking companies by their average trading volume.

**Logic:**
```python
avg_volume = df.groupby("Company")["Volume"].mean().sort_values(ascending=False)

sns.barplot(x=avg_volume.index, y=avg_volume.values)
plt.title("Average Trading Volume by Company")
```

---

### 🔗 6. Correlation Heatmap

> Heatmap of correlations between Open, High, Low, Close, and Volume.

**Logic:**
```python
correlation = df[["Open", "High", "Low", "Close", "Volume"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Between Stock Metrics")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 📅 `pd.to_datetime()` | Parsing date strings into datetime objects |
| 📥 `pd.read_csv()` | Loading tabular data into a DataFrame |
| 🔁 `for company in companies` | Iterating and plotting per-group time series |
| 📉 `.rolling(window=n).mean()` | Short- and long-term moving average calculation |
| 🏢 `groupby().mean()` | Company-wise aggregation of trading volume |
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
- 📈 **Company Price Trends** — Closing-price trajectories compared across all companies
- 📉 **Momentum Signals** — 10-day and 50-day moving averages highlighting short- vs long-term trend direction
- 🏢 **Volume Ranking** — Companies ordered by average trading volume
- 🔗 **Metric Correlations** — Heatmap showing how price and volume metrics move together

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core EDA concepts: parsing, rolling windows, and visualization in one notebook |
| 🔄 **Reusability** | Trend and moving-average logic can be reused for any OHLCV dataset |
| 📚 **Educational** | Each plot reinforces a specific market-analysis question |
| 🖥️ **Minimal Dependencies** | Runs with pandas, matplotlib, and seaborn only |
| ⚡ **Self-Contained** | Single notebook, instantly runnable end-to-end |
| 🧪 **Extensible** | Easy to add new companies, indicators (RSI, MACD), or forecasting models |
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
- 📈 [Investopedia — Moving Averages](https://www.investopedia.com/terms/m/movingaverage.asp) — Reference for moving average interpretation
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
