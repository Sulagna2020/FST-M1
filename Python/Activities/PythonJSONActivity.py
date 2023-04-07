import json

# read file
with open('currency.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

# show values
print("usd: " + str(obj['usd'])) 
print("eur: " + str(obj['eur']))
print("gbp: " + str(obj['gbp'])) 
