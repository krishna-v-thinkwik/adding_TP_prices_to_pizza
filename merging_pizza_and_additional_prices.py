from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Root route to verify deployment
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is live!"})

# Merge prices route
@app.route('/merge-prices', methods=['POST'])
def merge_prices():
    try:
        data = request.get_json()
        pizza_prices = data.get("pizza_prices", [])
        additional_amounts = data.get("additional_items", {}).get("amounts", [])

        combined = pizza_prices + additional_amounts
        return jsonify({"amounts": combined})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
