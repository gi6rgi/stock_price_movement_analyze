import pandas as pd
from pandas import DataFrame

from settings import data_settings


class StockDataProcessor:
    def __init__(self, file_path: str) -> None:
        self.data = pd.read_csv(
            file_path,
            names=["Timestamp", "Stock Price"],
            header=0,
            index_col=0,
            parse_dates=True,
        )

    def _append_ohlc_data(self) -> None:
        self.data = (
            self.data["Stock Price"]
            .resample(f"{data_settings.ohlc_calculation_time_interval_min * 60}S")
            .ohlc()
            .dropna()
        )

    def _append_ema_data(self) -> None:
        self.data["EMA"] = self.data[data_settings.ema_calculation_based_on].ewm(span=data_settings.ema_periods).mean()

    def process_data(self) -> DataFrame:
        self._append_ohlc_data()
        self._append_ema_data()
        return self.data
