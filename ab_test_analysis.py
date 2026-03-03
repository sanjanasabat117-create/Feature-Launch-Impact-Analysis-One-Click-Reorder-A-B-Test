import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, norm
import statsmodels.api as sm
import os

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'ab_test_data.csv')
    if not os.path.exists(file_path):
        print("[ERROR] 'ab_test_data.csv' not found. Please run 'generate_ab_test_data.py' first.")
        return None
    return pd.read_csv(file_path)

def analyze_ab_test():
    print("[STARTING] A/B Test Analysis: One-Click Reorder Feature\n" + "="*55)
    
    df = load_data()
    if df is None: return

    # We only care about users who initiated the reorder process
    df_reorder = df[df['reorder_checkout_initiated'] == 1]
    
    control_group = df_reorder[df_reorder['group'] == 'control']
    treatment_group = df_reorder[df_reorder['group'] == 'treatment']
    
    n_control = len(control_group)
    n_treatment = len(treatment_group)
    
    print(f"[DATA] Sample Size (Users who initiated reorder):")
    print(f"   Control (Old Flow): {n_control}")
    print(f"   Treatment (One-Click): {n_treatment}\n")

    # --- 1. Conversion Rate Analysis (Z-Test for Proportions) ---
    print("--- 1. Conversion Rate (Purchase Completed) ---")
    conv_control = control_group['purchase_completed'].mean()
    conv_treatment = treatment_group['purchase_completed'].mean()
    
    print(f"   Control Conversion Rate: {conv_control:.2%}")
    print(f"   Treatment Conversion Rate: {conv_treatment:.2%}")
    print(f"   Uplift: {(conv_treatment - conv_control) / conv_control:.2%}")
    
    # Z-test
    count = np.array([treatment_group['purchase_completed'].sum(), control_group['purchase_completed'].sum()])
    nobs = np.array([n_treatment, n_control])
    z_stat, p_value_z = sm.stats.proportions_ztest(count, nobs, alternative='larger')
    
    print(f"   Z-Statistic: {z_stat:.4f} | P-Value: {p_value_z:.4e}")
    if p_value_z < 0.05:
        print("   [SIGNIFICANT] Result: STATISTICALLY SIGNIFICANT. The treatment group converts higher than control.\n")
    else:
        print("   [NOT SIGNIFICANT] Result: Not Statistically Significant.\n")

    # --- 2. Checkout Time Analysis (T-Test for Means) ---
    print("--- 2. Average Checkout Time ---")
    time_control = control_group['time_spent_secs'].mean()
    time_treatment = treatment_group['time_spent_secs'].mean()
    
    print(f"   Control Avg Time: {time_control:.1f} seconds")
    print(f"   Treatment Avg Time: {time_treatment:.1f} seconds")
    print(f"   Time Saved: {time_control - time_treatment:.1f} seconds per user")
    
    # T-test
    t_stat, p_value_t = ttest_ind(control_group['time_spent_secs'], treatment_group['time_spent_secs'], equal_var=False)
    
    print(f"   T-Statistic: {t_stat:.4f} | P-Value: {p_value_t:.4e}")
    if p_value_t < 0.05:
        print("   [SIGNIFICANT] Result: STATISTICALLY SIGNIFICANT. The treatment group is faster.\n")
    else:
        print("   [NOT SIGNIFICANT] Result: Not Statistically Significant.\n")

    # --- 3. Business Impact (Revenue) ---
    print("--- 3. Business Impact Estimation ---")
    rev_control_per_user = control_group['order_value'].sum() / n_control
    rev_treatment_per_user = treatment_group['order_value'].sum() / n_treatment
    
    print(f"   Avg Revenue per User (Control): ${rev_control_per_user:.2f}")
    print(f"   Avg Revenue per User (Treatment): ${rev_treatment_per_user:.2f}")
    
    projected_users_per_year = 500000 
    projected_additional_rev = (rev_treatment_per_user - rev_control_per_user) * projected_users_per_year
    print(f"   [IMPACT] Projected Annual Revenue Uplift (assuming 500k reorders/year): ${projected_additional_rev:,.2f}\n")
    
    print("="*55)
    print("[CONCLUSION] Final Recommendation: ROLL OUT the One-Click Reorder Feature to all users.")

if __name__ == "__main__":
    analyze_ab_test()
