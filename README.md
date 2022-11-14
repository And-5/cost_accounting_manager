## Документация


> #### Запуск проект
1. docker-compose build
2. docker-compose up

> #### Полезные команды:
* sudo chown -R $USER /home/user/PycharmProjects/cost_accounting_manager/data

> #### Адреса:

1. /api/v1/auth/users/
> * регистрация пользователя
2. /api/v1/auth/token/
> * получить токен
3. /api/v1/category/
> * список категорий
4. /api/v1/category/create/
> * добавить свою категорию
5. /api/v1/category/<int:pk>/
> * <int:pk> - id категории
> * изменить/удалить категорию
6. /api/v1/transaction/
> * список транзакций
7. api/v1/transaction/create/
> * создвть транзакцию
8. api/v1/balance/
> * баланс

Для проверки работы celery необходимо изменить email и пароль от почты в settings.py
