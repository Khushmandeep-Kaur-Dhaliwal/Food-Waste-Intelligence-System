# Food-Waste-Intelligence-System
A Python-based Data Science project that analyses food waste patterns using publicly available datasets. It provides interactive visualizations, food category analysis, country-wise comparisons and supply-chain insights through a Streamlit dashboard to promote food waste awareness and reduction.
## ⚙️ How It Works

The **Food Waste Intelligence System** is an interactive web dashboard built with **Python**, **Streamlit**, **Pandas**, and **Plotly** to analyze global Food Loss and Waste (FLW) records:

1. **Data Loading & Preparation:** The app ingests cleaned product-level food waste records (`food_waste_clean.csv`) alongside pre-aggregated summaries (`country_summary.csv`, `food_group_summary.csv`, and `stage_summary.csv`).
2. **Interactive Sidebar Filtering:** Users can dynamically slice the dataset by **Measurement Unit** (e.g., `% of agricultural production`), **Country**, **Food Group**, and **Supply-Chain Stage**.
3. **Real-Time KPI Calculation:** As filters change, the system recalculates four headline metrics: *Records in View*, *Sum of Reported Quantities*, *Average per Record*, and *Countries Represented*.
4. **Visual Analytics & Record Search:** Plotly generates interactive bar and pie charts, while a live search box lets users look up specific products and export the filtered table as a CSV file.

---

## 📊 Output & Key Findings

For the `% of agricultural production` measurement view (**137 records across 10 countries**), the application outputs the following insights:

* **Highest Waste by Food Group:** **Vegetables and Vegetable Products (`03580`)** account for the largest reported loss volume, followed by **Meat and Meat Products (`18760`)** and **Fruit (`14220`)**.
* **Highest Loss by Supply-Chain Stage:** **Primary production** experiences the highest reported losses compared to **Processing and manufacturing** and **Retail**.
* **Top Countries in View:** **Sweden**, **Austria**, and **Finland** represent the highest cumulative reported quantities in the filtered dataset.
* **Actionable Data Export:** Users can filter records by product name (such as *Hen Eggs*, *Cow Milk*, or *Common Wheat Grain*) and download the exact subset via the **Download filtered records as CSV** button.

---

## 📸 Screenshots

### 1. Main Dashboard, Filters & KPIs
![Dashboard Overview](Food_Waste_Intelligence_Project%20(1)/screenshots/dashboard_overview.png)

### 2. Food Group & Supply Chain Stage Analysis
![Food Group and Supply Chain Charts](Food_Waste_Intelligence_Project%20(1)/screenshots/foodgroup_and_supplychains_charts.png)

### 3. Country Breakdown & Edible Fraction Analysis
![Country and Edible Fraction Charts](Food_Waste_Intelligence_Project%20(1)/screenshots/country_and_edible_charts.png)

### 4. Interactive Record Explorer & CSV Export
![Explore Records](Food_Waste_Intelligence_Project%20(1)/screenshots/explore_records.png)

### 5. Automated Insights & Possible Actions
![Insights Section](Food_Waste_Intelligence_Project%20(1)/screenshots/insights_section.png)
