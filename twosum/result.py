import json
from twosum_solution import shopping_list

with open ('costco_products.json', encoding='utf-8') as f: ## it has japanese characters
    data = json.load(f)

## convert list of dicts to {name: price} dict
product_dic = {item["name"]: item["price"] for item in data}

##print(product_dic)
dic = product_dic
budget = 10000
result = shopping_list(dic, budget)
print(result)