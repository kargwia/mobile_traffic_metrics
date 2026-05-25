# mobile_traffic_metrics
Mobile traffic metrics analysis with FastAPI, NumPy, Pandas and Matplotlib
# Mobile Traffic Metrics 

> Mobile traffic metrics analysis with FastAPI, NumPy, Pandas and Matplotlib

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.110-teal) ![NumPy](https://img.shields.io/badge/NumPy-1.26-orange) ![Pandas](https://img.shields.io/badge/Pandas-2.2-green)

## Жоба құрылымы

```
mobile_traffic_project/
├── traffic_record.py   # 1–3:  TrafficRecord dataclass + валидация
├── traffic_stats.py    # 4–6:  Функциялар + TrafficStats класы
├── data_generator.py   # 7–8:  Генератор + JSON оқу/жазу
├── analysis.py         # 9–12: NumPy/Pandas, groupby, CSV
├── visualizer.py       # 13:   Matplotlib трафик графигі
├── api.py              # 14:   FastAPI — JSON + PNG + CSV
├── main.py             # Барлық пункттерді іске қосу
└── requirements.txt
```

## Іске қосу

```bash
# 1. Тәуелділіктер
pip install -r requirements.txt

# 2. Барлық пункттерді тексеру
python main.py

# 3. API іске қосу
uvicorn api:app --reload
# → http://127.0.0.1:8000/docs
```

## API эндпоинттері

| Эндпоинт | Жауап | Сипаттама |
|---|---|---|
| `GET /stats` | JSON | Барлық қолданушылар статистикасы |
| `GET /stats/{user_id}` | JSON | Бір қолданушы + лимит ескертуі |
| `GET /numpy` | JSON | NumPy жаппай статистика |
| `GET /plot/{user_id}` | PNG | Трафик графигі |
| `GET /plot/all/overview` | PNG | Барлық қолданушылар |
| `GET /export/csv` | CSV | Статистиканы жүктеу |
| `GET /export/json` | JSON | Барлық жазбаларды жүктеу |

## Пункттер бойынша

| Пункт | Файл | Не жасалды |
|---|---|---|
| 1–3 | traffic_record.py | TrafficRecord dataclass, валидация |
| 4–6 | traffic_stats.py | Функциялар + TrafficStats класы |
| 7–8 | data_generator.py | Генератор, JSON сақтау/жүктеу |
| 9–11 | analysis.py | np.mean, np.percentile, NumPy |
| 12 | analysis.py | df.groupby("user_id").agg(...) |
| 13 | visualizer.py | Matplotlib сызық + лимит белгісі |
| 14 | api.py | FastAPI: JSON + PNG + CSV жауап |

## ООП талабы

Класстар: `TrafficRecord`, `TrafficStats`, `TrafficAnalyzer` — үш ООП нысаны. Дербес функциялар ООП класстарының 40%-дан аз бөлігін құрайды.
