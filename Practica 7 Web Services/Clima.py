import requests

def obtener_datos_meteorologicos(api_key, ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        if "main" in data and "weather" in data:
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            print(f"Temperatura: {temperatura:.2f}°C")
            print(f"Condiciones Climáticas: {condiciones_climaticas}")
        else:
            print("Datos meteorológicos no disponibles.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    #tu_api_key_de_openweathermap
    api_key = "2cd98342949aed8f1a96c5cbad392df1" #tu api key
    ciudad = input("Ingrese el nombre de la ciudad que desea consultar: ")
    obtener_datos_meteorologicos(api_key, ciudad)
