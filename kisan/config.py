import os
from os import getenv

class Config:
    BOT_TOKEN = getenv("BOT_TOKEN", None)
    
