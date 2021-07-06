import asyncio
from aiofile import AIOFile, LineReader
from src.util.util import DataUtil, PathUtil
from .data_service import DBHandler


class Sync:

    @staticmethod
    async def sync_substation(substation_path):
        async with AIOFile(substation_path, 'r') as file:
            async for line in LineReader(file):
                if not DataUtil.is_header(line):
                    equipment, measurement = DataUtil.get_objects(line)
                    equipment = await DBHandler.get_instance().save(equipment)
                    measurement.set_equipment_id(equipment.id)
                    await DBHandler.get_instance().save(measurement)

    @staticmethod
    async def import_data_as_tasks(data_path):
        path_list = PathUtil.get_files_from_dir(data_path)
        await asyncio.gather(*[Sync.sync_substation(file) for file in path_list])
