import flet as ft
from telas.menu_principal import tela_menu_principal


def main(page: ft.Page):
    page.title = "Sistema de Cadastro de Alunos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.GREY_50
    page.padding = 0
    tela_menu_principal(page)
    print(ft.__version__)

if __name__ == "__main__":
    ft.run(main)

ft.app(target=main,view=ft.AppView.FLET_APP)