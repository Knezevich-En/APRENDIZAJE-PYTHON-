import pandas as pd
from textblob import TextBlob

lista_sentimientos = []

df = pd.read_csv('DATA_AVANZADA\\reviews_amazon.csv')
print(df)

for comentario in df["COMENTARIO"]:
    print(f"El primer comentario es :{comentario}")
    analisis = TextBlob(comentario)
    if analisis.sentiment.polarity > 0:
        lista_sentimientos.append("Contento/a 😊")
    elif analisis.sentiment.polarity < 0:
        lista_sentimientos.append("Enojado/a 😠")
    else:
        lista_sentimientos.append("Neutral 😐")

print(lista_sentimientos)

df["SENTIMIENTO"] = lista_sentimientos
print(df)

df.to_excel("DATA_AVANZADA\\reviews_amazon_con_sentimiento.xlsx", index=False)
print("Archivo guardado correctamente")