class Pizza:
    def __init__(self):
        self._nombre = ""
        self._tamano = ""
        self._masa = ""
        self._salsa = ""
        self._ingredientes = ""
        self._precio = 0.0

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tamano(self):
        return self._tamano
    
    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    @property
    def masa(self):
        return self._masa
    
    @masa.setter
    def masa(self, masa):
        self._masa = masa
        
    @property
    def salsa(self):
        return self._salsa
    
    @salsa.setter
    def salsa(self, salsa):
        self._salsa = salsa
        
    @property
    def ingredientes(self):
        return self._ingredientes
    
    @ingredientes.setter
    def ingredientes(self, ingredientes):
        self._ingredientes = ingredientes

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,precio):
        self._precio = precio

    def ingredientesToStr(self):
        stringIngredientes=""
        for ingrediente in self.ingredientes:
            if(stringIngredientes == ""):
                stringIngredientes+=ingrediente
            else:
                stringIngredientes += ", "+ingrediente
        return stringIngredientes
    
    def to_csv(self):
        return f"{self.nombre};{self.tamano};{self.masa};{self.salsa};{self.ingredientesToStr()};{self.precio}"
