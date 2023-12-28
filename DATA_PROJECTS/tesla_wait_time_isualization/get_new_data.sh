python3 saveWebArchiveTeslaURLs.py

for file in wayback_LinkLists/*.json
do
  # Run the downloadHistoricHTML.py script with the current file as an argument
  python3 downloadHistoricHTML.py "$file"
done

python3 extractJSONFromHTML.py

python3 getTeslaModelData.py

python3 aggregateModelData.py

python3 createPriceCharts.py