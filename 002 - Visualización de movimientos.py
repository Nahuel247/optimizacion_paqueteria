#######################################################################################
# PROYECTO: Armado Óptimo de Vehículos de Transporte de Paquetes (Ramificación y Poda)
########################################################################################

# Autor: Nahuel Canelo
# Correo: nahuelcaneloaraya@gmail.com



## ===============================##

import time
import re

def simular_movimientos(yard_inicial, movimientos, vehiculo_objetivo, pausa=1.5):
    print("\n--- SIMULACIÓN DE MOVIMIENTOS ---\n")
    yard = create_yard(yard_inicial)
    vehiculo_armado = []

    for paso, instruccion in enumerate(movimientos, 1):
        print(f"🚧 Paso {paso}: {instruccion}")

        submovs = instruccion.split(";")
        for mov in submovs:
            mov = mov.strip()

            # Caso "Mover X de Fila Y a Fila Z"
            match = re.match(r"Mover (\w) de Fila (\d+) a Fila (\d+)", mov)
            if match:
                carro = match.group(1)
                origen = int(match.group(2)) - 1
                destino = int(match.group(3)) - 1

                if carro in yard[origen]:
                    yard[origen].remove(carro)
                    yard[destino] = [carro] + yard[destino]
                continue

            # Caso "Sacar X desde Fila Y" o "Sacar X directamente de Fila Y"
            match_sacar = re.match(r"Sacar (\w) (?:desde|directamente de) Fila (\d+)", mov)
            if match_sacar:
                carro = match_sacar.group(1)
                fila = int(match_sacar.group(2)) - 1
                if yard[fila] and yard[fila][0] == carro:
                    vehiculo_armado.append(carro)
                    yard[fila] = yard[fila][1:]

        # Mostrar el estado actual del patio y el vehiculo en construcción
        print("🎯 Vehiculo objetivo:", vehiculo_objetivo)
        print(" Vehiculo armado :", vehiculo_armado)
        print("📦 Estado actual del patio:")
        for i, fila in enumerate(yard):
            print(f"Fila {i+1}: {fila}")
        print("\n----------------------------\n")
        time.sleep(pausa)

    # Al final, resumen
    print("✅ Simulación finalizada")
    if vehiculo_armado == vehiculo_objetivo:
        print("🎉 El vehiculo armado coincide perfectamente con el vehiculo objetivo.")
    else:
        print("⚠️ El vehiculo armado NO coincide con el vehiculo objetivo.")
        print("vehiculo final   :", vehiculo_armado)
        print("🎯 vehiculo objetivo:", vehiculo_objetivo)

simular_movimientos(new_yard, result_limited.path, small_goal, pausa=1)
