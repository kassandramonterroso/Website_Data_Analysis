import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())


visits_cart_merge = pd.merge(visits,cart, how="left").reset_index()
print(visits_cart_merge)

null_carts = len(visits_cart_merge[visits_cart_merge.cart_time.isnull()])
print(null_carts)

no_cart = float(null_carts / len(visits_cart_merge))
print(no_cart)


cart_checkout_merge = pd.merge(cart,checkout,how="left")
print(cart_checkout_merge)

null_checkouts = len(cart_checkout_merge[cart_checkout_merge.checkout_time.isnull()])
print(null_checkouts)

no_checkout = float(null_checkouts / len(cart_checkout_merge))
print(no_checkout)
print(len(cart))


all_data = visits.merge(cart,how="left").merge(checkout,how="left").merge(purchase,how="left")
print(all_data.head())


checkout_purchase_merge = pd.merge(checkout,purchase,how="left")
null_purchases = len(checkout_purchase_merge[checkout_purchase_merge.purchase_time.isnull()])
print(null_purchases)

no_purchase = float(null_purchases / len(checkout_purchase_merge))
print(no_purchase)


print("{}% of users visited website but did not add item(s) to cart".format(int(no_cart*100)))
print("{}% of users added item(s) to cart but did not checkout".format(int(no_checkout*100)))
print("{}% of users checked out but did not purchase".format(int(no_purchase*100)))


all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase.mean())



