import os
import re
import json
from unittest import mock

from backend import lambda_function 

with open('final/template.yaml', 'r') as f: 
    TABLENAME = re.search(r'TableName: (.*)?', f.read()).group(1)

@mock.patch.dict(os.environ, {"TABLENAME": TABLENAME})
def test_lambda_handler():
    
    assert "AWS_ACCESS_KEY_ID" in os.environ  # Check AWS creds
    assert "AWS_SECRET_ACCESS_KEY" in os.environ

    ret = lambda_function.lambda_handler("", "")

    assert "statusCode" in ret     # Assert return keys
    assert "headers" in ret
    assert "body" in ret

    assert "Access-Control-Allow-Origin"  in ret["headers"] # Check for CORS in Headers
    assert "Access-Control-Allow-Methods" in ret["headers"]
    assert "Access-Control-Allow-Headers" in ret["headers"]

    if ret["statusCode"] == 200:     # Check status code
        assert "visit_count" in ret["body"]
        assert json.loads(ret["body"])["visit_count"].isnumeric()
    else:
        assert json.loads(ret["body"])["visit_count"] == -1

    return
