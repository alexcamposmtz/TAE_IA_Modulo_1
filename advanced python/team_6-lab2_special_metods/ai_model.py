"""
Lab 2: Special Methods (__init__, __str__, etc.)
Advanced Python - CINVESTAV Guadalajara
Team 6
Alejandro Campos Martínez
Agustín Jaime Navarro

Este módulo implementa una clase AIModel que demuestra el uso
de special methods (dunder methods) en Python para crear objetos
que se comportan de manera intuitiva e integrada con la sintaxis de Python.
"""


class AIModel:
    """
    Clase que representa un modelo de Inteligencia Artificial.    
    Esta clase implementa diversos special methods para demostrar cómo
    los objetos personalizados pueden integrarse con la sintaxis nativa
    de Python.    
    Attributes:
        name (str): Nombre del modelo de IA
        score (int/float): Puntuación de rendimiento del modelo
        active (bool): Estado de activación del modelo
    """
    
    def __init__(self, name, score, active=True):
        """
        Inicializa una nueva instancia de AIModel.        
        __init__ es llamado después de que __new__() crea la instancia,
        pero antes de que sea retornada al llamador. Se usa para
        personalizar el objeto recién creado.        
        Args:
            name (str): Nombre del modelo
            score (int/float): Puntuación del modelo
            active (bool): Estado inicial (por defecto True)
        """
        self.name = name
        self.score = score
        self.active = active
        print(f"[INIT] AIModel '{self.name}' initialized with score {self.score}")
    
    def __repr__(self):
        """
        Retorna la representación del objeto.        
        __repr__ debe retornar una cadena que idealmente sea código Python
        válido que pueda recrear el objeto. Se usa para debugging y desarrollo.
        Cuando no hay __str__, __repr__ se usa también para print().        
        Returns:
            str: Representación oficial del objeto
        """
        return f"AIModel('{self.name}', {self.score}, active={self.active})"
    
    def __str__(self):
        """
        Retorna la representación del objeto.        
        __str__ debe retornar una cadena legible y amigable para el usuario.
        Es llamado por str(), print() y format().        
        Returns:
            str: Representación amigable del objeto
        """
        status = "active" if self.active else "inactive"
        return f"Model '{self.name}' with score {self.score} ({status})"
    
    def __add__(self, other):
        """
        Define el comportamiento del operador +.        
        Permite sumar dos modelos, combinando sus scores.
        Se llama cuando usamos: model1 + model2        
        Args:
            other (AIModel): Otro modelo para sumar            
        Returns:
            int/float: Suma de los scores de ambos modelos
        """
        if not isinstance(other, AIModel):
            return NotImplemented
        return self.score + other.score
    
    def __lt__(self, other):
        """
        Define el comportamiento del operador < (less than).        
        Compara modelos basándose en sus scores.
        Se llama cuando usamos: model1 < model2        
        Args:
            other (AIModel): Otro modelo para comparar            
        Returns:
            bool: True si este modelo tiene menor score
        """
        if not isinstance(other, AIModel):
            return NotImplemented
        return self.score < other.score
    
    def __le__(self, other):
        """
        Define el comportamiento del operador <= (less than or equal).        
        Args:
            other (AIModel): Otro modelo para comparar            
        Returns:
            bool: True si este modelo tiene menor o igual score
        """
        if not isinstance(other, AIModel):
            return NotImplemented
        return self.score <= other.score
    
    def __gt__(self, other):
        """
        Define el comportamiento del operador > (greater than).        
        Compara modelos basándose en sus scores.
        Se llama cuando usamos: model1 > model2        
        Args:
            other (AIModel): Otro modelo para comparar            
        Returns:
            bool: True si este modelo tiene mayor score
        """
        if not isinstance(other, AIModel):
            return NotImplemented
        return self.score > other.score
    
    def __ge__(self, other):
        """
        Define el comportamiento del operador >= (greater than or equal).        
        Args:
            other (AIModel): Otro modelo para comparar            
        Returns:
            bool: True si este modelo tiene mayor o igual score
        """
        if not isinstance(other, AIModel):
            return NotImplemented
        return self.score >= other.score
    
    def __eq__(self, other):
        """
        Define el comportamiento del operador == (equal).        
        Dos modelos son iguales si tienen el mismo score.        
        Args:
            other (AIModel): Otro modelo para comparar            
        Returns:
            bool: True si ambos modelos tienen el mismo score
        """
        if not isinstance(other, AIModel):
            return NotImplemented
        return self.score == other.score
    
    def __ne__(self, other):
        """
        Define el comportamiento del operador != (not equal).        
        Args:
            other (AIModel): Otro modelo para comparar            
        Returns:
            bool: True si los modelos tienen diferentes scores
        """
        if not isinstance(other, AIModel):
            return NotImplemented
        return self.score != other.score
    
    def __call__(self, input_text):
        """
        Hace que el objeto sea "callable" (se pueda llamar como función).        
        Permite usar la sintaxis: model("texto") en lugar de model.process("texto")
        Es útil para crear objetos que actúan como funciones.        
        Args:
            input_text (str): Texto de entrada para procesar            
        Returns:
            str: Texto procesado por el modelo
        """
        if not self.active:
            return f"[ERROR] Model '{self.name}' is not active"
        return f"{self.name} processed: '{input_text}'"
    
    def __bool__(self):
        """
        Define el comportamiento en contextos booleanos.        
        Permite usar el modelo en condiciones if, while, etc.
        Se llama cuando usamos: bool(model), if model:, while model:        
        Returns:
            bool: True si el modelo está activo, False si no
        """
        return self.active
    
    def __del__(self):
        """
        Destructor - llamado cuando el objeto está a punto de ser destruido.        
        Se llama cuando no quedan referencias al objeto o se usa del.
        Útil para limpieza de recursos (cerrar archivos, conexiones, etc.) 
        """
        print(f"[CLEANUP] Model '{self.name}' is being deleted")


