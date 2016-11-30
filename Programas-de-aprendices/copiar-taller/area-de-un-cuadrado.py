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

# continuar aquí...

