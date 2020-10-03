import json
from flask import Response


class APIResponseHandler(object):

    @classmethod
    def _api_response(cls, success, message, status_code, data=None, mimetype=None):
        print(message)

        response = {
            'success': bool(success),
            'message': message,
            # data: data
        }

        try:
            response = json.dumps(response)
        except TypeError as e:
            response = json.dumps({
                'success': False,
                'message': 'Error: {}'.format(e)
            })
            status_code = 500

        return Response(response=response, status=status_code,
                        mimetype=mimetype or 'application/json')

    @classmethod
    def api_success_response(cls, message):
        return cls._api_response(True, message, 200)

    @classmethod
    def api_failure_response(cls, message):
        return cls._api_response(False, message, 500)

    @classmethod
    def api_bad_request_response(cls, message=None):
        return cls._api_response(None, message or 'Bad Request', 400)

    @classmethod
    def api_not_found_response(cls):
        return cls._api_response(None, 'Not Found', 404)
