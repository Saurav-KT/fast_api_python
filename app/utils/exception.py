from fastapi import HTTPException, status

class BusinessValidationError(HTTPException):
    def __init__(self, status_code:int, detail: str):
        super().__init__(status_code= status_code, detail=detail)
