# Install required packages
!pip install fpl pandas numpy matplotlib seaborn scikit-learn xgboost pulp requests aiohttp nest_asyncio

# Import libraries
import nest_asyncio
nest_asyncio.apply()
import aiohttp
from fpl import FPL
import pandas as pd
import numpy as np
import asyncio
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import pulp