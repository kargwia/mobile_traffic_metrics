# Mobile Traffic Metrics
Mobile traffic metrics analysis with FastAPI, NumPy, Pandas and Matplotlib.

#Project structure

```
mobile_traffic_project/
├── traffic_record.py   # TrafficRecord dataclass + validation
├── traffic_stats.py    # Functions + TrafficStats class
├── data_generator.py   # Data generator + JSON read/write
├── analysis.py         # NumPy/Pandas, groupby, CSV export
├── visualizer.py       # Matplotlib traffic chart
├── api.py              # FastAPI — JSON + PNG + CSV responses
├── main.py             # Run all modules
└── requirements.txt
```

#Setup
```bash
pip install -r requirements.txt.txt
```

#Run
```bash
python main.py
```

#API
```bash
uvicorn api:app --reload
```
Open: http://127.0.0.1:8000/docs

#Endpoints
- `GET /stats` — all users statistics (JSON)
- `GET /stats/{user_id}` — one user + limit warning (JSON)
- `GET /numpy` — NumPy global statistics (JSON)
- `GET /plot/{user_id}` — traffic chart (PNG)
- `GET /plot/all/overview` — all users chart (PNG)
- `GET /export/csv` — download statistics (CSV)
- `GET /export/json` — download all records (JSON)
