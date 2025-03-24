import pandas as pd
from sqlalchemy import create_engine

class DataHandler:
    def __init__(self, db_name="data_analysis.db"):
        self.engine = create_engine(f'sqlite:///{db_name}')
    
    def calculate_statistics(self, table_name):
        data = pd.read_sql(f"SELECT * FROM {table_name}", self.engine)
        return data.describe()