import json

def build_response_object(response, resp_code):
    """Construye un objeto de respuesta."""
    resp_code = str(resp_code) if not isinstance(resp_code, str) else resp_code

    response = {
        'statusCode': resp_code,
        'body': json.dumps(response),
        'headers': {'Content-Type': 'application/json', }
    }

    return response