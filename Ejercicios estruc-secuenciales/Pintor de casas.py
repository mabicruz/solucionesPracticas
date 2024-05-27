mts_largo = float(input("Ingrese en metros el largo de su pared:"))

mts_ancho = float(input("Ingrese en metros el ancho de su pared:"))

metros_total = mts_ancho * mts_largo

costo_pintor = 15000

calculador = costo_pintor * metros_total

print ("El costo es de:", int(calculador))