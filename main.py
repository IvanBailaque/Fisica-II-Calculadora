import os
import sys
from fractions import Fraction
import sympy as sp
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

calores_latentes = {
    "Helio": {
        "fusion": -269.65,
        "Calor latente de fusion": 5.23e3,
        "vapor": -268.93,
        "Calor latente de vapor": 2.09e4
    },
    "Nitrógeno": {
        "fusion": -209.97,
        "Calor latente de fusion": 2.55e4,
        "vapor": -195.81,
        "Calor latente de vapor": 2.01e5
    },
    "Oxígeno": {
        "fusion": -218.79,
        "Calor latente de fusion": 1.38e4,
        "vapor": -182.97,
        "Calor latente de vapor": 2.13e5
    },
    "Alcohol etílico": {
        "fusion": -114,
        "Calor latente de fusion": 1.04e5,
        "vapor": 78,
        "Calor latente de vapor": 8.54e5
    },
    "Agua": {
        "fusion": 0.00,
        "Calor latente de fusion": 3.33e5,
        "vapor": 100.00,
        "Calor latente de vapor": 2.26e6
    },
    "Azufre": {
        "fusion": 119,
        "Calor latente de fusion": 3.81e4,
        "vapor": 444.60,
        "Calor latente de vapor": 3.26e5
    },
    "Plomo": {
        "fusion": 327.3,
        "Calor latente de fusion": 2.45e4,
        "vapor": 1750,
        "Calor latente de vapor": 8.70e5
    },
    "Aluminio": {
        "fusion": 660,
        "Calor latente de fusion": 3.97e5,
        "vapor": 2450,
        "Calor latente de vapor": 1.14e7
    },
    "Plata": {
        "fusion": 960.80,
        "Calor latente de fusion": 8.82e4,
        "vapor": 2193,
        "Calor latente de vapor": 2.33e6
    },
    "Oro": {
        "fusion": 1063.00,
        "Calor latente de fusion": 6.44e4,
        "vapor": 2660,
        "Calor latente de vapor": 1.58e6
    },
    "Cobre": {
        "fusion": 1083,
        "Calor latente de fusion": 1.34e5,
        "vapor": 1187,
        "Calor latente de vapor": 5.06e6
    }
}

#1
def conversor_de_temperatura(temperatura, unidad_inicial, unidad_final):
    if unidad_inicial == 'c':
        if unidad_final == 'k':
            return temperatura + 273.15
        elif unidad_final == 'f':
            return (temperatura * 1.8) + 32
    elif unidad_inicial == 'k':
        if unidad_final == 'c':
            return temperatura - 273.15
        elif unidad_final == 'f':
            return ((temperatura - 273.15) * 1.8) + 32
    elif unidad_inicial == 'f':
        if unidad_final == 'c':
            return (temperatura - 32) * 0.556
        elif unidad_final == 'k':
            return ((temperatura - 32) * 0.556) + 273.15

#2
def volumen_de_gas(cantidad_mol, presion, temperatura):
    R = 0.0821  # Constante de los gases en atm·L/(mol·K)
    volumen = (cantidad_mol * R * temperatura) / presion
    return volumen


#3
def trabajo_realizado_por_sistema(variacion_de_energia_interna, calor_anadido_al_sistema):
    return variacion_de_energia_interna - calor_anadido_al_sistema

#4
def calor_necesario_para_cambio_de_fase(masa, sustancia, tipo_cambio):
    if sustancia not in calores_latentes:
        return "Sustancia no disponible"
    if tipo_cambio not in ["fusion", "vapor"]:
        return "Tipo de cambio no disponible"
    if tipo_cambio == "fusion":
        return masa * calores_latentes[sustancia]["Calor latente de fusion"]
    else:
        return masa * calores_latentes[sustancia]["Calor latente de vapor"]

#5
def eficiencia_maquina_termica(calor_absorbido_de_fuente_caliente, calor_expulsado_a_fuente_fria):
    return 1 - (calor_expulsado_a_fuente_fria / calor_absorbido_de_fuente_caliente)

#6
def fuerza_electrica(q1, q2, x1, y1, x2, y2):
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    fuerza = k * abs(q1 * q2) / distancia ** 2 # K * |Q1.Q2| / raiz de ((x2-x1)^2 + (y2-y1)^2)
    angulo = math.atan2(y2 - y1, x2 - x1)
    return fuerza, angulo

