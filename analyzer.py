import re
from collections import Counter

failed = Counter()
pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

with open("auth.log") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            failed[match.group(1)] += 1

print("Suspicious IPs (5+ failed logins):")
for ip, count in failed.most_common():
    if count >= 5:
        print(f"{ip} - {count} failed attempts")