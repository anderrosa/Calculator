from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        calculated_number = self.__process_data(input_data)

        formated_response = self.__format_response(calculated_number)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        input_data = body["numbers"]
        if not input_data:
            raise HttpUnprocessableEntityError("Lista de números vazia")
        
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        process_result = sum(input_data) / len(input_data)
        return process_result

    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": round(calculated_number, 2)
            }
        }