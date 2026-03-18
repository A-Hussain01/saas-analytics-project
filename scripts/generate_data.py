import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

NUM_CUSTOMERS = 1000
START_DATE = datetime(2023, 1, 1).date()
END_DATE = datetime(2023, 12, 31).date()

plans = [
    {"plan_id": 1, "plan_name": "Basic", "monthly_price": 29},
    {"plan_id": 2, "plan_name": "Pro", "monthly_price": 79},
    {"plan_id": 3, "plan_name": "Enterprise", "monthly_price": 199},
]

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):
    signup_date = fake.date_between(start_date=START_DATE, end_date=END_DATE)
    
    customers.append({
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "country": fake.country(),
        "signup_date": signup_date
    })

customers_df = pd.DataFrame(customers)

subscriptions = []

for customer in customers:
    plan = random.choice(plans)
    churn_probability = random.random()
    
    if churn_probability < 0.2:
        churn_date = customer["signup_date"] + timedelta(days=random.randint(30, 180))
    else:
        churn_date = None
    
    subscriptions.append({
        "subscription_id": customer["customer_id"],
        "customer_id": customer["customer_id"],
        "plan_id": plan["plan_id"],
        "start_date": customer["signup_date"],
        "end_date": churn_date
    })

subscriptions_df = pd.DataFrame(subscriptions)

payments = []

for sub in subscriptions:
    start = sub["start_date"]
    end = sub["end_date"] if sub["end_date"] else END_DATE
    
    current_date = pd.to_datetime(start).date()
    end = pd.to_datetime(end).date()

    while current_date <= end:
        plan_price = next(p["monthly_price"] for p in plans if p["plan_id"] == sub["plan_id"])
        
        payments.append({
            "payment_id": len(payments) + 1,
            "customer_id": sub["customer_id"],
            "plan_id": sub["plan_id"],
            "payment_date": current_date,
            "amount": plan_price
        })
        
        current_date += timedelta(days=30)

payments_df = pd.DataFrame(payments)

usage = []

for sub in subscriptions:
    if sub["end_date"]:
        active_end = pd.to_datetime(sub["end_date"]).date()
    else:
        active_end = END_DATE
    
    usage_days = random.randint(10, 200)
    
    for _ in range(usage_days):
        usage.append({
            "customer_id": sub["customer_id"],
            "usage_date": fake.date_between(start_date=sub["start_date"], end_date=active_end),
            "actions_performed": random.randint(1, 50)
        })

usage_df = pd.DataFrame(usage)

customers_df.to_csv("data/customers.csv", index=False)
subscriptions_df.to_csv("data/subscriptions.csv", index=False)
payments_df.to_csv("data/payments.csv", index=False)
usage_df.to_csv("data/usage.csv", index=False)

print("Data generation complete.")