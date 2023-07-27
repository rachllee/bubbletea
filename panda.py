import pandas as pd

with open('orders.txt', 'r') as file:
    dataset = file.read()


lines = dataset.strip().split('\n')

dates = []
stores = []
flavors = []
toppings = []


for line in lines:
    parts = line.split('|')
    date = parts[0]
    store = parts[1]
    flavor = parts[2]
    topping = parts[3] if len(parts) > 3 else ''

    dates.append(date)
    stores.append(store)
    flavors.append(flavor)
    toppings.append(topping)

df = pd.DataFrame({
    'Date': dates,
    'Store': stores,
    'Flavor': flavors, 
    'Toppings': toppings
})

df.to_pickle('bubble_tea_data.pkl')

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
print(df)
