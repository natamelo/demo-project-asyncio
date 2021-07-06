import aiounittest
from src.service.sync_service import Sync

'''
 to run (root path): python -m unittest tests/sync_service_test.py 
'''

class MyTest(aiounittest.AsyncTestCase):

    async def test1_await_async_fail(self):
        with self.assertRaises(Exception) as e:
            await Sync.sync_substation('invalid_path')
