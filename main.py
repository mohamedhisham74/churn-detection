from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import APIKeyHeader

from src.config import APP_NAME,VERSION,SECRET_KEY_TOKEN,preproccessor,model
from src.inferennce import predict_new
from src.request import CustomerData 