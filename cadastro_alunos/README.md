# Sistema de Cadastro de Alunos (Flet)

## Como rodar

```bash
pip install flet
python main.py
```

Isso abre uma janela desktop com o Menu Principal.

## Estrutura do projeto

```
cadastro_alunos/
├── main.py                  # ponto de entrada: cria a página e chama a primeira tela
├── telas/
│   ├── menu_principal.py    # Tela 1 - Menu Principal
│   ├── cadastrar_aluno.py   # Tela 2 - Cadastrar Aluno
│   └── listar_alunos.py     # Tela 3 - Listar/Excluir Alunos
├── componentes/
│   └── sidebar.py           # barra lateral de navegação, reaproveitada nas 3 telas
└── dados/
    └── alunos.py            # lista em memória com os alunos cadastrados
```

## Como funciona a transição de telas

Cada tela é uma função (`tela_menu_principal(page)`, `tela_cadastrar_aluno(page)`,
`tela_listar_alunos(page)`) que:

1. Chama `page.clean()` para apagar tudo o que estava desenhado antes.
2. Monta os componentes da tela nova (`Row`, `Column`, `Container`, `Text`,
   `TextField`, `ElevatedButton`...).
3. Chama `page.add(...)` para desenhar o novo conteúdo.
4. Chama `page.update()` para mandar isso pra tela.

Os botões do menu lateral e os botões dos cartões chamam essas funções,
passando a `page` adiante — não se abre nenhuma janela nova, é sempre a
mesma janela sendo "limpa e redesenhada".
