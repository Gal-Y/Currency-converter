from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "c520b12fd24d8edd6903bd32"  # Replace with your actual API key

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"].get(target_currency, None)

def get_all_currencies():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = response.json()
    return [code[0] for code in data.get("supported_codes", [])]

@app.route('/')
def index():
    currencies = get_all_currencies()
    return render_template('index.html', currencies=currencies)

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    base_currency = request.form['base_currency']
    target_currency = request.form['target_currency']

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        return jsonify({'success': True, 'converted_amount': converted_amount})
    else:
        return jsonify({'success': False, 'error': 'Invalid currency code'})

if __name__ == "__main__":
    app.run(debug=True)
