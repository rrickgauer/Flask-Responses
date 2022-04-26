"""
**********************************************************************************************

Configure the library

**********************************************************************************************
"""

import flask_responses


def toggle_envelope(envelope: bool):
    flask_responses.globals.envelope = envelope

def set_envelope_key(key: str):
    flask_responses.globals.envelope_key = key