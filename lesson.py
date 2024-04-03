import yaml
import csv

with open('regions.csv', 'r') as csvfile:
    reader = csv. DictReader(csvfile)
    data = [row for row in reader]
    with open('regions.yaml', 'w') as yamlfile:
        yaml.dump(data, yamlfile, encoding="utf-8", indent=4)


with open('districts.csv', 'r') as csvfile:
    reader = csv. DictReader(csvfile)
    data = [row for row in reader]
    with open('districts.yaml', 'w') as yamlfile:
        yaml.dump(data, yamlfile, encoding="utf-8", indent=4)