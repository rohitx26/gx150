import great_expectations as gx
import pandas as pd

# Get the Data Context
context = gx.get_context()

print("🔍 Running validation...")

# Get the data source and batch definition
data_source = context.data_sources.get("local_pandas_filesystem")
data_asset = data_source.get_asset("users_data")
batch_definition = data_asset.get_batch_definition("users_batch")

# Get the expectation suite
suite = context.suites.get("users_basic_expectations")

# Create a Validation Definition (modern GX 1.5+ approach)
validation_definition = context.validation_definitions.add(
    gx.ValidationDefinition(
        name="users_validation",
        data=batch_definition,
        suite=suite
    )
)

# Create and run a Checkpoint
checkpoint = context.checkpoints.add(
    gx.Checkpoint(
        name="users_checkpoint",
        validation_definitions=[validation_definition]
    )
)

# Execute the checkpoint
results = checkpoint.run()

print("✅ Validation complete!")
print(f"Success: {results.success}")

# Show detailed results
validation_result = results.run_results[list(results.run_results.keys())[0]]["validation_result"]
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