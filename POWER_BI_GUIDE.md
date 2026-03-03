# Power BI Visual Guide for A/B Testing

This guide helps you build a recruiter-friendly Power BI Dashboard based on the `ab_test_data.csv` you just generated.

## 1. Load & Transform Data
1. Open Power BI Desktop.
2. **Get Data** -> Text/CSV -> Select `ab_test_data.csv`.
3. Click **Transform Data**:
   - Filter `reorder_checkout_initiated` to `1` (we only care about users who tried to reorder).
   - Change `purchase_completed` to **Whole Number** or **True/False**.
   - Change `order_value` and `time_spent_secs` to **Decimal Number**.
4. Click **Close & Apply**.

## 2. Create Calculated Measures (DAX)
To create a recruiter-ready dashboard, you need DAX measures (recruiters look for DAX skills!). 

Right-click the table and choose **New Measure** for each of these:

```dax
Total Users = COUNTROWS(ab_test_data)

Total Revenue = SUM(ab_test_data[order_value])

Avg Checkout Time = AVERAGE(ab_test_data[time_spent_secs])

Conversion Rate = 
DIVIDE(
    CALCULATE(COUNTROWS(ab_test_data), ab_test_data[purchase_completed] = 1),
    [Total Users], 
    0
)
```

## 3. Recommended Visualizations (The Dashboard Layout)

### 🔝 Top Row: KPI Cards
Add 4 **Card** visuals across the top of the dashboard.
- [Card 1] **Conversion Rate** 
- [Card 2] **Avg Checkout Time**
- [Card 3] **Total Revenue**
- [Card 4] **Total Users** (who initiated)

### 📊 Middle Row: Group Comparisons
- **Clustered Column Chart (Conversion Rate by Group):**
  - X-Axis: `group` (Control vs Treatment)
  - Y-Axis: `Conversion Rate` (Measure)
  - *Why? Shows the clear uplift visually.*
- **Line and Clustered Column Chart (Revenue vs Users):**
  - X-Axis: `group`
  - Column Y-Axis: `Total Revenue`
  - Line Y-Axis: `Total Users`

### 📉 Bottom Row: Detail
- **Scatter Plot (Time vs Order Value):**
  - Values: `user_id` (Do not summarize)
  - X-Axis: `time_spent_secs`
  - Y-Axis: `order_value`
  - Legend: `group`
  - *Why? Visually proves that Treatment (One-Click) users cluster to the left (faster time) compared to Control.*

## 🎨 Theme & Polish (Crucial for Recruiters)
1. **Slicer:** Add a Slicer for `group` so users can click between Control and Treatment and watch the KPIs update interactively.
2. **Theme:** Use **View -> Themes** and pick a professional dark or executive blue theme. Avoid default colors.
3. **Title:** Add a Text Box at the top exactly like: *"A/B Test Results: One-Click Reorder Launch Analysis"*.

## 📸 Capture & Attach Your Work
To make this GitHub ready:
1. Use **Windows + Shift + S** to take high-quality screenshots of your dashboard.
2. Create a folder named `images` in your `feature_launch_ab_test` directory.
3. Save your screenshots as `dashboard_overview.png` and `statistical_detail.png` inside that folder.
4. The `README.md` is already set up to display these images automatically!
