import numpy as np
import itertools

class DetRule:

    def __init__(self,*Matrices: np.ndarray) -> None:
        self.mats = np.array(Matrices) # (i,j,k) i-th matrix j-th row k-th col
        self.shape = self.mats.shape
        assert self.shape[1]==self.shape[2],\
                'Check if all matrices are squared and of same dimension'
        self.terms = self.mats.shape[0]**self.mats.shape[1] # (t,n,n) ->t^n
        self.addMats = sum([self.mats[i]
                            for i in range(self.shape[0])])
        self.addedMatsDet = np.linalg.det(self.addMats)
        self.matsDet = [np.linalg.det(self.mats[i])
                          for i in range(self.shape[0])]
        
    def ComMats(self):
        terms = np.arange(self.shape[0])
        for combination in itertools.product(terms,repeat=self.shape[1]):
            yield np.array([self.mats[term][row] 
                            for row,term in enumerate(combination)])

    def ComMatsDet(self):
        for mat in self.ComMats():
            yield np.linalg.det(mat)

    def ComMatDetResult(self):
        Sum = 0
        for result in self.ComMatsDet():
            Sum+=result
        return Sum

        


        
