# Auth Core Lab (Neo-Brutalism Edition) 🟪🟨

Full-Stack приложение для безопасной аутентификации, выполненное в стиле Neo-Brutalism.

## Технологии
*   **Frontend:** React 18, TypeScript, Vite
*   **Backend:** Python 3.12, FastAPI, SQLModel (SQLAlchemy + Pydantic)
*   **Database:** PostgreSQL 16 (AsyncPG)
*   **DevOps:** Docker Compose

## Запуск

1.  **Старт системы:**
    ```bash
    docker compose up --build -d
    ```

2.  **Веб-интерфейс:**
    Откройте [http://localhost](http://localhost).

3.  **Документация API (OpenAPI):**
    Откройте [http://localhost:8000/docs](http://localhost:8000/docs).

## 🗄Управление Базой Данных (GUI)

Для просмотра данных развернут легковесный интерфейс **Adminer**.

1.  Перейдите: [http://localhost:8080](http://localhost:8080)
2.  Используйте данные из `.env` для входа:
    *   **System:** PostgreSQL
    *   **Server:** `database`
    *   **Username:** `neo_user`
    *   **Password:** `neo_pass`
    *   **Database:** `neo_auth_db`

## Тестирование

Запуск автоматических интеграционных тестов (регистрация, валидация, дубликаты, healthcheck):
```bash
docker compose exec backend pytest
```

## Реализованные меры защиты (Security Hardening)

1.  **Argon2id Hashing:** Использование `passlib` с настройками Argon2 (m=19456, t=2) для защиты от GPU-брутфорса.
2.  **Strict Validation:** Валидация сложности пароля и формата логина на уровне схем Pydantic/SQLModel.
3.  **DB Integrity:** Уникальные индексы и транзакционность операций.
4.  **Isolation:** Сетевая изоляция базы данных в Docker (нет прямого доступа извне).

## Структура БД (SQLModel)

Таблица `users_table`:
*   `id`: UUID (PK)
*   `login`: String (Unique Index)
*   `password_hash`: String (Argon2)
*   `created_at`: DateTime