def main():
    """
    Función principal que demuestra todos los special methods.
    """
    print("=" * 80)
    print("Lab 2: Special Methods - AIModel Implementation")
    print("=" * 80)
    print()
    
    # Test 1: __init__ - Inicialización
    print("Test 1: __init__ - Inicialización de Objetos")
    print("-" * 80)
    model1 = AIModel("gpt", 90)
    model2 = AIModel("bert", 85)
    model3 = AIModel("Inactive-Model", 70, active=False)
    print()
    
    # Test 2: __str__ - Representación en string
    print("Test 2: __str__ - Representación amigable para el usuario")
    print("-" * 80)
    print(f"model1: {model1}")
    print(f"model2: {model2}")
    print(f"model3: {model3}")
    print()
    
    # Test 3: __repr__ - Representación oficial
    print("Test 3: __repr__ - Representación para debugging")
    print("-" * 80)
    print(f"repr(model1): {repr(model1)}")
    print(f"repr(model2): {repr(model2)}")
    print()
    
    # Test 4: __add__ - Operador de suma
    print("Test 4: __add__ - Suma de modelos")
    print("-" * 80)
    combined_score = model1 + model2
    print(f"model1 + model2 = {combined_score}")
    print(f"Puntuación combinada de gpt y bert: {combined_score}")
    print()
    
    # Test 5: Operadores de comparación (__lt__, __gt__, __eq__)
    print("Test 5: Operadores de comparación")
    print("-" * 80)
    print(f"model1 > model2: {model1 > model2}")
    print(f"model1 < model2: {model1 < model2}")
    print(f"model1 == model2: {model1 == model2}")
    print(f"model1 >= model2: {model1 >= model2}")
    print(f"model1 != model2: {model1 != model2}")
    print()
    
    # Test 6: Ordenamiento usando métodos de comparación
    print("Test 6: Ordenamiento de modelos usando métodos de comparación")
    print("-" * 80)
    models = [model1, model2, model3]
    print("Antes de ordenar:")
    for m in models:
        print(f"  - {m}")
    
    sorted_models = sorted(models, reverse=True)
    print("\nDespués de ordenar (descendente por puntuación):")
    for m in sorted_models:
        print(f"  - {m}")
    print()
    
    # Test 7: __call__ - Objeto callable
    print("Test 7: __call__ - Comportamiento callable")
    print("-" * 80)
    result1 = model1("Traducir este texto al español")
    result2 = model2("Clasificar este sentimiento")
    result3 = model3("Esto debería fallar - el modelo está inactivo")
    print(result1)
    print(result2)
    print(result3)
    print()
    
    # Test 8: __bool__ - Contexto booleano
    print("Test 8: __bool__ - Evaluación booleana")
    print("-" * 80)
    print(f"bool(model1): {bool(model1)} - model1 está {'activo' if model1 else 'inactivo'}")
    print(f"bool(model2): {bool(model2)} - model2 está {'activo' if model2 else 'inactivo'}")
    print(f"bool(model3): {bool(model3)} - model3 está {'activo' if model3 else 'inactivo'}")
    print()
    
    # Usando modelos en declaraciones if
    print("Usando modelos en declaraciones condicionales:")
    if model1:
        print(f"{model1.name} está listo para usar")
    
    if not model3:
        print(f"{model3.name} no está activo y no se puede usar")
    print()
    
    # Test 9: __del__ - Limpieza
    print("Test 9: __del__ - Eliminación de objetos y limpieza")
    print("-" * 80)
    print("Eliminando model2...")
    del model2
    print("model2 ha sido eliminado")
    print()
    
    # Crear y eliminar inmediatamente
    print("Creando un modelo temporal...")
    temp_model = AIModel("TempModel", 50)
    print("Eliminando modelo temporal...")
    del temp_model
    print()
    
    print("=" * 80)
    print("¡Todas las pruebas completadas!")
    print("Nota: Los modelos restantes se limpiarán cuando el programa termine")
    print("=" * 80)


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Solo se ejecuta cuando el script se ejecuta directamente,
    no cuando es importado como módulo.
    """
    main()