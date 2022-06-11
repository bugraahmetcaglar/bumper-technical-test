class BaseResponse:
    @staticmethod
    def json_response(status_code, data):
        response = {
            "success": True,
            "error": False,
            "status_code": status_code,
            "data": data
        }
        return response

    @staticmethod
    def json_success_response(status, message, data):
        response = {
            "success": True,
            "error": False,
            "status_code": status,
            "message": message,
            "data": data
        }
        return response

    @staticmethod
    def success_response(status_code, message):
        response = {
            "success": True,
            "status_code": status_code,
            "error": False,
            "message": message
        }
        return response

    @staticmethod
    def error_response(status_code, message):
        response = {
            "success": False,
            "status_code": status_code,
            "error": True,
            "message": message
        }
        return response
