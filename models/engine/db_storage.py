#!/usr/bin/python3
'''This module defines a class to manage database storage for hbnb clone'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State
from os import getenv


class DBStorage:
    '''definition mysql database'''

    __engine = None
    __session = None

    def __init__(self) -> None:
        '''define the constructor of the db class'''
        usr, passwd = getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD')
        host, db = getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')

        connection = 'mysql+mysqldb://{}:{}@{}:3306/{}'.\
            format(usr, passwd, host, db)
        self.__engine = create_engine(connection, pool_pre_ping=True)

        if getenv('HBNB_DEV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None) -> dict:
        '''query on the current db session all objects
        depending on the class(cls) name
        If cls=None, query all types of
        objects(User, State, City, Amenity, Place and Review)'''

        dict = {}
        self.__session = sessionmaker(bind=self.__engine)()
        classes = [City, State]
        if cls in classes:
            query = self.__session.query(cls).all()
            for obj in query:
                key = '{}.{}'.format(cls.__class__.__name__, cls.id)
                dict[key] = obj
        else:
            for cls in classes:
                query = self.__session.query(cls).all()
                for obj in query:
                    key = '{}.{}'.format(cls.__class__.__name__, cls.id)
                    dict[key] = obj
        return dict

    def new(self, obj) -> None:
        '''add the object to the current database session'''
        self.__session.add(obj)

    def save(self) -> None:
        '''commit all changed of the current database session'''
        self.__session.commit()

    def delete(self, obj=None) -> None:
        '''delete from the current database session'''
        self.__session.delete(obj)

    def reload(self) -> None:
        '''Create the current database session from the engine,
        the session does not expire on commit'''
        Base.metadata.create_all(self.__engine)
        self.__Session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        self.__session = scoped_session(self.__Session)

    def close(self):
        '''close the session'''
        self.__session.remove()
