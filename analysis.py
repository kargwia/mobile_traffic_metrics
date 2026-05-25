import numpy as np
import pandas as pd


class TrafficAnalyzer:
    def __init__(self, records):
        self.df = pd.DataFrame([
            {"user_id": r.user_id, "mb_used": r.mb_used, "date": r.record_date}
            for r in records
        ])

    def stats(self):
        arr = self.df["mb_used"].values
        return {
            "mean": round(float(np.mean(arr)), 2),
            "max": round(float(np.max(arr)), 2),
            "min": round(float(np.min(arr)), 2)
        }

    def per_user(self):
        return self.df.groupby("user_id")["mb_used"].agg(
            total="sum", mean="mean", peak="max"
        ).round(2).reset_index()

    def export_csv(self, path="stats.csv"):
        self.per_user().to_csv(path, index=False)

if __name__ == "__main__":
    from data_generator import DataGenerator
    gen = DataGenerator([1, 2, 3, 4, 5])
    records = gen.generate()
    analyzer = TrafficAnalyzer(records)
    print(analyzer.stats())
    print(analyzer.per_user())