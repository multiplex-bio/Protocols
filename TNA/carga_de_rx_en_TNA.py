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
vol_total_beads = (50 * sample_number * 1)/1000 # uL usados para cada muestra * Cantidad de muestras * Cantidad de veces que se usan las beads / 1000 para tener el volumen en mL
vol_total_etanol = (130 * sample_number * 2)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_etanol_sal = (130 * sample_number * 1)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_elution_buffer = (50 * sample_number * 1)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_descarte = vol_total_beads + vol_total_etanol + vol_total_etanol_sal + vol_total_elution_buffer


# Calculamos cuantos wells de descarte van a ser necesarios
wells_descarte = 4 # Uno para cada una de los siguientes desechos: Beads, Etanol + Sal, Etanol (1er lavado) y Etanol (2do lavado)


# Output del script. Indica cuanto de cada reactivo se va a usar y donde debe ser cargado
print('\n\nPara llevar a cabo el protocolo ... \n')

print("Usarás {} mL de beads en la posición 'A1' del reservoir\n".format(vol_total_beads+1)) #+1 porque se vio experimentalmente que son necesarios para mejorar la precision del pipeteo

print("Usarás {} mL de etanol en las posiciones 'A2' y 'A3' del reservoir\n".format(vol_total_etanol/2))

print("Usarás {} mL de etanol sal en la posición 'A4'\n".format(vol_total_etanol_sal))

print("Usarás {} mL de agua ultra pura en la posición 'A5'\n".format(vol_total_elution_buffer))

print("Usarás {} mL de descarte. Tienes que dejar disponibles {} wells,".format(vol_total_descarte, wells_descarte) + " desde el 'A12' hasta el 'A" + str(12-wells_descarte) + "'\n")
