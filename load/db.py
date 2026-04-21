import psycopg2
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.db_config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)