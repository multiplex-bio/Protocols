# Instrucciones de uso
print("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de Extracción de TNA con Opentrons.")


# Input para calcular cuantos reactivos son necesarios según la cantidad de muestras a procesar
sample_number = int(input("\nIngrese la cantidad de muestras que desea procesar: "))

confirm_sample_number = input('\nConfirmas que vas a usar {} muestras (y/n)'.format(sample_number)).lower()
confirm_sample_number = confirm_sample_number.lower()

while confirm_sample_number != "y":
    sample_number = int(input("\nIngrese la cantidad de muestras que desea procesar: "))
    confirm_sample_number = input('\nConfirmas que vas a usar {} muestras (usa y/n para responder)'.format(sample_number)).lower()
    confirm_sample_number = confirm_sample_number.lower()

    
# Calculamos la cantidad de volumen que vamos a usar para cada reactivo
vol_total_beads = (75 * sample_number+5 * 1)/1000 # uL usados para cada muestra * Cantidad de muestras * Cantidad de veces que se usan las beads / 1000 para tener el volumen en mL
vol_total_etanol = (150 * sample_number+5 * 2)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_etanol_sal = (150 * sample_number+5 * 1)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_elution_buffer = (55 * sample_number+5 * 1)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL

list_of_vols = [vol_total_beads,
               vol_total_etanol,
               vol_total_etanol_sal,
               vol_total_elution_buffer]

# If the volume needed is lower than 3 mL, it is converted to 3 mL instead
list_of_vols = [3 if vol < 3 else vol for vol in list_of_vols]


# Output del script. Indica cuanto de cada reactivo se va a usar y donde debe ser cargado
print('\n\nPara llevar a cabo el protocolo ... \n')

print("Usarás {} mL de beads en la posición 'A1' del reservoir\n".format(list_of_vols[0]+1)) #+1 porque se vio experimentalmente que son necesarios para mejorar la precision del pipeteo

if list_of_vols[1] >= 6:
    print("Usarás {} mL de etanol en las posiciones 'A2' y 'A3' del reservoir\n".format(list_of_vols[1]/2))
else:
    print("Usarás {} mL de etanol en las posiciones 'A2' y 'A3' del reservoir\n".format(list_of_vols[1]))

print("Usarás {} mL de etanol sal en la posición 'A4'\n".format(list_of_vols[2]))

print("Usarás {} mL de agua ultra pura en la posición 'A5'\n".format(list_of_vols[3]))

print("Tienes que dejar disponibles 4 wells para el descarte")
