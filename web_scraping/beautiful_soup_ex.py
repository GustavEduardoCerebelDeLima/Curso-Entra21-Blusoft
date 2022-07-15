from bs4 import BeautifulSoup
import requests
from operator import itemgetter

products = []
prices = []
general = []

for i in range(100):
    target = f'https://www.havan.com.br/eletro/?departamentosHV=&p={i}'
    response = requests.get(target)
    html = BeautifulSoup(response.text, 'html.parser')

    for product in html.select('.product-item-link'):
        products.append(product.text.replace(' ', '').replace('\n', ''))

    for value in html.select('.weee:nth-child(1) .price'):
        prices.append(float(value.text.replace('.', '').replace('R$\xa0', '').replace(',', '.')))


for i in range(len(products)):
    new_registry = {'Product': products[i], 'Price': prices[i]}
    general.append(new_registry)


final_list = sorted(general, key=itemgetter('Price'), reverse=True)
for i in final_list:
    print(i)




