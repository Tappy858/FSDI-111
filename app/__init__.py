from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/products")
def products():
    product_list = ["apples", "oranges", "bananas"]
    bullet_list = "".join("<li>%s</li>" % product for product in product_list)
    return "<h1>Products:</h1><ul>%s</ul>" % bullet_list




