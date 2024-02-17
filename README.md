# Bruce

## Project structure

## Prerequisites Libs

- asgiref==3.5.2
- certifi==2022.6.15
- cffi==1.15.1
- charset-normalizer==2.1.1
- coreapi==2.3.3
- coreschema==0.0.4
- cryptography==38.0.1
- defusedxml==0.7.1
- Django==4.1.1
- django-cors-headers==3.12.0
- django-debug-toolbar==3.6.0
- django-rest-swagger==2.2.0
- django-seed==0.3.1
- django-templated-mail==1.1.1
- djangorestframework==3.13.1
- djangorestframework-simplejwt==4.8.0
- djoser==2.1.0
- drf-access-policy==1.1.1
- drf-yasg==1.20.0
- Faker==14.0.0
- idna==3.3
- inflection==0.5.1
- itypes==1.2.0
- Jinja2==3.1.2
- MarkupSafe==2.1.1
- oauthlib==3.2.1
- openapi-codec==1.3.2
- packaging==21.3
- psycopg2-binary==2.9.3
- pycparser==2.21
- PyJWT==2.4.0
- pyparsing==3.0.9
- python-dateutil==2.8.2
- python-decouple==3.6
- python3-openid==3.2.0
- pytz==2022.2.1
- requests==2.28.1
- requests-oauthlib==1.3.1
- ruamel.yaml==0.17.21
- ruamel.yaml.clib==0.2.6
- sentry-sdk==1.9.8
- simplejson==3.17.6
- six==1.16.0
- social-auth-app-django==4.0.0
- social-auth-core==4.3.0
- sqlparse==0.4.2
- toposort==1.7
- uritemplate==4.1.1
- urllib3==1.26.12
- django-filter==22.1
- django-breadcrumbs==1.1.3
- django-view-breadcrumbs==2.4.1
- celery==5.3.1
- redis==4.5.5
- django-celery-results==2.5.1



## [Quick start](#quickstart)


### Development

#### Instale pre-commit hooks para linting e formatação

Todo código submetido deve ser checado quanto à formatação (black/prettier) e linting (flake8/isort).
Configure seu editor ou IDE de acordo com esses padrões.

Adicionalmente, para garantir que esses checks sejam realizadas a cada commit, instale os pre-commit hooks definidos para o projeto.
Para isso, faça o download da ferramenta `pre-commit` (https://pre-commit.com) e execute:

```sh
pre-commit install
```

#### Instale docker e docker-compose

Instale o `docker` e `docker-compose` segundo a documentação oficial.

No Ubuntu, as linhas abaixo podem ser usadas para instalar ambos.
Porém, versões mais atualizadas do `docker-compose` podem ser encontradas no [repositório oficial](https://github.com/docker/compose) :

```
# docker-ce-edge:
curl -L  "https://get.docker.com"  -o get-docker.sh
sh get-docker.sh
sudo usermod -aG docker `whoami`

# docker-compose:
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Você deve precisar reiniciar o seu computador para que o Docker Daemon inicie corretamente.

Para inciar a aplicação com docker compose, basta rodar o comando abaixo:

```sh
docker compose up -d
```