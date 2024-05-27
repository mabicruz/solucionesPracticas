precioInicial= int(input("Ingrese el precio: "))

ivaIngresado= float(input("Ingrese el porcentaje del IVA: "))



iva= precioInicial * ivaIngresado

precioFinal= precioInicial + iva

print("El precio final es: ", precioFinal)

