import os
print("Starting Retail Analytics Pipeline")
os.system("python preprocessing.py")
os.system("python retail_analysis.py")
print("Retail Analytics Pipeline Executed Successfully")