import requests

API_KEY = "4ecdd521a786187034bfd46b2151a80d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

cidade = input("Digite o nome da cidade: ")

url = f"{BASE_URL}?q={cidade}&appid={API_KEY}&units=metric"

resposta = requests.get(url)

print(f"Código de status: {resposta.status_code}")

if resposta.status_code == 200:
    dados = resposta.json()  # Converter a resposta para JSON
    umidade = dados['main']['humidity']
    vento = dados['wind']['speed']
    print(f"\033[32mUmidade: {umidade}%")
    print(f"Velocidade do vento: {vento} m/s")
    temperatura = dados['main']['temp']
    descricao = dados['weather'][0]['description']
    print(f"Temperatura em {cidade}: {temperatura}°C")
    print(f"Condição: {descricao}")
else:
    print("Erro ao obter os dados. Verifique a cidade, a chave da API ou a conexão.")

![App rodando]()
