from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head><meta charset="utf-8"><title>MAESTRO Verify Test</title></head>
      <body>
        <h1>MAESTRO browser verification test</h1>
        <p>If you can see this rendered, the verify phase works.</p>
        <p>MAESTRO orchestrates and verifies system workflows to ensure reliability and correctness through automated testing and validation.</p>
      </body>
    </html>
    """
