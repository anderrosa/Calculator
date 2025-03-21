# Calculadora Maluca

Este projeto é uma aplicação desenvolvida para treinar design de código, seguindo as melhores práticas de desenvolvimento. A aplicação oferece operações matemáticas básicas e avançadas através de rotas específicas.

## Funcionalidades

- **Rota `/calculator_1`**: Realiza operações matemáticas em um número fornecido via requisição `POST`. O número é dividido por 3, e dois processos matemáticos são aplicados ao resultado. O resultado final é a soma desses processos com o número dividido.

- **Rota `/calculator_2`**: Processa uma lista de números fornecida via requisição `POST`. Aplica um processo matemático a cada número e calcula o inverso do desvio padrão dos resultados.

- **Rota `/calculator_3`**: Calcula a variância e a multiplicação de uma lista de números fornecida via requisição `POST`. Verifica se a variância é maior que a multiplicação e retorna o resultado da variância.

- **Rota `/calculator_4`**: Calcula a média de uma lista de números fornecida via requisição `POST`.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`src/`**: Contém o código-fonte da aplicação.
  - **`calculators/`**: Implementação das calculadoras e seus testes.
  - **`drivers/`**: Drivers específicos para integrações externas.
    - **`interfaces/`**: Interfaces e handlers para integração com bibliotecas externas.
  - **`errors/`**: Controle e definição de erros personalizados.
  - **`main/`**: Código principal da aplicação.
    - **`factories/`**: Fábricas para criação de objetos e instâncias.
    - **`routes/`**: Definição das rotas da aplicação.
    - **`server/`**: Configuração e inicialização do servidor.
- **`requirements.txt`**: Lista de dependências necessárias para executar a aplicação.
- **`run.py`**: Script principal para iniciar a aplicação.

## Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/anderrosa/Calculator.git
