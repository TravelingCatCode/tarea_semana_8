class Ruta:
    # Clase que representa una ruta de entrega con atributos identificador, distancia y capacidad
    def __init__(self, id_ruta, distancia, capacidad):
        self.id_ruta = id_ruta  # Identificador único de la ruta
        self.distancia = distancia  # Distancia de la ruta en kilómetros
        self.capacidad = capacidad  # Capacidad de carga de la ruta en kilogramos

    def __str__(self):
        # Representación en texto de la ruta para mostrar información de forma legible
        return f"Ruta(ID: {self.id_ruta}, Distancia: {self.distancia}, Capacidad: {self.capacidad})"


class Nodo:
    # Clase que representa un nodo del árbol binario
    def __init__(self, ruta):
        self.ruta = ruta  # Objeto de tipo Ruta que almacena los datos
        self.izquierdo = None  # Hijo izquierdo del nodo
        self.derecho = None  # Hijo derecho del nodo


class ArbolBinarioRutas:
    # Clase que implementa un Árbol Binario de Búsqueda para gestionar rutas de entrega
    def __init__(self):
        self.raiz = None  # Inicialización del árbol con una raíz vacía

    def agregar(self, ruta):
        # Método para agregar una nueva ruta al árbol
        nuevo_nodo = Nodo(ruta)  # Crear un nuevo nodo con la ruta proporcionada
        if not self.raiz:  # Si el árbol está vacío, el nuevo nodo será la raíz
            self.raiz = nuevo_nodo
        else:  # Si no está vacío, se llama al método recursivo para insertarlo
            self._agregar_recursivo(self.raiz, nuevo_nodo)

    def _agregar_recursivo(self, actual, nuevo):
        # Método recursivo para ubicar la posición correcta de un nodo
        if nuevo.ruta.id_ruta < actual.ruta.id_ruta:  # Comparar identificadores para decidir el lado
            if actual.izquierdo:
                self._agregar_recursivo(actual.izquierdo, nuevo)
            else:
                actual.izquierdo = nuevo  # Si no existe hijo izquierdo, asignar el nuevo nodo
        else:
            if actual.derecho:
                self._agregar_recursivo(actual.derecho, nuevo)
            else:
                actual.derecho = nuevo  # Si no existe hijo derecho, asignar el nuevo nodo

    def buscar(self, id_ruta):
        # Método para buscar una ruta específica por su identificador
        return self._buscar_recursivo(self.raiz, id_ruta)

    def _buscar_recursivo(self, actual, id_ruta):
        # Método recursivo que realiza la búsqueda en el árbol
        if not actual:  # Si el nodo actual es nulo, la ruta no existe
            return None
        if actual.ruta.id_ruta == id_ruta:  # Si el identificador coincide, retornar la ruta
            return actual.ruta
        if id_ruta < actual.ruta.id_ruta:  # Buscar en el subárbol izquierdo si es menor
            return self._buscar_recursivo(actual.izquierdo, id_ruta)
        else:  # Buscar en el subárbol derecho si es mayor
            return self._buscar_recursivo(actual.derecho, id_ruta)

    def eliminar(self, id_ruta):
        # Método para eliminar una ruta específica del árbol
        self.raiz = self._eliminar_recursivo(self.raiz, id_ruta)

    def _eliminar_recursivo(self, actual, id_ruta):
        # Método recursivo que elimina un nodo y reorganiza el árbol
        if not actual:  # Si el nodo actual no existe, retornar None
            return None
        if id_ruta < actual.ruta.id_ruta:  # Buscar en el subárbol izquierdo si es menor
            actual.izquierdo = self._eliminar_recursivo(actual.izquierdo, id_ruta)
        elif id_ruta > actual.ruta.id_ruta:  # Buscar en el subárbol derecho si es mayor
            actual.derecho = self._eliminar_recursivo(actual.derecho, id_ruta)
        else:  # Nodo encontrado
            if not actual.izquierdo:  # Si no tiene hijo izquierdo, retornar hijo derecho
                return actual.derecho
            if not actual.derecho:  # Si no tiene hijo derecho, retornar hijo izquierdo
                return actual.izquierdo

            # Caso con dos hijos: encontrar el nodo menor del subárbol derecho
            nodo_min = self._encontrar_min(actual.derecho)
            actual.ruta = nodo_min.ruta  # Reemplazar la ruta del nodo actual con la mínima
            actual.derecho = self._eliminar_recursivo(actual.derecho, nodo_min.ruta.id_ruta)
        return actual

    def _encontrar_min(self, actual):
        # Método auxiliar para encontrar el nodo con el valor mínimo en un subárbol
        while actual.izquierdo:  # Seguir descendiendo hacia la izquierda
            actual = actual.izquierdo
        return actual

    def generar_informe(self):
        # Método para generar un informe de todas las rutas ordenadas por identificador
        rutas = []
        self._inorden(self.raiz, rutas)  # Llenar la lista mediante un recorrido en inorden
        return rutas

    def _inorden(self, actual, rutas):
        # Método recursivo para realizar un recorrido en inorden
        if actual:
            self._inorden(actual.izquierdo, rutas)  # Recorrer subárbol izquierdo
            rutas.append(actual.ruta)  # Agregar la ruta actual a la lista
            self._inorden(actual.derecho, rutas)  # Recorrer subárbol derecho


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia del árbol binario
    arbol = ArbolBinarioRutas()

    # Agregar rutas al árbol
    arbol.agregar(Ruta(1, 50, 200))  # Ruta con ID 1
    arbol.agregar(Ruta(3, 30, 150))  # Ruta con ID 3
    arbol.agregar(Ruta(2, 40, 180))  # Ruta con ID 2

    # Buscar una ruta específica
    ruta = arbol.buscar(2)
    print("Ruta encontrada:", ruta)  # Mostrar la ruta encontrada

    # Generar un informe de todas las rutas ordenadas
    informe = arbol.generar_informe()
    print("\nInforme de rutas ordenadas:")
    for r in informe:
        print(r)

    # Eliminar una ruta del árbol
    arbol.eliminar(3)  # Eliminar la ruta con ID 3
    print("\nInforme tras eliminar la ruta con ID 3:")
    informe = arbol.generar_informe()
    for r in informe:
        print(r)