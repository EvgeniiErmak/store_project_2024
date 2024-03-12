# Store Project 2024

Этот проект представляет собой пример простого веб-приложения для онлайн магазина, разработанного с использованием Python, FastAPI и SQLAlchemy.

## Структура проекта

store_project_2024
├── README.md
├── alembic
│ ├── README
│ ├── env.py
│ ├── script.py.mako
│ └── versions
├── app
│ ├── init.py
│ ├── api
│ │ ├── init.py
│ │ ├── cart.py
│ │ ├── categories.py
│ │ ├── products.py
│ │ └── subcategories.py
│ ├── auth.py
│ ├── crud.py
│ ├── database.py
│ ├── models.py
│ └── schemas.py
├── main.py
├── poetry.lock
├── project_structure.txt
├── pyproject.toml
└── tests
├── init.py
├── test_cart.py
├── test_categories.py
└── test_products.py


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

## Установка и запуск проекта

1. Убедитесь, что у вас установлен Python версии 3.7 или выше.
2. Клонируйте репозиторий на локальную машину:

    ```
    git clone https://github.com/EvgeniiErmak/store_project_2024.git
    ```

3. Перейдите в каталог проекта:

    ```
    cd store_project_2024
    ```

4. Установите зависимости с помощью Poetry:

    ```
    poetry install
    ```

5. Запустите приложение с помощью Uvicorn:

    ```
    uvicorn main:app --reload
    ```

6. Перейдите по адресу `http://127.0.0.1:8000/docs` в вашем браузере для доступа к интерактивной документации API.

## Дополнительная информация

Для более подробной информации о проекте, включая использованные технологии и инструкции по развертыванию, обратитесь к файлу `project_structure.txt`.
