# scrapy-django-react

# Install requirements
```
pip install -r requirements.txt
```
> ```
> Django>=3.2<3.3
>django-dotenv==1.4.2
>djangorestframework==3.12.4
>Scrapy==2.5.0
>scrapy-djangoitem==1.1.1
> ```

# Criar Tabelas no Banco de dados
```
cd base
python3 manage.py migrate
```
# Criar .env
O arquivo `.env` precisa estar no mesmo diretório que o `manage.py`
```
DEBUG=1 # True
SECRET_KEY=Gere uma secret key
ALLOWED_HOSTS=127.0.0.1
```
# Rodar o Projeto Django
```
python3 manage.py runserver
```
<img src="docs/django_rodando.png" style="width:648;height:400;">

# Scrape quotes
```
cd crawler
scrapy crawl quotes

```

# Run React app
branch Frontend
```
npm start
```
