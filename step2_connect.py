import great_expectations as gx
import pandas as pd

print(f"Great Expectations version: {gx.__version__}")

# Initialize Great Expectations Data Context
context = gx.get_context()

# Read the CSV data
df = pd.read_csv('./data/users.csv')

print("✅ Setting up data connection...")

# Create a Pandas filesystem Data Source (GX 1.5+ fluent API)
source_folder = "./data"
data_source_name = "data"
data_source = context.data_sources.add_pandas_filesystem(
    name=data_source_name, base_directory=source_folder
)

# Add a Data Asset for the CSV file
data_asset_name = "users"
file_csv_asset = data_source.add_csv_asset(name=data_asset_name)
# Create a Batch Definition
batch_definition_name = "users.csv"
batch_definition_path = "users.csv"  # Path relative to base_directory

batch_definition = file_csv_asset.add_batch_definition_path(
    name=batch_definition_name, path=batch_definition_path
)

batch = batch_definition.get_batch()

print("✅ Connected to data!")
print(f"Data Source: {data_source_name}")
print(f"Data Asset: {data_asset_name}")
print(f"Batch Definition: {batch_definition.name}")

print(f"\nData preview:")
print(df.head())
print(f"Shape: {df.shape}")
print("\nNext: Run step3_expectations.py to define data quality rules")