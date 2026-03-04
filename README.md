# 📈 Feature Launch Impact Analysis: One-Click Reorder A/B Test

## 📝 Project Overview
This project simulates an end-to-end A/B test for an E-commerce platform testing a new **"One-Click Reorder"** button on the product page. 

The goal is to determine if bypassing the standard 3-step checkout process increases the **Conversion Rate**, reduces **Checkout Time**, and ultimately drives more **Revenue**.

## 🛠️ Tech Stack
- **Python:** Data Generation & Statistical Analysis (`pandas`, `numpy`, `scipy`, `statsmodels`).
- **Power BI:** Interactive Dashboard for Stakeholders.

## 📁 Repository Structure
```
feature_launch_ab_test/
├── assets/                    # Presentation assets (DAX screenshots, Dashboard)
├── generate_ab_test_data.py   # Script to generate realistic A/B testing user data
├── ab_test_analysis.py        # Script to perform statistical significance testing
├── ab_test_data.csv           # Raw data (simulated 10k users)
├── requirements.txt           # Python dependencies
├── .gitignore                 # Standard Python ignores
└── README.md                  # Detailed project documentation
```

## 🚀 How to Run Locally

### 1. Generate the Data
This simulates 10,000 users split cleanly into `Control` (Standard Checkout) and `Treatment` (One-Click Reorder).
```bash
python generate_ab_test_data.py
```
*This will create the `ab_test_data.csv` file.*

### 2. Run the Statistical Analysis
This runs a Two-Sided Z-Test for Proportions (Conversion Rate) and a T-Test for Means (Time Spent), outputting the P-values and Business Impact projections.
```bash
python ab_test_analysis.py
```

## 📊 Business Problem & Hypothesis
- **Problem:** Returning users find the standard 3-step checkout tedious when simply trying to reorder a previously purchased item, leading to cart abandonment.
- **Null Hypothesis ($H_0$):** The One-Click Reorder button has no effect on checkout conversion rate.
- **Alternative Hypothesis ($H_A$):** The One-Click Reorder button significantly increases the checkout conversion rate.

## 📊 Data Modeling & DAX Measures
To build the interactive dashboard, I implemented several key performance indicators (KPIs) using DAX. These allow for dynamic filtering by group (Control vs. Treatment).

### 1. Total User Count
```dax
Total_user = COUNTROWS(ab_test_data)
```
![Total User Measure](assets/total_user_dax.png)

### 2. Average Checkout Time
*Used to measure the efficiency gain from the One-Click Reorder feature.*
```dax
Avg_checkout_time = AVERAGE(ab_test_data[time_spent_secs])
```
![Avg Checkout Time Measure](assets/avg_checkout_time_dax.png)

### 3. Conversion Rate (%)
*A critical metric for calculating business impact. It filters for successful purchases divided by total users.*
```dax
Conversion_rate = 
DIVIDE(
    CALCULATE(COUNTROWS(ab_test_data), ab_test_data[purchase_completed] = 1),
    [Total_user], 
    0
)
```
![Conversion Rate Measure](assets/conversion_rate_dax.png)

### 4. Total Revenue
```dax
Total_revenue = SUM(ab_test_data[order_value])
```
![Total Revenue Measure](assets/total_revenue_dax.png)

## 🎨 Interactive Dashboard Preview
The Power BI dashboard provides a high-level overview for stakeholders while allowing deep-dives into user behavior.

![Full Dashboard Preview](assets/dashboard_full.png)

> **Key Insight:** The treatment group (Treatment) shows a dramatic shift towards lower checkout times (centered around 30s) compared to the control group (Control, centered around 90s).

## 🎯 Results & Conclusion
Based on the generated statistical analysis:
1. **Conversion Rate Uplift:** The One-Click Button significantly increases conversion.
2. **Checkout Time:** Reduced by ~60 seconds per user, statistically significant (p-value < 0.05).
3. **Rollout Recommendation:** ✅ Roll Out the feature to 100% of users. The estimated revenue uplift is highly positive.

