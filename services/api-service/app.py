from fastapi import FastAPI
import logging
import time

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
def root():
    logging.info("Root endpoint hit")
    return {"status": "ATLAS API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/work")
def work():
    start = time.time()
    time.sleep(0.2)
    duration = time.time() - start
    logging.info(f"Work completed in {duration} seconds")
    return {"work_time": duration}
