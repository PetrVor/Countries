# CountriesDjango

## Инструкция по развертыванию проекта 

1. 'python3 -m venv django_venv'

2. 'source django_venv/bin/activate'

3. 'pip install -r requirements.txt'

4. 'python manage.py runserver'

## дополнительно
1.Полезное дополнения для шаблонов Django.
'''
ext install batisteo.vscode-django
'''

Добавить в 'settings.json'

'''
"emmet.includeLanguages":{
    "django-html" : "html"
    },
"files.associations":{
        "*.html": "django-html"
    }
'''