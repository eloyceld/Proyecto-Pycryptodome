from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Generar clave y vector de inicialización (IV)
clave = get_random_bytes(16)
cipher = AES.new(clave, AES.MODE_EAX)

texto = input("\nDame un texto a Cifrar: ")

# Crear directorio si no existe
if not os.path.exists("archivos"):
    os.makedirs("archivos")


# Cifrar mensaje
mensaje = texto.encode()
print("-----------------------------------")
print("Mensaje a Cifrar:", texto)
print("-----------------------------------")

cifrado, tag = cipher.encrypt_and_digest(mensaje)
print("Texto Cifrado:", cifrado)

# Guardar el mensaje cifrado en un archivo
with open("archivos/cifrado.txt", "wb") as file:
    file.write(cifrado)

# Descifrar mensaje
cipher_dec = AES.new(clave, AES.MODE_EAX, cipher.nonce)
mensaje_descifrado = cipher_dec.decrypt(cifrado).decode()
print("Texto Descifrado:", mensaje_descifrado)

# Guardar el mensaje descifrado en un archivo
with open("archivos/descrifrado.txt","w") as file:
    file.write(mensaje_descifrado)