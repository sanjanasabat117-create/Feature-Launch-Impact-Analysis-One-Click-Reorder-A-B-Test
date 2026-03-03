import pandas as pd
import numpy as np
import random
import os

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_users = 10000
groups = ['control', 'treatment']

# Generate basic user info
user_ids = range(1, n_users + 1)
assigned_group = np.random.choice(groups, n_users, p=[0.5, 0.5])

# Simulated behavior probabilities based on group
# Treatment has a "One-Click Reorder" button.
# Control goes through standard "Add to Cart" -> "Checkout" -> "Purchase"

data = []

for i in range(n_users):
    group = assigned_group[i]
    
    # 1. Did they enter the reorder flow? (Assume 40% of users try to reorder)
    intent_to_reorder = np.random.choice([0, 1], p=[0.6, 0.4])
    
    if intent_to_reorder == 0:
        # User didn't intend to reorder
        reorder_checkout_initiated = 0
        purchase_completed = 0
        time_spent_secs = np.random.normal(loc=120, scale=30) # Browsing time
        order_value = 0.0
    else:
        # User intended to reorder
        reorder_checkout_initiated = 1
        
        if group == 'control':
            # Control: Standard 3-step checkout. Conversion rate ~45%
            purchase_completed = np.random.choice([0, 1], p=[0.55, 0.45])
            time_spent_secs = np.random.normal(loc=90, scale=20) # Takes longer
        else:
            # Treatment: One-click reorder. Conversion rate ~65%
            purchase_completed = np.random.choice([0, 1], p=[0.35, 0.65])
            time_spent_secs = np.random.normal(loc=30, scale=10) # Much faster
            
        # If purchased, assign an order value
        if purchase_completed == 1:
            order_value = round(np.random.normal(loc=85, scale=25), 2)
            order_value = max(10.0, order_value) # No negative or tiny orders
        else:
            order_value = 0.0

    # Ensure time spent is positive
    time_spent_secs = max(5.0, round(time_spent_secs, 1))

    data.append([
        user_ids[i],
        group,
        reorder_checkout_initiated,
        purchase_completed,
        time_spent_secs,
        order_value
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'user_id', 
    'group', 
    'reorder_checkout_initiated', 
    'purchase_completed', 
    'time_spent_secs', 
    'order_value'
])

# Save to CSV
output_path = os.path.join(os.path.dirname(__file__), 'ab_test_data.csv')
df.to_csv(output_path, index=False)

print(f"[SUCCESS] Generated A/B testing data for {n_users} users.")
print(f"[INFO] Saved to: {output_path}")

# Quick summary
print("\n--- Data Summary ---")
print(df.groupby('group')['purchase_completed'].mean().reset_index().rename(columns={'purchase_completed': 'Conversion Rate'}))
