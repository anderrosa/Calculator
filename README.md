# Calculadora Maluca

Este projeto é uma aplicação desenvolvida para treinar design de código, seguindo as melhores práticas de desenvolvimento. A aplicação oferece operações matemáticas básicas e avançadas através de rotas específicas.

## Funcionalidades

- **Rota `/calculator_1`**: Realiza operações matemáticas básicas (adição, subtração, multiplicação, divisão) entre dois números fornecidos via requisição `POST`.
- **Rota `/calculator_2`**: Calcula a potência de um número base elevado a um expoente, recebidos via requisição `POST`.
- **Rota `/calculator_3`**: Calcula a raiz quadrada de um número fornecido via requisição `POST`.
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
