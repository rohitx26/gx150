import great_expectations as gx
import pandas as pd

print(f"Great Expectations version: {gx.__version__}")

# Initialize Great Expectations Data Context
context = gx.get_context()

# Read the CSV data
df = pd.read_csv('./data/users.csv')

print("✅ Setting up data connection...")

# Create a Pandas filesystem Data Source (GX 1.5+ fluent API)
data_source = context.data_sources.add_pandas_filesystem(
    name="local_pandas_filesystem",
    base_directory="./data"
)

# Add a Data Asset for the CSV file
data_asset = data_source.add_csv_asset(
    name="users_data",
    filename="users.csv"
)

# Create a Batch Definition
batch_definition = data_asset.add_batch_definition_whole_table("users_batch")

print("✅ Connected to data!")
print(f"Data Source: {data_source.name}")
print(f"Data Asset: {data_asset.name}")
print(f"Batch Definition: {batch_definition.name}")

print(f"\nData preview:")
print(df.head())
print(f"Shape: {df.shape}")
print("\nNext: Run step3_expectations.py to define data quality rules")