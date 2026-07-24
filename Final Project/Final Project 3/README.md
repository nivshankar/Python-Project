<div align="center">

# -- ! Titanic Survival Analysis ! --
### *Exploratory Data Analysis & Visualization of the Titanic Dataset*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"Data doesn't just tell you what happened — it tells you why it mattered."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Cleaning](#-part-a--data-cleaning)
- [📊 Part B — Exploratory Analysis](#-part-b--exploratory-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Titanic Survival Analysis** is a data-analysis and visualization project built using **pandas**, **matplotlib**, and **seaborn** to explore the well-known Titanic passenger dataset. The notebook loads the raw data, handles missing values, and produces a series of visual breakdowns of who survived the disaster and why.

This project is designed to:
- Strengthen understanding of data cleaning and missing-value imputation
- Practice exploratory data analysis (EDA) using pandas
- Apply statistical visualization techniques with seaborn and matplotlib
- Uncover relationships between passenger attributes and survival outcome

---

## 🎯 Problem Statement

> **Objective:** Analyze the Titanic passenger dataset to understand which factors most influenced survival.

Given a dataset of Titanic passengers containing attributes like class, sex, age, fare, and number of relatives aboard, the notebook cleans the data and visually explores how each factor relates to survival, culminating in a correlation study of the numeric features.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Loading & Inspection | Analysis | Reads CSV, inspects structure, types, and summary stats |
| Missing Value Handling | Cleaning | Fills missing Age and Embarked values |
| Survival Count | Visualization | Overall count of survivors vs non-survivors |
| Class & Gender Breakdown | Visualization | Survival rate grouped by Pclass and Sex |
| Age Distribution | Visualization | Age spread of survivors vs non-survivors |
| Correlation Heatmap | Analysis | Relationships between numeric features and survival |

The goal is to demonstrate a **complete, beginner-friendly EDA workflow** on a real-world dataset.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📥 **CSV Data Loading** | Reads `titanic_data.csv` into a pandas DataFrame |
| 🔍 **Data Inspection** | Displays head, info, describe, and null-value summary |
| 🧹 **Missing Value Imputation** | Fills `Age` with median, `Embarked` with mode |
| 📊 **Survival Rate Calculation** | Computes overall passenger survival rate |
| 📈 **Multiple Visualizations** | Countplot, barplots, histogram, and heatmap |
| 🎨 **Seaborn Styling** | Clean, publication-ready statistical plots |
| 🧮 **Correlation Analysis** | Numeric feature correlation against survival |
| 🖼️ **Figure Sizing & Labels** | Every plot titled and labeled for clarity |

---

## 🏗️ Project Structure

```
📦 titanic-survival-analysis/
│
├── 📓 titanic_analysis.ipynb    ← Main Jupyter notebook (entry point)
├── 📄 titanic_data.csv          ← Source dataset (expected in same directory)
│
└── 📄 README.md                 ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset
      │
      ▼
┌─────────────────────────────┐
│  Inspect Data (head/info/    │
│  describe/isnull)            │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Clean Missing Values         │
│  (Age → median,               │
│   Embarked → mode)            │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Compute Overall Survival     │
│  Rate                         │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Generate Visualizations:     │
│  Survival Count · Class ·     │
│  Gender · Age · Correlation   │
└────────────┬────────────────┘
             │
             ▼
        Insights Ready ✅
```

---

## 🧹 Part A — Data Cleaning

### 📝 1. Loading & Inspecting the Data

The dataset is read directly from `titanic_data.csv`, followed by a quick structural inspection.

**Logic:**
```python
df = pd.read_csv("titanic_data.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

---

### 🧼 2. Handling Missing Values

Missing `Age` values are filled with the column median, and missing `Embarked` values are filled with the most frequent category (mode).

**Logic:**
```python
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
```

---

### 📐 3. Overall Survival Rate

> A single summary statistic computed as the mean of the binary `Survived` column.

**Logic:**
```python
survival_rate = df["Survived"].mean()
print("Overall survival rate:", survival_rate)
```

---

## 📊 Part B — Exploratory Analysis

### 🔍 4. Survival Count

> A simple countplot comparing the number of passengers who survived versus those who did not.

**Logic:**
```python
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
```

---

### 🎟️ 5. Survival Rate by Passenger Class

> Bar plot comparing survival rate across the three ticket classes (1st, 2nd, 3rd).

**Logic:**
```python
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival Rate by Passenger Class")
```

---

### 🚻 6. Survival Rate by Gender

> Bar plot comparing survival rate between male and female passengers.

**Logic:**
```python
sns.barplot(x="Sex", y="Survived", data=df)
plt.title("Survival Rate by Gender")
```

---

### 🎂 7. Age Distribution by Survival

> Stacked histogram showing how age relates to survival outcome.

**Logic:**
```python
sns.histplot(data=df, x="Age", hue="Survived", multiple="stack", bins=20)
plt.title("Age Distribution by Survival")
```

---

### 🔗 8. Correlation Heatmap

> Heatmap of correlations between key numeric features and survival.

**Logic:**
```python
correlation = df[["Pclass", "Age", "SibSp", "Parch", "Fare", "Survived"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 📥 `pd.read_csv()` | Loading tabular data into a DataFrame |
| 🧹 `fillna()` | Median/mode imputation for missing values |
| 📊 `sns.countplot()` / `barplot()` | Categorical comparison visualizations |
| 📈 `sns.histplot()` | Distribution visualization with hue grouping |
| 🔗 `df.corr()` + `sns.heatmap()` | Feature correlation analysis |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, and manipulation |
| 📊 **Matplotlib** | Latest | Base plotting and figure control |
| 🎨 **Seaborn** | Latest | Statistical visualization on top of matplotlib |
| 📓 **Jupyter Notebook** | Latest | Interactive analysis environment |

---

## 📈 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Cleaned Dataset** — No missing values remain in `Age` or `Embarked`
- 📊 **Overall Survival Rate** — A single clear summary statistic
- 🎟️ **Class-Based Trends** — Higher classes show higher survival rates
- 🚻 **Gender-Based Trends** — Clear survival disparity between genders
- 🎂 **Age Patterns** — Distribution of survivors across age groups
- 🔗 **Feature Correlations** — Heatmap highlighting the strongest predictors of survival

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Core EDA concepts: cleaning, grouping, and visualization in one notebook |
| 🔄 **Reusability** | Cleaning and plotting logic can be reused for other datasets |
| 📚 **Educational** | Each plot reinforces a specific data-analysis question |
| 🖥️ **Minimal Dependencies** | Runs with pandas, matplotlib, and seaborn only |
| ⚡ **Self-Contained** | Single notebook, instantly runnable end-to-end |
| 🧪 **Extensible** | Easy to add new features, models, or additional plots |
| 📖 **Readable Code** | Clear, linear structure from loading to insight |
| 🛡️ **Data Safety** | Missing values are handled before any analysis runs |

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
- 📖 [Kaggle — Titanic Dataset](https://www.kaggle.com/c/titanic) — Source of the Titanic dataset
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
