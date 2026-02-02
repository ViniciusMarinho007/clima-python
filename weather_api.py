import requests

API_KEY = "b552995cb5b09bcc0ae57e9db602dc7c"

def buscar_clima(cidade):
    """
    Consulta o clima de uma cidade usando a API OpenWeatherMap.

    Args:
        cidade (str): Nome da cidade

    Returns:
        dict: Dados do clima (temperatura, sensação, descrição, umidade)
    """
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    )

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code != 200:
            return {
                "erro": True,
                "mensagem": dados.get("message", "Erro desconhecido"),
                "codigo": resposta.status_code
            }

        clima = {
            "cidade": dados["name"],
            "temperatura": dados["main"]["temp"],
            "sensacao": dados["main"]["feels_like"],
            "descricao": dados["weather"][0]["description"].capitalize(),
            "umidade": dados["main"]["humidity"],
            "erro": False
        }
        return clima

    except requests.exceptions.RequestException as erro:
        return {
            "erro": True,
            "mensagem": str(erro),
            "codigo": None
        }
