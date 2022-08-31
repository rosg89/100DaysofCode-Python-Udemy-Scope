################### Scope ####################

#Local Scope
def drink_potion():
  potion_strenght = 2
  print(potion_strenght)
 
#Va a dar error porque la variable potion_strenght está definida dentro de la función y no se puede acceder a ella desde fuera
print(potion_strenght)

#Global scope
player_health = 10

def better_health():
  print(player_health)
  
#Este lo va a imprimir porque fue definido fuera de la función
better_health()

#Namespace
#Be aware where you create it. Ver donde creamos la variable por el tema del scope. 

#Si creamos una variable dentro de una función, solo será available dentro de esa función. 

#Lo del scope no aplica a los bloques, tipo if, for, while, por ejemplo.


#Para modificar una variable global desde una función hay que hacer esto, pero no se recomienda:
enemies = 1

def increase_enemies():
  #Si quiero acceder desde la función a la variable de afuera
  global enemies
  enemies += 1
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function:{enemies}")

#Se recomienda hacer esto:
enemigos = 1
def increase_enemigos():
  print(f"Enemigos dentro de la función: {enemigos}")
  return enemigos + 1

enemigos = increase_enemigos()
print(f"Enemigos fuera de la función: {enemigos}")

#Global Constants
#Están en upper case para diferencia
PI = 3.14159

