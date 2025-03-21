# Importando o tipo Dict (para tipagem) e o método raises (para testes de exceções)
from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1  # Importando a classe Calculator1, onde está o método de cálculo

# Classe MockRequest que simula uma requisição
class MockRequest:
    # Construtor que recebe um dicionário e o armazena no atributo json
    def __init__(self, body: Dict) -> None:
        self.json = body  # Atribui o dicionário passado ao atributo `json`

# Função de teste para verificar o comportamento do cálculo
def test_calculate():
    # Criando uma instância de MockRequest com o corpo da requisição (número 1)
    mock_request = MockRequest(body={ "number": 1 })
    # Criando a instância do objeto Calculator1, que contém a lógica de cálculo
    calculator_1 = Calculator1()

    # Chamando o método `calculate` da calculadora e passando a requisição mockada
    response = calculator_1.calculate(mock_request)
    
    # Conferindo se a resposta tem o formato correto
    assert "data" in response  # Verificando se "data" está na resposta
    assert "Calculator" in response["data"]  # Verificando se "Calculator" está na chave "data"
    assert "result" in response["data"]  # Verificando se "result" está na chave "data"

    # Testando se os valores da resposta estão corretos
    assert response["data"]["result"] == 14.25  # Verificando se o resultado é 14.25
    assert response["data"]["Calculator"] == 1  # Verificando se o "Calculator" tem o valor 1

# Função de teste para verificar o comportamento com um erro no corpo da requisição
def test_calculate_with_body_error():
    # Criando uma instância de MockRequest com um corpo de requisição mal formatado
    mock_request = MockRequest(body={ "numberss": 1 })  # "numberss" está errado
    calculator_1 = Calculator1()  # Criando a instância da calculadora

    # Usando `raises` para testar se uma exceção será levantada
    with raises(Exception) as excinfo:  # Esperamos que uma exceção seja levantada
        calculator_1.calculate(mock_request)  # Chamando o cálculo com o corpo errado
    
    # Verificando se a mensagem de erro da exceção é a esperada
    assert str(excinfo.value) == "body mal formatado"  # A mensagem de erro deve ser "body mal formatado"
