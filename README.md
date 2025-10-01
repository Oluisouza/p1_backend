#   Projeto Domain-Driven Design

Exercício prático evoluindo de uma classe Python simplesparauma Entidade de Domínio, aplicando conceitos de DDD, serialização e eventos de domínio.

## Principais Conceitos Demonstrados

###  @static method

>   Tipo de método, estático, que recebe um self, porém não tem acesso à instância nem à classe. Ajuda a criar funções utilitárias que têm relação lógica com a classe, mas não dependem do estado de nenhuma instância particular.

###  Dataclasses

>   Decorador que cria automaticamente os métodos básicos de uma classe, como o __init__.

###  Eventos de Domínio

>   Padrão do Domain-Driven Design que serve para capturar ocorrências de negócio significativas como objetos de primeira classe. Um evento representa um fato que aconteceu no passado e é imutável.

###  Decoradores

>   Função que recebe outra função, ou classe, como argumento, adiciona alguma funcionalidade a ela, e a retorna modificada. Permite modificar ou estendero comportamento de classes e funções de forma limpa.

###  DDD

>   Abordagem de desenvolvimento de software que busca modelar o software para corresponder a um domínio de negócio. Seu objetivo é alinhar o software com as necessidades do negócio, utilizando uma linguagem comum e partilhada por todos.


##  Estrutura de Arquivos

|--- domain/
|   --- category.py
|--- events/
|   --- category_events.py
|--- main.py
|--- README.md

## Como Começar

Siga os passos abaixo

Siga os passos abaixo para executar o projeto em sua máquina local.

### Pré-requisitos

*   Python 3.8 ou superior.

### Instalação

1.  **Clone o repositório:**
    ```sh
    git clone git@github.com:Oluisouza/p1_backend.git
    ```
2.  **Navegue até a pasta do projeto:**
    ```sh
    cd seu-repositorio
    ```
3.  **(Opcional, mas recomendado) Crie e ative um ambiente virtual:**
    ```sh
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  Este projeto utiliza apenas bibliotecas padrão do Python, portanto, **não há dependências externas para instalar**.

##  Como Executar

Para ver a entidade `Category` em ação, execute o script `main.py`. Ele irá criar uma categoria, serializá-la, reconstruí-la e simular seu ciclo de vida, imprimindo os eventos gerados em cada etapa.

```sh
python main.py
```