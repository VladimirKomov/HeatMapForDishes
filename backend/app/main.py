from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Settings CORS
app.add_middleware(
    CORSMiddleware,
    # only local, [*] for all
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    # for methods
    allow_methods=["*"],
    # for headers
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
