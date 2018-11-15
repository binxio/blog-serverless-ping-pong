from lambdas.common import *

def test_determine_region_and_account():
    arn = 'arn:aws:lambda:eu-west-1:612483924670:function:serverless-ping-pong-serverless-pingp-PingFunction-16DJONH1PWZLU'
    assert determine_region_and_account(arn) == ('eu-west-1', '612483924670')