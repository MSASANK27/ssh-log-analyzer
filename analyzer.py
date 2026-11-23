import re
import csv
import urllib.request
import json
from collections import Counter

failed = Counter()
pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

with open("auth.log") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            failed[match.group(1)] += 1

def get_location(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        with urllib.request.urlopen(url, timeout=3) as response:
            data = json.loads(response.read())
            return f"{data.get('city', 'Unknown')}, {data.get('country', 'Unknown')}"
    except Exception:
        return "Lookup failed"

print("Suspicious IPs (5+ failed logins):\n")

results = []
for ip, count in failed.most_common():
    if count >= 5:
        location = get_location(ip)
        print(f"{ip} - {count} failed attempts - {location}")
        results.append([ip, count, location])

with open("report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP Address", "Failed Attempts", "Location"])
    writer.writerows(results)

print("\nReport saved to report.csv")