# Django Aupi Boilerplate

Boilerplate para projetos Django da Aupi com Postgress + Django + Django Rest e Jazzmin

## PREREQUISITES
Ter docker e docker composer v2 e o virtualenv
```bash
sudo apt install docker-compose-v2 docker.io python3-virtualenv
```

Criar um virtual env e ativa-lo
```bash
virtualenv venv
source venv/bin/activate
```

Instalar o Poetry
```bash
pip install poetry
```

Rodar as dependências
```bash
poetry install
```

rodar a primeira vez
```bash
cp .env.example .env
make runserver
```


## RUN PROJECT
Para rodar o projeto em dev você pode usar o docker de banco de dados e em seguida subir a aplicação em dev
```bash
make rundb
make runserver
```

> [!CAUTION]
> NÃO USAR PIP INSTALL PARTA NENHUMA DEPENDÊNCIA, SOMENTE 'poetry add'

Para mais comandos de uma avaliada no Makefile


## HOW TO COMMIT
- git checkout main
- git pull
- git branch <your_beautiful_branch_name>
- git checkout <your_beautiful_branch_name>
- ... a lot of code...
- git add .
- git commit -m [<message_using_conventional_commits> ](https://www.conventionalcommits.org/en/v1.0.0/)
- git push origin <your_beautiful_branch_name>
- gh pr create -f
- win

## CODE FORMATTERS

We are using black, flake8 and isort.
So, you should run make lint to enable pre-commit hooks and use black as default formatter in vscode!


## Instruções do Docker de Produção e CERTBOT
Para colocar em produção, na primeira execução é necessário fazer a criação do SSL do letsencrypt. O passi inical é validar se o certbot está rodando, para isso rode:
`sudo docker compose -f docker-compose-ssl-init.yml run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d NOMEDODOMINIO.COM.BR`

Tendo sucesso nesta operação pode rodar o primeiro certificado com o comando:
`sudo docker compose -f docker-compose-ssl-init.yml run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d NOMEDODOMINIO.COM.BR`

TODO: Renovar o certbot



# Deploy Infra

Criar EC2 ubunto 22.04
Instalar git e docker
`sudo apt install docker.io docker-composer-v2`

atribuir IP elático

clonar repositorio
clonar repositoriod e pgadmin
conetar no banco




Criar RDS
- 

Criar S3
Fazer chave de acesos no S3

Criar arquivo .env com S3 e etc.