
class AppException(Exception):

    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail

class DuplicateException(AppException):

    def __init__(self, detail):
        super().__init__(409, detail)

class NotFoundException(AppException):

    def __init__(self, detail):
        super().__init__(404, detail)

class BadRequestException(AppException):

    def __init__(self, detail):
        super().__init__(400, detail)

class RateLimitException(AppException):

    def __init__(self, detail):
        super().__init__(429, detail)