import pandas as pd
from flask import render_template

def calculate_statistics():
    df = pd.read_pickle('bubble_tea_data.pkl')
    
    total_orders = df.shape[0]

    #Topping related numbers
    orders_with_popping = df['Toppings'].str.contains('popping', case=False, na=False).sum()
    orders_with_mpopping = df['Toppings'].str.contains('mango popping', case=False, na=False).sum()
    orders_with_jelly = df['Toppings'].str.contains('jelly', case=False, na=False).sum()
    orders_with_tapioca = df['Toppings'].str.contains('tapioca', case=False, na=False).sum()
    orders_with_notopping = df['Toppings'].str.contains('', case=False, na=True).sum()

    #Date related numbers
    #Month
    orders_january = df['Date'].str.contains('January', case=False, na=False).sum()
    orders_february = df['Date'].str.contains('February', case=False, na=False).sum()
    orders_march = df['Date'].str.contains('March', case=False, na=False).sum()
    orders_april = df['Date'].str.contains('April', case=False, na=False).sum()
    orders_may = df['Date'].str.contains('May', case=False, na=False).sum()
    orders_june = df['Date'].str.contains('June', case=False, na=False).sum()
    orders_july = df['Date'].str.contains('July', case=False, na=False).sum()
    orders_august = df['Date'].str.contains('August', case=False, na=False).sum()
    orders_september = df['Date'].str.contains('September', case=False, na=False).sum()
    orders_october = df['Date'].str.contains('October', case=False, na=False).sum()
    orders_november = df['Date'].str.contains('November', case=False, na=False).sum()
    orders_december = df['Date'].str.contains('December', case=False, na=False).sum()
    #Year
    orders_21 = df['Date'].str.contains('2021', case=False, na=False).sum()
    orders_22 = df['Date'].str.contains('2022', case=False, na=False).sum()
    orders_23 = df['Date'].str.contains('2023', case=False, na=False).sum()
    #Week
    orders_wk1 = df['Date'].str.contains(' 1 | 2 | 3 | 4 | 5 | 6 | 7 ', case=False, na=False).sum()
    orders_wk2 = df['Date'].str.contains(' 8 | 9 | 10 | 11 | 12 | 13 | 14 ', case=False, na=False).sum()
    orders_wk3 = df['Date'].str.contains(' 15 | 16 | 17 | 18 | 19 | 20 | 21 ', case=False, na=False).sum()
    orders_wk4 = df['Date'].str.contains(' 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 ', case=False, na=False).sum()

    #Store
    orders_kungfu = df['Store'].str.contains('Kung', case=False, na=False).sum()
    orders_moose = df['Store'].str.contains('Moose', case=False, na=False).sum()
    orders_ding = df['Store'].str.contains('Ding', case=False, na=False).sum()
    orders_teagather = df['Store'].str.contains('Gather', case=False, na=False).sum()
    orders_teado = df['Store'].str.contains('Tea Do|Tea-Do', case=False, na=False).sum()
    orders_sharetea = df['Store'].str.contains('Share', case=False, na=False).sum()

    store_orders = {
        'Kung Fu': orders_kungfu,
        'Moose': orders_moose,
        'Ding': orders_ding,
        'Tea Gather': orders_teagather,
        'Tea Do': orders_teado,
        'Sharetea': orders_sharetea
    }

    most_frequented_store = max(store_orders, key=store_orders.get)
    most_frequented_store_num = store_orders[most_frequented_store]

    
    store_df = df[df['Store'] == most_frequented_store]
    flavor_counts = store_df['Flavor'].value_counts()
    bystore_flavor = flavor_counts.idxmax()
    bystore_flavor_num = flavor_counts.max()

    print(bystore_flavor)
    print(bystore_flavor_num)

    return {
                            'total_orders': total_orders,
                            'orders_with_popping': orders_with_popping,
                            'orders_with_mpopping': orders_with_mpopping,
                            'orders_with_jelly': orders_with_jelly,
                            'orders_with_tapioca': orders_with_tapioca,
                            'orders_with_notopping': orders_with_notopping,
                            'orders_january': orders_january,
                            'orders_february': orders_february,
                            'orders_march': orders_march,
                            'orders_april': orders_april,
                            'orders_may': orders_may,
                            'orders_june': orders_june,
                            'orders_july': orders_july,
                            'orders_august': orders_august,
                            'orders_september': orders_september,
                            'orders_october': orders_october,
                            'orders_november': orders_november,
                            'orders_december': orders_december,
                            'orders_21': orders_21,
                            'orders_22': orders_22,
                            'orders_23': orders_23,
                            'orders_wk1': orders_wk1,
                            'orders_wk2': orders_wk2,
                            'orders_wk3': orders_wk3,
                            'orders_wk4': orders_wk4,
                            'orders_kungfu': orders_kungfu,
                            'orders_moose': orders_moose,
                            'orders_ding': orders_ding,
                            'orders_teagather': orders_teagather,
                            'orders_teado': orders_teado,
                            'orders_sharetea': orders_sharetea,
                            'most_frequented_store': most_frequented_store,
                            'most_frequented_store_num': most_frequented_store_num,
                            'bystore_flavor': bystore_flavor,
                            'bystore_flavor_num': bystore_flavor_num
    }

