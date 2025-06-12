import pandas as pd
import os

# Create a data directory
os.makedirs('data', exist_ok=True)

# Create sample user data
users_data = {
    'user_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'age': [25, 30, 35, 28, 22, 45],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 
              'diana@email.com', 'eve@email.com', 'frank@email.com'],
    'score': [85.5, 92.0, 78.5, 88.0, 95.5, 82.0]
}

df = pd.DataFrame(users_data)
df.to_csv('data/users.csv', index=False)

print("✅ Sample data created!")
print(f"Created file: data/users.csv")
print("\nData preview:")
print(df)
print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")