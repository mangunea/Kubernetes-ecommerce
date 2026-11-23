from flask import Flask, jsonify

app = Flask(__name__)

#premade products list
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 1200,
        "stock": 10
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 800,
        "stock": 15
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 100,
        "stock": 25
    },
    {
        "id": 4,
        "name": "Keyboard",
        "price": 50,
        "stock": 30
    }
]

#route /products shows the products made above
@app.route("/products", methods=["GET"])
def get_products():

    return jsonify(products)

#route shows the specific product by its id
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    for product in products:

        if product["id"] == product_id:
            return jsonify(product)

    return jsonify({
        "error": "Product not found"
    }), 404

#route shows the health of the service
@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "healthy",
        "service": "product-service"
    })

#run on port 5001 for products
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001
    )