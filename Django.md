
# Estudo sobre Django

Django é um framework web em Python que facilita a criação de aplicativos web complexos e escaláveis por isso resolvi estudar e criar esse repositorio.


![Logo](https://static.djangoproject.com/img/logos/django-logo-negative.1d528e2cb5fb.png)


## Apêndice

Django segue o padrão Model-View-Template (MVT), que é semelhante ao padrão MVC, mas com a adição de um componente de Template. A camada Model representa o modelo de dados, a camada View processa a lógica de negócios e a camada Template é responsável por renderizar a saída para o usuário.

O Django inclui um sistema de autenticação robusto e flexível, que permite gerenciar usuários, grupos e permissões. Ele também inclui suporte para login social, como autenticação do Google e do Facebook.

O Django possui uma grande comunidade de desenvolvedores ativos, que criam e mantêm bibliotecas e pacotes que estendem a funcionalidade do framework. Algumas dessas bibliotecas populares incluem django-crispy-forms para gerar formulários de maneira fácil e estilosa e django-rest-framework para criar APIs RESTful.

O Django suporta vários bancos de dados populares, incluindo PostgreSQL, MySQL e SQLite. Ele também suporta bancos de dados NoSQL, como o MongoDB, através de bibliotecas de terceiros.

O Django inclui um sistema de cache que pode melhorar significativamente o desempenho do aplicativo. O cache pode ser configurado para usar diferentes backends, como memória, banco de dados ou cache distribuído.

O Django possui uma poderosa ferramenta de linha de comando chamada "manage.py", que permite executar tarefas comuns de gerenciamento de aplicativos, como criar um novo aplicativo, executar migrações de banco de dados e criar um superusuário para o painel de administração.

O Django é altamente seguro e inclui várias medidas de segurança integradas, como proteção contra ataques CSRF (Cross-Site Request Forgery) e XSS (Cross-Site Scripting).

O Django é compatível com vários provedores de hospedagem, incluindo Heroku, AWS, Google Cloud Platform e DigitalOcean. Alguns provedores de hospedagem oferecem suporte específico para o Django, como o PythonAnywhere, que permite hospedar aplicativos Django diretamente do navegador.

O Django possui uma documentação abrangente e bem escrita, que inclui tutoriais, guias e referências para ajudar os desenvolvedores a começar a usar o framework. A documentação também inclui um conjunto de boas práticas e diretrizes de segurança recomendadas para ajudar a criar aplicativos web seguros e escaláveis.


## Variáveis de Ambiente

As variáveis de ambiente (também conhecidas como variáveis de configuração) são valores dinâmicos que podem ser acessados pelo seu aplicativo Django durante a sua execução. Elas são especialmente úteis para armazenar informações confidenciais, como senhas, chaves de API e outras informações de autenticação que não devem ser expostas publicamente.

O Django pode ler essas variáveis de ambiente por meio do pacote django-environ ou de outras bibliotecas semelhantes. Essa biblioteca ajuda a carregar as variáveis de ambiente do arquivo .env e adicioná-las ao os.environ, permitindo que seu aplicativo Django acesse esses valores facilmente.

Para usar variáveis de ambiente no Django, você precisará seguir os seguintes passos:

1) Instalar a biblioteca django-environ através do comando pip install django-environ.

2) Crie um arquivo .env na raiz do projeto Django, onde você pode armazenar suas variáveis de ambiente. Por exemplo:

```bash
SECRET_KEY='your-secret-key-here'

DEBUG=True

DATABASE_URL='postgresql://user:password@localhost:5432/database_name'

```
1) Em seu arquivo de configuração do Django (geralmente settings.py), importe a biblioteca django-environ e carregue as variáveis de ambiente do arquivo .env. Por exemplo:

```bash
import environ

# Cria uma instância do objeto `environ.Env`
env = environ.Env()

# Carrega as variáveis de ambiente do arquivo `.env`
environ.Env.read_env()

# Configurações do Django
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
DATABASES = {'default': env.db('DATABASE_URL')}
```
Agora você pode acessar suas variáveis de ambiente em todo o seu aplicativo Django, simplesmente chamando env('variavel_de_ambiente') em qualquer lugar onde precisar desses valores.

O uso de variáveis de ambiente no Django é uma prática recomendada para garantir que as informações confidenciais do seu aplicativo sejam armazenadas de forma segura e não sejam expostas publicamente.
## FAQ

#### Questão 1

Resposta 1

#### Questão 2

Resposta 2


## Instalação

Instale Estudo-sobre-Django com git

```bash
  git clone git@github.com:Taunt-byte/Estudo-sobre-Django.git
```

Entre no diretório do projeto

```bash
  cd Estudo-sobre-Django
```

    
## Aprendizados

Aprendi bastante sobre o django com esse repositorio.


## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:Taunt-byte/Estudo-sobre-Django.git
```

Entre no diretório do projeto

```bash
  cd Estudo-sobre-Django
```

Para rodar um aplicativo Django localmente, siga estes passos:

1) Instale o Django: se você ainda não tiver o Django instalado, instale-o usando o pip. Abra o terminal e execute o seguinte comando:

```bash
pip install Django
```

2) Crie um novo projeto Django: depois de instalar o Django, você pode criar um novo projeto Django usando o comando django-admin em seu terminal. Para criar um novo projeto Django, digite o seguinte comando:

```bash
django-admin startproject meu_projeto
```

Substitua "meu_projeto" pelo nome do seu projeto.

3) Acesse o diretório do projeto: depois de criar o projeto, acesse o diretório do projeto usando o seguinte comando:

```bash

cd meu_projeto
```
4) Execute as migrações do banco de dados: Antes de executar o servidor local, execute as migrações do banco de dados usando o seguinte comando:

```bash
python manage.py migrate
```

Isso criará as tabelas do banco de dados no SQLite.

5) Execute o servidor local: Por fim, execute o servidor local usando o seguinte comando:

```bash
python manage.py runserver
```

Este comando iniciará o servidor de desenvolvimento do Django e você poderá acessar o aplicativo em seu navegador digitando o seguinte endereço na barra de endereços do navegador:

```bash

http://localhost:8000/
```
