import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from importlib import import_module


_funciones = import_module("funciones")

limpiar_ventana = _funciones.limpiar_ventana

# EMPRESA
crear_empresa = _funciones.crear_empresa
actualizar_empresa = _funciones.actualizar_empresa
eliminar_empresa = _funciones.eliminar_empresa
listar_empresas = _funciones.listar_empresas
buscar_empresas = _funciones.buscar_empresas
seleccionar_empresas = _funciones.seleccionar_empresas

# EMPLEADO
crear_empleado = _funciones.crear_empleado
actualizar_empleado = _funciones.actualizar_empleado
eliminar_empleado = _funciones.eliminar_empleado
listar_empleados = _funciones.listar_empleados
buscar_empleado = _funciones.buscar_empleado
seleccionar_empleado = _funciones.seleccionar_empleado

# PROYECTO
crear_proyecto = _funciones.crear_proyecto
actualizar_proyecto = _funciones.actualizar_proyecto
eliminar_proyecto = _funciones.eliminar_proyecto
listar_proyectos = _funciones.listar_proyectos
buscar_proyecto = _funciones.buscar_proyecto
seleccionar_proyecto = _funciones.seleccionar_proyecto

# SERVICIO
crear_servicio = _funciones.crear_servicio
actualizar_servicio = _funciones.actualizar_servicio
eliminar_servicio = _funciones.eliminar_servicio
listar_servicios = _funciones.listar_servicios
buscar_servicio = _funciones.buscar_servicio
seleccionar_servicio = _funciones.seleccionar_servicio

# CITAS
crear_cita = _funciones.crear_cita
actualizar_cita = _funciones.actualizar_cita
eliminar_cita = _funciones.eliminar_cita
listar_citas = _funciones.listar_citas
buscar_citas = _funciones.buscar_citas
seleccionar_cita = _funciones.seleccionar_cita

# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================

TAM = 16
TAM_LISTA = 15

FUENTE = ("Arial", TAM)
FUENTE_TITULO = ("Arial", TAM + 3, "bold")


# ==========================================
# COMPONENTES REUTILIZABLES
# ==========================================

def cerrar_sesion(ventana):
    vista_login(ventana)

def ir_a(ventana, vista):
    ventana.after(200, lambda: vista(ventana))

def barra_navegacion(ventana):
    opc = ctk.CTkFrame(ventana, fg_color="transparent")
    opc.pack(side="top", fill="x", padx=10, pady=8)

    ctk.CTkButton(opc, text="Empresas", width=110, height=36, font=FUENTE, command=lambda: ir_a(ventana, vista_empresa)).grid(row=0, column=0, padx=3)

    ctk.CTkButton(opc, text="Empleados", width=110, height=36, font=FUENTE, command=lambda: ir_a(ventana, vista_empleado)).grid(row=0, column=1, padx=3)

    ctk.CTkButton(opc, text="Proyectos", width=110, height=36, font=FUENTE, command=lambda: ir_a(ventana, vista_proyecto)).grid(row=0, column=2, padx=3)

    ctk.CTkButton(opc, text="Servicios", width=110, height=36, font=FUENTE, command=lambda: ir_a(ventana, vista_servicio)
    ).grid(row=0, column=3, padx=3)

    ctk.CTkButton(opc, text="Citas", width=110, height=36, font=FUENTE, command=lambda: ir_a(ventana, vista_cita)).grid(row=0, column=4, padx=3)

    ctk.CTkButton(opc, text="Cerrar sesión", width=130, height=36, font=FUENTE, fg_color="#c0392b", hover_color="#962d22", command=lambda: ir_a(ventana, cerrar_sesion)).grid(row=0, column=5, padx=(30, 3))

