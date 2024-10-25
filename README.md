# Integração Prolog com FastAPI

Integração entre Prolog e Python usando FastAPI, permitindo realizar consultas sobre uma base de conhecimento de sintomas e doenças.

## Funcionalidades

- Consulta de sintomas de pacientes
- Listagem de doenças e seus respectivos sintomas
- Verificação de possíveis doenças para um paciente com base em seus sintomas

## Estrutura do Projeto
    
- main.py: Arquivo principal contendo o código da API em FastAPI.
- base-integracao.pl: Base de conhecimento Prolog com os fatos sobre pacientes, sintomas e doenças.

## Pré-requisitos

- **Python 3.10 ou superior**
- **pip** (para gerenciar pacotes Python)
- **SWI-Prolog** instalado na máquina (para rodar o Prolog)

## Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/BosaP3/integra-o-prolog-python.git
   
2. **Crie e inicialize um ambiente virtual**:

3. **Instale os requirements no seu ambiente**:

    pip install -r requirements.txt

## Execução

1. **Inicie o servidor FastAPI:**

    uvicorn main:app --reload

2. **Acesse a documentação gerada pelo Swagger em**

    http://127.0.0.1:8000/docs
    
