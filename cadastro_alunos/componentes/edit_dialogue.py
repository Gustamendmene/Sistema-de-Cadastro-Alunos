import flet as ft
import dados.database 

def abrir_dialog_editar_aluno(page: ft.Page, id_aluno, nome, matricula, curso, ao_atualizar=None):
    campo_nome = ft.TextField(
        label="Nome",
        value=nome,
        width=400
    )

    campo_matricula = ft.TextField(
        label="Matrícula",
        value=str(matricula),
        width=400
    )

    campo_curso = ft.Dropdown(
        leading_icon=ft.Icons.SCHOOL,
        label="Selecione seu curso",
        options=[
            ft.DropdownOption(key="Desenvolvimento de Sistemas",text="Desenvolvimento de Sistemas"),
            ft.DropdownOption(key="Marketing",text="Marketing")
        ],
        width=400,
        value=curso
    )

    def atualizar(e):
        try:
            matricula_atualizada = int(campo_matricula.value)
        except ValueError:
            page.snack_bar = ft.SnackBar(
                ft.Text("A matrícula deve ser um número."),
                bgcolor=ft.Colors.RED_700
            )
            page.snack_bar.open = True
            page.update()
            return

        sucesso,erro = dados.database.editar_aluno(
            id_aluno,
            campo_nome.value,
            matricula_atualizada,
            campo_curso.value
        )

        if(sucesso and erro == None):
            page.pop_dialog()
            if ao_atualizar:
                ao_atualizar()
            page.show_dialog(ft.SnackBar(
                ft.Text("Aluno atualizado com sucesso!"),
                bgcolor=ft.Colors.GREEN_700
            ))
            page.update()

        elif(erro == "Matricula"):
            page.pop_dialog()
            page.show_dialog(ft.SnackBar(
                ft.Text("Já existe um aluno com essa matrícula."),
                bgcolor=ft.Colors.RED_700
            ))
            page.update()

        elif(erro == "Banco"):
            page.pop_dialog()
            page.show_dialog(ft.SnackBar(
                ft.Text("Ocorreu um erro inesperado ao tentar atualizar o aluno"),
                bgcolor=ft.Colors.RED_700
            ))
            page.update()

    def cancelar(e):
        page.pop_dialog()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Editar Aluno"),
        content=ft.Column(
            tight=True,
            controls=[
                campo_nome,
                campo_matricula,
                campo_curso,
            ],
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=cancelar),
            ft.ElevatedButton("Salvar", on_click=atualizar),
        ],
    )
    page.show_dialog(dialog)
    page.update()
