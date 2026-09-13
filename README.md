# Job Tracker

A little Python tool I built to pull remote job listings from the Remotive API and filter out the ones that actually match what I'm looking for — developer and engineer roles.

## Why I built this
I'm a CS student on the hunt for a coop, and I got tired of manually scrolling through job boards looking for relevant postings. So I figured I'd write something that does the filtering for me and saves the results I actually care about.

## How it works
1. Pulls job listings from Remotive's public API
2. Filters out anything that isn't a developer or engineer role
3. Saves the matching jobs to a CSV file, ready to open in a spreadsheet

## Built with
- Python
- `requests` — for calling the API
- `csv` — for saving the results

## Running it yourself
1. Clone this repo
2. Install the one dependency: `pip install requests`
3. Run it: `python main.py`
4. Open `jobs.csv` to see the results

## About me
Melika Talebhagh — [https://www.linkedin.com/in/melikath05]