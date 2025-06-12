import great_expectations as gx

# Initialize Great Expectations context
context = gx.get_context()

# Connect to your CSV data
datasource = context.sources.add_pandas_filesystem(
    name="local_files",
    base_directory="./data"
)

# Define the data asset (your CSV file)
data_asset = datasource.add_csv_asset(
    name="users_data",
    filepath_or_buffer="users.csv"
)

print("✅ Connected to data!")
print(f"Datasource: {datasource.name}")
print(f"Data asset: {data_asset.name}")

# Get a batch of data to work with
batch_request = data_asset.build_batch_request()
batch = data_asset.get_batch(batch_request)

print(f"\nData preview:")
print(batch.data.head())
print(f"Shape: {batch.data.shape}")