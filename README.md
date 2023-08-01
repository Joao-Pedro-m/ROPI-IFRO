# ROPI-IFRO


O ROPI (repositorio de projetos integradores) é um sistema que documente os projetos integradores desenvolvidos a partir do ano de 2023 no Instituto Federal de educação, ciência e tecnologia de Rondônia - IFRO Câmpus Porto Velho Calama.

## Iniciando o setup

### Iniciar o ambiente de desenvolvimento virtual(venv)


Em um terminal na pasta base do projeto, rode os sequintes comandos

```
pip install venv
python -m venv activate
```

### Instalando as dependencias


Em um terminal na pasta base do projeto, rode os sequintes comandos

```
pip install -r requirements.txt
```

### Criando o banco de dados


Em um terminal na pasta base do projeto, rode os sequintes comandos

```
python manage.py makemigrations
python manage.py migrate
```

### Criar super usuario


Em um terminal na pasta base do projeto, rode os sequintes comandos

```
python manage.py createsuperuser
```


### Rodando o Django

Em um terminal na pasta base do projeto, rode os sequintes comandos
```
python manage.py runserver
```

### Adicionando dependencias


Adicione a dependencia normalmente e logo após rode o seguinte comando no terminal
```
pip freeze > requirements.txt
```

## Desenvolvedores do Projeto


* Willians de Paula Pereira - Coordenador
* Tayná Vitória Queiroz Moraes - Estudante
* Yasmin Leal de Oliveira - Estudante
* João Pedro Monteiro Ferreira - Estudante 
* Vinicius Silva de Oliveira - Estudante

## Desenvolvimento
* Python
* Django
* Bootstrap
* Github
* React JS