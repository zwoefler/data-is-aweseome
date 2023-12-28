import pandas as pd
import plotly.express as px


def plot_abortions(df):
    fig = px.line(df)
    fig.show()


def main():
    df = pd.read_csv(
        filepath_or_buffer="data/Terminations of pregnancy.csv", index_col=0
    )
    plot_abortions(df)


if __name__ == "__main__":
    main()
