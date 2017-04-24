from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    #check tahta we get a 404 on the / URL
    res = app.request("/")
    assert_response(resp, status="404")

    # test our first GET request to /hello
    rest = app.request("/")
    assert_response(resp)

    # make sure default valies work the form 
    resp = app.request("/hello", method ="POST")
    assert_response(resp, contains="Nobody")

    # test that we get expected values
    data = {'name':'Zed','greet': 'Hola'}
    resp = app.request('/hello', method="POST", data=data)
    assert_response(resp, contains="Zed")
