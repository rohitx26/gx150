import great_expectations as gx

# Get the context
context = gx.get_context()

# Get your data and expectations
datasource = context.get_datasource("local_files")
data_asset = datasource.get_asset("users_data")
batch_request = data_asset.build_batch_request()

# Run validation
print("🔍 Running validation...")
checkpoint = context.add_checkpoint(
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