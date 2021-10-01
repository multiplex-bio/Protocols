print("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de Extracción de TNA con Opentrons.")

sample_number = int(input("\nIngrese la cantidad de muestras que desea procesar: "))

confirm_sample_number = input('Confirmas que vas a usar {} muestras (y/n)'.format(sample_number)).lower()
confirm_sample_number = confirm_sample_number.lower()

while confirm_sample_number != "y":
    sample_number = int(input("Ingrese la cantidad de muestras que desea procesar: "))
    confirm_sample_number = input('Confirmas que vas a usar {} muestras (usa y/n para responder)'.format(sample_number)).lower()
    confirm_sample_number = confirm_sample_number.lower()

vol_total_beads = (50 * sample_number * 1)/1000 # uL usados para cada muestra * Cantidad de muestras * Cantidad de veces que se usan las beads / 1000 para tener el volumen en mL
vol_total_etanol = (130 * sample_number * 2)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_etanol_sal = (130 * sample_number * 1)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_elution_buffer = (60 * sample_number * 1)/1000 # uL usados para lavar cada muestra * Cantidad de muestras * Cantidad de lavados para cada muestra / 1000 para tener el volumen en mL
vol_total_descarte = vol_total_beads + vol_total_etanol + vol_total_etanol_sal + vol_total_elution_buffer

max_vol_reservoir = 15 # max vol de cada well en mL


import math

wells_beads = math.ceil(vol_total_beads/max_vol_reservoir)
wells_etanol = math.ceil(vol_total_etanol/max_vol_reservoir)
wells_etanol_sal = math.ceil(vol_total_etanol_sal/max_vol_reservoir)
wells_elution_buffer = math.ceil(vol_total_elution_buffer/max_vol_reservoir)
wells_descarte = math.ceil(vol_total_descarte/max_vol_reservoir)

print('\n\nPara llevar a cabo el protocolo ... \n')

print("Usarás {} mL de beads. Tienes que cargar {} well, en la posición 'A1' del reservoir\n".format(vol_total_beads+1, wells_beads)) #+1 porque se vio experimentalmente que son necesarios para mejorar la precision del pipeteo

if wells_etanol > 1:
    print("Usarás {} mL de etanol. Tienes que cargar {} mL en las posiciones 'A2' y 'A3' del reservoir\n".format(vol_total_etanol, vol_total_etanol/wells_etanol))
else:
    print("Usarás {} mL de etanol. Tienes que cargar {} mL en la posición 'A2' del reservoir\n".format(vol_total_etanol, vol_total_etanol/wells_etanol))

if wells_etanol > 1:    
    print("Usarás {} mL de etanol sal. Tienes que cargar {} mL en la posición 'A4'\n".format(vol_total_etanol_sal, vol_total_etanol_sal/wells_etanol_sal))
else:
    print("Usarás {} mL de etanol sal. Tienes que cargar {} mL en la posición 'A3'\n".format(vol_total_etanol_sal, vol_total_etanol_sal/wells_etanol_sal))

if wells_etanol > 1:    
    print("Usarás {} mL de agua ultra pura. Tienes que cargar {} mL en la posición 'A5'\n".format(vol_total_elution_buffer, vol_total_elution_buffer/wells_elution_buffer))
else:
    print("Usarás {} mL de agua ultra pura. Tienes que cargar {} mL en la posición 'A4'\n".format(vol_total_elution_buffer, vol_total_elution_buffer/wells_elution_buffer))

if wells_descarte > 1:
    print("Usarás {} mL de descarte. Tienes que dejar disponibles {} wells,".format(vol_total_descarte, wells_descarte) + " desde el 'A12' hasta el 'A" + str(12-wells_descarte) + "'\n")
else:
    print("Usarás {} mL de descarte. Tienes que dejar disponibles {} well, en la posición 'A12'\n".format(vol_total_descarte, wells_descarte))