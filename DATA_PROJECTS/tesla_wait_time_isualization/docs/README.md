# Tesla Price Data Visualizer

RENEWING THE PROJECT

# Rewriting using TDD in python
1. Start with extracting data from HTML


See form which countries we got the raw HTML:
`ll | awk '{split($NF, parts, "_"); print parts[1] "_" parts[2] "_" parts[3] "_" parts[4]}' | sort | uniq -c`

See list of models:
`ll | awk '{split($NF, parts, "_"); print parts[1] "_" parts[2] "_" parts[3] "_" parts[4] "_" parts[5] }' | sort | uniq -c`
