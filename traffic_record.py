from datetime import date

class TrafficRecord:
    def __init__(self, user_id, mb_used, record_date):
        if user_id <= 0:
            raise ValueError("user_id must be positive")
        if mb_used < 0:
            raise ValueError("mb_used cannot be negative")

        self.user_id = user_id
        self.mb_used = mb_used
        self.record_date = record_date

    def __repr__(self):
        return f"User {self.user_id} | {self.mb_used} MB | {self.record_date}"

if __name__ == "__main__":
    r = TrafficRecord(1, 150.5, date(2024, 1, 15))
    print(r)