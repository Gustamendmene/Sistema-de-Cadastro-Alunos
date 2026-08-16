import sqlite3 as sql

connection = sql.connect('siepe.db')
cursor = connection.cursor()

def registrar_aluno(nome:str,matricula:int,curso:str):
    try:
        data = (nome,matricula,curso)
        query = "INSERT INTO ALUNO (nome,matricula,curso) VALUES (?,?,?)"
        cursor.execute(query,data)
        connection.commit()
        return True,None

    except sql.IntegrityError as error:
        print(f"Ja existe matricula com esse numero: {error}")
        return False,"Matricula"
    except sql.Error as error:
        print(f"Ocorreu um erro inesperado: {error}")
        return False, "Banco"

def editar_aluno(id:int,nome:str,matricula:int,curso:str):
    try:
        query_update = "UPDATE ALUNO SET nome=?, matricula=?, curso=? WHERE id=?"
        cursor.execute(query_update, (nome, matricula, curso, id))
        connection.commit()
        return True, None
    except sql.IntegrityError as error:
        print(f"Ja existe matricula com esse numero: {error}")
        return False,"Matricula"
    except sql.Error as error:
        print(f"Ocorreu um erro inesperado: {error}")
        return False, "Banco"

def excluir_aluno(id:int):
    query_select = "SELECT * FROM ALUNO WHERE id=?"
    cursor.execute(query_select,(id,))
    aluno = cursor.fetchone()
    if(aluno):
        query_delete = "DELETE FROM ALUNO WHERE id=?"
        cursor.execute(query_delete,(id,))
        connection.commit()

def listar_alunos():
    cursor.execute("SELECT * FROM ALUNO")
    return cursor.fetchall()

def iniciar_banco():
    try:
        cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ALUNO(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            matricula INTEGER NOT NULL UNIQUE,
            curso VARCHAR(255) NOT NULL
    ) 
    """)
        connection.commit()
    
    except sql.Error as error:
        print(f"Ocorreu um erro inesperado: {error}")
        return False, "Banco"

iniciar_banco()
