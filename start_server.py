import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=8800,
        reload=True,
        log_level=10,
    )
