# Stock Price Movement Analyzer

This is a simple application that allows you to visualize stock price data from a CSV file as OHLC (Open, High, Low, Close) candlestick charts along with Exponential Moving Averages (EMAs).

![Example Chart](https://github.com/gi6rgi/stock_price_movement_analyze/blob/4cdea7ad2e0a719cb742f080dcdc47db33efbdc6/data/output/output.png)

## Prerequisites

Before running the app, you can specify the following settings:

- **OHLC_CALCULATION_TIME_INTERVAL_MIN**: This defines the time interval (in minutes) for OHLC candlestick calculations.

- **EMA_PERIODS**: Set the number of periods for calculating the Exponential Moving Average (EMA).

- **INPUT_FILE_NAME**: Specify the name of the CSV file containing your stock price data. The default is `prices.csv`, but you can change it if you're using a different file.

## How to Run the App

Follow these steps to run the Stock Price Movement Analyzer:

1. **Clone the Repository**: Clone this GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/gi6rgi/stock_price_movement_analyze.git
   ```

2. **Navigate to the Repository Directory**: Change your current directory to the cloned repository:Clone this GitHub repository to your local machine using the following command:

   ```bash
   cd stock_price_movement_analyze
   ```

3. **Prepare Your Data**:
   - You can either use the sample CSV file provided in the repository (located at input/prices.csv) or replace it with your own CSV file containing the stock price data.
   - Ensure that your CSV file has rows with timestamps and stock prices at each timestamp.


4. **Install Dependencies and Run App**: Install the required dependencies using pipenv. If you don't have pipenv installed, you can do so using pip:

   ```bash
   pip install pipenv
   ```

    Then, install the dependencies and everyhing is ready to run the app:
   ```bash
   pipenv install && pipenv run python src/main.py
   ```
    You can find generated plot in output folder (if not specified, output/output.png)
