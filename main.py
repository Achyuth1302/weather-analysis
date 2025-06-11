from src.data_loader import load_and_clean_data
from src.eda import perform_eda
from src.visualizer import plot_weather_trends


def main():
    file_path = 'data/historical_weather.csv'

    df = load_and_clean_data(file_path)
    print(" Data Loaded and Cleaned")

    perform_eda(df)
    print(" EDA Completed")

    plot_weather_trends(df)
    print("Visualizations Generated")


if __name__ == "__main__":
    main()
