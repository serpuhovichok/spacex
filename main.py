from models import *
from loaders.rockets import RocketsLoader


POSTGRESQL = 'postgresql+psycopg2://postgres:postgres@postgres:5432/spacex'
SPACEX = 'https://spacex-production.up.railway.app/'

if __name__ == "__main__":
    create_tables(POSTGRESQL)
    loaders = [RocketsLoader(source=SPACEX, dest=POSTGRESQL)]
    for loader in loaders:
        loader.process()
