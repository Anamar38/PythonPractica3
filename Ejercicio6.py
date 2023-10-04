class Producto:
    # Constructor de clase
    def __init__(self, codigo, nombre, precio, año):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.año = año
        print('Se ha agregado el producto :', self.nombre)

    def __str__(self):
        return f"{self.nombre} - Código: {self.codigo}, Precio: ${self.precio}, Año: {self.año}"
    pass


class Catalogo:

    productos = []  # Esta lista contendrá objetos de la clase Producto

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar(self, producto):  
        self.productos.append(producto)

    def mostrar(self):
        for producto in self.productos:
            print(producto) 

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return productos_filtrados
    
    def filtrar_por_precio(self, precio_min, precio_max):
        productos_filtrados = [producto for producto in self.productos if precio_min <= producto.precio <= precio_max]
        return productos_filtrados

catalogo_autopartes = Catalogo()

# Agregar productos al catálogo
producto1 = Producto(123, "Asientos", 150.00, 2023)
producto2 = Producto(121, "Manijas", 80.00, 2021)
producto3 = Producto(223, "Cajuelas", 75.50, 2023)
producto4 = Producto(122, "Volantes", 100.50, 2022)

catalogo_autopartes.agregar(producto1)
catalogo_autopartes.agregar(producto2)
catalogo_autopartes.agregar(producto3)
catalogo_autopartes.agregar(producto4)

# Mostrar todo el catálogo
print("Catálogo completo:")
catalogo_autopartes.mostrar()

# Filtrar productos por año
año_filtro = 2023
productos_filtrados = catalogo_autopartes.filtrar_por_año(año_filtro)

print(f"\nProductos del año {año_filtro}:")
for producto in productos_filtrados:
    print(producto)

# Filtrar productos por precio
precio_min = 70.0
precio_max = 100.0
productos_filtrados_precio = catalogo_autopartes.filtrar_por_precio(precio_min, precio_max)

print(f"\nProductos con precio entre {precio_min} y {precio_max}:")
for producto in productos_filtrados_precio:
    print(producto)