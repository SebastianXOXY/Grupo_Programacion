#Vamos a medir la distancia de un corredor realizando un ciclo de while que permita calcular o efectuar la tarea 
#empleandose las variables velociadad x tiempo, y en ese sentido calcular la distancia 
#que ejecuta el corredor

distancia = 0

while (distancia <= 1500):
    velocidad = float (input("Digita la velocidad que quiere que el atleta desarrolle (m/s)"))
    tiempo = int(input("Digite el tiempo que obtuvo el atleta en el momento de desplazarse  (s)"))

    distancia = velocidad * tiempo

    if (distancia <= 1500):
        print ("El atleta corrio  "  , distancia ,  "Metros recorridos")
        print ("La distancia recorrida minima debe ser mayor a 1500 m ")
    else:
        print ("El atleta recorre ", distancia , "metros")
        print ("El atleta recorrio mas de 1500 m ")