def crear_formulario(ventana, titulo, etiquetas):

    frame = ctk.CTkFrame(ventana)
    frame.pack(fill="x", padx=10, pady=10)

    ctk.CTkLabel(frame, text=titulo, font=FUENTE_TITULO).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(8, 4))

    entries = []

    for i, texto in enumerate(etiquetas, start=1):

        ctk.CTkLabel(frame, text=texto, font=FUENTE).grid(row=i, column=0, sticky="e", padx=(10, 5), pady=3)

        entry = ctk.CTkEntry(frame, width=320, height=34, font=FUENTE)
        entry.grid(row=i, column=1, sticky="w", pady=3)
        entries.append(entry)
    return frame, entries, len(etiquetas) + 1

def crear_botones(frame, fila, f_crear, f_actualizar, f_eliminar):
    frame_botones = ctk.CTkFrame(frame, fg_color="transparent")
    frame_botones.grid(row=fila, column=0, columnspan=2, pady=10)

    ctk.CTkButton(frame_botones, text="Crear", width=110, height=34, font=FUENTE, command=f_crear).grid(row=0, column=0, padx=3)

    ctk.CTkButton(frame_botones, text="Actualizar", width=110, height=34, font=FUENTE, command=f_actualizar).grid(row=0, column=1, padx=3)

    ctk.CTkButton(frame_botones, text="Eliminar", width=110, height=34, font=FUENTE, fg_color="#c0392b", hover_color="#962d22", command=f_eliminar).grid(row=0, column=2, padx=3)

def crear_busqueda(ventana, f_buscar):

    ctk.CTkLabel(ventana, text="Buscar por nombre:", font=FUENTE).pack( anchor="w", padx=12, pady=(10, 2))

    frame_busqueda = ctk.CTkFrame(ventana, fg_color="transparent")

    frame_busqueda.pack(anchor="w", padx=10)

    entry_busqueda = ctk.CTkEntry( frame_busqueda,width=300,height=34,font=FUENTE)

    entry_busqueda.grid( row=0,column=0,padx=3)

    ctk.CTkButton(frame_busqueda, text="Buscar", width=110, height=34, font=FUENTE, command=lambda: f_buscar(entry_busqueda)).grid( row=0, column=1, padx=3)

    entry_busqueda.bind("<Return>", lambda event: f_buscar(entry_busqueda))

def crear_tabla(ventana, columnas, encabezados, anchos):

    estilo = ttk.Style()

    estilo.configure("Treeview", font=("Arial", TAM_LISTA), rowheight=TAM_LISTA * 2 + 4)

    estilo.configure("Treeview.Heading", font=("Arial", TAM_LISTA, "bold"))

    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=8, selectmode="browse")

    for columna, encabezado, ancho in zip(columnas, encabezados, anchos):

        tabla.heading(columna, text=encabezado)

        tabla.column(columna, width=ancho, minwidth=70, stretch=True)

    tabla.pack(fill="both", expand=True, padx=10, pady=10)
    return tabla

# ==========================================
# VISTA LOGIN
# ==========================================

USUARIOS = {
    "admin": "1234",
    "codigojoven": "joven2026",
}

def vista_login(ventana):
    limpiar_ventana(ventana)

    ventana.title("Código Joven - Iniciar sesión")
    ventana.geometry("400x480")

    frame = ctk.CTkFrame(ventana, corner_radius=15)
    frame.pack(expand=True, fill="both", padx=30, pady=30)

    ctk.CTkLabel(frame, text="Código Joven", font=ctk.CTkFont(size=26, weight="bold")).pack(pady=(40, 5))

    ctk.CTkLabel(frame, text="Sistema de Gestión", font=ctk.CTkFont(size=14)).pack(pady=(0, 25))

    entry_usuario = ctk.CTkEntry(frame, placeholder_text="Usuario", width=240, height=38)
    entry_usuario.pack(pady=8)

    entry_clave = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="*", width=240, height=38)
    entry_clave.pack(pady=8)

    def iniciar_sesion(event=None):
        usuario = entry_usuario.get().strip()
        clave = entry_clave.get()

        if not usuario or not clave:
            messagebox.showwarning("Campos vacíos", "Ingresa usuario y contraseña.")
            return

        if USUARIOS.get(usuario) == clave:
            ventana.title("Sistema de Gestión de Código Joven")
            ventana.geometry("1000x700")
            ventana.after(200, lambda: vista_empresa(ventana))

        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
            entry_clave.delete(0, "end")

    ctk.CTkButton(frame, text="Iniciar sesión", width=240, height=40, command=iniciar_sesion).pack(pady=(25, 10))

    entry_usuario.bind("<Return>", iniciar_sesion)
    entry_clave.bind("<Return>", iniciar_sesion)

    entry_usuario.focus()

