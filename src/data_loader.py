#!/usr/bin/env python
# coding: utf-8

#import and load
import duckdb
import pandas as pd

def load_data(db_path: str) -> pd.DataFrame:
    conn = duckdb.connect(database=db_path, read_only=True)
    df = conn.execute("SELECT * FROM superheroes").fetchdf()
    conn.close()
    return df

