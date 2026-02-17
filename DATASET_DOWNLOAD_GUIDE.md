# Dataset Download Guide

## Option 1: Manual Download from Kaggle (Recommended)

### Steps:

1. **Visit Kaggle**
   - Go to [Kaggle Datasets](https://www.kaggle.com/datasets)
   - Search for "airline flights" or "flight delays"
   - Common datasets:
     - "2015 Flight Delays and Cancellations" by DOT
     - "Airline Delay and Cancellation Data"

2. **Download the Dataset**
   - Click on the dataset
   - Click the "Download" button (requires Kaggle account)
   - Save the ZIP file to your Downloads folder

3. **Extract to Project**
   - Extract the ZIP file
   - Copy all CSV files to: `E:\Developments\AirFly Insights\data\raw\`
   - Expected files: `flights.csv`, `airlines.csv`, `airports.csv`

4. **Verify**
   - Check that CSV files are in `data/raw/` directory
   - Note the main flights CSV filename (you'll need to update the notebook)

---

## Option 2: Kaggle API (Advanced)

### Prerequisites:
- Kaggle account
- Kaggle API token

### Setup Kaggle API:

1. **Get API Credentials**
   - Go to https://www.kaggle.com/account
   - Scroll to "API" section
   - Click "Create New API Token"
   - This downloads `kaggle.json`

2. **Install Credentials**
   - Windows: Place `kaggle.json` in `C:\Users\<YourUsername>\.kaggle\`
   - Create the `.kaggle` folder if it doesn't exist

3. **Download Dataset**
   ```bash
   # Activate virtual environment first
   venv\Scripts\activate
   
   # Download dataset (replace with actual dataset name)
   kaggle datasets download -d usdot/flight-delays -p data/raw/
   
   # Unzip
   cd data/raw
   tar -xf flight-delays.zip
   ```

---

## After Download

### Update the Notebook

Open `notebooks/01_data_exploration.ipynb` and update this line:

```python
# Update this with your actual CSV filename
DATA_FILE = RAW_DATA_DIR / 'flights.csv'  # Change 'flights.csv' to your actual filename
```

### Run the Notebook

1. **Activate Virtual Environment**
   ```bash
   venv\Scripts\activate
   ```

2. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

3. **Open Notebook**
   - Navigate to `notebooks/01_data_exploration.ipynb`
   - Run all cells

---

## Expected Dataset Structure

The main flights CSV should contain columns like:
- YEAR, MONTH, DAY, DAY_OF_WEEK
- AIRLINE, FLIGHT_NUMBER, TAIL_NUMBER
- ORIGIN_AIRPORT, DESTINATION_AIRPORT
- SCHEDULED_DEPARTURE, DEPARTURE_TIME, DEPARTURE_DELAY
- SCHEDULED_ARRIVAL, ARRIVAL_TIME, ARRIVAL_DELAY
- CANCELLED, CANCELLATION_REASON
- CARRIER_DELAY, WEATHER_DELAY, NAS_DELAY, SECURITY_DELAY, LATE_AIRCRAFT_DELAY

---

## Troubleshooting

### "No CSV files found"
- Verify files are in `E:\Developments\AirFly Insights\data\raw\`
- Check file extensions are `.csv` (not `.CSV` or `.txt`)

### "File too large"
- The notebook uses sampling (1M rows) for initial exploration
- Full dataset processing will be done in chunks

### "Module not found"
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

---

## Recommended Datasets

1. **2015 Flight Delays and Cancellations**
   - URL: https://www.kaggle.com/datasets/usdot/flight-delays
   - Size: ~5.8M rows
   - Good for learning

2. **Airline On-Time Performance**
   - URL: https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018
   - Size: 60M+ rows
   - Matches project requirements

---

**Need Help?** Check the README.md for more information.
