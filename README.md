# Api Based
## Versão 1.1.15
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![FastAPI](https://img.shields.io/badge/FastAPI-%23FF4F00.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-%23E10098.svg?style=for-the-badge&logo=graphql&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) 
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) 
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

Uma breve descrição sobre o que esse projeto faz e para quem ele é, API Based é um projeto open source.
Baseado na ideia de facilitar a crição de apis do absoluto, este projeto é uma ótima opção para os que se perguntem do que é composta uma api excelente em termos de seguranca, performance e escalabilidade/flexibilidade.

## Este projeto contara com:
- ### Melhores Práticas de Segurança

    - #### Autenticação e Autorização:
        - Utiliza métodos robustos de autenticação, como OAuth 2.0 ou JWT (JSON Web Tokens), para garantir que apenas usuários autorizados possam acessar a API.

    - #### HTTPS:
        - Sempre usar HTTPS para criptografar a comunicação entre o cliente e o servidor, protegendo os dados em trânsito.

    - #### Validação de Entrada:
        - Validar e sanitizar todas as entradas do usuário para evitar injeções de SQL, XSS (Cross-Site Scripting) e outros ataques.

    - #### Controle de Acesso:
        - Implementar controle de acesso baseado em funções (RBAC) para garantir que os usuários só possam acessar os recursos que têm permissão.

    - #### Limitação de Taxa (Rate Limiting):
        - Implementar throttling e rate limiting para proteger a API contra abusos e ataques de negação de serviço (DoS).

    - #### CORS (Cross-Origin Resource Sharing):
        - Configurar CORS adequadamente para controlar quais domínios podem acessar sua API.

    - #### Registros e Monitoramento:
        - Mantenher logs detalhados de acessos e erros, e monitore a API para detectar atividades suspeitas.

    - #### Segurança de Dados:
        - Armazenar senhas de forma segura usando algoritmos de hash como bcrypt, e evite armazenar dados sensíveis desnecessariamente.

    - #### Atualizações e Patches:
        - Manter todas as dependências e bibliotecas atualizadas para proteger contra vulnerabilidades conhecidas.

    - #### Proteção contra CSRF (Cross-Site Request Forgery):
        - Utilizar tokens CSRF para proteger endpoints que alteram o estado do servidor.


- ### Melhores Práticas de Performance

    - #### Cache:
        - Utilizar caching (como Redis ou Memcached) para armazenar respostas de requisições frequentes e reduzir a carga no servidor.
    
    - #### Paginação:
        - Implementar paginação em endpoints que retornam listas grandes de dados para evitar sobrecarga e melhorar a performance.
    
    - #### Compressão de Resposta:
        - Utilizar compressão (como Gzip) para reduzir o tamanho das respostas e melhorar o tempo de carregamento.
    
    - #### Minimização de Dados:
        - Retornar apenas os dados necessários nas respostas da API, evitando sobrecarregar a rede com informações desnecessárias.
    
    - #### Otimização de Consultas:
        - Otimizar consultas ao banco de dados, utilizando índices e evitando consultas N+1.
    
    - #### Asynchronous Processing:
        - Utilizar processamento assíncrono para operações que podem ser realizadas em segundo plano, melhorando a capacidade de resposta da API.
    
    - #### Monitoramento de Performance:
        - Implementar ferramentas de monitoramento de performance para identificar gargalos e otimizar a API continuamente.
    
    - #### Versionamento da API:
        - Utilizar versionamento de API para garantir que mudanças não quebrem a compatibilidade com clientes existentes.
    
    - #### Documentação Clara:
        - Forneçer documentação clara e abrangente para a API, facilitando a integração e o uso por desenvolvedores.




## Estrutura do projeto.
    src/
    ├── core
    │   ├── auth
    │   │   ├── auth.py
    │   ├── config
    │   │   ├── config_db.py
    │   │   ├── config.py
    │   │   ├── __init__.py
    │   ├── __init__.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   ├── routes
    │   │   ├── all_routes.py
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   ├── schemas
    │   │   ├── __init__.py
    │   │   └── schemas.py
    │   ├── services
    │   │   ├── __init__.py
    │   │   └── service.py
    │   └── task_email
    │       └── background.py
    ├── logs
    │   ├── app.log
    │   ├── auth.log
    │   └── db.log
    ├── main.py
    ├── models
    │   └── models.py
    ├── pytest.ini
    ├── requirements.txt
    ├── routes
    │   ├── all_routes.py
    │   ├── __init__.py
    │   └── routes.py
    ├── schemas
    │   └── schemas.py
    └── tests
        ├── __init__.py
        ├── test_route_home.py
        └── test_route_user.py


## Subindo projeto com Docker:

### Docker Compose
```bash
  docker-compose build
  docker-compose up
```


## Autores
- [@Rodrigo_Kelven](https://github.com/Rodrigo-Kelven)
