from core.exceptions import CustomException


class CarModelNotFoundException(CustomException):
    code = 404
    error_code = 404
    message = "car model not found"


class DuplicateCarModelException(CustomException):
    code = 400
    error_code = 400
    message = "duplicate car model"
