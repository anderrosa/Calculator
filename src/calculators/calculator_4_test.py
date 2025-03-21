from typing import Dict
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate_with_empty_list():
    mock_request = MockRequest({ "numbers": [] })
    calculator_4 = Calculator4()
    
    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == 'Lista de números vazia'

def test_calculate_with_invalid_body():
    mock_request = MockRequest({ "numberss": 1 })
    calculator_4 = Calculator4()
    
    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado'

def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4()
    
    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'result': 3.0}}