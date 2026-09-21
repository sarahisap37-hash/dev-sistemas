from app.database import SessionLocal
from app.models import Curso, Aluno

def popular_banco():
    db = SessionLocal()
    try:
        if db.query(Curso).count() > 0:
            print("Banco já populado. Pulando...")
            return

        db.add_all([
            Curso(nome='Desenvolvimento de Sistemas', duracao=1200),
            Curso(nome='Design Gráfico', duracao=800),
            Curso(nome='Automação Industrial', duracao=1000)
        ])

        db.add_all([
            Aluno(nome='Sarah', email='sarah@senai.com', matricula='2025006'),
            Aluno(nome='Ana Laura', email='ana@senai.com', matricula='2025007'),
            Aluno(nome='Luisa', email='luisa@senai.com', matricula='2025008'),
            Aluno(nome='Igor', email='igor@senai.com', matricula='2025009')
        ])

        db.commit()
        print('Banco populado com sucesso!')

    except Exception as e:
        db.rollback()
        print(f'Erro: {e}')
    finally:
        db.close()
