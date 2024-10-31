#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hi": "Lab6"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@api.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}

@api.get("/square/{c}")
def squaring(c: int):
    return {"product": c * c}

@api.get("/working")  # zone apex
def zone_apex2():
    return {"Is this working?": "yes"}

@api.get("/customer/{idx}")
def customer(idx: int):
    #read the data into a df
    df = pd.read_csv("../customers.csv")
    #filter the data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@api.post("/get_body")
def get_body(request: Request):
    return request.json()

