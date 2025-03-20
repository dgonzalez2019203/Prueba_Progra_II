from abc import ABC, abstractmethod

# Excepciones Personalizadas
class ValorNegativoError(Exception):
    """Excepción personalizada para valores negativos o cero."""
    pass

class Cliente(ABC):
    """Clase abstracta para representar un cliente."""
    
    def __init__(self, id_cliente, nombre, compras_promedio):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.validar_compras_promedio(compras_promedio)
        self.compras_promedio = compras_promedio

    @abstractmethod
    def obtener_tipo(self):
        """Método abstracto que será sobrescrito en las subclases."""
        pass
    
    def validar_compras_promedio(self, compras):
        if compras <= 0:
            raise ValorNegativoError("Error: La cantidad de compras promedio no puede ser negativa o cero.")

class ClientePresencial(Cliente):
    def obtener_tipo(self):
        return "Presencial"

class ClienteInternacional(Cliente):
    def obtener_tipo(self):
        return "Internacional"

class ClienteTelefono(Cliente):
    def obtener_tipo(self):
        return "Por Teléfono"

class ClienteEnLinea(Cliente):
    def obtener_tipo(self):
        return "En Línea"


def determinar_tipo_cliente(id_cliente, nombre, compras_promedio, tipo):
    """Determina el tipo de cliente y retorna la instancia correspondiente."""
    tipos_clientes = {
        "Presencial": ClientePresencial,
        "Internacional": ClienteInternacional,
        "Por Teléfono": ClienteTelefono,
        "En Línea": ClienteEnLinea
    }
    return tipos_clientes[tipo](id_cliente, nombre, compras_promedio)


def mostrar_reporte(clientes):
    """Muestra los datos de los clientes en formato de reporte."""
    print("\nReporte de Clientes:")
    print("="*40)
    for cliente in clientes:
        print(f"ID: {cliente.id_cliente}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Compras Promedio: {cliente.compras_promedio}")
        print(f"Tipo de Cliente: {cliente.obtener_tipo()}")
        print("-"*40)

# Solicitar datos al usuario
clientes = []
tipos = ["Presencial", "Internacional", "Por Teléfono", "En Línea"]
for i in range(5):
    try:
        id_cliente = input(f"Ingrese el ID del cliente {i+1}: ").strip()
        nombre = input(f"Ingrese el nombre del cliente {i+1}: ").strip()
        compras_promedio = float(input(f"Ingrese la cantidad de compras promedio del cliente {i+1}: "))
        print("Seleccione el tipo de cliente:")
        for idx, tipo in enumerate(tipos, start=1):
            print(f"{idx}. {tipo}")
        tipo_seleccionado = int(input("Ingrese el número del tipo de cliente: "))
        tipo_cliente = tipos[tipo_seleccionado - 1]

        cliente = determinar_tipo_cliente(id_cliente, nombre, compras_promedio, tipo_cliente)
        clientes.append(cliente)
    
    except ValorNegativoError as e:
        print(e)
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar valores numéricos para las compras promedio.")
    except IndexError:
        print("Error: Opción de tipo de cliente no válida.")

# Mostrar el reporte de clientes\mostrar_reporte(clientes)

mostrar_reporte(clientes)
