# UpTrader - тестовое задание


### Задание
См. [issue](https://github.com/vlad397/uptraider_test/issues/1)


### Описание

`Админка` доступна по адресу *http://127.0.0.1:8000/admin/*


Возможности проекта:

- создание древовидного меню в админке;
- просмотр древовидного меню с раскрывающимися подменюшками;


### Подробности выполнения

Древовидное меню выполнено с помощью библиотеки django-mptt.

Каждое меню и подменю являются ссылками для перехода по ним. Сами ссылки никакой информации не содержат, но изменения
можно заметить в адресной строке, где видно, что переход действительно осуществляется.


### Запуск проекта
После клонирования репозитария в терминале выполните следующие команды:

`pip install -r requirements.txt` *Для установки зависимостей*

Перейдите на уровень файла `manage.py`:

`python manage.py makemigrations` *Для создания миграций*

`python manage.py migrate` *Для применения миграций*

`python manage.py createsuperuser` *Для создания суперпользователя*

`python manage.py runserver` *Для запуска проекта на 8000 порту*
