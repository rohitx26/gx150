import great_expectations as gx
import pandas as pd

# Initialize Great Expectations context
context = gx.get_context()

# Read the CSV data directly with pandas
df = pd.read_csv('./data/users.csv')

# For Great Expectations 1.0+, we need to add a datasource differently
try:
    # Try the modern API first
    datasource = context.add_or_update_datasource(
        name="local_files",
        class_name="Datasource",
        execution_engine={
            "class_name": "PandasExecutionEngine"
        },
        data_connectors={
            "default_inferred_data_connector_name": {
                "class_name": "InferredAssetDataConnector",
                "base_directory": "./data",
                "default_regex": {
                    "group_names": ["data_asset_name"],
                    "pattern": "(.*)\\.csv"
                }
            }
        }
    )
    
    # Get the data asset
    batch_request = {
        "datasource_name": "local_files",
        "data_connector_name": "default_inferred_data_connector_name",
        "data_asset_name": "users"
    }
    
    print("✅ Connected to data!")
    print(f"Datasource: {datasource.name}")
    
except Exception as e:
    print(f"Error with datasource creation: {e}")
    print("Using direct DataFrame approach...")
    
    # Fallback: work directly with the DataFrame
    batch_request = None

print(f"\nData preview:")
print(df.head())
print(f"Shape: {df.shape}")
print("\nNext: Run step3_expectations.py to define data quality rules")