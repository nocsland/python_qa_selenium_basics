# home_work_selenium_basics

repo for home work python qa engineer, selenium basics

Домашнее задание

Основы Selenium Цель:

Научиться настраивать окружение для Selenium тестов, написать тесты, настроить ожидания к проекту. Научиться писать
простые selenium скрипты.

Задание 1. 
1.1. Написать фикстуру для запуска разных браузеров (firefox, chrome, opera, по желанию - safari, edge, yandex).
1.2. Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest. 
1.3. По завершению работы тестов должно осуществляться закрытие браузера. 
1.4. Добавить опцию командной строки, которая указывает базовый URL opencart. 
1.3. Написать тест, который открывает основную страницу opencart и проверяет что title соответствует
ожидаемому.

Задание 2. Написать тесты проверяющие наличие элементов на разных страницах приложения opencart. Реализовать минимум
пять тестов (одни тест = одна страница приложения). Использовать методы явного ожидания элементов.

Какие элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы.

Покрыть нужно: 
2.1 Главную / 
2.2 Каталог /index.php?route=product/category&path=20 
2.3 Карточку товара /index.php?route=product/product&path=57&product_id=49 
2.4 Страницу логина /index.php?route=account/login 
2.5 Страницу логина в админку /admin/ Критерии оценки:

    Весь написанный код оформлен в формате pull-request'a
    Соблюдается минимальный кодстай (встроенный форматтер PyCharm'a)
    Реализованы все проверки перечисленные в задании.

