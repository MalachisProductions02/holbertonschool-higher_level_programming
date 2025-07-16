from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON source
def read_json_products():
    with open('products.json', 'r') as file:
        return json.load(file)

# CSV source
def read_csv_products():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# SQLite source
def read_sql_products(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception as e:
        return f"DB_ERROR: {str(e)}"

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', default=None, type=int)

    error = None
    data = []

    if source == 'json':
        data = read_json_products()
    elif source == 'csv':
        data = read_csv_products()
    elif source == 'sql':
        data = read_sql_products(product_id)
        if isinstance(data, str) and data.startswith("DB_ERROR"):
            error = f"Database error: {data[9:]}"
            data = []
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id is not None and source != 'sql':
        filtered = [product for product in data if product["id"] == product_id]
        if not filtered:
            error = "Product not found"
            return render_template('product_display.html', error=error)
        data = filtered

    if product_id is not None and len(data) == 0:
        error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
