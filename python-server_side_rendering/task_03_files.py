from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)

# Function to read products from JSON file
def read_json_products():
    with open('products.json', 'r') as file:
        return json.load(file)

# Function to read products from CSV file
def read_csv_products():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert data types properly
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def products():
    # Get 'source' and optional 'id' from query parameters
    source = request.args.get('source')
    product_id = request.args.get('id', default=None, type=int)

    # Initialize variables
    data = []
    error = None

    # Validate the source type
    if source == 'json':
        data = read_json_products()
    elif source == 'csv':
        data = read_csv_products()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Filter by ID if provided
    if product_id is not None:
        filtered = [product for product in data if product["id"] == product_id]
        if not filtered:
            error = "Product not found"
            return render_template('product_display.html', error=error)
        data = filtered

    # Render product data
    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
