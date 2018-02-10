prices = {'apple': 0.40, 'banana': 0.50, 'strawberries':1.00}
my_purchase = {
    'apple': 1,
    'banana': 6,
    'strawberries':15}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print 'I owe the grocer $%.2f' % grocery_bill
