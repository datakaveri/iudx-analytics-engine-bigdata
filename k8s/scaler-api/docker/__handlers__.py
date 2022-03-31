from flask import jsonify
from functools import update_wrapper
from flask import request


__all__  = ['ResponseHandler', 'AuthHandler']

class ResponseHandler:
    def __init__(self, function):
        update_wrapper(self, function)
        self.function = function
        
    def __name__(self):
        return 'ResponseHandler'

    def __call__(self, *args, **kwargs):
        try:
            response = self.function(*args, **kwargs)
            return self.success(response)

        except Exception as err:
            return self.error(str(err))

    def success(self, _json=None):
        json = {
            "response": _json if _json else "success" 
        }
        return jsonify(json), 200

    def error(self, _json=None):
        json = {
            "error": _json if _json else "Unknown Error" 
        }
        return jsonify(json), 400
