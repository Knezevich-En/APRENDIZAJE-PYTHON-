import imaplib

conexion= imaplib.IMAP4_SSL("imap.gmail.com")

conexion.login("fkaknezevi@gmail.com", "dnpq prvq yosq tqhh")

conexion.select("inbox")

print("Señor, estamos adentro del sistema de correos")