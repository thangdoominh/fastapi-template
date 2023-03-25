from core.exceptions import CustomException


class DuplicateTheNameOfCarBrand(CustomException):
    code = 400
    error_code = 20001
    message = "duplicate name of car brand"


class CarBrandNotFoundException(CustomException):
    code = 404
    error_code = 20002
    message = "car brand not found"


class DuplicateCarBrandException(CustomException):
    code = 400
    error_code = 20003
    message = "duplicate car brand"
