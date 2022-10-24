@echo off

start http://localhost:8000/docs
start http://localhost:8000/redoc
start http://localhost:8000/hello

uvicorn 1:app --reload