import logging
import random

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import pandas as pd
from pydantic import BaseModel, Field, validator

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
import json

import base64
import requests
import datetime
from urllib.parse import urlencode
import os
from dotenv import load_dotenv
from joblib import load


load_dotenv()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""
    post_title: str = Field(..., example='This is a title of my post')
    post_body: str = Field(..., example='This is the body of the post!')    
    

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        dataframe = pd.DataFrame([dict(self)])
        return dataframe



@router.post('/predict')
async def predict(item: Item):    
    """Use a KNN model to made song predictions"""
    preds = {"rec1": "subreddit1", 
             "rec2": "subreddit2",
            "rec3": "subreddit3",
            "rec4": "subreddit4",
            "rec5": "subreddit5}
    return JSONResponse(content=preds)
