import pandas as pd
import matplotlib.pyplot as plt


def plot_co2_emissions(df, labels_column, ticks_every=5):
    amount_options = len(df[labels_column])
    max_y = amount_options * ticks_every
    y_steps_list = list(range(ticks_every, max_y + 1, ticks_every))

    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    for i, value in enumerate(y_steps_list):
        min_value = df.iloc[i]["Min"]
        max_value = df.iloc[i]["Max"]
        ax.broken_barh([(min_value, (max_value - min_value))], (value - 0.5, 1))
        # create_bar(df.iloc[i]["Min"], df.iloc[i]["Max"], value)
    # ax.broken_barh([(740, (910-740))], (3.5, 3))
    ax.set_ylim(0, max_y + ticks_every)
    ax.set_yticks(y_steps_list, labels=df["Options"])
    ax.set_xlim(0, 1000)
    ax.set_xlabel("CO2 Emissions")

    plt.grid(True)
    plt.show()


def main():
    df = pd.read_csv("data/co2_emissions.csv")
    plot_co2_emissions(df, "Options")


if __name__ == "__main__":
    main()
