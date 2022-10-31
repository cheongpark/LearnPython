@echo off

start http://localhost:8000/docs
start http://localhost:8000/redoc

uvicorn 1:app --reload