# ENCRIPTACIÓN Y DESENCRIPTACIÓN DE MENSAJES MEDIANTE CRIPTOGRAFÍA LINEAL CON MATRICES

Proyecto final para el curso de Álgebra Lineal, desarrollado por estudiantes de Ingeniería en Sistemas de la Universidad Mariano Gálvez de Guatemala.

## 📸 Captura de Pantalla

![Captura del programa](https_URL_DE_TU_IMAGEN_AQUI.png)

> **Instrucción (¡Borra esto!):** Para agregar la captura de pantalla:
> 1. Toma una captura de tu programa, llámala `captura.png`.
> 2. Súbela a tu repositorio de GitHub (igual que subiste el logo).
> 3. Haz clic en el archivo `captura.png` dentro de GitHub.
> 4. Copia la URL de esa imagen.
> 5. Reemplaza el texto `https_URL_DE_TU_IMAGEN_AQUI.png` con la URL que copiaste.

## 📝 Descripción del Proyecto

Este programa es una aplicación de escritorio desarrollada en **Python** que permite encriptar y desencriptar mensajes de texto utilizando los principios de álgebra lineal. El sistema implementa una versión del **Cifrado de Hill**, que utiliza la multiplicación de matrices y la aritmética modular para transformar texto plano en texto cifrado y viceversa.

### Características Principales
* **Cifrado por Matrices:** Utiliza una matriz clave invertible (2x2 o 3x3) seleccionada por el usuario.
* **Aritmética Modular (Módulo 27):** Permite encriptar un alfabeto de 27 caracteres (A-Z y el espacio), resultando en un texto cifrado legible (solo letras).
* **Interfaz Gráfica (GUI):** Interfaz visual intuitiva creada con **Tkinter** que permite ingresar el mensaje y la matriz clave fácilmente.
* **Validación de Clave:** El programa comprueba automáticamente si la matriz clave es válida para la encriptación (es decir, si su determinante es invertible en módulo 27).

## 🚀 Cómo Usar

Existen dos formas de ejecutar esta aplicación:

### Opción 1: Ejecutable (Recomendado para usuarios)

1.  Ve a la sección de **"Releases"** en la barra lateral derecha de este repositorio.
2.  Descarga el archivo `EncriptadorAlgebra.exe`.
3.  Ejecuta el archivo.
    *(Nota: Windows Defender o tu antivirus pueden mostrar una advertencia por ser un programa no firmado. Es un falso positivo, puedes darle a "Ejecutar de todas formas").*

### Opción 2: Desde el Código Fuente (Desarrolladores)

Si tienes Python instalado, puedes ejecutarlo directamente.

1.  Clona o descarga este repositorio:
    ```bash
    git clone [https://github.com/TuUsuario/TuRepositorio.git](https://github.com/TuUsuario/TuRepositorio.git)
    ```
    *(--- ¡Reemplaza la URL con la de tu repositorio! ---)*

2.  Navega a la carpeta del proyecto:
    ```bash
    cd TuRepositorio
    ```

3.  Instala las dependencias necesarias:
    ```bash
    pip install numpy pillow
    ```

4.  Ejecuta el script de Python:
    ```bash
    python encriptador_visual.py
    ```

## 🛠️ Tecnologías Utilizadas

* **Python 3:** Lenguaje principal de programación.
* **Tkinter:** Para la interfaz gráfica de usuario (GUI).
* **NumPy:** Para los cálculos matemáticos avanzados (matrices, determinantes, inversas).
* **Pillow (PIL):** Para cargar la imagen del logo en la ventana de créditos.
* **PyInstaller:** Para empaquetar la aplicación en un archivo `.exe` portable.

## 👨‍💻 Desarrolladores

Este proyecto fue desarrollado por:

* --- (Nombre Completo - Carné) ---
* --- (Nombre Completo - Carné) ---
* --- (Nombre Completo - Carné) ---
* --- (Nombre Completo - Carné) ---
