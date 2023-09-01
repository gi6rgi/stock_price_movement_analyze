from abc import ABC, abstractmethod
from typing import List

from pandas import DataFrame
import matplotlib.pyplot as plt

from settings import plot_settings, app_settings


class DataPlotter(ABC):
    @abstractmethod
    def add_data_to_plot(self, plt):
        pass


class CandlestickDataPlotter(DataPlotter):
    def __init__(self, data: DataFrame) -> None:
        self.data = data

    def _get_increasing_decreasing_movement(self) -> (DataFrame, DataFrame):
        return self.data[self.data.close >= self.data.open], self.data[self.data.close < self.data.open]

    def add_data_to_plot(self, plt) -> None:
        up, down = self._get_increasing_decreasing_movement()

        plt.bar(
            up.index,
            up.close - up.open,
            plot_settings.candlestick_close_open_width,
            bottom=up.open,
            color=plot_settings.increase_color,
        )
        plt.bar(
            up.index,
            up.high - up.close,
            plot_settings.candlestick_low_high_width,
            bottom=up.close,
            color=plot_settings.increase_color,
        )
        plt.bar(
            up.index,
            up.low - up.open,
            plot_settings.candlestick_low_high_width,
            bottom=up.open,
            color=plot_settings.increase_color,
        )

        plt.bar(
            down.index,
            down.close - down.open,
            plot_settings.candlestick_close_open_width,
            bottom=down.open,
            color=plot_settings.decrease_color,
        )
        plt.bar(
            down.index,
            down.high - down.open,
            plot_settings.candlestick_low_high_width,
            bottom=down.open,
            color=plot_settings.decrease_color,
        )
        plt.bar(
            down.index,
            down.low - down.close,
            plot_settings.candlestick_low_high_width,
            bottom=down.close,
            color=plot_settings.decrease_color,
        )


class EMADataPlotter(DataPlotter):
    def __init__(self, data: DataFrame) -> None:
        self.data = data["EMA"]

    def add_data_to_plot(self, plt) -> None:
        plt.plot(self.data, label="Exponential Moving Average Value")
        plt.legend()


class PlotBuilder:
    def __init__(self, plots: List[DataPlotter], output_file_path: str) -> None:
        self.output_file_path = output_file_path
        plt.figure()
        self.plots = plots

    def _add_plots_to_figure(self) -> None:
        {plot.add_data_to_plot(plt) for plot in self.plots}

    def show_plot(self) -> None:
        self._add_plots_to_figure()
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()

        plt.xticks(rotation=45, ha="right")
        plt.grid()
        plt.savefig(self.output_file_path)
        plt.show()
