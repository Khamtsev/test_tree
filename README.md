### Описание
Приложение Django, в котором с помощью tamplate tag 
реализовано древовидное меню, редактируемое в админ-зоне Django. Меню по 
названию можно отрисовать на любой странице Приложения, 
используя следующие теги:
```
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```

### Технологии
* Python 3.9.10
* Django 3.2

### Запуск проекта
Для Windows:

```
git clone git@github.com:khamtsev/test_tree.git
cd test_tree
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```
Для Linux:

```
git clone git@github.com:khamtsev/test_tree.git
cd test_tree
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

Для добавления меню необходимо создать суперпользователя:
```
python manage.py createsuperuser
```

Запустить сервер разработки
```
python manage.py runserver
```

Админ-зона будет доступна по адресу
<http://localhost:8000/admin/>

На главной странице по-умолчанию выводится меню с именем "main_menu"

Приложение реализовано в рамках тестового задания.
Автор: Денис Хамцев, [GitHub](https://github.com/Khamtsev).
