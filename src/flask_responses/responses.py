"""
**********************************************************************************************

This module handles generating flask responses.

A flask response is a tuple that consists of:
    - the body
    - return code

**********************************************************************************************
"""

from http import HTTPStatus
import flask
import flask_responses.globals as g

#----------------------------------------------------------
# Resource successfully GET - the normal return
#----------------------------------------------------------
def get(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.OK)

#----------------------------------------------------------
# Resource was successfully UPDATED
#----------------------------------------------------------
def updated(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.OK)

#----------------------------------------------------------
# Resource was successfully CREATED
#----------------------------------------------------------
def created(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.CREATED)

#----------------------------------------------------------
# Resource was successfully DELETED
#----------------------------------------------------------
def deleted(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.NO_CONTENT)


#----------------------------------------------------------
# Not found error
#----------------------------------------------------------
def not_found(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.NOT_FOUND)

#----------------------------------------------------------
# Forbidden
#----------------------------------------------------------
def forbidden(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.FORBIDDEN)

#----------------------------------------------------------
# Forbidden
#----------------------------------------------------------
def internal_error(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.INTERNAL_SERVER_ERROR)

#----------------------------------------------------------
# Client error
#----------------------------------------------------------
def bad_request(output=None) -> flask.Response:
    return _standard_return(output, HTTPStatus.BAD_REQUEST)

#----------------------------------------------------------
# The standard return logic for all the methods
#----------------------------------------------------------
def _standard_return(output, response_code: HTTPStatus) -> tuple:
    if isinstance(output, type(None)):
        return (flask.jsonify(output), response_code)

    if g.envelope:
        output = {g.envelope_key: output}
    
    try:
        output_string = flask.jsonify(output)
    except Exception as ex:
        output_string = ''

    return (output_string, response_code)

