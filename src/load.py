import pandas as pd
import pyodbc
import configparser
from sqlalchemy import create_engine
import urllib

def load_to_sql(df_flat, df_milestones, df_members,df_flat2):
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    c = config['SQL_SERVER']


    params = urllib.parse.quote_plus(
        f"DRIVER={{{c['driver']}}};"
        f"SERVER={c['DB_SERVER']};"
        f"DATABASE={c['DB_NAME']};"
        f"UID={c['DB_USER']};"
        f"PWD={c['DB_PASSWORD']}"
    )

# Create engine
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    df_flat.to_sql("projects", con=engine, if_exists="replace", index=False)
    df_milestones.to_sql("project_milestones", con=engine, if_exists="replace", index=False)
    df_members.to_sql("project_members", con=engine, if_exists="replace", index=False)
    df_flat2.to_sql("projects2", con=engine, if_exists="replace", index=False)