# Program description and input from user ...

print("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de Real Time PCR con Opentrons.")

# Handling correct inputs from the user:
is_number = False

while not is_number:
    try:
        sample_number = int(input("\nIngresa la cantidad de muestras que quieres procesar (considera los 4 controles como muestras): "))
        
        if sample_number >= 1 and sample_number < 94:
            is_number = True
            
        else:
            print("\nDebes ingresar un número entre 1 y 96")
            
    except ValueError:
        print("\nDebes ingresar un número entre 1 y 96")
    

    
    
## Calculations of the volumes we gonna need ...


# We need a mix h2o and primers:
vol_96_samples = 335 # uL needed to analyze 96 samples
vol_my_samples = round((vol_96_samples * sample_number) / 96, 2) # uL needed the samples I want to analyze

# The mix with primers and h2o nuclease free has the following proportions:
h2o_prop = 11/12
primers_prop = 1/12

# So, for the mix of primers and h2o, we will need:
vol_h2o_my_samples = round(vol_my_samples * h2o_prop, 2)
vol_primers_my_samples = round(vol_my_samples * primers_prop, 2)

# Additionally, we need 5 uL of mastermix for each sample, so we will use
vol_mastermix_my_samples = (sample_number+5)*5 # We load an extra of mastermix.




# Program's output ...

print("\n\n-> Para preparar el mix de agua y primers, debes cargar los siguientes volumenes en un tubo eppendorf de 1.5 mL: ")
print("\n\t{} uL de H2O nuclease free".format(vol_h2o_my_samples))
print("\n\t{} uL de primers".format(vol_primers_my_samples))
print("\n\tEl eppendorf con H2O free y Primers se debe colocar en la posición A1 del rack")


print("\n\n-> Adicionalmente, debes agregar: ")
print("\n\t50 uL de Control + en un eppendorf, que se debe colocar en la posición B1 del rack\n")
print("\t50 uL de Control - en un eppendorf, que se debe colocar en la posición C1 del rack\n")


print("\n\n-> Finalmente, en otro tubo eppendorf de 1.5 mL, debes agregar: ")
print("\n\t{} uL de Master Mix 2x".format(vol_mastermix_my_samples))
print("\n\tEl eppendorf con Master Mix 2x se debe colocar en la posición D1 del rack\n")
