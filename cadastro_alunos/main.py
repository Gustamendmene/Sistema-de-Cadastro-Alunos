import flet as ft
from telas.menu_principal import tela_menu_principal


def main(page: ft.Page):
    page.title = "Sistema de Cadastro de Alunos"
    page.window.width = 1000
    page.window.height = 620
    page.window.resizable = True
    page.bgcolor = ft.Colors.GREY_50
    page.padding = 0

    # A primeira tela exibida é sempre o Menu Principal.
    tela_menu_principal(page)


if __name__ == "__main__":
    ft.run(main)
