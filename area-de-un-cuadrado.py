# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
pilas.fondos.Tarde()

titulo = pilas.actores.Texto(u"Área de un cuadrado", y=200, magnitud=30)
descri = u"""Para calcular el área de un cuadrado lo que se necesita es conocer la longitud de uno de sus lados y luego aplicar la fórmula:
   área = lado x lado
"""
parrafo1 = pilas.actores.Texto(descri, y=160, ancho=400)
parrafo1.centro_y = 'arriba'

etiqueta1 = pilas.actores.Texto("Lado =", y=60, x=-200)
etiqueta1.centro_x = 'izquierda'
entrada = pilas.interfaz.IngresoDeTexto(texto='0', y=60, x=-130, ancho=50)
entrada.centro_x = 'izquierda'

area = 0
def calcular_area():
    lado = int(entrada.texto)
    area = lado * lado
    asistente.decir(u"Área = " + str(area))
    asistente.sonreir()

boton = pilas.interfaz.Boton("Calcular")
boton.y = 10
boton.escala = 1.5
boton.conectar(calcular_area)

asistente = pilas.actores.Mono(225, -150)
asistente.escala = 1

pilas.ejecutar()

