# JSON to CSV converter
🚧 UNTESTED!

Transposes the parkhous JSON to a CSV.
Headings are: 
- "timestamp"
- "free_spaces"
- "occupied_spaces"
- "max_spaces"

🚀 USAGE:
`python3 transpose_json_to_csv.py samstag_rathaus.json`
Writes `samstag_rathaus.csv` into same folder


JSON needs to be in format:
```
{
    "name": "Rathaus",
    "occupation_data": [
        {
            "timestamp": 1716627660,
            "free_spaces": 207,
            "occupied_spaces": 43,
            "max_spaces": 250
        },
        {
            "timestamp": 1716627660,
            "free_spaces": 207,
            "occupied_spaces": 43,
            "max_spaces": 250
        },
    ]
}
```
