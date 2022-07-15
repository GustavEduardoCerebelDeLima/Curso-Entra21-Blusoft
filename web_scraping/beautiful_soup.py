# from bs4 import BeautifulSoup
# import requests
# from operator import itemgetter
#
# products = []
# values = []
# general = []
#
# for i in range(100):
#     target = f'https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html?p={i}'
#     response = requests.get(target)
#     html = BeautifulSoup(response.text, 'html.parser')
#     # print(html)
#
#     for product in html.select('.product-item-link'):
#         products.append(product.text.replace('  ', '').replace('\n', ''))
#
#     for value in html.select('.product-item~ .product-item+ .product-item .price-wrapper .price , .special-price .price , #product-price-11835 .price'): | # .price-wrapper .price
#         values.append(float(value.text.replace('.', '').replace(',', '.').replace('R$', '')))
#
#     # for i in range(len(products)):
#     #     print(f'{products[i]} : {values[i]}')
#
# for i in range(len(products)):
#     new_registry = {'product': products[i], 'Value': values[i]}
#     general.append(new_registry)
#
# final_list = sorted(general, key=itemgetter('Value'), reverse=True)
#
# for i in final_list:
#     print(i)



