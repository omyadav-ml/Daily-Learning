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