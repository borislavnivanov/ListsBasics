TICKET_PRICE = 150
MARKUP = 1.40
LIMITS: dict = {'Clothes': 50.00, 'Shoes': 35.00, 'Accessories': 20.50}

purchases: list = str.split(input(), '|')
budget = float(input())
sales: list = []
cost: float = 0
sum_sales: float = 0


def validate_for_purchase(item_type: str, item_cost: float) -> bool:
    if item_cost <= LIMITS[item_type]:
        return True
    else:
        return False


for purchase in purchases:
    item, str_price = str.split(purchase, '->')
    price = float(str_price)

    if validate_for_purchase(item, price) and budget >= price:
        cost += price
        budget -= price
        new_price = price * MARKUP
        sales.append(new_price)
        print(f'{new_price:.2f} ', end='')

for sale in sales:
    sum_sales += sale

print(f'\nProfit: {sum_sales - cost:.2f}')

if sum_sales + budget >= TICKET_PRICE:
    print('Hello, France!')
else:
    print('Not enough money.')
