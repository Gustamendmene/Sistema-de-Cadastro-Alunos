import flet as ft
import sys 

def criar_menu_lateral(page: ft.Page, tela_ativa: str) -> ft.Container:
 
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
        page.window.prevent_close = False
        sys.exit(0)

    def item_menu(icone, texto, chave, ao_clicar):
        ativo = chave == tela_ativa
        return ft.Container(content=ft.ListTile(
            leading=icone,
            title=texto,
            bgcolor=ft.Colors.BLUE_600 if ativo else ft.Colors.TRANSPARENT,
            on_click=ao_clicar,
            icon_color=ft.Colors.WHITE,
            text_color=ft.Colors.WHITE
        ),border_radius=ft.BorderRadius.all(10))

    return ft.Container(
        width=230,
        bgcolor=ft.Colors.BLUE_900,
        padding=ft.Padding.symmetric(vertical=25, horizontal=16),
        content=ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    controls=[
                            ft.Icon(ft.Icons.SCHOOL, color=ft.Colors.WHITE, size=34,align=ft.Alignment.CENTER),   
                        ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Text(
                    "Sistema de\nCadastro de Alunos",
                    color=ft.Colors.WHITE,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    width=200
                ),
                ft.Divider(color=ft.Colors.BLUE_700, height=30),
                ft.ListView(
                    controls=[
                        item_menu(ft.Icons.HOME_OUTLINED, "Menu Principal", "menu", ir_para_menu),
                        item_menu(ft.Icons.PERSON_ADD_ALT_1, "Cadastrar Aluno", "cadastrar", ir_para_cadastro),
                        item_menu(ft.Icons.LIST_ALT, "Listar/Excluir Alunos", "listar", ir_para_listagem),
                    ]
                ),

                ft.Container(expand=True),  # empurra o "Sair" para o rodapé
                ft.Divider(color=ft.Colors.BLUE_700),
                item_menu(ft.Icons.LOGOUT, "Sair", "sair", sair),
            ],
        ),
    )
