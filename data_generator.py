import random
import json
from datetime import date, timedelta
from traffic_record import TrafficRecord

class DataGenerator:
    def __init__(self, user_ids, days=30):
        self.user_ids = user_ids
        self.days = days
        self.start = date(2024, 1, 1)

    def generate(self):
        records = []
        for uid in self.user_ids:
            for i in range(self.days):
                r = TrafficRecord(uid, round(random.uniform(10, 500), 2), self.start + timedelta(days=i))
                records.append(r)
        return records

    def save_json(self, records, path="traffic.json"):
        data = [{"user_id": r.user_id, "mb_used": r.mb_used, "date": str(r.record_date)} for r in records]
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def load_json(self, path="traffic.json"):
        with open(path) as f:
            data = json.load(f)
        return [TrafficRecord(d["user_id"], d["mb_used"], date.fromisoformat(d["date"])) for d in data]

if __name__ == "__main__":
    from traffic_stats import TrafficStats
    gen = DataGenerator([1, 2, 3, 4, 5])
    records = gen.generate()
    gen.save_json(records)
    print(f"Generated {len(records)} records")