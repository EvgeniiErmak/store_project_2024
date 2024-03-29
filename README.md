# Проект "Store Project 2024"

Этот проект представляет собой интернет-магазин, разработанный на основе FastAPI. Здесь вы найдете информацию о том, как запустить проект и как использовать его API.

## Автор

**Евгений Ермак**
- Телефон: +7 930-290-99-80
- Telegram: [https://t.me/DJErmak3000](https://t.me/DJErmak3000)
- Электронная почта: [ew.ermak5000@mail.ru](mailto:ew.ermak5000@mail.ru)
- GitHub: [https://github.com/EvgeniiErmak](https://github.com/EvgeniiErmak)

## Описание

Этот проект представляет собой интернет-магазин, разработанный с использованием FastAPI. Он включает в себя функции управления категориями товаров, подкатегориями, товарами и корзиной покупок.

## Описание файлов и каталогов

- **alembic**: содержит файлы для работы с миграциями базы данных с помощью Alembic.
- **app**: основной каталог приложения.
    - **api**: содержит модули для обработки запросов API.
    - **auth.py**: содержит функции и классы для аутентификации и авторизации.
    - **crud.py**: содержит функции для выполнения операций CRUD (Create, Read, Update, Delete) в базе данных.
    - **database.py**: содержит настройки для подключения к базе данных.
    - **models.py**: содержит описания моделей SQLAlchemy.
    - **schemas.py**: содержит описания схем Pydantic для валидации данных.
- **main.py**: файл, в котором запускается FastAPI приложение.
- **poetry.lock** и **pyproject.toml**: файлы для управления зависимостями проекта с помощью Poetry.
- **tests**: содержит модули и файлы для тестирования.

## Запуск приложения

1. Убедитесь, что у вас установлены Python и pip.
2. Клонируйте репозиторий: `git clone https://github.com/EvgeniiErmak/store_project_2024.git`
3. Перейдите в каталог проекта: `cd store_project_2024`
4. Установите зависимости: `pip install -r requirements.txt`
5. Запустите приложение: `uvicorn main:app --reload`

## Использование API

После запуска приложения вы сможете использовать его API. Документация API доступна по адресу `http://127.0.0.1:8000/docs`.
