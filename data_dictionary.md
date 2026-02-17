# AirFly Insights - Data Dictionary

## Dataset Overview

**Source:** Kaggle Airlines Flights Data  
**Size:** 60+ million records  
**Time Period:** [To be determined after data exploration]  
**File Format:** CSV

---

## Column Definitions

### Temporal Columns

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `YEAR` | int16 | Year of flight | 2015, 2016 | |
| `MONTH` | int8 | Month of flight (1-12) | 1, 2, ..., 12 | |
| `DAY` | int8 | Day of month (1-31) | 1, 2, ..., 31 | |
| `DAY_OF_WEEK` | int8 | Day of week (1-7) | 1=Monday, 7=Sunday | |

### Flight Identification

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `AIRLINE` | category | Airline code | AA, DL, UA, WN | IATA airline codes |
| `FLIGHT_NUMBER` | int16 | Flight number | 1234 | Unique within airline |
| `TAIL_NUMBER` | category | Aircraft tail number | N12345 | Unique aircraft identifier |

### Route Information

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `ORIGIN_AIRPORT` | category | Origin airport code | ATL, ORD, LAX | IATA airport codes |
| `DESTINATION_AIRPORT` | category | Destination airport code | JFK, SFO, DFW | IATA airport codes |
| `DISTANCE` | int16 | Flight distance in miles | 500, 1200, 2500 | |

### Departure Information

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `SCHEDULED_DEPARTURE` | int16 | Scheduled departure time (HHMM) | 1430 = 2:30 PM | 24-hour format |
| `DEPARTURE_TIME` | int16 | Actual departure time (HHMM) | 1445 = 2:45 PM | Null if cancelled |
| `DEPARTURE_DELAY` | float32 | Departure delay in minutes | -5, 0, 15, 60 | Negative = early |
| `TAXI_OUT` | float32 | Taxi out time in minutes | 10, 15, 20 | Time from gate to takeoff |
| `WHEELS_OFF` | int16 | Wheels off time (HHMM) | 1500 | Actual takeoff time |

### Flight Duration

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `SCHEDULED_TIME` | int16 | Scheduled flight time in minutes | 120, 180, 240 | Gate to gate |
| `ELAPSED_TIME` | float32 | Actual elapsed time in minutes | 125, 185, 250 | Actual gate to gate |
| `AIR_TIME` | float32 | Time in air in minutes | 100, 160, 220 | Wheels off to wheels on |

### Arrival Information

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `WHEELS_ON` | int16 | Wheels on time (HHMM) | 1700 | Actual landing time |
| `TAXI_IN` | float32 | Taxi in time in minutes | 5, 10, 15 | Time from landing to gate |
| `SCHEDULED_ARRIVAL` | int16 | Scheduled arrival time (HHMM) | 1630 | 24-hour format |
| `ARRIVAL_TIME` | int16 | Actual arrival time (HHMM) | 1645 | Null if cancelled |
| `ARRIVAL_DELAY` | float32 | Arrival delay in minutes | -5, 0, 15, 60 | **Primary delay metric** |

### Delay Causes

All delay columns are in minutes and only populated when `ARRIVAL_DELAY > 0`.

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `CARRIER_DELAY` | float32 | Delay due to airline | 0, 15, 30 | Maintenance, crew, etc. |
| `WEATHER_DELAY` | float32 | Delay due to weather | 0, 20, 45 | Storms, wind, etc. |
| `NAS_DELAY` | float32 | National Air System delay | 0, 10, 25 | Air traffic control |
| `SECURITY_DELAY` | float32 | Delay due to security | 0, 5, 10 | Rare |
| `LATE_AIRCRAFT_DELAY` | float32 | Delay due to late incoming aircraft | 0, 15, 40 | Previous flight delayed |

**Note:** Delay cause columns may not sum to `ARRIVAL_DELAY` due to rounding and reporting practices.

### Cancellation and Diversion

| Column | Data Type | Description | Example Values | Notes |
|--------|-----------|-------------|----------------|-------|
| `CANCELLED` | int8 | Flight cancelled (0/1) | 0, 1 | 1 = cancelled |
| `CANCELLATION_REASON` | category | Reason for cancellation | A, B, C, D | See codes below |
| `DIVERTED` | int8 | Flight diverted (0/1) | 0, 1 | 1 = diverted |

**Cancellation Reason Codes:**
- `A` = Carrier (airline fault)
- `B` = Weather
- `C` = National Air System (NAS)
- `D` = Security

---

## Derived Features (To be created in Week 2)

| Feature | Description | Calculation |
|---------|-------------|-------------|
| `ROUTE` | Origin-Destination pair | `ORIGIN_AIRPORT + '-' + DESTINATION_AIRPORT` |
| `DEPARTURE_HOUR` | Hour of scheduled departure | `SCHEDULED_DEPARTURE // 100` |
| `DEPARTURE_PERIOD` | Time of day category | Morning/Afternoon/Evening/Night |
| `MONTH_NAME` | Month name | January, February, etc. |
| `IS_WEEKEND` | Weekend indicator | Saturday/Sunday = 1 |
| `SEASON` | Season of year | Winter/Spring/Summer/Fall |
| `IS_DELAYED` | Delay indicator | `ARRIVAL_DELAY > 15` |
| `DELAY_CATEGORY` | Delay severity | On-time/Minor/Moderate/Severe |

---

## Key Performance Indicators (KPIs)

1. **On-Time Performance:** % of flights with arrival delay ≤ 15 minutes
2. **Average Delay:** Mean arrival delay in minutes
3. **Cancellation Rate:** % of flights cancelled
4. **Delay by Cause:** Distribution across carrier, weather, NAS, security, late aircraft
5. **Busiest Routes:** Top origin-destination pairs by flight count
6. **Seasonal Trends:** Flight patterns across months and seasons

---

## Data Quality Notes

*To be updated after initial exploration:*

- [ ] Null value percentages by column
- [ ] Duplicate records count
- [ ] Data type inconsistencies
- [ ] Outliers and anomalies
- [ ] Date range coverage
- [ ] Airport and airline coverage

---

**Last Updated:** February 16, 2026  
**Status:** Template - To be populated after data exploration
