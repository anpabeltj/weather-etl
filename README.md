# 🌤️ Weather ETL Pipeline

A simple ETL (Extract, Transform, Load) data pipeline that fetches daily weather forecast data from the [Open-Meteo API](https://open-meteo.com/), transforms it into a structured format, and loads it into a PostgreSQL database, all orchestrated with Apache Airflow and visualized via Metabase.

---

## 🏗️ Architecture

```
Open-Meteo API
      │
  🔍 Extract       → Fetch coordinates + 7-day weather forecast
      │
  🔄 Transform     → Clean & structure data with Pandas
      │
  📦 Load          → Store into PostgreSQL (weather_db)
      │
  📊 Metabase      → Visualize weather data
```

---

## 📁 Project Structure

```
weather-api/
├── dags/
│   └── weather_dag.py      # Airflow DAG orchestrating the ETL pipeline
├── scripts/
│   ├── extract.py          # Fetch weather data from Open-Meteo API
│   ├── transform.py        # Transform raw JSON into a Pandas DataFrame
│   └── load.py             # Load DataFrame into PostgreSQL
├── logs/                   # Airflow logs
├── docker-compose.yml      # Multi-service Docker setup
└── README.md
```

---

## 🔧 Tech Stack

| Tool              | Purpose                  |
| ----------------- | ------------------------ |
| 🐍 Python         | ETL scripting            |
| 🌐 Open-Meteo API | Free weather data source |
| 🐼 Pandas         | Data transformation      |
| 🐘 PostgreSQL     | Data storage             |
| 🌀 Apache Airflow | Pipeline orchestration   |
| 📊 Metabase       | Data visualization       |
| 🐳 Docker Compose | Container management     |

---

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose installed

### Run the Stack

```bash
docker compose up -d
```

This will spin up:

- **Airflow** → [http://localhost:8080](http://localhost:8080) (admin / admin)
- **Metabase** → [http://localhost:3000](http://localhost:3000)
- **PostgreSQL (weather_db)** → `localhost:5434`

---

## 📡 Data Source

Weather data is fetched from the **Open-Meteo API** (free, no API key required):

- **Geocoding**: `https://geocoding-api.open-meteo.com/v1/search`
- **Forecast**: `https://api.open-meteo.com/v1/forecast`

### Fields collected (daily, past 7 days):

| Column          | Description              |
| --------------- | ------------------------ |
| `date`          | Date of record           |
| `temp_max`      | Maximum temperature (°C) |
| `temp_min`      | Minimum temperature (°C) |
| `precipitation` | Total precipitation (mm) |
| `city`          | City name                |

---

## 🗄️ Database

Two PostgreSQL instances are running:

| Instance           | Purpose              | Port                                                  |
| ------------------ | -------------------- | ----------------------------------------------------- |
| `postgres-airflow` | Airflow metadata DB  | internal                                              |
| `postgres-weather` | Weather data storage | `5434` for local development or `5432` for production |

### Weather DB connection:

| Setting  | Value           |
| -------- | --------------- |
| Host     | `localhost`     |
| Port     | `5434`          |
| Database | `weather_db`    |
| User     | `weather_user`  |
| Password | `weather_pass`  |
| Table    | `weather_daily` |

---

## 🌀 Airflow DAG

The `weather_pipeline` DAG runs daily and executes three tasks in sequence:

```
extract_weather_data >> transform_weather_data >> load_weather_data
```

Data is passed between tasks using Airflow XCom.

---

## ▶️ Running Scripts Manually

```bash
cd scripts/

# Extract only
python extract.py

# Transform only
python transform.py

# Full ETL (Extract → Transform → Load)
python load.py
```

---

## 📌 Notes

- Timezone is set to `Asia/Jakarta` (UTC+7)
- Default city is **Jakarta**: update the city name in `weather_dag.py` to fetch data for other cities
- The `weather_daily` table uses `append` mode, so re-running will add new rows
- Airflow runs with `LocalExecutor` and loads examples disabled

---

## 📄 License

This project is open-source and free to use for learning and experimentation. 🎉
