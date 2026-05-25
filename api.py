from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from data_generator import DataGenerator
from analysis import TrafficAnalyzer
from visualizer import TrafficVisualizer
from fastapi.responses import RedirectResponse

app = FastAPI()

generator = DataGenerator(user_ids=[1, 2, 3, 4, 5])
records = generator.generate()
analyzer = TrafficAnalyzer(records)
visualizer = TrafficVisualizer(analyzer.df)

@app.get("/")
def home():
    return RedirectResponse("/docs")

@app.get("/stats")
def get_stats():
    return JSONResponse(analyzer.per_user().to_dict(orient="records"))


@app.get("/stats/{user_id}")
def get_user(user_id: int):
    user_df = analyzer.df[analyzer.df["user_id"] == user_id]
    if user_df.empty:
        raise HTTPException(404, detail="User not found")
    return {
        "user_id": user_id,
        "total_mb": round(float(user_df["mb_used"].sum()), 2),
        "mean_mb": round(float(user_df["mb_used"].mean()), 2)
    }


@app.get("/plot/{user_id}")
def get_plot(user_id: int):
    path = visualizer.plot(user_id, path=f"plot_{user_id}.png")
    return FileResponse(path, media_type="image/png")


@app.get("/export/csv")
def export_csv():
    analyzer.export_csv("stats.csv")
    return FileResponse("stats.csv", media_type="text/csv")

if __name__ == "__main__":
    import uvicorn
    print("Сервер: http://127.0.0.1:8000/docs")
    uvicorn.run("api:app", reload=True)