import flet as ft
from componentes.sidebar import criar_menu_lateral
from dados.database import registrar_aluno


def tela_cadastrar_aluno(page: ft.Page):
    page.clean()

    campo_nome = ft.TextField(prefix_icon=ft.Icons.PERSON,label="Nome do aluno", width=600)
    campo_matricula = ft.TextField(prefix_icon=ft.Icons.BADGE,
                                   label="Matricula", width=600, keyboard_type=ft.KeyboardType.NUMBER,input_filter=ft.NumbersOnlyInputFilter())
    campo_curso = ft.Dropdown(leading_icon=ft.Icons.SCHOOL,label="Selecione seu curso",
                            options=[
                                ft.DropdownOption(key="Desenvolvimento de Sistemas",text="Desenvolvimento de Sistemas"),
                                ft.DropdownOption(key="Marketing",text="Marketing")
                            ],
                            width=600
                        )

    mensagem_erro = ft.Text(value="", color=ft.Colors.RED_600, size=12)
    def mostrar_status(mensagem, cor):
        page.show_dialog(
            ft.SnackBar(
                content=ft.Text(mensagem),
                bgcolor=cor,
            )
        )
    def limpar_formulario():
        campo_nome.value = ""
        campo_matricula.value = ""
        campo_curso.value = None
        mensagem_erro.value = ""
    def salvar_aluno(e):
        nome = campo_nome.value.strip() if campo_nome.value else ""
        matricula = campo_matricula.value.strip() if campo_matricula.value else ""
        curso = campo_curso.value.strip() if campo_curso.value else ""

        # Validação simples: nenhum campo pode ficar vazio.
        if not nome or not matricula or not curso:
            mensagem_erro.value = "Preencha todos os campos antes de cadastrar."
            page.update()
            return
        sucesso,erro = registrar_aluno(nome, matricula, curso)
        if(sucesso and erro == None):
            nome_cadastrado = nome
            limpar_formulario()
            mostrar_status(f"Aluno '{nome_cadastrado}' cadastrado com sucesso!", ft.Colors.GREEN_700)
        elif(erro == "Matricula"):
            limpar_formulario()
            mostrar_status(f"Aluno '{nome_cadastrado}' não pode ser cadastrado pois ja existe um aluno com esse numero de Matricula", ft.Colors.RED_700)
        elif(erro=="Banco"):
            limpar_formulario()
            mostrar_status(f"Ocorreu um erro inesperado ao cadastrar o aluno '{nome_cadastrado}'.", ft.Colors.RED_700)
    conteudo_central = ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Cadastrar Aluno",size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text(
                    "Preencha os dados abaixo para adicionar um novo aluno.",
                    size=16,
                    color=ft.Colors.GREY_700,
                ),
                ft.Container(height=20),
                ft.Container(
                    padding=30,
                    border_radius=12,
                    bgcolor=ft.Colors.WHITE,
                    border=ft.Border.all(1, ft.Colors.GREY_300),
                    content=ft.Column(
                        controls=[
                            campo_nome,
                            campo_matricula,
                            campo_curso,
                            mensagem_erro,
                            ft.Container(height=10),
                            ft.ElevatedButton(
                                content=ft.Text("Cadastrar"),
                                bgcolor=ft.Colors.BLUE_700,
                                color=ft.Colors.WHITE,
                                width=180,
                                on_click=salvar_aluno,
                            ),
                        ],
                        spacing=15,
                        tight=True,
                    ),
                ),
            ],
        ),
    )

    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                criar_menu_lateral(page, tela_ativa="cadastrar"),
                conteudo_central,
            ],
        )
    )
    page.update()
