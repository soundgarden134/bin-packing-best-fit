import copy
import math
from classes import Bin
from classes import State

def transition(state):      #agrega objetos a la maleta correspondiente y los borra de la lista de objetos
    new_graph = copy.deepcopy(state)
    i = new_graph.find_next_object()
    new_graph.current_bin.objects_list.append(new_graph.objects_list[i])
    del new_graph.objects_list[i]
    return new_graph


# 17 paquetes de 0.5kg, 8 de 1kg, 10 de 1.5 kg, 9 de 2 kg, 7 de 2.5 kg 2 de 3 kg, 3 de 3.5 kgs, 1 de 4 kg, 4 de 4.5 kgs 5 de 5 kg.  
objects = []
for i in range(17):
    objects.append(0.5)

for i in range(17, 25):
    objects.append(1)
    
for i in range(25, 35):
    objects.append(1.5)
    
for i in range(35, 44):
    objects.append(2)

for i in range(44, 51):
    objects.append(2.5)

for i in range(51,53):
    objects.append(3)

for i in range(53,56):
    objects.append(3.5)

for i in range(56,57):
    objects.append(4)

for i in range(57, 61):
    objects.append(4.5)

for i in range(61, 66):
    objects.append(5)


min_bins = math.ceil(sum(objects)/20)
print("Lowest number of bins: "+ str(min_bins))

#Se invierte el array para que quede de manera descendente y funcionar mejor en First Fit
objects.sort(reverse = True)

state = State(objects)  #inicializa el estado con los objetos iniciales
bin_graph = []
bin_graph.append(state)

while len(objects) > 0: #mientras haya objetos, se hacen transiciones
    bin_graph.append(transition(bin_graph[-1]))
    if (bin_graph[-1].is_final()):
        break

    

for i in range(len(state.previous_bins)):
    print("Bin number "+ str(i+1) + ": " + str(state.previous_bins[i]))
print("Final bin: "+ str(state.current_bin.objects_list))


    