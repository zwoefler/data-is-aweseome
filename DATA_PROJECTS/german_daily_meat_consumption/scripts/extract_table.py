import pdfplumber
import re
import pandas as pd

pdf_path = "forsa-ernaehrungsreport-2024-tabellen.pdf"

def split_and_merge_table_lines(input_lines):
    processed_table = []
    merged_line = ""

    for i, line in enumerate(input_lines):
        stripped_line = line[0].strip()

        if i == 0:
            year_row = [''] + re.split(r'\s+', stripped_line)
            processed_table.append(year_row)
            continue

        if re.search(r'\d|\*', stripped_line):
            if merged_line:
                stripped_line = merged_line + " " + stripped_line
                merged_line = ""

            match = re.search(r'[^\d\*]+', stripped_line) 
            if match:
                text_part = match.group(0).strip()
                number_part = stripped_line[len(text_part):].strip()

                numbers = re.split(r'\s+', number_part)

                processed_table.append([text_part] + numbers)
            else:
                processed_table.append(re.split(r'\s+', stripped_line))
        else:
            merged_line = stripped_line

    return processed_table

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[11 - 1]
    lower_half_bbox = (0, 475, page.width, page.height - 180)
    cropped_page = page.within_bbox(lower_half_bbox)
    lines = cropped_page.extract_text_lines()

table_lines = [[line["text"]] for line in lines]

del table_lines[1]
processed_table = split_and_merge_table_lines(table_lines)
df = pd.DataFrame(processed_table)

print(df)

df.to_csv("data/daily_german_meat_consumption.csv", index=False)

