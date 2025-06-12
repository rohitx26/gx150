import great_expectations as gx
import webbrowser
import os

# Get the context
context = gx.get_context()

print("📊 Building Data Docs (HTML reports)...")

# Build data docs - this creates beautiful HTML reports
context.build_data_docs()

# Get the path to the data docs
docs_sites = context.get_docs_sites_urls()

if docs_sites:
    docs_url = docs_sites[0]['site_url']
    print(f"✅ Data Docs generated!")
    print(f"📍 Location: {docs_url}")
    
    # Try to open in browser
    try:
        webbrowser.open(docs_url)
        print("🌐 Opening in your default browser...")
    except:
        print("💡 Manually open the URL above in your browser")
else:
    print("❌ Could not generate Data Docs")

print("\n🎯 What you can see in the reports:")
print("- Expectation Suite details")
print("- Validation results with charts")
print("- Data profiling and statistics")
print("- Visual indicators for passed/failed expectations")

print("\n🎉 Tutorial Complete!")
print("\nYou've learned:")
print("✓ How to create sample data")
print("✓ How to connect Great Expectations to data")
print("✓ How to define expectations (data quality rules)")
print("✓ How to validate data")
print("✓ How to generate beautiful reports")

print("\n🚀 Next Steps:")
print("- Try modifying the data to see failed expectations")
print("- Add more complex expectations")
print("- Connect to real databases or APIs")
print("- Set up automated validation pipelines")