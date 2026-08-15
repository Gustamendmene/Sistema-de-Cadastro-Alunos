import flet as ft


def criar_menu_lateral(page: ft.Page, tela_ativa: str) -> ft.Container:
    """
    Monta a barra lateral azul de navegação, igual à da imagem de referência.

    Parâmetros:
        page: a página do Flet (precisamos dela para trocar de tela
              quando o usuário clicar em um item do menu).
        tela_ativa: string que identifica qual tela está sendo exibida
              no momento ("menu", "cadastrar" ou "listar"). É usada só
              para destacar visualmente o botão correspondente.
    """

    # Os imports das telas ficam DENTRO das funções (e não no topo do
    # arquivo) para evitar import circular: sidebar.py precisa conhecer
    # as telas, e as telas precisam do sidebar.py. Importando aqui
    # dentro, o Python só resolve essa dependência na hora do clique.
    def ir_para_menu(e):
        from telas.menu_principal import tela_menu_principal
        tela_menu_principal(page)

    def ir_para_cadastro(e):
        from telas.cadastrar_aluno import tela_cadastrar_aluno
        tela_cadastrar_aluno(page)

    def ir_para_listagem(e):
        from telas.listar_alunos import tela_listar_alunos
        tela_listar_alunos(page)

    def sair(e):
        page.window.close()

    def item_menu(icone, texto, chave, ao_clicar):
        ativo = chave == tela_ativa
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icone, color=ft.Colors.WHITE, size=20),
                    ft.Text(texto, color=ft.Colors.WHITE, size=14),
                ],
                spacing=10,
            ),
            padding=ft.Padding.symmetric(vertical=12, horizontal=14),
            border_radius=8,
            bgcolor=ft.Colors.BLUE_600 if ativo else ft.Colors.TRANSPARENT,
            on_click=ao_clicar,
            ink=True,
        )

    return ft.Container(
        width=230,
        bgcolor=ft.Colors.BLUE_900,
        padding=ft.Padding.symmetric(vertical=25, horizontal=16),
        content=ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    [ft.Icon(ft.Icons.SCHOOL, color=ft.Colors.WHITE, size=34)],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text(
                    "Sistema de\nCadastro de Alunos",
                    color=ft.Colors.WHITE,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(color=ft.Colors.BLUE_700, height=30),
                item_menu(ft.Icons.HOME_OUTLINED, "Menu Principal", "menu", ir_para_menu),
                item_menu(ft.Icons.PERSON_ADD_ALT_1, "Cadastrar Aluno", "cadastrar", ir_para_cadastro),
                item_menu(ft.Icons.LIST_ALT, "Listar/Excluir Alunos", "listar", ir_para_listagem),
                ft.Container(expand=True),  # empurra o "Sair" para o rodapé
                ft.Divider(color=ft.Colors.BLUE_700),
                item_menu(ft.Icons.LOGOUT, "Sair", "sair", sair),
            ],
        ),
    )
