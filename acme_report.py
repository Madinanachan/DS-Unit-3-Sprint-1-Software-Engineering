from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'TNT']


def generate_products(num_products=30):
    products = ['0']*num_products
    for i in range (num_products):
      name=ADJECTIVES[randint(0,4)]+' '+NOUNS[randint(0,4)]
      prod=Product(name)
      prod.weight=randint(5,100)
      prod.price=randint(5,100)
      prod.flammability=randint(0,2.5)/randint(1,100)#random float 0<=float<2.5
      products[i]=prod 
    return products


def unique (list_prod):
    list_names=['0']*len(list_prod)
    for i in range (len(list_prod)):
        list_names[i]=list_prod[i].name
    unique_list=[]
    for x in list_names: 
        if x not in unique_list:
            unique_list.append(x)
    return len(unique_list)

def inventory_report(products):
    m=unique(products)
    average_p=0
    average_w=0
    average_flam=0
    for i in range(len(products)):
        average_p+=products[i].price
        average_w+=products[i].weight
        average_flam+=products[i].flammability
    average_p=average_p/len(products)
    average_w=average_w/len(products)
    average_flam=average_flam/len(products)


    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique Product Names:',m)
    print('Average Price:',average_p)
    print('Average Weight:',average_w)
    print('Average Flammability:',average_flam)
    