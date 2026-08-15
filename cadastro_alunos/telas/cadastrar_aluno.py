import flet as ft
from componentes.sidebar import criar_menu_lateral
from dados.alunos import adicionar_aluno


def tela_cadastrar_aluno(page: ft.Page):
    page.clean()

    campo_nome = ft.TextField(label="Nome do aluno", width=350)
    campo_idade = ft.TextField(label="Idade", width=350, keyboard_type=ft.KeyboardType.NUMBER)
    campo_curso = ft.TextField(label="Curso", width=350)

    mensagem_erro = ft.Text(value="", color=ft.Colors.RED_600, size=12)

    def salvar_aluno(e):
        nome = campo_nome.value.strip() if campo_nome.value else ""
        idade = campo_idade.value.strip() if campo_idade.value else ""
        curso = campo_curso.value.strip() if campo_curso.value else ""

        # Validação simples: nenhum campo pode ficar vazio.
        if not nome or not idade or not curso:
            mensagem_erro.value = "Preencha todos os campos antes de cadastrar."
            page.update()
            return

        adicionar_aluno(nome, idade, curso)

        # Limpa o formulário para o próximo cadastro
        campo_nome.value = ""
        campo_idade.value = ""
        campo_curso.value = ""
        mensagem_erro.value = ""

        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Aluno '{nome}' cadastrado com sucesso!"),
            bgcolor=ft.Colors.GREEN_700,
        )
        page.snack_bar.open = True
        page.update()

    conteudo_central = ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Cadastrar Aluno", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text(
                    "Preencha os dados abaixo para adicionar um novo aluno.",
                    size=13,
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
                            campo_idade,
                            campo_curso,
                            mensagem_erro,
                            ft.Container(height=10),
                            ft.ElevatedButton(
                                content="Cadastrar",
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
