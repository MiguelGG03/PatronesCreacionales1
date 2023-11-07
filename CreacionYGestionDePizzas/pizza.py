class Pizza:
    def __init__(self):
        self._nombre = ""
        self._tamano = ""
        self._masa = ""
        self._salsa = ""
        self._ingredientes = ""

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
    
    def __str__(self):
        return f"nombre: {self.nombre} \nmasa: {self.masa}\nsalsa: {self.salsa}\ningredientes: {self.ingredientes}"
