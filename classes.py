class Bin:
    max_weight = 20
    objects_array = []

    
    def current_weight(self):
        return sum(self.objects_array)
    



class State:
    bin_number = 1
    current_bin = Bin()
    objects_array = []
    previous_bins = []
    
    def __init__ (self, objects):
        self.objects_array = objects
    
    def find_next_object(self):  #retorna el indice del objeto a ser añadido en la maleta
       objects = self.objects_array 
       current_bin = self.current_bin
       current_weight = current_bin.current_weight()
       for i in range(len(objects)):
           if current_weight + objects[i] <= 20:  #si encuentra un objeto que no sobrecargue la maleta, lo retorna
               return i
        #si no encontro objeto que cupiera, se guarda la maleta y se inicia una nueva
       self.bin_number += 1
       self.previous_bins.append(current_bin.objects_array)
       self.current_bin.objects_array = []
       return 0
        


                
        
        