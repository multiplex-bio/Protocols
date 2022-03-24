# Instrucciones de uso
print("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de Extracción de TNA con Opentrons.")


# Handling correct inputs from the user:
is_number = False

while not is_number:
    try:
        sample_number = int(input("\nIngresa la cantidad de muestras que quieres procesar (considera los controles de extracción como muestras): "))
        
        if sample_number >= 1 and sample_number <= 96:
            is_number = True
            
        else:
            print("\nDebes ingresar un número entre 1 y 96")
            
    except ValueError:
        print("\nDebes ingresar un número entre 1 y 96")

    
# Calculamos la cantidad de volumen que vamos a usar para cada reactivo
vol_total_beads = (50 * (sample_number+5))/1000 # (uL usados para cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL
vol_total_isop_1 = (80 * (sample_number+5))/1000 # (uL usados para lavar cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL
vol_total_isop_2 = (180 * (sample_number+5))/1000
vol_total_etanol = (150 * (sample_number+5))/1000 # (uL usados para lavar cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL
vol_total_elution_buffer = (35 * (sample_number+5))/1000 # (uL usados para lavar cada muestra * Cantidad de muestras) / 1000 para tener el volumen en mL


# If the volume we need for a reagent is lower than 3 mL, it is automatically increased to 3 mL
list_of_vols = [vol_total_beads, vol_total_isop_1, vol_total_isop_2, vol_total_etanol, vol_total_elution_buffer]
list_of_vols = [3 if vol < 3 else vol for vol in list_of_vols]


# Output del script. Indica cuanto de cada reactivo se va a usar y donde debe ser cargado
print('\n\n-> Para llevar a cabo el protocolo de Extracción ... \n')

print("\tDebes agregar {} mL de BEADS en el carril 'A1' del reservoir\n".format(list_of_vols[0]+1)) #+1 porque se vio experimentalmente que son necesarios para mejorar la precision del pipeteo

print("\tDebes agregar {} mL de Isopropanol en el carril 'A2' del reservoir\n".format(list_of_vols[1]))

print("\tDebes agregar {} mL de Isopropanol en el carril 'A3' del reservoir\n".format(list_of_vols[2]))

print("\tDebes agregar {} mL de ETANOL 80% en el carril 'A4'\n".format(list_of_vols[3]))

print("\tDebes agregar {} mL de AGUA ULTRA PURA en el carril 'A5'\n".format(list_of_vols[4]))

fin = input("Cuando estés listo/a, cierra la consola.")