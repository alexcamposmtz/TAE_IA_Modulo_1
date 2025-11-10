# task_5.py
# Seccion 1. Practica de Programacion
# Alejandro Campos Martinez
# Team 6

"""
Task 5: Metodos Especiales
Crear una clase Book con atributos title y num_pages. Sobrescribir:
- __str__() para imprimir "Book: X, Pages: Y".
- __len__() para que len(book) devuelva el numero de paginas.
"""


class Book:
    """
    Clase que representa un libro.
    
    Atributos:
        title (str): Titulo del libro
        num_pages (int): Numero de paginas del libro
    """
    
    def __init__(self, title, num_pages):
        """
        Constructor de la clase Book.
        
        Parametros:
            title (str): Titulo del libro
            num_pages (int): Numero de paginas del libro
        """
        self.title = title
        self.num_pages = num_pages
    
    def __str__(self):
        """
        Metodo especial para representacion en string del objeto.
        
        Este metodo se llama automaticamente cuando usamos print() o str()
        sobre un objeto de tipo Book.
        
        Retorna:
            str: Representacion en formato "Book: X, Pages: Y"
        """
        return f"Book: {self.title}, Pages: {self.num_pages}"
    
    def __len__(self):
        """
        Metodo especial para obtener la longitud del objeto.
        
        Este metodo se llama automaticamente cuando usamos len()
        sobre un objeto de tipo Book.
        
        Retorna:
            int: Numero de paginas del libro
        """
        return self.num_pages
    
    def __repr__(self):
        """
        Metodo especial para representacion tecnica del objeto.
        
        Retorna:
            str: Representacion tecnica del objeto
        """
        return f"Book(title='{self.title}', num_pages={self.num_pages})"


if __name__ == "__main__":
    print("=" * 70)
    print("TASK 5: METODOS ESPECIALES - BOOK")
    print("=" * 70)
    
    print("\nLos metodos especiales (dunder methods) permiten que nuestras")
    print("clases se comporten como tipos de datos nativos de Python.")
    print()
    
    print("--- Creando libro 1 ---")
    book1 = Book("Cien Anos de Soledad", 417)
    
    print("\nUsando print() que internamente llama a __str__():")
    print(book1)
    
    print("\nUsando len() que internamente llama a __len__():")
    print(f"El libro tiene {len(book1)} paginas")
    
    print("\n" + "-" * 70)
    
    print("\n--- Creando libro 2 ---")
    book2 = Book("Don Quijote de la Mancha", 863)
    
    print("\nUsando print():")
    print(book2)
    
    print("\nUsando len():")
    print(f"El libro tiene {len(book2)} paginas")
    
    print("\n" + "-" * 70)
    
    print("\n--- Creando libro 3 ---")
    book3 = Book("El Principito", 96)
    
    print("\nUsando print():")
    print(book3)
    
    print("\nUsando len():")
    print(f"El libro tiene {len(book3)} paginas")
    
    print("\n" + "-" * 70)
    
    print("\n--- Comparacion de paginas ---")
    books = [book1, book2, book3]
    print("\nLista de libros:")
    for book in books:
        print(f"  - {book}")
    
    print("\nLibro mas largo:")
    longest_book = max(books, key=len)
    print(f"  {longest_book}")
    
    print("\nLibro mas corto:")
    shortest_book = min(books, key=len)
    print(f"  {shortest_book}")
