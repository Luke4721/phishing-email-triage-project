# Phishing & Email Triage and Response Simulation Project

## Project Overview

This project simulates a Security Operations Center (SOC) analyst’s workflow for detecting, analyzing, and responding to phishing email threats. Using a real-world phishing email dataset, the goal is to extract meaningful insights by cleaning and enriching the data, then building dashboards to support threat detection and prioritization.

---

## Data Preparation and Cleaning (Python)

The original phishing email dataset was provided as a CSV file containing fields such as sender, receiver, date, subject, body, phishing label, and URLs. The CSV required preprocessing for accurate ingestion and analysis in Splunk.

### Cleaning Steps:

- **Loaded the CSV using Python's pandas library** to handle structured data efficiently.
- **Dropped rows missing critical fields**: emails with empty sender, body, or label fields were removed to ensure data quality.
- **Normalized text fields** (e.g., stripped whitespace from email body).
- **Extracted URLs from the email body** using regular expressions to identify embedded phishing links.
- **Converted extracted URL lists to tuples** to enable reliable duplication removal (since lists are unhashable).
- **Removed duplicate records based on URLs** to avoid repeated analysis of identical phishing attempts.
- **Saved the cleaned and enriched dataset** as a new CSV file (`cleaned_emails.csv`) ready for Splunk ingestion.

This processing ensured that the dataset was clean, consistent, and contained relevant data points for SOC analysis.

---

## Data Ingestion and Analysis (Splunk)

The cleaned CSV was uploaded into Splunk for interactive analysis and dashboard creation.

### Key Actions in Splunk:

- Imported the cleaned CSV, assigning it the appropriate sourcetype for email phishing data.
- Used the **`rex field=_raw "\^(?<sender>[^,]+),\(?<receiver>[^,]+),\\"(?<date>[^\"]+)\",\\"(?<subject>[^\"]+)\",\\"(?<body>[^\"]+)\",\(?<label>\d+),\\"?\(?'?(?<urls>[^'\)]+)'?\)?\"?"` ** to extract and validate important fields: sender, receiver, date, subject, body, label, and URLs. Later found that my search mode was set on fast rather than verbose which could have extracted all the fields without the need for a regex command
- Built SPL queries to generate visual insights on:
  - Phishing volume trends over time.
  - Top phishing senders by volume.
  - Top targeted receiver email addresses.
  - Frequent phishing URLs and domains.
  - Comparison of phishing vs benign email counts.

### Dashboard Visualization:

- **Top Phishing Senders:** Horizontal bar chart listing senders responsible for most phishing attempts.
- **Top Targeted Receivers:** Horizontal bar chart showing most targeted users by phishing emails.
- **Frequent Phishing URLs:** Treemap or bar chart summarizing the most common URLs found in phishing emails.
- **Phishing vs Benign Counts:** Pie or stacked bar chart comparing proportions of phishing and non-phishing emails.

---

## Project Outcome

This project demonstrates an end-to-end SOC analyst workflow using Python for data preprocessing and Splunk for threat detection and visualization. The dashboards provide actionable intelligence supporting quick identification and mitigation of phishing threats.

---

## How to Use

1. Run the Python cleaning script to load the raw CSV, extract URLs, remove duplicates, and save the clean file.
2. Upload the cleaned CSV file to Splunk and configure field extraction.
3. Use provided SPL queries (in project materials) to explore data and build the recommended dashboards.
4. Analyze phishing trends and generate incident reports based on dashboard insights.

---

## Tools and Technologies

- Python (pandas, regex) for data cleaning and enrichment.
- Splunk for data ingestion, field extraction, search, and dashboard visualization.
- Regular expressions for URL extraction and field parsing.
- CSV files for data storage and interchange.

---

If you need detailed scripts or SPL queries for this project, please refer to the corresponding files in this repository or reach out for assistance.
