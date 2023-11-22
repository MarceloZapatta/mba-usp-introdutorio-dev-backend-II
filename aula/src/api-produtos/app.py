from fastapi import FastAPI
from models.product import Product
app = FastAPI()

# @app.get('/api/{name}')
# def say_hello(name:str):
#     if not name:
#         pass
#     return {'Hello': name}

products = [
    Product(id=1, name='Tenis Nike Air', description='Calçados', price=799.99),
    Product(id=2, name='Iphone', description='Tecnologia', price=3998.99),
    Product(id=3, name='Notebook', description='Tecnologia', price=4980.99),
]

@app.get('/api/products')
def get_products():
    return products

@app.get('/api/products/sale')
def get_sale():
    """
    Endpoint que exibe o produto com desconto
    """
    return products[0]
