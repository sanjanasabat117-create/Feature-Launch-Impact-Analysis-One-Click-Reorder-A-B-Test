# 📖 Project Story & Interview Study Guide
## Feature Launch Impact Analysis: One-Click Reorder A/B Test

This document is designed to help you explain this project in an interview. It breaks down the "Why", "How", and "So What" in a storytelling format (STAR Method) and provides common recruiter questions.

---

## 🎭 The Story: From Problem to Solution

### 1. The Business Problem (The "Why")
Imagine you are a Data Analyst at a growing E-commerce company. The UX team notices that returning customers are frustrated with the 3-step checkout process for items they buy every month. They suspect we are losing revenue due to "friction."
**The Hypothesis:** If we implement a "One-Click Reorder" button, we will reduce checkout time and increase the conversion rate.

### 2. The Implementation (The "How")
I built this project in three distinct phases:

*   **Phase A: Data Simulation (Python)**
    *   Since I didn't have real production data, I wrote a Python script (`generate_ab_test_data.py`) using `numpy` and `pandas`.
    *   I simulated 10,000 users, splitting them into Control (Standard Flow) and Treatment (One-Click Flow).
    *   I baked in "real-world" noise: Treatment users had lower checkout times (~30s vs ~90s) and higher conversion probabilities.

*   **Phase B: Statistical Analysis (Python)**
    *   I used `scipy.stats` and `statsmodels` to run a **Z-Test for Proportions** (Conversion Rate) and a **T-Test for Means** (Time Spent).
    *   I calculated the **P-Value** to ensure the results weren't just due to random luck (Statistical Significance).

*   **Phase C: Visualization & DAX (Power BI)**
    *   I imported the data into Power BI and created custom **DAX Measures** to show stakeholders the results.
    *   I built a dashboard that highlights the "Speed shift" in the scatter plot and the KPI uplifts clearly.

### 3. The Business Impact (The "So What")
The analysis showed a clear winner. We projected an annual revenue uplift of **$191.68K** by rolling out this feature to all users.

---

## 🎤 Interview Q&A (Storytelling Format)

### Q1: "Can you walk me through a project where you used data to solve a business problem?"
**A (STAR Method):**
*   **Situation:** I noticed that checkout friction was a potential bottleneck for returning customers in an e-commerce setting.
*   **Task:** My goal was to test if a "One-Click Reorder" feature would actually improve conversion and speed up the process.
*   **Action:** I designed an A/B test simulation for 10,000 users. I used Python to generate the data and perform a Z-test for conversion rates. Then, I visualized the results in Power BI using DAX to show the impact to stakeholders.
*   **Result:** The test was statistically significant (p < 0.05). We found a 20% uplift in conversion and a 60-second reduction in checkout time, projecting nearly $200k in annual revenue growth.

### Q2: "Why did you use Python for analysis instead of just doing it in Power BI?"
**A:** "Great question. Power BI is excellent for visualization, but for **statistical rigor**, I prefer Python. Python libraries like `statsmodels` allow me to run precise Z-tests and T-tests and calculate exact P-values more easily. This ensures that the 'Big Numbers' we see on the dashboard are mathematically backed and not just random variance."

### Q3: "What is a P-Value, and why does it matter in this project?"
**A:** "In this project, the P-Value is the probability that the difference we see between the old checkout and 'One-Click' happened by pure chance. Since our P-Value was extremely small (less than 0.05), it gave me the confidence to tell the business: 'This isn't a fluke; the new feature really works.'"

### Q4: "What were your most important DAX measures?"
**A:** "I focused on four KPIs. The most critical was the **Conversion Rate**. I used the `DIVIDE` and `CALCULATE` functions to ensure that even if we filtered the data by group or date, the percentage would remain accurate. This matched the conversion count against the total user base for each group."

### Q5: "How did you handle the data quality/structure?"
**A:** "While generating the data, I ensured there were no 'impossible' values, like negative checkout times or negative order values. I also included a `.gitignore` and `requirements.txt` in the repository to follow professional dev-ops standards, making the project reproducible for other team members."

---

## 💡 Pro-Tip for your Interview
When showing this on your screen, **start with the Power BI Dashboard**. Captivate them with the visuals first, then "peel back the curtain" by showing your Python code and README to prove your technical depth!
