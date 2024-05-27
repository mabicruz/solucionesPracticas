#Realizar un programa en python que nos indique el costo de la leche con todos los descuentos aplicados al precio original. 

leche_litro = 1000

litros_a_comprar = int(input("Ingrese los litros de leche que desea comprar: "))

edad_comprador= int(input("Ingrese su edad: "))

precio_sin_descuento = leche_litro * litros_a_comprar



if litros_a_comprar > 12 and litros_a_comprar < 24:

    descuento_10 = precio_sin_descuento * 10 / 100

    precio_con_descuento10 = precio_sin_descuento -descuento_10

    if edad_comprador > 60:

        descuento_jubilado = precio_con_descuento10 * 10 / 100

        precio_desc_jubilado = precio_con_descuento10 - descuento_jubilado

        print ("Usted tiene un descuento del 10%, y ademas un 10%, extra por ser jubilado. El costo final es de:" , precio_desc_jubilado )

    else:
        print ("Usted tiene un descuento del 10%. El costo final es de:", int(precio_con_descuento10))
    
elif litros_a_comprar >= 24:
    descuento_15 = precio_sin_descuento * 15 / 100

    precio_con_descuento15 = precio_sin_descuento - descuento_15    

    if edad_comprador > 60:

        descuento_jubilado = precio_con_descuento15 * 10 / 100

        precio_desc_jubilado = precio_con_descuento15 - descuento_jubilado

        print ("Usted tiene un descuento del 15%, y ademas un 10%, extra del  por ser jubilado. El costo final es de:" , precio_desc_jubilado )

    else:
        print ("Usted tiene un descuento del 15%. El costo final es de:", int(precio_con_descuento15))
        
else: 

    if edad_comprador > 60:

        descuento_jubilado = precio_sin_descuento * 10 / 100 

        precio_desc_jubilado = precio_sin_descuento - descuento_jubilado

        print ("Usted tiene un 10%, de descuento, por ser jubilado. El precio final es: ", precio_desc_jubilado)

    else:
        print ("El precio final es de: ", int(precio_sin_descuento))