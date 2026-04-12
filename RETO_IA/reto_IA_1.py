from textblob import TextBlob

while True:
    try:
        texto = input("Escribe un mensaje de cliente(en INGLÉS, o escribe 'salir' para terminar): ")
        if texto.lower().strip() == "salir":
            print("Gracias por usar el sistema de emociones 👌...")
            break
        analisis = TextBlob(texto)
        emocion_matematica = analisis.sentiment.polarity
        if emocion_matematica > 0:
            print("El cliente esta Contento 😊")
        elif emocion_matematica < 0:
            print("El cliente esta Enojado 😠")
        else:
            print("El cliente esta Neutral 😐")
    except ValueError:
        print("Error: Debes ingresar un mensaje correcto...")
    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        break