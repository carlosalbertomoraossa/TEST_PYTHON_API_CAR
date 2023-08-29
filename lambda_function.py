import json
import sys
import traceback

from app import settings
from app.controller.item_controller import ItemController
from app.dummy import DummyHandler
from app.utils import build_response_object


def lambda_handler(event, context):
    """AWS Lambda entry point."""
    
    print('Received event: ' + json.dumps(event))

    try:

        resource = event['resource'].lstrip('/').lower()

        if resource == 'items' and event["httpMethod"] == "GET":
            itemController = ItemController()
            payload = itemController.get_items()
            status_code = 200
        else:
            handler = DummyHandler(event)
            payload, status_code = handler.process()
        
        response = build_response_object(payload, status_code)

    except Exception as e:
        print(e)
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        response = build_response_object(e.args[0], 500)

    return response