# ==========================================
# VISTA EMPRESA
# ==========================================

def vista_empresa(ventana):

    limpiar_ventana(ventana)

    barra_navegacion(ventana)

    frame, (entry_nombre, entry_area, entry_tamaño), fila = crear_formulario(ventana,"Datos de la Empresa", ["Nombre:", "Área:", "Tamaño:"])

    crear_botones(
        frame,
        fila,
        lambda: crear_empresa(
            entry_nombre,
            entry_area,
            entry_tamaño,
            tabla
        ),
        lambda: actualizar_empresa(
            entry_nombre,
            entry_area,
            entry_tamaño,
            tabla
        ),
        lambda: eliminar_empresa(
            entry_nombre,
            entry_area,
            entry_tamaño,
            tabla
        )
    )

    crear_busqueda(ventana, lambda e: buscar_empresas(e, tabla))

    tabla = crear_tabla(
        ventana,
        ("nombre", "area", "tamaño"),
        ("Nombre", "Área", "Tamaño"),
        (200, 200, 200)
    )

    tabla.bind("<<TreeviewSelect>>", lambda event: seleccionar_empresas(event, tabla, entry_nombre, entry_area, entry_tamaño))

    listar_empresas(tabla)

# ==========================================
# VISTA EMPLEADO
# ==========================================

def vista_empleado(ventana):

    limpiar_ventana(ventana)

    barra_navegacion(ventana)

    frame, campos, fila = crear_formulario(ventana, "Datos del Empleado", ["Nombre:","Apellido:","Edad:","Puesto:","Salario (C$):"])

    crear_botones(
        frame,
        fila,
        lambda: crear_empleado(*campos, tabla),
        lambda: actualizar_empleado(*campos, tabla),
        lambda: eliminar_empleado(*campos, tabla)
    )

    crear_busqueda(ventana, lambda e: buscar_empleado(e, tabla))

    tabla = crear_tabla(
        ventana,
        ("nombre", "apellido", "edad", "puesto", "salario"),
        ("Nombre", "Apellido", "Edad", "Puesto", "Salario"),
        (150, 150, 80, 250, 150)
    )

    tabla.bind("<<TreeviewSelect>>", lambda event: seleccionar_empleado(event, tabla, *campos))

    listar_empleados(tabla)


# ==========================================
# VISTA PROYECTO
# ==========================================

def vista_proyecto(ventana):

    limpiar_ventana(ventana)

    barra_navegacion(ventana)

    frame, campos, fila = crear_formulario(ventana, "Datos del Proyecto",["Nombre:", "Descripción:", "Presupuesto (C$):"])

    crear_botones(
        frame,
        fila,
        lambda: crear_proyecto(*campos, tabla),
        lambda: actualizar_proyecto(*campos, tabla),
        lambda: eliminar_proyecto(*campos, tabla)
    )

    crear_busqueda(ventana, lambda e: buscar_proyecto(e, tabla))

    tabla = crear_tabla(
        ventana,
        ("nombre", "descripcion", "presupuesto"),
        ("Nombre", "Descripción", "Presupuesto"),
        (300, 450, 150)
    )

    tabla.bind( "<<TreeviewSelect>>", lambda event: seleccionar_proyecto(event, tabla, *campos))

    listar_proyectos(tabla)


# ==========================================
# VISTA SERVICIO
# ==========================================

