import os 

from .client import *
from .block import *

def run_test():
	client = NotionClient(os.environ.get('NOTION_KEY'))
	cv = client.get_collection_view(os.environ.get('RESTAURANT_DB'))
	print(cv.default_query().execute())
	print('wtfffff')