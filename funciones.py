import tkinter as tk
from tkinter import messagebox
from importlib import import_module
from datetime import datetime

_entidades = import_module("entidades")

empresa = _entidades.empresa
lista_empresas = _entidades.lista_empresas

empleado = _entidades.empleado
lista_empleados = _entidades.lista_empleados

proyecto = _entidades.proyecto
lista_proyectos = _entidades.lista_proyectos

servicio = _entidades.servicio
lista_servicios = _entidades.lista_servicios

cita = _entidades.Cita
lista_citas = _entidades.lista_citas

# ==========================================
# UTILIDADES GENERALES
# ==========================================

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()


def limpiar_entries(*entries):
    for e in entries:
        e.delete(0, tk.END)


def poner_texto(entry, valor):
    entry.delete(0, tk.END)
    entry.insert(0, str(valor))


def llenar_tabla(tabla, datos, formato, filtro=""):
    tabla.delete(*tabla.get_children())

    encontrados = 0

    for i, elemento in enumerate(datos):
        if filtro in elemento.nombre.lower():
            tabla.insert("", tk.END, iid=str(i), values=formato(elemento))
            encontrados += 1

    return encontrados


def indice_real(tabla):
    seleccion = tabla.selection()

    if not seleccion:
        return None

    return int(seleccion[0])


def buscar_en_tabla(entry_busqueda, tabla, datos, formato):

    texto = entry_busqueda.get().strip().lower()

    encontrados = llenar_tabla(tabla, datos, formato, texto)

    if texto and encontrados == 0:

        messagebox.showinfo("Búsqueda", "No se encontraron coincidencias.")

        llenar_tabla(tabla, datos, formato)

# ==========================================
# VALIDACIÓN DE CITAS
# ==========================================

