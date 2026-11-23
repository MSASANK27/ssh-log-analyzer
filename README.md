# SSH Log Analyzer

A Python tool that parses SSH authentication logs and detects possible brute-force attacks by flagging IPs with 5 or more failed login attempts.

## Usage
python analyzer.py

## Sample Output
![Output](output.png)

## How it works
- Reads auth.log line by line
- Uses a regex to extract source IPs from "Failed password" entries
- Counts attempts per IP and reports those above the threshold

## Note
Includes a sample log for demonstration.