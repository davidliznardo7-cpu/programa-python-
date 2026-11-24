# Constante de horas semanales estándar
LIMITE_HORAS_SEMANALES = 40.0


def evaluar_jornada(horas_diarias):
    """Calcula el total de horas semanales y clasifica la jornada laboral."""
    total_horas = 0.0
    for horas in horas_diarias:
        total_horas += horas

    if total_horas > LIMITE_HORAS_SEMANALES:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"

    return total_horas, clasificacion


def mostrar_reporte(matriz_recursos):
    """Recorre la matriz de recursos y muestra el resumen semanal."""
    print("\n--- REPORTE DE JORNADA LABORAL SEMANAL ---")
    for fila in matriz_recursos:
        nombre = fila[0]
        horas_semana = fila[1:]
        total, clasificacion = evaluar_jornada(horas_semana)
        print(f"Recurso: {nombre} | Total horas: {total:.1f} | Jornada: {clasificacion}")


def main():
    # Matriz: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes] (4 recursos)
    jornadas = [
        ["Ana Gómez", 8, 8, 8, 8, 8],         # 40.0 -> Horario estándar
        ["Carlos Ruiz", 9, 8.5, 9, 8, 8],     # 42.5 -> Sobretiempo
        ["Laura Pérez", 7, 8, 7.5, 8, 6],     # 36.5 -> Horario estándar
        ["Diego Torres", 10, 9, 8, 8, 7]      # 42.0 -> Sobretiempo
    ]

    mostrar_reporte(jornadas)


if __name__ == "__main__":
    main()