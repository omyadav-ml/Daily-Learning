<<<<<<< HEAD
class Two_D_vector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        
    
class Three_D_vector:
    def __init__(self,i,j,k):
        super().__init__(self,i,j)
        self.k=k

a=Two_D_vector(1,2)
b=Three_D_vector(1,2,3)
=======
#q1.]
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()
>>>>>>> ddec1c1 (organized messey file)
