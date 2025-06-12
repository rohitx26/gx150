import great_expectations as gx

# Get the Data Context
context = gx.get_context()

print("✅ Creating expectations...")

# Create an Expectation Suite using the modern API
suite = context.suites.add(gx.ExpectationSuite(name="users_basic_expectations"))

# Get the data source and batch definition that we created in step2
data_source = context.data_sources.get("local_pandas_filesystem")
data_asset = data_source.get_asset("users_data")
batch_definition = data_asset.get_batch_definition("users_batch")

print("✓ Setting up expectations on the data...")

# Add expectations to the suite using the modern expectation classes
suite.add_expectation(gx.expectations.ExpectTableColumnsToMatchOrderedList(
    column_list=["user_id", "name", "age", "email", "score"]
))
print("✓ Columns should match expected list")

suite.add_expectation(gx.expectations.ExpectColumnValuesToBeUnique(
    column="user_id"
))
print("✓ user_id should be unique")

suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(
    column="age", 
    min_value=18, 
    max_value=100
))
print("✓ age should be between 18-100")

suite.add_expectation(gx.expectations.ExpectColumnValuesToMatchRegex(
    column="email",
    regex=r".*@.*"
))
print("✓ email should contain @")

suite.add_expectation(gx.expectations.ExpectColumnValuesToBeBetween(
    column="score",
    min_value=0,
    max_value=100
))
print("✓ score should be between 0-100")

# Add non-null expectations for all columns
for column in ["user_id", "name", "age", "email", "score"]:
    suite.add_expectation(gx.expectations.ExpectColumnValuesToNotBeNull(
        column=column
    ))
print("✓ No columns should have null values")

print(f"\n✅ Saved {len(suite.expectations)} expectations!")
print("Next: Run step4_validate.py to test your data against these rules")