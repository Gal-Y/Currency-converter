from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "c520b12fd24d8edd6903bd32"

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/c520b12fd24d8edd6903bd32/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"].get(target_currency, None)

@app.route('/')
def index():
    return render_template('index.html')

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