#7
def campo_electrico(q, xq, yq, xp, yp):
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    distancia = math.sqrt((xp - xq) ** 2 + (yp - yq) ** 2)
    campo = k * abs(q) / distancia ** 2
    angulo = math.atan2(yp - yq, xp - xq)
    return campo, angulo

#8
def campo_electrico_anillo(q, r, z):
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    campo = k * q * z / (r ** 2 + z ** 2) ** (3 / 2)
    return campo

#9
def campo_electrico_disco(densidad, r, z):
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    campo = 2 * math.pi * k * densidad * (1 - z / math.sqrt(r ** 2 + z ** 2))
    return campo

#10
def campo_electrico_hilo_infinito(densidad, r):
    k = 8.99e9  # Constante de Coulomb en N m^2 / C^2
    campo = 2 * k * densidad / r
    return campo

if __name__ == '__main__':
    while True:
        try:
            print("\n\t.: Calculadora - Final de Física II :.\n")
            print("\t.: Este programa le permitira obtener los valores de diversas fórmulas asociadas al calor y la termodinámica,\n\t          como también valores asociados al campo eléctrico y la fuerza eléctrica :.\n")
            print("\t1: Conversor de temperatura ")
            print("\t2: Volumen de un gas ideal")
            print("\t3: Primera ley de termodinámica - Trabajo realizado por el sistema")
            print("\t4: Calor necesario para cambiar de fase una sustancia")
            print("\t5: Eficiencia de una máquina térmica")
            print("\t6: Ley de Coulomb: Fuerza eléctrica generada por una carga 1 sobre una carga 2: Módulo y ángulo")
            print("\t7: Campo eléctrico generado por una carga en un punto")
            print("\t8: Campo eléctrico generado por un anillo cargado sobre un punto en su eje")
            print("\t9: Campo eléctrico generado por un disco cargado sobre un punto en su eje")
            print("\t10: Campo eléctrico generado por un hilo infinito")
            print("\t11: Salir del sistema")

            op = input("\nElija una opción: ")
            if op == "1":
                temp = Fraction(input("Indique el valor de temperatura inicial: "))
                print("\tc: Celcius ")
                print("\tk: Kelvin ")
                print("\tf: Farenheit ")
                ui = input("\nElija unidad inicial: [c/k/f] ").lower()
                if ui not in ["c", "k", "f"]:
                    raise KeyError

                print("\tc: Celcius ")
                print("\tk: Kelvin ")
                print("\tf: Farenheit ")
                uf = input("\nElija unidad final: [c/k/f] ").lower()
                if uf not in ["c", "k", "f"]:
                    raise KeyError

                resultado = conversor_de_temperatura(temp, ui, uf)
                print(f"\nLa temperatura convertida es: {resultado} {uf.upper()}")

            elif op == "2":
                print("\nEsta fórmula calcula el volumen de un gas ideal utilizando la ecuación de estado de los gases ideales.")
                cantidad_mol = Fraction(input("Indique el numero de moles: "))
                p = Fraction(input("Indique la presion (atm): "))
                temp = Fraction(input("Indique la temperatura (K): "))
                resultado = volumen_de_gas(cantidad_mol, p, temp)
                print(f"\nEl volumen del gas es: {resultado} L")

            elif op == "3":
                print("\nLa primera ley de la termodinámica se expresa como el cambio en la energía interna de un sistema.")
                variacion_energia_interna = Fraction(input("Indique la variacion de energia interna (J): "))
                calor_anadido = Fraction(input("Indique el calor añadido al sistema (J): "))
                resultado = trabajo_realizado_por_sistema(variacion_energia_interna, calor_anadido)
                print(f"\nEl trabajo realizado por el sistema es: {resultado} J")

            elif op == "4":
                print("\nEsta fórmula calcula el calor necesario para cambiar de fase una sustancia.")
                print("\nElija una sustancia de la siguiente lista:")
                for sustancia in calores_latentes:
                    print(f"\t{sustancia}")

                sustancia = input("Indique la sustancia: ")
                if sustancia not in calores_latentes:
                    raise KeyError("Sustancia no disponible en la tabla")

                tipo_cambio = input("Indique el tipo de cambio (fusion/vapor): ").lower()
                masa = Fraction(input("Indique la masa (kg): "))

                resultado = calor_necesario_para_cambio_de_fase(masa, sustancia, tipo_cambio)
                print(f"\nEl calor necesario para cambiar de fase {masa} kg de {sustancia} es: {resultado} J")

            elif op == "5":
                print("\nLa eficiencia de una máquina térmica se define como la relación entre el trabajo realizado y el calor absorbido de la fuente caliente.")
                calor_absorbido = float(input("Indique el calor absorbido de la fuente caliente (J): "))
                calor_expulsado = float(input("Indique el calor expulsado a la fuente fría (J): "))
                if calor_absorbido <= 0 or calor_expulsado <= 0:
                    raise KeyError("Los valores de calor deben ser positivos")
                if calor_expulsado >= calor_absorbido:
                    raise KeyError("El calor expulsado no puede ser mayor o igual al calor absorbido")
                resultado = eficiencia_maquina_termica(calor_absorbido, calor_expulsado)
                print(f"\nLa eficiencia de la máquina térmica es: {resultado * 100}%")

            elif op == "6":
                print("\nEsta fórmula calcula la fuerza eléctrica entre dos cargas puntuales.")
                q1 = Fraction(input("Indique la carga 1 (C): "))
                q2 = Fraction(input("Indique la carga 2 (C): "))
                x1 = Fraction(input("Indique la posición X de la carga 1 (m): "))
                y1 = Fraction(input("Indique la posición Y de la carga 1 (m): "))
                x2 = Fraction(input("Indique la posición X de la carga 2 (m): "))
                y2 = Fraction(input("Indique la posición Y de la carga 2 (m): "))
                fuerza, angulo = fuerza_electrica(q1, q2, x1, y1, x2, y2)
                print(f"\nLa fuerza eléctrica es: {fuerza} N, con un ángulo de {math.degrees(angulo)} grados")

            elif op == "7":
                print("\nEsta fórmula calcula el campo eléctrico generado por una carga puntual en un punto específico.")
                q = Fraction(input("Indique la carga (C): "))
                xq = Fraction(input("Indique la posición X de la carga (m): "))
                yq = Fraction(input("Indique la posición Y de la carga (m): "))
                xp = Fraction(input("Indique la posición X del punto (m): "))
                yp = Fraction(input("Indique la posición Y del punto (m): "))
                campo, angulo = campo_electrico(q, xq, yq, xp, yp)
                print(f"\nEl campo eléctrico es: {campo} N/C, con un ángulo de {math.degrees(angulo)} grados")

            elif op == "8":
                print("\nEsta fórmula calcula el campo eléctrico generado por un anillo cargado sobre un punto en su eje.")
                q = Fraction(input("Indique la carga del anillo (C): "))
                r = Fraction(input("Indique el radio del anillo (m): "))
                z = Fraction(input("Indique la distancia desde el centro del anillo al punto en el eje (m): "))
                campo = campo_electrico_anillo(q, r, z)
                print(f"\nEl campo eléctrico generado por el anillo en el punto es: {campo} N/C")

            elif op == "9":
                print("\nEsta fórmula calcula el campo eléctrico generado por un disco cargado sobre un punto en su eje.")
                densidad = Fraction(input("Indique la densidad de carga superficial (C/m^2): "))
                r = Fraction(input("Indique el radio del disco (m): "))
                z = Fraction(input("Indique la distancia desde el centro del disco al punto en el eje (m): "))
                campo = campo_electrico_disco(densidad, r, z)
                print(f"\nEl campo eléctrico generado por el disco en el punto es: {campo} N/C")

            elif op == "10":
                print("\nEsta fórmula calcula el campo eléctrico generado por un hilo infinito cargado.")
                densidad = Fraction(input("Indique la densidad de carga lineal (C/m): "))
                r = Fraction(input("Indique la distancia al hilo (m): "))
                campo = campo_electrico_hilo_infinito(densidad, r)
                print(f"\nEl campo eléctrico generado por el hilo infinito es: {campo} N/C")

            elif op == "11":
                print("\nSaliendo del sistema...")
                break
            else:
                print("\nOpción no válida, intente nuevamente.")

        except KeyError as e:
            print(e)
            print("\nHubo un error con su entrada. Por favor, intente nuevamente.")
        except ValueError:
            print("\nHubo un error con su entrada. Por favor, intente nuevamente.")
