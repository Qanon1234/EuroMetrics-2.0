import pandas as pd
from database import connect_database

countries = pd.read_csv("data/processed/countries.csv")
pps = pd.read_csv("data/processed/gdp_pps_2000_2025.csv")

db = connect_database()
cursor = db.cursor()

# Importera länderna till geography
for index, row in countries.iterrows():
    country_code = row["country_code"]
    country_name = row["country_name"]
    region = row["region"]

    cursor.execute("""
        INSERT INTO geography
        (country_code, country_name, region, entity_type)
        VALUES (%s, %s, %s, %s)
    """, (country_code, country_name, region, "country"))

# Registrera ekonomisk indikator
cursor.execute("""
    INSERT INTO indicator
    (indicator_id, indicator_name, unit, description, source_dataset)
    VALUES
    (1, 'GDP per capita PPS', 'EU27 = 100',
    'GDP per capita adjusted for purchasing power',
    'prc_ppp_ind_1')
""")

# Importera PPS-statistiken till observation
for index, row in pps.iterrows():
    country_code = row["country_code"]
    year = row["year"]
    value = row["pps_index"]
    quality_flag = row["quality_flag"]

    if pd.isna(quality_flag):
        quality_flag = None

    cursor.execute("""
        INSERT INTO observation
        (country_code, indicator_id, year, value, quality_flag)
        VALUES (%s, %s, %s, %s, %s)
    """, (country_code, 1, year, value, quality_flag))

db.commit()

cursor.close()
db.close()