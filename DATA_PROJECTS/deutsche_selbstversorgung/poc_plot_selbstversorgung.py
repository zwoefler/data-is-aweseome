import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# from tabula import read_pdf


# Data from
# https://www.bmel-statistik.de/fileadmin/daten/0070010-0000.pdf


def read_table_from_PDF():
    # Fucking tabula-py needs java...

    # pdf_url = "https://www.bmel-statistik.de/fileadmin/daten/0070010-0000.pdf"
    # tables = read_pdf(pdf_url, pages="all", multiple_tables=True)
    # df = tables[0]
    # print(df)
    # # Data
    return

    # Download PDF
    # Get data
    # Cleanup / Processing

    # Visualization


def visualize_data(df):
    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Year", y="Obst", data=df, marker="o", label="Obst")
    sns.lineplot(x="Year", y="Gemüse", data=df, marker="o", label="Gemüse")

    plt.xlabel("Year")
    plt.ylabel("Quantity")
    plt.title("Obst and Gemüse Quantity Over the Years")

    plt.legend()
    plt.ylim(0, 100)
    plt.show()


def main():
    years = [
        "2010/11",
        "2011/12",
        "2012/13",
        "2013/14",
        "2014/15",
        "2015/16",
        "2016/17",
        "2017/18",
        "2018/19",
        "2019/20",
        "2020/21",
    ]
    obst_values = [18, 20, 20, 17, 24, 22, 22, 13, 22, 20, 20]
    gemuse_values = [35, 37, 39, 36, 37, 35, 36, 38, 35, 37, 36]
    df = pd.DataFrame({"Year": years, "Obst": obst_values, "Gemüse": gemuse_values})
    visualize_data(df)


if __name__ == "__main__":
    main()
