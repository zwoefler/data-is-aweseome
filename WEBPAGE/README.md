# Data is Awesome Webpage
Visualize the data in this project via a simple userinterface

## Setup
```bash
npm install
npm run dev
```

## Data format (for line charts)
JSON and CSV.

CSV: standard table, with the labels in the first column. The data from the second column and following.
JSON: An Object with 2 parts. A "labels" Array (x-Axis) and a "data" object (data rows / y-axis).
- labels: An array of strings. Labels for x-axis
- data: Dictionary, each key is a string representing a category. Each value is an Array of numbers (data points)
```JSON
{
    "labels": ["2020", "2021", "2022", "2023"], // Years for the x-axis
    "data": {
      "Meat Consumption": [150, 200, 250, 300], // Data points for Meat Consumption
      "Vegetable Consumption": [100, 120, 150, 180], // Data points for Vegetable Consumption
      "Fruit Consumption": [80, 90, 100, 110] // Data points for Fruit Consumption
    }
}
```

## How to add a datastroy
1. Create markdown in `content/data-blog/your_new_blog.md`
2. Add your data (json and csv) to `assets/your_new_data.(csv/json)`
3. To display your data, create a component `component/content/your_data_component.vue`
4. Add the following dummy content
```markdown
# Your New Blog

<SHORT SHORT SUMMARY - WILL BE DISPLAYED ON MAIN PAGE>

:your_data_component

More Text if needed

---
## ❓️ Fragen
- Woher kommen die Daten?
- Warum ist xyz zu beobachten?

---

## 📚️ Quellen:

```
5. `git push` and merge branch into master.