def vista_servicio(ventana):

    limpiar_ventana(ventana)

    barra_navegacion(ventana)

    frame, campos, fila = crear_formulario(ventana, "Datos del Servicio", ["Servicio:", "Descripción:", "Precio (C$):"])

    crear_botones(
        frame,
        fila,
        lambda: crear_servicio(*campos, tabla),
        lambda: actualizar_servicio(*campos, tabla),
        lambda: eliminar_servicio(*campos, tabla)
    )

    crear_busqueda(ventana, lambda e: buscar_servicio(e, tabla))

    tabla = crear_tabla(
        ventana,
        ("nombre", "descripcion", "precio"),
        ("Servicio", "Descripción", "Precio"),
        (200, 500, 150)
    )

    tabla.bind("<<TreeviewSelect>>", lambda event: seleccionar_servicio(event, tabla, *campos))

    listar_servicios(tabla)

# ==========================================
# NUEVA VISTA: CITAS
# ==========================================

def formato_fecha(event):
    entrada = event.widget

    numeros = "".join(
        caracter for caracter in entrada.get()
        if caracter.isdigit()
    )[:8]

    fecha = numeros

    if len(numeros) > 2:
        fecha = numeros[:2] + "/" + numeros[2:]

    if len(numeros) > 4:
        fecha = numeros[:2] + "/" + numeros[2:4] + "/" + numeros[4:]

    entrada.delete(0, tk.END)
    entrada.insert(0, fecha)
    entrada.icursor(tk.END)


def formato_hora(event):
    entrada = event.widget
    texto = entrada.get().lower().replace(".", "").replace(" ", "")
    letras = "".join(
        caracter for caracter in texto
        if caracter.isalpha()
    )
    periodo = ""
    if letras in ("a", "am", "p", "pm"):
        periodo = letras.upper()
    numeros = "".join(
        caracter for caracter in texto
        if caracter.isdigit()
    )[:4]
    hora = numeros
    if len(numeros) == 3:
        hora = numeros[0] + ":" + numeros[1:]
    elif len(numeros) == 4:
        hora = numeros[:2] + ":" + numeros[2:]
    if periodo:
        hora += " " + periodo
    entrada.delete(0, tk.END)
    entrada.insert(0, hora)
    entrada.icursor(tk.END)

