from flask import Flask, render_template
import json  # To handle JSON file reading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        # Try to open and read the JSON file
        with open('items.json', 'r') as file:
            data = json.load(file)
            # Extract the "items" list, or return empty list if not present
            item_list = data.get("items", [])
    except Exception as e:
        # Log error if something goes wrong and use empty list
        print(f"Error reading JSON file: {e}")
        item_list = []

    # Render the items.html template with the list of items
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    # Run the Flask app on port 5000 with debug mode enabled
    app.run(debug=True, port=5000)
