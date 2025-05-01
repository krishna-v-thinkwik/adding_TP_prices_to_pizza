from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/merge-prices', methods=['POST'])
def merge_prices():
    try:
        data = request.get_json()
        pizza_prices = data.get("pizza_prices", [])
        additional_amounts = data.get("additional_items", {}).get("amounts", [])

        # Combine both arrays
        combined = pizza_prices + additional_amounts

        return jsonify({"amounts": combined})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
