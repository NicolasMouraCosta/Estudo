from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Função para buscar preços na Binance
def fetch_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={BTCUSDT}"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data['price'])  # Retorna o preço como float
    except Exception as e:
        return {"error": f"Erro na API da Binance: {str(e)}"}

# Função para buscar preços no Mercado Bitcoin
def fetch_mercado_bitcoin_price(symbol):
    url = f"https://www.mercadobitcoin.net/api/{symbol}/ticker/"
    try:
        response = requests.get(url)
        data = response.json()
        if 'ticker' in data and 'last' in data['ticker']:
            return float(data['ticker']['last'])  # Retorna o preço em BRL
        else:
            return {"error": f"Resposta inesperada do Mercado Bitcoin: {data}"}
    except Exception as e:
        return {"error": f"Erro na API do Mercado Bitcoin: {str(e)}"}

# Função para converter BRL para USD
def convert_brl_to_usd(price_brl, usd_brl_rate=5.0):
    return price_brl / usd_brl_rate

# Rota principal
@app.route("/", methods=["GET", "POST"])
def compare_prices():
    if request.method == "POST":
        binance_symbol = request.form["binance_symbol"]
        mercado_bitcoin_symbol = request.form["mercado_bitcoin_symbol"]
        quantity = float(request.form["quantity"])
        currency_choice = request.form["currency_choice"]

        # Buscar preços
        binance_price = fetch_binance_price(binance_symbol)
        mercado_bitcoin_price = fetch_mercado_bitcoin_price(mercado_bitcoin_symbol)

        # Tratamento de erros
        if isinstance(binance_price, dict) and 'error' in binance_price:
            return render_template("index.html", error=f"Erro na Binance: {binance_price['error']}")

        if isinstance(mercado_bitcoin_price, dict) and 'error' in mercado_bitcoin_price:
            return render_template("index.html", error=f"Erro no Mercado Bitcoin: {mercado_bitcoin_price['error']}")

        # Conversão de BRL para USD se necessário
        if currency_choice == "usd":
            mercado_bitcoin_price = convert_brl_to_usd(mercado_bitcoin_price)
            price_label = "USD"
        elif currency_choice == "brl":
            price_label = "BRL"
        else:
            return render_template("index.html", error="Opção inválida. Escolha entre 'USD' ou 'BRL'.")

        # Calcular valores
        value_in_binance = binance_price * quantity
        value_in_mercado_bitcoin = mercado_bitcoin_price * quantity

        # Definindo as taxas
        compra_taxa = 0.005
        venda_taxa = 0.005

        # Cálculo da diferença de preço e lucro após taxas
        preco_compra = binance_price * (1 + compra_taxa)  # Preço de compra com taxa
        preco_venda = mercado_bitcoin_price * (1 - venda_taxa)  # Preço de venda com taxa
        diferenca = preco_venda - preco_compra  # Diferença entre preço de venda e compra
        lucro_total = diferenca * quantity  # Lucro total para a quantidade especificada

        # Renderizar o template com os resultados
        return render_template(
            "index.html",
            binance_price=binance_price,
            mercado_bitcoin_price=mercado_bitcoin_price,
            quantity=quantity,
            price_label=price_label,
            value_in_binance=value_in_binance,
            value_in_mercado_bitcoin=value_in_mercado_bitcoin,
            diferenca=diferenca,
            lucro_total=lucro_total,
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
