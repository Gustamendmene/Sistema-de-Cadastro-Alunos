import flet as ft
from componentes.sidebar import criar_menu_lateral
from telas.menu_principal import tela_menu_principal
from dados.database import listar_alunos, excluir_aluno
from componentes.edit_dialogue import abrir_dialog_editar_aluno


def tela_listar_alunos(page: ft.Page):
    page.clean()
    alunos = listar_alunos() or []
    def excluir(indice: int):
        def ao_clicar(e):
            excluir_aluno(indice)
            tela_listar_alunos(page)

        return ao_clicar
    def atualizar(page,id_aluno, nome, matricula, curso):
        abrir_dialog_editar_aluno(
            page,
            id_aluno,
            nome,
            matricula,
            curso,
            ao_atualizar=lambda: tela_listar_alunos(page),
        )
    # Monta as DataRow a partir da lista_alunos
    rows = []
    for aluno in alunos:
        id_aluno, nome, matricula, curso =  aluno[0], aluno[1], aluno[2],aluno[3]
        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(matricula),color=ft.Colors.BLACK)),
                    ft.DataCell(ft.Text(nome,color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)),
                    ft.DataCell(ft.Text(curso,color=ft.Colors.BLACK)),
                    ft.DataCell(
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE,
                                    icon_color=ft.Colors.RED_600,
                                    tooltip="Excluir aluno",
                                    on_click=excluir(id_aluno),
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    icon_color=ft.Colors.BLACK,
                                    tooltip="Editar aluno",
                                    on_click=lambda e, id=id_aluno, n=nome, m=matricula, c=curso: atualizar(page, id, n, m, c),
                                ),
                            ],
                            spacing=5,
                        ),
                    )
                ]
            )
        )

    if not rows:
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
        corpo_lista = ft.ListView(
            expand=True,
            controls=[
                ft.DataTable(
                    border=ft.border.all(1, ft.Colors.GREY_300),
                    border_radius=10,
                    vertical_lines=ft.BorderSide(1, ft.Colors.GREY_200),
                    horizontal_lines=ft.BorderSide(1, ft.Colors.GREY_200),
                    heading_row_color=ft.Colors.BLUE_50,
                    columns=[
                        ft.DataColumn(ft.Text("Matricula", weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE), numeric=True),
                        ft.DataColumn(ft.Text("Nome", weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE)),
                        ft.DataColumn(ft.Text("Curso", weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE)),
                        ft.DataColumn(ft.Text("Ações", weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE)),
                    ],
                    rows=rows,
                )
            ]
        )
    def ir_para_menu():
        page.clean()
        tela_menu_principal(page)

    conteudo_central = ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            expand=True,
            controls=[
                ft.Text("Listar/Excluir Alunos", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text(
                    f"Total de alunos cadastrados: {len(alunos)}",
                    size=13,
                    color=ft.Colors.GREY_700,
                ),
                ft.Container(height=20),
                corpo_lista,
                ft.OutlinedButton("Voltar",icon=ft.Icons.ARROW_BACK,on_click= ir_para_menu)
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