def vista_cita(ventana):

    limpiar_ventana(ventana)
    barra_navegacion(ventana)

    # FORMULARIO
    frame = ctk.CTkFrame(ventana)
    frame.pack(fill="x", padx=10, pady=10)

    ctk.CTkLabel(
        frame,
        text="Datos de la Cita",
        font=FUENTE_TITULO
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="w",
        padx=10,
        pady=(8, 4)
    )

    # Cliente
    ctk.CTkLabel(
        frame,
        text="Cliente:",
        font=FUENTE
    ).grid(row=1, column=0, sticky="e", padx=(10, 5), pady=3)

    entry_cliente = ctk.CTkEntry(
        frame,
        width=320,
        height=34,
        font=FUENTE
    )
    entry_cliente.grid(row=1, column=1, sticky="w", pady=3)

    validacion_cliente = (ventana.register(_funciones.cliente_valido), "%P")

    entry_cliente.configure(validate="key", validatecommand=validacion_cliente)

    # Fecha
    ctk.CTkLabel(
        frame,
        text="Fecha (DD/MM/AAAA):",
        font=FUENTE
    ).grid(row=2, column=0, sticky="e", padx=(10, 5), pady=3)

    entry_fecha = ctk.CTkEntry(
        frame,
        width=320,
        height=34,
        font=FUENTE,
        placeholder_text="Ejemplo: 31/10/2026"
    )
    entry_fecha.grid(row=2, column=1, sticky="w", pady=3)
    entry_fecha.bind("<KeyRelease>", formato_fecha)
    # Hora
    ctk.CTkLabel(
        frame,
        text="Hora:",
        font=FUENTE
    ).grid(row=3, column=0, sticky="e", padx=(10, 5), pady=3)

    entry_hora = ctk.CTkEntry(
        frame,
        width=320,
        height=34,
        font=FUENTE,
        placeholder_text="Ejemplo: 8:00 a.m."
    )
    entry_hora.grid(row=3, column=1, sticky="w", pady=3)
    entry_hora.bind("<KeyRelease>", formato_hora)
    # Motivo
    ctk.CTkLabel(
        frame,
        text="Motivo:",
        font=FUENTE
    ).grid(row=4, column=0, sticky="e", padx=(10, 5), pady=3)

    entry_motivo = ctk.CTkTextbox(
    frame,
    width=320,
    height=65,
    font=FUENTE,
    border_width=2,
    border_color="#565b5e",
    corner_radius=6
)
    entry_motivo.grid(row=4, column=1, sticky="w", pady=3)

    # Modalidad
    ctk.CTkLabel(
        frame,
        text="Modalidad:",
        font=FUENTE
    ).grid(row=5, column=0, sticky="e", padx=(10, 5), pady=3)

    entry_modalidad = ctk.CTkComboBox(
        frame,
        width=320,
        height=34,
        font=FUENTE,
        values=["Presencial", "Virtual"],
        state="readonly"
    )
    entry_modalidad.grid(row=5, column=1, sticky="w", pady=3)
    entry_modalidad.set("")

    # Estado
    ctk.CTkLabel(
        frame,
        text="Estado:",
        font=FUENTE
    ).grid(row=6, column=0, sticky="e", padx=(10, 5), pady=3)

    entry_estado = ctk.CTkComboBox(
        frame,
        width=320,
        height=34,
        font=FUENTE,
        values=["Pendiente", "Confirmada", "Completada", "Cancelada"],
        state="readonly"
    )
    entry_estado.grid(row=6, column=1, sticky="w", pady=3)
    entry_estado.set("")

    # BOTONES
    crear_botones(
        frame,
        7,
        lambda: crear_cita(
            entry_cliente,
            entry_fecha,
            entry_hora,
            entry_motivo,
            entry_modalidad,
            entry_estado,
            tabla
        ),
        lambda: actualizar_cita(
            entry_cliente,
            entry_fecha,
            entry_hora,
            entry_motivo,
            entry_modalidad,
            entry_estado,
            tabla
        ),
        lambda: eliminar_cita(
            entry_cliente,
            entry_fecha,
            entry_hora,
            entry_motivo,
            entry_modalidad,
            entry_estado,
            tabla
        )
    )

    # BÚSQUEDA POR CLIENTE
    ctk.CTkLabel(
        ventana,
        text="Buscar por cliente:",
        font=FUENTE
    ).pack(anchor="w", padx=12, pady=(5, 2))

    frame_busqueda = ctk.CTkFrame(
        ventana,
        fg_color="transparent"
    )
    frame_busqueda.pack(anchor="w", padx=10)

    entry_busqueda = ctk.CTkEntry(
        frame_busqueda,
        width=300,
        height=34,
        font=FUENTE
    )
    entry_busqueda.grid(row=0, column=0, padx=3)

    ctk.CTkButton(
        frame_busqueda,
        text="Buscar",
        width=110,
        height=34,
        font=FUENTE,
        command=lambda: buscar_citas(entry_busqueda, tabla)
    ).grid(row=0, column=1, padx=3)

    entry_busqueda.bind(
        "<Return>",
        lambda event: buscar_citas(entry_busqueda, tabla)
    )

    # TABLA DE CITAS
    tabla = crear_tabla(
        ventana,
        ("cliente", "fecha", "hora", "motivo", "modalidad", "estado"),
        ("Cliente", "Fecha", "Hora", "Motivo", "Modalidad", "Estado"),
        (160, 110, 100, 250, 130, 130)
        )

    # SELECCIONAR UNA CITA
    tabla.bind(
        "<<TreeviewSelect>>",
        lambda event: seleccionar_cita(
            event,
            tabla,
            entry_cliente,
            entry_fecha,
            entry_hora,
            entry_motivo,
            entry_modalidad,
            entry_estado
        )
    )

    listar_citas(tabla)