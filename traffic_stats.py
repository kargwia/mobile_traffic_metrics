from traffic_record import TrafficRecord

def total_mb(records):
    return sum(r.mb_used for r in records)

def average_mb(records):
    return total_mb(records) / len(records)

class TrafficStats:
    def __init__(self, records):
        self.records = records

    def total(self):
        return total_mb(self.records)

    def average(self):
        return average_mb(self.records)

    def peak(self):
        return max(self.records, key=lambda r: r.mb_used)

    def summary(self):
        return {
            "total": self.total(),
            "average": round(self.average(), 2),
            "peak": self.peak().mb_used
        }

if __name__ == "__main__":
    from datetime import date
    records = [
        TrafficRecord(1, 200.0, date(2024, 1, 1)),
        TrafficRecord(2, 350.0, date(2024, 1, 2)),
        TrafficRecord(3, 50.0, date(2024, 1, 3)),
    ]
    stats = TrafficStats(records)
    print(stats.summary())