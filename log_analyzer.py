#log_analyzer.py
with open("log.txt") as f:
    lines = f.readlines()

errors = [line for line in lines if "ERROR" in line]

print("Total Errors:", len(errors))
