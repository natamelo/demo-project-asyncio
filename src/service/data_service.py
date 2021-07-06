from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.model.models import Base
from src.util.environment import Env

class DBHandler:

    _instance = None

    def __init__(self):
        self.engine = None

    def _get_engine(self):
        if not self.engine:
            self.engine = create_async_engine(Env.get_env_variable('db_path'))
        return self.engine

    def _create_session(self):
        session = sessionmaker(self._get_engine(), expire_on_commit=False, class_=AsyncSession)
        return session

    async def save(self, object):
        async_session = self._create_session()
        async with async_session() as session:
            async with session.begin():
                session.add(object)
                await session.flush()
                await session.refresh(object)
            await session.close()
        return object

    async def create_db(self):

        engine = self._get_engine()

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    def get_instance():
        if DBHandler._instance == None:
            DBHandler._instance = DBHandler()
        return DBHandler._instance
