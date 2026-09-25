from app.database import SessionLocal
from app.models import Departamento, Cargo, Funcionario

def popular_banco():
    db = SessionLocal()  # abrir sessão
    try:
        # Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamento(nome='Tecnologica da Informação', sigla='TI'),
            Departamento(nome='Recurso Humano', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(titulo='desenvolvedor', nivel='pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='pleno', salario_min=3500, salario_max=6000),
        ])

        db.add_all([
            Funcionario(nome='Ana Souza', email='ana.souza@empresa.com', telefone='11999990001', salario=4500.00, ativo=True),
            Funcionario(nome='Bruno Lima', email='bruno.lima@empresa.com', telefone='11999990002', salario=5200.00, ativo=True),
            Funcionario(nome='Carla Mendes', email='carla.mendes@empresa.com', telefone='11999990003', salario=3800.00, ativo=True),
            Funcionario(nome='Diego Santos', email='diego.santos@empresa.com', telefone='11999990004', salario=6100.00, ativo=False),
        ])

        db.commit()  # confirma tudo no banco de uma vez
        print('Banco preenchindo com sucesso')

    except Exception as erro:
        db.rollback()  # desfaz tudo se de erro
        print(f'Erro: {erro}')

    finally:
        db.close()  # lembre-se sempre de fechar a sessão


if __name__ == '__main__':
    popular_banco() 