import pickle, sys, os, random

os.system("clear") #para limpiar depende la terminal que usen en sus sistema puede variar clear se utiliza en linux y cls creo que en windows

numero_random = random.randrange(1000, 9999) #con esto crean un numero random

"""
with open(guardar, "wb") as f:
        pickle.dump(ticket, f)
        
Con este comando van a generar y guardar el archivo
la palabra guardar es una variable que debe contener el nombre del archivo
la palabra ticket es una variable que contendra el diccionario (Objeto)

with open(abrir, "rb") as f:
        ticket = pickle.load(f)
        
similar a lo anterior, la palabra abrir contendra el nombre del archivo a abrir 
la palabra ticket es el diccionario donde se guardara ese objeto        
        
        """
        
os.path.isfile(ruta) # la palabra ruta obtendra el nombre del archivo y verificara que exista

sys.exit() #con este comando cierra la ejecucion del programa