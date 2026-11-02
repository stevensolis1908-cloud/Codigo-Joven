import dataclasses


@dataclasses.dataclass
class empresa:
    nombre: str
    area: str
    tamaño: str


lista_empresas = [
    empresa(
        nombre="TecnoNica", 
        area="Tecnología", 
        tamaño="Grande"),
    empresa(
        nombre="Farmacia Esperanza",
        area="Salud",
        tamaño="Mediana"
    ),
    empresa(
        nombre="La esquina",
        area="Comercio",
        tamaño="Pequeña"
    )
]


@dataclasses.dataclass
class empleado:
    nombre: str
    apellido: str
    edad: int
    puesto: str
    salario: float


lista_empleados = [
    empleado(
        nombre="Sophia",
        apellido="Ponce",
        edad=30,
        puesto="Diseñadora",
        salario=16000.0
    ),
    empleado(
        nombre="Lisbeth",
        apellido="Chow",
        edad=28,
        puesto="Gerente",
        salario=25000.0
    ),
    empleado(
        nombre="Isaias",
        apellido="Solis",
        edad=35,
        puesto="Desarrollador",
        salario=22000.0
    ),
    empleado(
        nombre="Marcello",
        apellido="Martinez",
        edad=24,
        puesto="Atención al cliente",
        salario=9000.0
    ),
    empleado(
        nombre="Dayana",
        apellido="Sanchez",
        edad=42,
        puesto="Analista de datos",
        salario=20000.0
    )
]


@dataclasses.dataclass
class proyecto:
    nombre: str
    descripcion: str
    presupuesto: float


lista_proyectos=[
     proyecto(
        nombre="Sistema de predicción mediante Machine Learning",
        descripcion="Desarrollo de un sistema que utiliza datos históricos para realizar predicciones que ayuden a la empresa en la toma de decisiones.",
        presupuesto=80000.0
    ),
    proyecto(
        nombre="Análisis de datos de ventas",
        descripcion="Análisis de las ventas de medicamentos para identificar cuáles tienen mayor demanda y mejorar el control de inventario.",
        presupuesto=25000.0
    ),
    proyecto(
        nombre="Sistema de ventas e inventario",
        descripcion="Desarrollo de un sistema para registrar las ventas y controlar los productos disponibles en el negocio.",
        presupuesto=45000.0
    )
]

@dataclasses.dataclass
class servicio:
    nombre: str
    descripcion: str
    precio: float

lista_servicios = []

@dataclasses.dataclass
class Cita:
    cliente: str
    fecha: str
    hora: str
    motivo: str 
    modalidad: str
    estado: str

lista_citas = []