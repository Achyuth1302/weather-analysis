import matplotlib.pyplot as plt
import seaborn as sns


def plot_weather_trends(df):
    plt.figure(figsize=(12, 5))
    sns.lineplot(x='date', y='temperature', data=df)
    plt.title('Average Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 5))
    sns.lineplot(x='date', y='precipitation', data=df)
    plt.title('Precipitation Over Time')
    plt.xlabel('Date')
    plt.ylabel('Precipitation (mm)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 5))
    sns.lineplot(x='date', y='humidity', data=df)
    plt.title('Humidity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
