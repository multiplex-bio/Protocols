# Program description and input from user ...
print("\nCon este script vamos a calcular la cantidad de reactivos que son necesarios para realizar el protocolo de qPCR con Opentrons.")





# Handling correct inputs from the user:
valid_number = False

while not valid_number:
    try:
        sample_number = int(input("\nIngresa la cantidad de muestras que quieres procesar (considera los controles de extracción y de RT como muestras): "))

        if type(sample_number) is int:
            if 1 <= sample_number < 94:
                valid_number = True
            else:
                print("\nDebes ingresar un número entre 1 y 96")
        else:
            print("Debes ingresar un número entre 1 y 96")
            
            
    except ValueError:
        print("\nDebes ingresar un número entre 1 y 96")
    

   

    
## Volumes we gonna need ...

Vol_GoTaq_qPCR_MasterMix_2x = (sample_number + 5) * 7.5 # To add an extra of 5 samples
Vol_FnR_primers = (sample_number + 5) * 0.15 # The same variable can be used for both types of primers
Vol_H2O =  (sample_number + 5) * 6.45

#total_volume = (Vol_GoTaq_qPCR_MasterMix_2x + Vol_FnR_primers + Vol_H2O)





# Program's output ...

print("\n\n-> Para preparar el Master Mix, debes cargar los siguientes volumenes en un tubo eppendorf de 2 mL: ")
print("\n\t{} uL de Master Mix 2x GoTaq qPCR".format(Vol_GoTaq_qPCR_MasterMix_2x))
print("\n\t{} uL de primer F".format(Vol_FnR_primers))
print("\n\t{} uL de primer R".format(Vol_FnR_primers))
print("\n\t{} uL de H2O free".format(Vol_H2O))
print("\n\tEste eppendorf se debe colocar en la posición A1 del rack")


print("\n\n-> Adicionalmente, debes agregar: ")
print("\n\t25 uL de Control - en un eppendorf de 1.5 mL, que se debe colocar en la posición C6 del rack\n")
print("\t25 uL de Control + en un eppendorf de 1.5 mL, que se debe colocar en la posición D6 del rack\n")

