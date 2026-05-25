import matplotlib.pyplot as plt

class TrafficVisualizer:
    def __init__(self, df, limit=300):
        self.df = df
        self.limit = limit

    def plot(self, user_id, path="plot.png"):
        user_df = self.df[self.df["user_id"] == user_id].sort_values("date")
        plt.figure(figsize=(10, 4))
        plt.plot(user_df["date"], user_df["mb_used"], marker="o", label=f"User {user_id}")
        plt.axhline(self.limit, color="red", linestyle="--", label=f"Limit {self.limit} MB")
        plt.title(f"User {user_id} Traffic")
        plt.legend()
        plt.tight_layout()
        plt.savefig(path)
        plt.close()
        return path

if __name__ == "__main__":
    from data_generator import DataGenerator
    from analysis import TrafficAnalyzer
    gen = DataGenerator([1, 2, 3, 4, 5])
    records = gen.generate()
    analyzer = TrafficAnalyzer(records)
    viz = TrafficVisualizer(analyzer.df)
    viz.plot(1)
    print("Plot saved!")