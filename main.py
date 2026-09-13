import requests
import csv

# Remotive's API
url = "https://remotive.com/api/remote-jobs?search=software"
response = requests.get(url)

# Convert the response into Python data
data = response.json()
jobs = data["jobs"]

# Filter developer/engineer roles and save them to a CSV file
with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "URL"])  # header row

    for job in jobs:
        title = job["title"].lower()
        if "developer" in title or "engineer" in title:
            writer.writerow([job["title"], job["company_name"], job["url"]])

print("Saved to jobs.csv")