class book: 
    def __init__(self, title, autohor):
        self.title = title
        self.author = autohor
        self.available = True

        def borrow(self): 
            if self.available:
                self.available = False
                print("El libro de Ronaldo {self.title} ha sido prestado")
            else 
                print(f"El libro {self.title} no esta disponible")
        
        def return_book(self):
            self.aviable = True
            print(f"El libro {self.title} ha sido devuelto")

