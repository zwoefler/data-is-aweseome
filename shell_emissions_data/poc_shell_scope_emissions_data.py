import matplotlib.pyplot as plt
import numpy as np

data = {
    "Year": [2016, 2017, 2018, 2019, 2020, 2021, 2022],
    "Scope 1": [72, 73, 71, 70, 63, 60, 51],
    "Scope 2": [11, 12, 11, 10, 8, 8, 7],
    "Scope 3": [0, 0, 1351, 1271, 1054, 1010, 910],
}

fig, ax = plt.subplots()
bar_width = 0.5

bottom = np.zeros(len(data["Year"]))
for scope, color, label in zip(
    ["Scope 1", "Scope 2", "Scope 3"],
    ["darkblue", "turquoise", "red"],
    [
        "Scope 1 emissions - direct GHG emissions",
        "Scope 2 emissions - market-based method",
        "Scope 3 emissions - Use of sold products",
    ],
):
    ax.bar(
        data["Year"], data[scope], bar_width, label=label, color=color, bottom=bottom
    )
    bottom += data[scope]

plt.title("Scope 1, 2 and 3 emissions by Shell")
plt.suptitle("Million tonnes CO2e", fontsize=12)

footnotes = [
    "Scope 1 emissions - direct GHG emissions",
    "Scope 2 emissions - market-based method",
    "Use of sold products",
    "Source: Sustainability Report 2022 Shell. p.25 & p.76",
]
plt.figtext(0.5, -0.01, "\n".join(footnotes), fontsize=8, va="center", ha="center")

ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

plt.show()
