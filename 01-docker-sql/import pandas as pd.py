import pandas as pd
from sqlalchemy import create_engine

df_trips = pd.read_parquet("green_tripdata_2025-11.parquet")
df_zones = pd.read_csv("taxi_zone_lookup.csv")

engine = create_engine("postgresql://postgres:postgres@localhost:5432/ny_taxi")

df_trips.to_sql("green_tripdata_2025_11", engine, if_exists="replace", index=False)
df_zones.to_sql("taxi_zones", engine, if_exists="replace", index=False)

print("✅ Data loaded successfully into Postgres!")


## Question 3: Counting short trips

```sql
SELECT COUNT(*) AS short_trips
FROM green_tripdata_2025_11
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
 
Answer: 8,007