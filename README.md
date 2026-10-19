# Air Quality Data Pipeline

A Python-based data pipeline that collects hourly air quality data for Mumbai, cleans it using pandas, stores it in PostgreSQL, and analyzes pollution trends using SQL.

## Overview

This project demonstrates an end-to-end data engineering workflow, from fetching data through an API to storing and querying it in a relational database.

### What It Does

- **Fetches data:** Retrieves hourly PM2.5 and PM10 readings from the Open-Meteo Air Quality API.
- **Cleans data:** Uses pandas to convert timestamps, remove rows without any pollutant readings, and filter out negative concentration values.
- **Stores data:** Loads cleaned readings into PostgreSQL.
- **Prevents duplicates:** Uses a primary key and conflict handling to avoid inserting duplicate timestamps.
- **Analyzes data:** Uses SQL queries to explore daily pollution averages, peak PM2.5 readings, and hourly pollution patterns.

## Tech Stack

- **Language:** Python
- **Data Processing:** pandas
- **API Requests:** requests
- **Database:** PostgreSQL
- **Database Connectivity:** psycopg2
- **Environment Variables:** python-dotenv
- **Visualization:** Matplotlib (optional)

## Data Source

This project uses the [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api) to retrieve hourly air quality data.

The pipeline is configured for Mumbai, India, using the following coordinates:

- Latitude: 19.07
- Longitude: 72.88

The requested pollutants are PM2.5 and PM10, covering historical readings and forecast data as configured in the API request.

## Project Structure

```text
air-quality-pipeline/
├── main.py
├── db.py
├── run_queries.py
├── queries.sql
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

Optional files, such as `explore.py` and `plot.py`, can be included if they are part of your implementation.

## Getting Started

### Prerequisites

- Python 3.10 or later
- PostgreSQL
- Git

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd air-quality-pipeline
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows PowerShell**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the Database

Open PostgreSQL or pgAdmin and execute:

```sql
CREATE DATABASE air_quality;
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
DB_NAME=air_quality
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
```

Replace the placeholder password with your local PostgreSQL password.

**Important:** Never commit your `.env` file or expose database credentials publicly.

### 6. Run the Pipeline

Fetch, clean, and store the data:

```bash
python main.py
```

Execute the analytical SQL queries:

```bash
python run_queries.py
```

Ensure that PostgreSQL is running and the database credentials are correct before running the pipeline.

## SQL Analysis

The project includes queries to analyze:

1. Daily average PM2.5 concentrations.
2. The five hours with the highest PM2.5 readings.
3. Days when average PM2.5 exceeds 60 µg/m³.
4. Average PM2.5 levels by hour of the day.

These queries help explore pollution trends and identify periods with higher particulate matter concentrations.

## Design Decisions

- **Primary key:** The timestamp uniquely identifies each hourly reading and prevents duplicate records.
- **Data cleaning:** Rows with no PM2.5 or PM10 readings are removed, and negative concentration values are filtered out.
- **Conflict handling:** Existing timestamps are skipped during insertion, making repeated pipeline runs safe against duplicate records.
- **Environment variables:** Database credentials are stored separately from the application code.

## Future Improvements

- Extend the pipeline to support multiple cities.
- Schedule automated daily data collection.
- Add logging and monitoring.
- Build interactive dashboards for pollution trends.
- Deploy the pipeline to a cloud environment.
- Add automated tests and data-quality checks.

## Learning Outcomes

This project demonstrates practical skills in API integration, Python data processing, relational database management, SQL analytics, and Git-based version control.

---

*Built as a hands-on data engineering project.*
