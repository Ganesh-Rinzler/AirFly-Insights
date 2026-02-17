"""
Configuration file for AirFly Insights project.
Contains paths, constants, and data type mappings for memory optimization.
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SAMPLES_DATA_DIR = DATA_DIR / "samples"

# Output directories
OUTPUT_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
REPORTS_DIR = OUTPUT_DIR / "reports"

# Ensure directories exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, SAMPLES_DATA_DIR, FIGURES_DIR, REPORTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Data loading parameters
CHUNK_SIZE = 100000  # Number of rows to read at a time
SAMPLE_SIZE = 1000000  # Number of rows for initial sampling
RANDOM_STATE = 42  # For reproducibility

# Memory optimization: Data type mappings
# These will be applied when loading the dataset to reduce memory usage
DTYPE_MAPPINGS = {
    # Categorical columns (will be converted to 'category' dtype)
    'categorical': [
        'AIRLINE',
        'ORIGIN_AIRPORT',
        'DESTINATION_AIRPORT',
        'CANCELLATION_REASON',
        'DAY_OF_WEEK',
        'TAIL_NUMBER'
    ],
    
    # Integer columns (will be converted to int16 or int32 as appropriate)
    'integer': {
        'YEAR': 'int16',
        'MONTH': 'int8',
        'DAY': 'int8',
        'DAY_OF_WEEK': 'int8',
        'FLIGHT_NUMBER': 'int16',
        'SCHEDULED_DEPARTURE': 'int16',
        'DEPARTURE_TIME': 'int16',
        'DEPARTURE_DELAY': 'float32',
        'TAXI_OUT': 'float32',
        'WHEELS_OFF': 'int16',
        'SCHEDULED_TIME': 'int16',
        'ELAPSED_TIME': 'float32',
        'AIR_TIME': 'float32',
        'DISTANCE': 'int16',
        'WHEELS_ON': 'int16',
        'TAXI_IN': 'float32',
        'SCHEDULED_ARRIVAL': 'int16',
        'ARRIVAL_TIME': 'int16',
        'ARRIVAL_DELAY': 'float32',
        'DIVERTED': 'int8',
        'CANCELLED': 'int8',
        'CARRIER_DELAY': 'float32',
        'WEATHER_DELAY': 'float32',
        'NAS_DELAY': 'float32',
        'SECURITY_DELAY': 'float32',
        'LATE_AIRCRAFT_DELAY': 'float32'
    }
}

# Expected columns in the dataset (will be updated after initial exploration)
EXPECTED_COLUMNS = [
    'YEAR', 'MONTH', 'DAY', 'DAY_OF_WEEK',
    'AIRLINE', 'FLIGHT_NUMBER', 'TAIL_NUMBER',
    'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT',
    'SCHEDULED_DEPARTURE', 'DEPARTURE_TIME', 'DEPARTURE_DELAY',
    'TAXI_OUT', 'WHEELS_OFF', 'SCHEDULED_TIME', 'ELAPSED_TIME',
    'AIR_TIME', 'DISTANCE', 'WHEELS_ON', 'TAXI_IN',
    'SCHEDULED_ARRIVAL', 'ARRIVAL_TIME', 'ARRIVAL_DELAY',
    'DIVERTED', 'CANCELLED', 'CANCELLATION_REASON',
    'CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY',
    'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY'
]

# Delay-related columns
DELAY_COLUMNS = [
    'DEPARTURE_DELAY',
    'ARRIVAL_DELAY',
    'CARRIER_DELAY',
    'WEATHER_DELAY',
    'NAS_DELAY',
    'SECURITY_DELAY',
    'LATE_AIRCRAFT_DELAY'
]

# Key Performance Indicators (KPIs)
KPIS = {
    'on_time_performance': 'Percentage of flights with arrival delay <= 15 minutes',
    'average_delay': 'Average delay duration in minutes',
    'cancellation_rate': 'Percentage of cancelled flights',
    'delay_by_cause': 'Distribution of delays by cause (carrier, weather, NAS, etc.)',
    'busiest_routes': 'Top routes by flight volume',
    'seasonal_trends': 'Flight patterns across months and seasons'
}

# Visualization settings
VIZ_STYLE = 'seaborn-v0_8-darkgrid'
FIGURE_SIZE = (12, 6)
DPI = 100
COLOR_PALETTE = 'Set2'

# Analysis thresholds
ON_TIME_THRESHOLD = 15  # minutes - flights delayed less than this are considered on-time
SIGNIFICANT_DELAY_THRESHOLD = 60  # minutes - delays above this are considered significant
