# Tesla Deliveries Script
Script to generate a dataset of how many cars/product Tesla produced and delivered per quarter.

## How to use
Generate Dataset:
`python3 tesla_deliveries.py`

Add new quarterly data to the dataset:
`python3 tesla_deliveries.py --add <URL_TO_PRESSRELEASE>`
    - Fails when: Data is already present

Write dataset to file:
`python3 tesla_deliveries.py --to-file <NAME_OF_DATASET>`

## Goal
- File with all the deliveries data that people can import into excel and generate graphs
- Dataset should include "ALL" information from the press release
 


## Development
Start with single press release:
- For given URL, get the data for production
- Print to console
- Get data for Deliveries
- Print to console
- Subject to operating lease accounting
- print
- Get Title, Date, Reason above table, info below table
- Write to file
- make function take URL as parameter

Get links from Investor relations webpage:
- Get all press release links from ir webpage
- itearte them with the function above
