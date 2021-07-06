import asyncio
import sys

from src.service.sync_service import Sync
from src.util.environment import Env

from src.service.data_service import DBHandler


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        action = args[0]
        if action == 'create_db':
            asyncio.run(DBHandler.get_instance().create_db())
        elif action == 'sync_data':
            data_path = Env.get_env_variable('data_path')
            asyncio.run(Sync.import_data_as_tasks(data_path))
    else:
        print('Nothing to do!')
