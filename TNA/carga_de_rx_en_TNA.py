print("Con este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de Extracción de TNA con Opentrons.")

sample_number = int(input("Ingrese la cantidad de muestras que desea procesar: "))

confirm_sample_number = input('Confirmas que vas a usar {} muestras (y/n)'.format(sample_number)).lower()
confirm_sample_number = confirm_sample_number.lower()

while confirm_sample_number != "y":
    sample_number = int(input("Ingrese la cantidad de muestras que desea procesar: "))
    confirm_sample_number = input('Confirmas que vas a usar {} muestras (usa y/n para responder)'.format(sample_number)).lower()
    confirm_sample_number = confirm_sample_number.lower()

vol_total_beads = (30 * sample_number * 1)/1000 # uL usados para cada muestra * Cantidad de muestras * Cantidad de veces que se usan las beads / 1000 para tener el volumen en mL
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

print('Para llevar a cabo el protocolo necesitarás ...')
print('{} mL de beads. Tienes que cargar {} wells'.format(vol_total_beads, wells_beads))
print('{} mL de etanol. Tienes que cargar {} wells'.format(vol_total_etanol, wells_etanol))
print('{} mL de etanol sal. Tienes que cargar {} wells'.format(vol_total_etanol_sal, wells_etanol_sal))
print('{} mL de agua ultra pura. Tienes que cargar {} wells'.format(vol_total_elution_buffer, wells_elution_buffer))
print('{} mL de descarte. Tienes que dejar disponibles {} wells'.format(vol_total_descarte, wells_descarte))