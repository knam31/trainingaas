import pandas as pd
df = pd.read_parquet('./files/sample.parquet') 
df.to_csv('./files/sample.csv')