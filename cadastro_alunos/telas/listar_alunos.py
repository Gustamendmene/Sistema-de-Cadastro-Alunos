import flet as ft
from componentes.sidebar import criar_menu_lateral
from dados.alunos import lista_alunos, remover_aluno


def tela_listar_alunos(page: ft.Page):
    page.clean()

    def excluir(indice: int):
        def ao_clicar(e):
            remover_aluno(indice)
            # Reconstrói a tela do zero para refletir a lista atualizada.
            # Como page.clean() já roda no início da função, chamar a
            # tela de novo é a forma mais simples de "atualizar" a lista.
            tela_listar_alunos(page)

        return ao_clicar

    def linha_aluno(indice: int, aluno: dict) -> ft.Row:
        return ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Column(
                    spacing=2,
                    controls=[
                        ft.Text(aluno["nome"], size=14, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            f"Idade: {aluno['idade']}   |   Curso: {aluno['curso']}",
                            size=12,
                            color=ft.Colors.GREY_600,
                        ),
                    ],
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE_OUTLINE,
                    icon_color=ft.Colors.RED_600,
                    tooltip="Excluir aluno",
                    on_click=excluir(indice),
                ),
            ],
        )

    # Monta a lista de linhas, uma por aluno cadastrado
    linhas = []
    for indice, aluno in enumerate(lista_alunos):
        linhas.append(
            ft.Container(
                padding=15,
                border_radius=10,
                bgcolor=ft.Colors.WHITE,
                border=ft.Border.all(1, ft.Colors.GREY_300),
                content=linha_aluno(indice, aluno),
            )
        )

    if not linhas:
        corpo_lista = ft.Container(
            padding=30,
            alignment=ft.Alignment.CENTER,
            content=ft.Text(
                "Nenhum aluno cadastrado ainda.",
                color=ft.Colors.GREY_600,
                italic=True,
            ),
        )
    else:
        corpo_lista = ft.Column(controls=linhas, spacing=12, scroll=ft.ScrollMode.AUTO, expand=True)

    conteudo_central = ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            expand=True,
            controls=[
                ft.Text("Listar/Excluir Alunos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text(
                    f"Total de alunos cadastrados: {len(lista_alunos)}",
                    size=13,
                    color=ft.Colors.GREY_700,
                ),
                ft.Container(height=20),
                corpo_lista,
            ],
        ),
    )

    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                criar_menu_lateral(page, tela_ativa="listar"),
                conteudo_central,
            ],
        )
    )
    page.update()
