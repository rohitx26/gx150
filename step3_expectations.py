import great_expectations as gx

# Get the context and data
context = gx.get_context()
datasource = context.get_datasource("local_files")
data_asset = datasource.get_asset("users_data")

# Create an Expectation Suite (a collection of expectations)
expectation_suite_name = "users_basic_expectations"
suite = context.add_expectation_suite(expectation_suite_name)

# Get a validator to work with
batch_request = data_asset.build_batch_request()
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=expectation_suite_name
)

print("✅ Creating expectations...")

# Expectation 1: Check that required columns exist
validator.expect_table_columns_to_match_ordered_list(
    column_list=["user_id", "name", "age", "email", "score"]
)
print("✓ Columns should match expected list")

# Expectation 2: user_id should be unique
validator.expect_column_values_to_be_unique(column="user_id")
print("✓ user_id should be unique")

# Expectation 3: age should be between 18 and 100
validator.expect_column_values_to_be_between(
    column="age", 
    min_value=18, 
    max_value=100
)
print("✓ age should be between 18-100")

# Expectation 4: email should contain @ symbol
validator.expect_column_values_to_match_regex(
    column="email",
    regex=r".*@.*"
)
print("✓ email should contain @")

# Expectation 5: score should be between 0 and 100
validator.expect_column_values_to_be_between(
    column="score",
    min_value=0,
    max_value=100
)
print("✓ score should be between 0-100")

# Expectation 6: No null values in any column
for column in ["user_id", "name", "age", "email", "score"]:
    validator.expect_column_values_to_not_be_null(column=column)
print("✓ No columns should have null values")

# Save the expectations
validator.save_expectation_suite()
print(f"\n✅ Saved {len(suite.expectations)} expectations!")
print("Next: Run step4_validate.py to test your data against these rules")