def fecha_valida(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def hora_valida(hora):
    hora = hora.strip().lower()
    hora = hora.replace(".", "")

    try:
        datetime.strptime(hora, "%I:%M %p")
        return True
    except ValueError:
        return False

def cliente_valido(cliente):
    return all(caracter.isalpha() or caracter.isspace() for caracter in cliente)

def _leer_cita(entry_cliente, entry_fecha, entry_hora,entry_motivo, entry_modalidad, entry_estado):

    cliente = entry_cliente.get().strip()
    fecha = entry_fecha.get().strip()
    hora = entry_hora.get().strip()
    motivo = entry_motivo.get("1.0", "end-1c").strip()
    modalidad = entry_modalidad.get().strip()
    estado = entry_estado.get().strip()

    if not cliente or not fecha or not hora or not motivo or not modalidad or not estado:
        messagebox.showwarning("Aviso", "Debe llenar todos los campos.")
        return None
    
    if not cliente_valido(cliente):
        messagebox.showwarning("Aviso", "El nombre del cliente no puede contener números ni símbolos.")
        return None

    if not fecha_valida(fecha):
        messagebox.showwarning("Aviso", "La fecha debe tener el formato DD/MM/AAAA y ser válida.")
        return None

    if not hora_valida(hora):
        messagebox.showwarning("Aviso", "Ingrese una hora válida. Ejemplo: 8:00 a.m.")
        return None

    if modalidad not in ("Presencial", "Virtual"):
        messagebox.showwarning("Aviso", "Seleccione una modalidad válida.")
        return None

    if estado not in ("Confirmada", "Completada", "Cancelada", "Pendiente"):
        messagebox.showwarning("Aviso", "Seleccione un estado válido.")
        return None

    return cliente, fecha, hora, motivo, modalidad, estado

# ==========================================
# VALIDACIÓN DE DATOS
# ==========================================

def _leer_empresa(entry_nombre, entry_area, entry_tamaño):

    nombre = entry_nombre.get().strip()
    area = entry_area.get().strip()
    tamaño = entry_tamaño.get().strip()

    if nombre == "" or area == "" or tamaño == "":
        messagebox.showwarning(
            "Aviso", "Debe llenar todos los campos.")
        return None
    
    if any(caracter.isdigit() for caracter in area) or any(caracter.isdigit() for caracter in tamaño):
        messagebox.showwarning("Aviso", "El área y el tamaño no pueden contener números.")
        return None

    return nombre, area, tamaño


def _leer_empleado(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario):

    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    edad = entry_edad.get().strip()
    puesto = entry_puesto.get().strip()
    salario = entry_salario.get().strip()

    if "" in (nombre, apellido, edad, puesto, salario):
        messagebox.showwarning("Aviso", "Debe llenar todos los campos.")
        return None

    if any(caracter.isdigit() for caracter in nombre) or any(caracter.isdigit() for caracter in apellido) or any(caracter.isdigit() for caracter in puesto):
        messagebox.showwarning("Aviso", "El nombre, el apellido y el puesto no pueden contener números.")
        return None

    try:
        edad = int(edad)
        salario = float(salario)

    except ValueError:
        messagebox.showwarning("Aviso", "Edad y salario deben ser números.")
        return None

    if edad < 0 or salario < 0:
        messagebox.showwarning("Aviso", "La edad y el salario no pueden ser negativos.")
        return None

    return nombre, apellido, edad, puesto, salario


def _leer_proyecto(entry_nombre, entry_descripcion, entry_presupuesto):

    nombre = entry_nombre.get().strip()
    descripcion = entry_descripcion.get().strip()
    presupuesto = entry_presupuesto.get().strip()

    if nombre == "" or descripcion == "" or presupuesto == "":
        messagebox.showwarning("Aviso", "Debe llenar todos los campos.")
        return None

    if any(caracter.isdigit() for caracter in nombre):
        messagebox.showwarning("Aviso", "El nombre no debe conetener números")
        return None

    try:
        presupuesto = float(presupuesto)

    except ValueError:
        messagebox.showwarning("Aviso", "El presupuesto debe ser un número.")
        return None

    if presupuesto < 0:
        messagebox.showwarning("Aviso", "El presupuesto no puede ser negativo.")
        return None

    return nombre, descripcion, presupuesto


def _leer_servicio(entry_nombre, entry_descripcion, entry_precio):

    nombre = entry_nombre.get().strip()
    descripcion = entry_descripcion.get().strip()
    precio = entry_precio.get().strip()

    if nombre == "" or descripcion == "" or precio == "":
        messagebox.showwarning("Aviso", "Debe llenar todos los campos.")
        return None

    if any(caracter.isdigit() for caracter in nombre):
        messagebox.showwarning("Aviso", "El nombre no debe conetener números")
        return None
    
    try:
        precio = float(precio)

    except ValueError:
        messagebox.showerror("Error", "El precio debe ser un número.")
        return None

    if precio < 0:
        messagebox.showerror("Error", "El precio no puede ser negativo.")
        return None

    return nombre, descripcion, precio

# ==========================================
# EMPRESA
# ==========================================

def formato_empresa(p):

    return (
        p.nombre,
        p.area,
        p.tamaño
        )


def listar_empresas(tabla):

    llenar_tabla(tabla, lista_empresas, formato_empresa)


def crear_empresa(entry_nombre, entry_area, entry_tamaño, tabla):

    datos = _leer_empresa(entry_nombre, entry_area, entry_tamaño)

    if datos is None:
        return

    if datos[0].lower() in [e.nombre.lower() for e in lista_empresas]:  
        messagebox.showwarning("Aviso", "Ya existe una empresa con ese nombre.")
        return

    lista_empresas.append(empresa(*datos))

    limpiar_entries(entry_nombre, entry_area, entry_tamaño)

    listar_empresas(tabla)


def actualizar_empresa(entry_nombre, entry_area, entry_tamaño, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione una empresa de la lista.")
        return

    datos = _leer_empresa(entry_nombre, entry_area, entry_tamaño)

    if datos is None:
        return

    e = lista_empresas[index]

    if datos[0].lower() in [e.nombre.lower() for i, e in enumerate(lista_empresas) if i != index]:
        messagebox.showwarning("Aviso", "Ya existe una empresa con ese nombre.")
        return

    e.nombre, e.area, e.tamaño = datos

    limpiar_entries(entry_nombre, entry_area, entry_tamaño)

    listar_empresas(tabla)

def eliminar_empresa( entry_nombre, entry_area, entry_tamaño, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione una empresa de la lista.")
        return

    del lista_empresas[index]

    limpiar_entries(entry_nombre, entry_area, entry_tamaño)

    listar_empresas(tabla)


def seleccionar_empresas(event, tabla, entry_nombre, entry_area, entry_tamaño):

    index = indice_real(tabla)

    if index is None:
        return

    p = lista_empresas[index]

    poner_texto(entry_nombre, p.nombre)
    poner_texto(entry_area, p.area)
    poner_texto(entry_tamaño, p.tamaño)


def buscar_empresas(entry_busqueda, tabla):

    buscar_en_tabla(entry_busqueda, tabla, lista_empresas, formato_empresa)


# ==========================================
# EMPLEADO
# ==========================================

def formato_empleado(p):

    return (
        p.nombre,
        p.apellido,
        p.edad,
        p.puesto,
        f"C${p.salario:,.2f}"
    )


def listar_empleados(tabla):

    llenar_tabla(tabla, lista_empleados, formato_empleado)


def crear_empleado(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario, tabla):

    datos = _leer_empleado(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario)

    if datos is None:
        return

    lista_empleados.append(empleado(*datos))

    limpiar_entries(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario)

    listar_empleados(tabla)


def actualizar_empleado(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione un empleado de la lista.")
        return

    datos = _leer_empleado(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario)

    if datos is None:
        return

    e = lista_empleados[index]

    e.nombre, e.apellido, e.edad, e.puesto, e.salario = datos

    limpiar_entries(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario)

    listar_empleados(tabla)


def eliminar_empleado(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione un empleado de la lista.")
        return

    del lista_empleados[index]

    limpiar_entries(entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario)

    listar_empleados(tabla)


def seleccionar_empleado(event, tabla, entry_nombre, entry_apellido, entry_edad, entry_puesto, entry_salario):

    index = indice_real(tabla)

    if index is None:
        return

    p = lista_empleados[index]

    poner_texto(entry_nombre, p.nombre)
    poner_texto(entry_apellido, p.apellido)
    poner_texto(entry_edad, p.edad)
    poner_texto(entry_puesto, p.puesto)
    poner_texto(entry_salario, p.salario)


def buscar_empleado(entry_busqueda, tabla):

    buscar_en_tabla(entry_busqueda, tabla, lista_empleados, formato_empleado)


# ==========================================
# PROYECTO
# ==========================================

def formato_proyecto(p):

    return (
        p.nombre,
        p.descripcion,
        f"C${p.presupuesto:,.2f}"
    )


def listar_proyectos(tabla):

    llenar_tabla(tabla, lista_proyectos, formato_proyecto)


def crear_proyecto( entry_nombre,entry_descripcion,entry_presupuesto,tabla):

    datos = _leer_proyecto(entry_nombre, entry_descripcion, entry_presupuesto)

    if datos is None:
        return

    if datos[0].lower() in [e.nombre.lower() for e in lista_proyectos]:  
        messagebox.showwarning("Aviso", "Ya existe un proyecto con ese nombre.")
        return
    
    lista_proyectos.append(proyecto(*datos))

    limpiar_entries(entry_nombre, entry_descripcion, entry_presupuesto)

    listar_proyectos(tabla)


def actualizar_proyecto(entry_nombre, entry_descripcion, entry_presupuesto, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione un proyecto de la lista.")
        return

    datos = _leer_proyecto(entry_nombre, entry_descripcion, entry_presupuesto)

    if datos is None:
        return

    if datos[0].lower() in [e.nombre.lower() for i, e in enumerate(lista_proyectos) if i != index]:
        messagebox.showwarning("Aviso", "Ya existe un proyecto con ese nombre.")
        return
    
    p = lista_proyectos[index]

    p.nombre, p.descripcion, p.presupuesto = datos

    limpiar_entries(entry_nombre, entry_descripcion, entry_presupuesto)

    listar_proyectos(tabla)


def eliminar_proyecto(entry_nombre, entry_descripcion, entry_presupuesto, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione un proyecto de la lista.")
        return

    del lista_proyectos[index]

    limpiar_entries(entry_nombre, entry_descripcion, entry_presupuesto)

    listar_proyectos(tabla)


def seleccionar_proyecto(event, tabla, entry_nombre, entry_descripcion, entry_presupuesto):

    index = indice_real(tabla)

    if index is None:
        return

    p = lista_proyectos[index]

    poner_texto(entry_nombre, p.nombre)
    poner_texto(entry_descripcion, p.descripcion)
    poner_texto(entry_presupuesto, p.presupuesto)


def buscar_proyecto(entry_busqueda, tabla):

    buscar_en_tabla(entry_busqueda, tabla, lista_proyectos, formato_proyecto)


# ==========================================
# SERVICIO
# ==========================================

def formato_servicio(p):

    return (
        p.nombre,
        p.descripcion,
        f"C${p.precio:,.2f}"
    )


def listar_servicios(tabla):

    llenar_tabla(tabla, lista_servicios, formato_servicio) 


def crear_servicio(entry_nombre, entry_descripcion, entry_precio, tabla):

    datos = _leer_servicio(entry_nombre, entry_descripcion, entry_precio)

    if datos is None:
        return

    if datos[0].lower() in [e.nombre.lower() for e in lista_servicios]:  
        messagebox.showwarning("Aviso", "Ya existe un servicio con ese nombre.")
        return
    
    lista_servicios.append(servicio(*datos))

    limpiar_entries( entry_nombre, entry_descripcion, entry_precio)

    listar_servicios(tabla)


def actualizar_servicio(entry_nombre, entry_descripcion, entry_precio, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione un servicio de la lista.")
        return

    datos = _leer_servicio(entry_nombre, entry_descripcion, entry_precio)

    if datos is None:
        return

    if datos[0].lower() in [e.nombre.lower() for i, e in enumerate(lista_servicios) if i != index]:
        messagebox.showwarning("Aviso", "Ya existe un servicio con ese nombre.")
        return
    
    s = lista_servicios[index]

    s.nombre, s.descripcion, s.precio = datos

    limpiar_entries(entry_nombre, entry_descripcion, entry_precio)

    listar_servicios(tabla)


def eliminar_servicio(entry_nombre, entry_descripcion, entry_precio, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione un servicio de la lista.")
        return

    del lista_servicios[index]

    limpiar_entries(entry_nombre, entry_descripcion, entry_precio)

    listar_servicios(tabla)


def seleccionar_servicio(event, tabla, entry_nombre, entry_descripcion, entry_precio):

    index = indice_real(tabla)

    if index is None:
        return

    p = lista_servicios[index]

    poner_texto(entry_nombre, p.nombre)
    poner_texto(entry_descripcion, p.descripcion)
    poner_texto(entry_precio, p.precio)


def buscar_servicio(entry_busqueda, tabla):

    buscar_en_tabla( entry_busqueda, tabla, lista_servicios, formato_servicio)

# ==========================================
# CITAS
# ==========================================

def formato_cita(p):
    return ( p.cliente, p.fecha, p.hora, p.motivo, p.modalidad, p.estado)


def listar_citas(tabla):

    tabla.delete(*tabla.get_children())

    for i, elemento in enumerate(lista_citas):
        tabla.insert("", tk.END, iid=str(i), values=formato_cita(elemento))

def crear_cita(entry_cliente, entry_fecha, entry_hora, entry_motivo, entry_modalidad, entry_estado, tabla):

    datos = _leer_cita(entry_cliente, entry_fecha, entry_hora, entry_motivo, entry_modalidad, entry_estado
    )

    if datos is None:
        return

    lista_citas.append(cita(*datos))

    limpiar_entries(entry_cliente, entry_fecha, entry_hora)

    entry_motivo.delete("1.0", tk.END)
    entry_modalidad.set("")
    entry_estado.set("")

    listar_citas(tabla)

def actualizar_cita(entry_cliente, entry_fecha, entry_hora, entry_motivo, entry_modalidad, entry_estado, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione una cita de la lista.")
        return

    datos = _leer_cita(entry_cliente, entry_fecha, entry_hora, entry_motivo, entry_modalidad, entry_estado)

    if datos is None:
        return

    c = lista_citas[index]

    c.cliente, c.fecha, c.hora, c.motivo, c.modalidad, c.estado = datos

    limpiar_entries(entry_cliente, entry_fecha, entry_hora)

    entry_motivo.delete("1.0", tk.END)
    entry_modalidad.set("")
    entry_estado.set("")

    listar_citas(tabla)

def eliminar_cita(entry_cliente, entry_fecha, entry_hora, entry_motivo, entry_modalidad, entry_estado, tabla):

    index = indice_real(tabla)

    if index is None:
        messagebox.showwarning("Aviso", "Seleccione una cita de la lista.")
        return

    del lista_citas[index]

    limpiar_entries(entry_cliente, entry_fecha, entry_hora)

    entry_motivo.delete("1.0", tk.END)
    entry_modalidad.set("")
    entry_estado.set("")

    listar_citas(tabla)

def seleccionar_cita(event, tabla, entry_cliente, entry_fecha, entry_hora, entry_motivo, entry_modalidad, entry_estado):

    index = indice_real(tabla)

    if index is None:
        return

    c = lista_citas[index]

    poner_texto(entry_cliente, c.cliente)
    poner_texto(entry_fecha, c.fecha)
    poner_texto(entry_hora, c.hora)

    entry_motivo.delete("1.0", tk.END)
    entry_motivo.insert("1.0", c.motivo)

    entry_modalidad.set(c.modalidad)
    entry_estado.set(c.estado)

def buscar_citas(entry_busqueda, tabla):

    texto = entry_busqueda.get().strip().lower()

    tabla.delete(*tabla.get_children())

    encontrados = 0
    for i, c in enumerate(lista_citas):
        if texto in c.cliente.lower():
            tabla.insert("", tk.END, iid=str(i), values=formato_cita(c))
            encontrados += 1

    if texto and encontrados == 0:
        messagebox.showinfo("Búsqueda", "No se encontraron coincidencias.")
        listar_citas(tabla)