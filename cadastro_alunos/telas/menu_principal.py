import flet as ft
from componentes.sidebar import criar_menu_lateral


def tela_menu_principal(page: ft.Page):
    # page.clean() remove tudo o que estava desenhado na página antes
    # de montar a tela nova. É a técnica de transição pedida no
    # enunciado: em vez de abrir uma janela nova, a gente "limpa o
    # quadro" e desenha o próximo conteúdo por cima.
    page.clean()

    def ir_para_cadastro(e):
        from telas.cadastrar_aluno import tela_cadastrar_aluno
        tela_cadastrar_aluno(page)

    def ir_para_listagem(e):
        from telas.listar_alunos import tela_listar_alunos
        tela_listar_alunos(page)

    def cartao_atalho(icone, titulo, descricao, texto_botao, cor_botao, ao_clicar):
        """Um dos dois cartões brancos do centro da tela (Cadastrar / Listar)."""
        return ft.Container(
            width=280,
            padding=25,
            border_radius=12,
            bgcolor=ft.Colors.WHITE,
            border=ft.Border.all(1, ft.Colors.GREY_300),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        content=ft.Icon(icone, color=ft.Colors.BLUE_700, size=28),
                        bgcolor=ft.Colors.BLUE_50,
                        width=56,
                        height=56,
                        border_radius=28,
                        alignment=ft.Alignment.CENTER,
                    ),
                    ft.Text(titulo, size=16, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        descricao,
                        size=12,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.ElevatedButton(
                        content=texto_botao,
                        bgcolor=cor_botao,
                        color=ft.Colors.WHITE,
                        width=200,
                        on_click=ao_clicar,
                    ),
                ],
                spacing=10,
            ),
        )

    conteudo_central = ft.Container(
        expand=True,
        padding=40,
        content=ft.Column(
            controls=[
                ft.Text("Bem-vindo!", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text(
                    "Gerencie os alunos de forma fácil e eficiente.",
                    size=14,
                    color=ft.Colors.GREY_700,
                ),
                ft.Container(height=30),
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    spacing=25,
                    controls=[
                        cartao_atalho(
                            ft.Icons.PERSON_ADD_ALT_1,
                            "Cadastrar aluno",
                            "Adicione um novo aluno ao sistema.",
                            "Cadastrar",
                            ft.Colors.BLUE_700,
                            ir_para_cadastro,
                        ),
                        cartao_atalho(
                            ft.Icons.FORMAT_LIST_BULLETED,
                            "Listar/Excluir alunos",
                            "Visualize e exclua alunos cadastrados.",
                            "Acessar",
                            ft.Colors.BLUE_700,
                            ir_para_listagem,
                        ),
                    ],
                ),
            ],
        ),
    )

    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                criar_menu_lateral(page, tela_ativa="menu"),
                conteudo_central,
            ],
        )
    )
    page.update()
