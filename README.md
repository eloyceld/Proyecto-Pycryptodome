# Proyecto-Pycryptodome

## Descripción
Este proyecto implementa un sistema básico de cifrado y descifrado de texto utilizando el algoritmo AES (Advanced Encryption Standard) a través de la biblioteca PyCryptodome en Python. La aplicación permite al usuario ingresar un texto, cifrarlo utilizando AES en modo EAX, y luego descifrarlo para verificar el proceso.

AES es un estándar de cifrado ampliamente utilizado y reconocido por organizaciones gubernamentales y empresas para proteger información sensible. Este proyecto sirve como una introducción práctica a los conceptos básicos de criptografía simétrica.

## Características
- Cifrado de texto utilizando AES en modo EAX
- Generación segura de claves criptográficas aleatorias
- Almacenamiento de texto cifrado y descifrado en archivos separados
- Interfaz sencilla de línea de comandos

## Pre-requisitos
- Python 3.6 o superior
- Biblioteca PyCryptodome

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/Proyecto-Pycryptodome.git
cd Proyecto-Pycryptodome
```

### 2. Crear un entorno virtual
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install pycryptodome
```

## Uso
Para ejecutar el script de cifrado/descifrado:

```bash
python pycryptodome.py
```

El programa te pedirá que ingreses un texto para cifrar. Una vez ingresado, el script:
1. Cifrará el texto utilizando AES
2. Mostrará el texto cifrado en la terminal
3. Guardará el texto cifrado en `archivos/cifrado.txt`
4. Descifrará el texto automáticamente
5. Mostrará el texto descifrado en la terminal
6. Guardará el texto descifrado en `archivos/descrifrado.txt`

## Ejemplo de uso

```
Dame un texto a Cifrar: Este es un mensaje secreto

-----------------------------------
Mensaje a Cifrar: Este es un mensaje secreto
-----------------------------------
Texto Cifrado: b'\xa3\x9c\xf2\x8e\x1b\xd0\x8f\xab\x12\x7f\x8d\xab\xe7\xd2\x9f...'
Texto Descifrado: Este es un mensaje secreto
```

## Limitaciones

Este script fue creado con fines educativos y tiene las siguientes limitaciones:

1. **No persiste la clave criptográfica**: La clave se genera cada vez que se ejecuta el script y no se almacena. En una aplicación real, necesitarías un método seguro para almacenar y recuperar la clave.

2. **No guarda el nonce ni el tag**: Para poder descifrar un mensaje en una ejecución futura, es necesario almacenar tanto el nonce como el tag de autenticación junto con el texto cifrado.

3. **No verifica la integridad**: Aunque el modo EAX genera un tag de autenticación, el script actual no lo utiliza para verificar la integridad del mensaje durante el descifrado.

## Conceptos criptográficos utilizados

- **AES (Advanced Encryption Standard)**: Algoritmo de cifrado simétrico adoptado como estándar por el gobierno de los Estados Unidos.
  
- **Modo EAX**: Un modo de operación que proporciona confidencialidad y autenticación (cifrado autenticado).
  
- **Nonce**: Número utilizado una sola vez para garantizar que cifrados idénticos produzcan resultados diferentes.
  
- **Tag de autenticación**: Código que verifica la integridad y autenticidad del mensaje cifrado.

## Seguridad

Para una implementación más segura, se recomienda:

1. Implementar un sistema para el manejo seguro de claves
2. Almacenar el nonce y el tag junto con el texto cifrado
3. Verificar el tag de autenticación durante el descifrado
4. Utilizar contraseñas fuertes o frases de paso para derivar claves

---

Desarrollado como proyecto educativo para aprender los fundamentos de la criptografía moderna en Python.