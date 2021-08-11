from os import system
import random

def run():

    try:
        nuevo_juego = Ahorcado()
        while nuevo_juego.juego_en_curso:
            nuevo_juego.pedir_palabra()
    except ValueError as error:
        print(error)

class Ahorcado():
    def __init__(self):
        self.__palabra = {}
        self.__palabras_adivinadas = {}
        self.__salida_juego = ""
        self.__juego_en_curso = True
        self.palabras = []
        self.iniciar_juego()

    def iniciar_juego(self):
        self.agregar_nueva_palabra()

    def obtener_plabras(self):
        with open("./palabras.txt", "r", encoding="utf-8") as file:
            for palabra in file:
                self.palabras.append(palabra.strip())
            

    def agregar_nueva_palabra(self):
        self.obtener_plabras()
        palabra_randon = random.choice(self.palabras)
        cont = 0
        for i in palabra_randon:
            self.__palabra[cont] = i
            self.__palabras_adivinadas[cont] = " _ "
            self.__salida_juego += " _ "

            cont = cont + 1

    def pintar_salida_juego(self):
        self.__salida_juego = ""
        for items, values in self.__palabras_adivinadas.items():
            self.__salida_juego += values
        if self.__palabras_adivinadas == self.__palabra:
            self.__juego_en_curso = False
            print("juego terminado")

    def validar_palabra(self, palabra_elegida):
        self.validar_tipo_dato(palabra_elegida)
        for items, values in self.__palabra.items():
            if values == palabra_elegida:
                self.__palabras_adivinadas[items] = values
        self.pintar_salida_juego()

    def pedir_palabra(self):
        system("clear")
        print(self.salida_juego)
        palabra_elegida = input("Favor ingrese una palabra:")
        self.validar_palabra(palabra_elegida)

    def validar_tipo_dato(self, palabra_elegida):
        if not palabra_elegida.isalpha():
            raise ValueError("Solo se aceptan letras")

    @property
    def salida_juego(self):
        return self.__salida_juego
    
    @property
    def juego_en_curso(self):
        return self.__juego_en_curso


if __name__ == "__main__":
    run()
