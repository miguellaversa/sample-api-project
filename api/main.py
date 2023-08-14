from fastapi import FastAPI
import uvicorn

from routes import routes, auth


# --------------------------------------------------


app = FastAPI(
            title = "PRGX API", 
            description = "", 
            version = "1.0"
        )

app.include_router(routes.router)
app.include_router(auth.router)


# --------------------------------------------------


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)