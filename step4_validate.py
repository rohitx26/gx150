import great_expectations as gx
import pandas as pd

# Get the context and read the data
context = gx.get_context()
df = pd.read_csv('./data/users.csv')

# Create a batch request for validation
batch_request = gx.core.batch.RuntimeBatchRequest(
    datasource_name="pandas",
    data_connector_name="default_runtime_data_connector_name", 
    data_asset_name="users_data",
    runtime_parameters={"batch_data": df},
    batch_identifiers={"default_identifier_name": "default_identifier"}
)

# Run validation
print("🔍 Running validation...")
checkpoint = context.add_or_update_checkpoint(
    name="users_checkpoint",
    batch_request=batch_request,
    expectation_suite_name="users_basic_expectations"
)

# Execute the checkpoint
results = checkpoint.run()

print("✅ Validation complete!")
print(f"Success: {results.success}")

# Show detailed results
validation_result = results.list_validation_results()[0]
print(f"\nValidation Results:")
print(f"- Total expectations: {validation_result.statistics['evaluated_expectations']}")
print(f"- Successful: {validation_result.statistics['successful_expectations']}")
print(f"- Failed: {validation_result.statistics['unsuccessful_expectations']}")
print(f"- Success percentage: {validation_result.statistics['success_percent']:.1f}%")

# Show any failed expectations
if not results.success:
    print("\n❌ Failed expectations:")
    for result in validation_result.results:
        if not result.success:
            print(f"- {result.expectation_config.expectation_type}")
else:
    print("\n🎉 All expectations passed!")

print(f"\nNext: Run step5_reports.py to generate an HTML report")