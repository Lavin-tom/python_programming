class A:
    var = None  #public data
    _var = None #protected data
    __var = None #private data


    def __init__(self):
        self.var = 10
        self._var = 20
        self.__var =30       

    def getData(self):
        print(self.var,self._var,self.__var)


class B(A):

    def getData(self):
        super().getData()   #with super method
        print(self.var,self._var,self._A__var)      #second method
        #__var is a protected data can't access here, to access add _A__var. syn (_parentClass__variableName)

obja = A()
obja.getData()

objb = B()
objb.getData()