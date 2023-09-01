from schemas.plot import PlotColors
from schemas.data import EMACalculationType

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    input_file_name: str = "prices.csv"
    output_file_name: str = "output.png"


class DataSettings(BaseSettings):
    ohlc_calculation_time_interval_min: int = 60 * 24
    ema_calculation_based_on: EMACalculationType = EMACalculationType.CLOSE
    ema_periods: int = 14


class PlotSettings(BaseSettings):
    decrease_color: PlotColors = PlotColors.RED
    increase_color: PlotColors = PlotColors.GREEN
    candlestick_low_high_width: float = 0.05
    candlestick_close_open_width: float = 0.4


app_settings = AppSettings()
data_settings = DataSettings()
plot_settings = PlotSettings()
