# Great Expectations Tutorial - Learn by Doing

## What is Great Expectations?

Great Expectations (GX) helps you validate, document, and profile your data to maintain quality and catch issues early.

## Setup

1. **Activate your virtual environment:**

```bash
source .venv/bin/activate
```

2. **Install Great Expectations:**

```bash
pip install great-expectations pandas
```

3. **Initialize Great Expectations:**

```bash
great_expectations init
```

## Tutorial Steps

### Step 1: Create Sample Data

We'll start with a simple CSV file containing user data.

### Step 2: Connect to Data

Configure GX to read your data source.

### Step 3: Create Expectations

Define rules about what your data should look like.

### Step 4: Validate Data

Run validations to check if your data meets expectations.

### Step 5: Generate Reports

Create HTML reports showing validation results.

## What You'll Learn

- How to set up Great Expectations
- Creating and managing data expectations
- Running validations
- Interpreting results
- Best practices for data quality

Let's get started! Follow the files in order: `step1_data.py`, `step2_connect.py`, etc.
