from pathlib import Path

from settings import app_settings
from plot_builder import CandlestickDataPlotter, EMADataPlotter, PlotBuilder
from data_processor import StockDataProcessor


def main():
    input_folder = f"{Path(__file__).parent.parent}/data/input"
    output_folder = f"{Path(__file__).parent.parent}/data/output"
    input_file_path = f"{input_folder}/{app_settings.input_file_name}"
    output_file_path = f"{output_folder}/{app_settings.output_file_name}"

    not Path.exists(Path(output_folder)) and Path(Path(output_folder)).mkdir()

    data_processor = StockDataProcessor(input_file_path)
    data = data_processor.process_data()

    plot_builder = PlotBuilder([CandlestickDataPlotter(data), EMADataPlotter(data)], output_file_path)
    plot_builder.show_plot()


if __name__ == "__main__":
    main()
