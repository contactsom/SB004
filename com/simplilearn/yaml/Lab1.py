#https://zetcode.com/python/yaml/
import yaml

with open('items.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)