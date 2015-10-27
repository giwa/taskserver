from collections import Iterable
import json

from flask import jsonify, Response

def mjsonify(obj):
    if isinstance(obj, Iterable):
        return Response(json.dumps(obj), mimetype="application/json")
    else:
        return jsonify(obj)
