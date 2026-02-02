from weather_api import buscar_clima

def main():
    cidade = input("Digite o nome da cidade: ").strip()
    resultado = buscar_clima(cidade)

    if resultado["erro"]:
        print("❌ Erro ao consultar o clima")
        print("Código:", resultado.get("codigo"))
        print("Mensagem:", resultado.get("mensagem"))
    else:
        print("\n--- CLIMA ATUAL ---")
        print(f"Cidade: {resultado['cidade']}")
        print(f"Temperatura: {resultado['temperatura']}°C")
        print(f"Sensação térmica: {resultado['sensacao']}°C")
        print(f"Clima: {resultado['descricao']}")
        print(f"Umidade: {resultado['umidade']}%")

if __name__ == "__main__":
    main()
