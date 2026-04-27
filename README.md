# Yatube API

API для социальной сети Yatube.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:yandex-praktikum/api-final-yatube-ad.git
```

```
cd api-final-yatube-ad
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Документация:

После запуска документация будет доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```
