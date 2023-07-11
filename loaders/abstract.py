from abc import ABC, abstractmethod
from sqlalchemy import orm, create_engine
import requests
import json
from typing import List
from models import Base

class AbstractLoader(ABC):
    def __init__(self, source: str, dest: str):
        self._source = source
        self._dest = dest
        engine = create_engine(self._dest)
        self._dest_session = orm.sessionmaker(bind=engine)

    @abstractmethod
    def _get_name(self) -> str:
        pass

    @abstractmethod
    def _get_query(self) -> str:
        pass

    @abstractmethod
    def _convert_data(self, data: dict) -> List[Base]:
        pass

    def _load_data(self, data_list: List[Base]):
        session = self._dest_session()
        for data_object in data_list:
            session.add(data_object)
            session.commit()
        session.close()

    def process(self):
        data = self._select_data()
        data_list = self._convert_data(data)
        self._load_data(data_list)
        print(f"{self._get_name()} loaded!")

    def _get_variables(self) -> dict:
        return dict()

    def _select_data(self) -> dict:
        json_data = {
            'query': self._get_query(),
            'variables': self._get_variables()
        }

        response = requests.post(url=self._source, json=json_data)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception(response)
