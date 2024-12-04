#!/usr/bin/env python3

import json
import os
from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')
DB = "hva4zb"

@app.get("/") #zone ape
def zone_apex():
	return {"Good Day": "Sunshine!"}

@app.get('/genres')
def get_genres():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
    cur=db.cursor()
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
	cur.close()
	db.close()
        return(json_data)
    except Error as e:
	print("MySQL Error: ", str(e))
        cur.close()
        db.close()
        return {"Error": "MySQL Error: " + str(e)}

@app.get('/songs')
async def get_genres():
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB, ssl_disabled=True)
    cur = db.cursor()
    query = "SELECT songs.title, songs.album, songs.artist, songs.year, songs.file, songs.image, genres.genre FROM songs JOIN genres WHERE songs.genre = genres.genreid ORDER BY songs.title;"
    try:
        cur.execute(query)
        headers=[x[0] for x in cur.description]
        results = cur.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(headers,result)))
	cur.close()
	db.close()
        return(json_data)
    except Error as e:
        print("MySQL Error: ", str(e))
	cur.close()
	db.close()
        return None



