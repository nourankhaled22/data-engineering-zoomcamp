 # Module 1: Docker & SQL Homework

This repository contains my solutions for Module 1: Docker & SQL homework of Data Engineering Zoomcamp 2026.

---

## Question 1: Understanding Docker images

I ran the following command:

```bash
docker run -it --entrypoint=bash python:3.13
```````
Inside the container, I checked the pip version using:
pip --version```````
**Answer:** 25.3


---
## Question 2: Understanding Docker networking and docker-compose

In docker-compose, containers communicate with each other using the service name as the hostname
and the internal container port.

Since pgadmin and postgres are in the same docker-compose network:
- Hostname: postgres
- Port: 5432

**Answer:** postgres:5432
---
## Question 3: Counting short trips

I ran the following SQL query on the green taxi trips data for November 2025:

```sql
SELECT COUNT(*) AS short_trips
FROM green_tripdata_2025_11
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
```````
**Answer:** 8,007
