import pandas as pd
import sys

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


def main() -> None:
    if len(sys.argv) != 2:
        return

    engine = create_engine('sqlite:///meu_banco.db', echo=True)

    Base = declarative_base()

    class Account(Base):
        __tablename__ = 'accounts'

        numero = Column(String, primary_key=True)
        titular = Column(String)
        saldo = Column(String)
        limite = Column(String)
        data_abertura = Column(String)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    if ".csv" in sys.argv[1]:
        df = pd.read_csv(sys.argv[1])
    if ".jsonl" in sys.argv[1]:
        df = pd.read_json(sys.argv[1], lines=True)
    
    for _, row in df.iterrows():
        existente = session.query(Account).filter_by(numero=row['numero']).first()
        if existente:
            existente.titular = row['titular']
            existente.saldo = row['saldo']
            existente.limite = row['limite']
            existente.data_abertura = row['data_abertura']
        else:
            account = Account(numero=row['numero'], titular=row['titular'], saldo=row['saldo'], limite=row['limite'], data_abertura=row['data_abertura'])
            session.add(account)

    session.commit()

    session.close()

if __name__ == '__main__':
    main()