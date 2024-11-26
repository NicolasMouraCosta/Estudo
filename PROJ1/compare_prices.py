import requests

# Função para buscar preço na Binance
def fetch_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data['price'])  # Extrai o preço do campo "price"
    except Exception as e:
        return {"error": f"Erro na API da Binance: {str(e)}"}

# Função para buscar preço no Mercado Bitcoin
def fetch_mercado_bitcoin_price(symbol):
    url = f"https://www.mercadobitcoin.net/api/{symbol}/ticker/"
    try:
        response = requests.get(url)
        data = response.json()
        if 'ticker' in data and 'last' in data['ticker']:
            return float(data['ticker']['last'])  # Retorna preço em BRL
        else:
            return {"error": f"Resposta inesperada do Mercado Bitcoin: {data}"}
    except Exception as e:
        return {"error": f"Erro na API do Mercado Bitcoin: {str(e)}"}

# Função para converter BRL para USD
def convert_brl_to_usd(price_brl, usd_brl_rate=5.0):
    return price_brl / usd_brl_rate

# Função principal para comparar os preços
def compare_prices():
    # Perguntar ao usuário qual moeda comparar
    binance_symbol = input("Digite o ticker da moeda na Binance (ex.: BTCUSDT): ").strip()
    mercado_bitcoin_symbol = input("Digite o ticker da moeda no Mercado Bitcoin (ex.: BTC): ").strip()
    quantity = float(input("Digite a quantidade da moeda que você quer comparar: ").strip())

    # Perguntar em qual moeda o usuário quer ver os preços
    currency_choice = input("Escolha a moeda para exibir o preço (USD ou BRL): ").strip().lower()

    # Buscar preços
    binance_price = fetch_binance_price(binance_symbol)
    mercado_bitcoin_price = fetch_mercado_bitcoin_price(mercado_bitcoin_symbol)

    # Verificar erros
    if isinstance(binance_price, dict) and 'error' in binance_price:
        print(f"Erro na Binance: {binance_price['error']}")
        return
    if isinstance(mercado_bitcoin_price, dict) and 'error' in mercado_bitcoin_price:
        print(f"Erro no Mercado Bitcoin: {mercado_bitcoin_price['error']}")
        return

    # Conversão de BRL para USD se necessário
    if currency_choice == "usd":
        mercado_bitcoin_price = convert_brl_to_usd(mercado_bitcoin_price)
        price_label = "USD"
    elif currency_choice == "brl":
        price_label = "BRL"
    else:
        print("Opção inválida. Escolha entre 'USD' ou 'BRL'.")
        return

    # Calcular valor total
    value_in_binance = binance_price * quantity
    value_in_mercado_bitcoin = mercado_bitcoin_price * quantity

    # Definindo as taxas
    compra_taxa = 0.005  # Exemplo de 0.5% de taxa de compra
    venda_taxa = 0.005  # Exemplo de 0.5% de taxa de venda

    # Cálculo da diferença de preço e lucro após taxas
    preco_compra = binance_price * (1 + compra_taxa)  # Preço de compra com taxa
    preco_venda = mercado_bitcoin_price * (1 - venda_taxa)  # Preço de venda com taxa
    diferenca = preco_venda - preco_compra  # Diferença entre preço de venda e compra
    lucro_total = diferenca * quantity  # Lucro total para a quantidade especificada

    # Exibir resultados
    print("\nResultados:")
    print(f"Preço na Binance ({price_label}): {binance_price:.2f}")
    print(f"Preço no Mercado Bitcoin ({price_label}): {mercado_bitcoin_price:.2f}")
    print(f"Quantidade: {quantity} moedas")
    print(f"Valor total na Binance: {value_in_binance:.2f} {price_label}")
    print(f"Valor total no Mercado Bitcoin: {value_in_mercado_bitcoin:.2f} {price_label}")
    print(f"Diferença de preço (venda - compra): {diferenca:.2f} {price_label}")
    print(f"Lucro após taxas: {lucro_total:.2f} {price_label}")

if __name__ == "__main__":
    compare_prices()
