import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "Formulario de Registro de Eventos"
    
    titulo = ft.Text(
        value="Registro de Eventos",
        size=25,
        weight=ft.FontWeight.BOLD,
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
            ft.dropdown.Option("Convención"),
            ft.dropdown.Option("Curso"),
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
        max=9,
        divisions=8,
        label="{value} horas",
        value=2
    )

    campo_fecha = ft.TextField(
        label="Fecha del evento",
        hint_text="Selecciona una fecha",
        read_only=True
    )

    def cambiar_fecha(e):
        if fecha_evento.value:
            campo_fecha.value = fecha_evento.value.strftime("%d/%m/%Y")
            page.update()

    fecha_evento = ft.DatePicker(
        first_date=datetime.date.today(),
        on_change=cambiar_fecha
    )

    page.overlay.append(fecha_evento)

    def seleccionar_fecha(e):
        fecha_evento.open = True
        page.update()

    boton_fecha = ft.ElevatedButton(
        "Seleccionar fecha",
        on_click=seleccionar_fecha
    )

    fila_fecha = ft.Row([campo_fecha, boton_fecha])

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
            error_text.value = "El nombre del evento no puede estar vacío."
            resumen.value = ""

        elif campo_fecha.value == "":
            error_text.value = "Debes seleccionar una fecha."
            resumen.value = ""

        else:
            error_text.value = ""
            resumen.value = (
                f"Evento: {nombre_evento.value}\n"
                f"Tipo: {tipo_evento.value}\n"
                f"Modalidad: {modalidad.value}\n"
                f"Inscripción previa: {'Sí' if inscripcion.value else 'No'}\n"
                f"Duración: {int(duracion.value)} horas\n"
                f"Fecha: {campo_fecha.value}"
            )

        page.update()

    boton_resumen = ft.ElevatedButton(
        "Mostrar resumen",
        on_click=mostrar_resumen,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN,
            color=ft.Colors.WHITE
        )
    )

    contenido = ft.Container(
        content=ft.Column(
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
                ft.Divider(),
                error_text,
                resumen
            ],
            spacing=15,
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.Colors.GREY_100,
        width=500
    )

    page.add(contenido)


ft.app(target=main)
