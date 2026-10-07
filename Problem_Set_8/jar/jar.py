class Jar:
    def __init__(self,capacity=12):
        #Validamos que la capacidad sea un entero no negativo
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")

        #Inicializamos las variables protegidas
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        #Multiplicamos el emoji por la cantidad de galletas actuales
        return "🍪" * self.size

    def deposit(self, n):
        #Validamos que no se exceda la capacidad del tarro
        if self.size + n > self.capacity:
            raise ValueError("Exceeds capacity")
        self._size += n

    def withdraw(self, n):
        #Validamos que haya suficientes galletas para sacar
        if n > self.size:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        #Devuelve la capacidad maxima del tarro
        return self._capacity

    @property
    def size(self):
        #Devuelve el numero de galletas dentro del tarro
        return self._size

