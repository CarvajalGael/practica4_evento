import flet as ft


def main(page: ft.Page):
    page.title = "Formulario de Registro de Eventos"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text(
        value="Registro de Eventos",
        size=28,
        weight=ft.FontWeight.BOLD,
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
        hint_text="Ej: Innovación 2026"
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial"
    )

    inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=2
    )

    fecha_evento = ft.DatePicker()
    page.overlay.append(fecha_evento)

    campo_fecha = ft.TextField(
        label="Fecha del evento",
        hint_text="Selecciona una fecha",
        read_only=True
    )

    def seleccionar_fecha(e):
        fecha_evento.pick_date()

    def cambiar_fecha(e):
        if fecha_evento.value:
            campo_fecha.value = fecha_evento.value.strftime("%d/%m/%Y")
            page.update()

    fecha_evento.on_change = cambiar_fecha

    boton_fecha = ft.ElevatedButton(
        content=ft.Text("Seleccionar fecha"),
        on_click=seleccionar_fecha
    )

    fila_fecha = ft.Row([campo_fecha, boton_fecha])

    linea = ft.Divider()

    resumen = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE
    )

    error_text = ft.Text(
        value="",
        size=14,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.RED
    )

    def mostrar_resumen(e):
        if nombre_evento.value.strip() == "":
            error_text.value = "⚠ El nombre del evento no puede estar vacío."
            resumen.value = ""
        else:
            error_text.value = ""
            resumen.value = (
                f"Evento: {nombre_evento.value}\n"
                f"Tipo: {tipo_evento.value}\n"
                f"Modalidad: {modalidad.value}\n"
                f"Inscripción previa: {'Sí' if inscripcion.value else 'No'}\n"
                f"Duración: {int(duracion.value)} horas\n"
                f"Fecha: {campo_fecha.value if campo_fecha.value else 'No seleccionada'}"
            )
        page.update()

    boton_resumen = ft.ElevatedButton(
        content=ft.Text("Mostrar resumen", color=ft.Colors.WHITE),
        on_click=mostrar_resumen,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN,
        )
    )

    contenido = ft.Column(
        controls=[
            titulo,
            nombre_evento,
            tipo_evento,
            ft.Text("Modalidad"),
            modalidad,
            inscripcion,
            ft.Text("Duración estimada (horas)"),
            duracion,
            fila_fecha,
            boton_resumen,
            linea,
            error_text,
            resumen
        ],
        spacing=15,
        width=500
    )

    page.add(contenido)


ft.app(target=main)