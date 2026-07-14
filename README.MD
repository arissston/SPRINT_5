Тестирование сервиса продажи межзвёздных булок. Улучшенное тестирование :)

Структура проекта:

    conftest.py  — фикстуры (браузер, регистрация пользователя через API)
    urls.py      — все урлы и эндпоинты проекта
    locators.py  — все локаторы, сгруппированные по страницам
    helpers.py   — генераторы тестовых данных (email, пароль)
    TESTS/       — тестовые модули, один класс на функциональность


Проверяем:


Регистрация — TESTS/test_registration.py :: TestRegistration

    test_successful_registration — успешная регистрация. Поле «Имя» не пустое;
    в поле Email введён email в формате логин@домен; пароль от шести символов.

    test_failed_registration_after_short_password — ошибка для некорректного
    пароля (короче шести символов).


Вход — TESTS/test_login.py, Класс TestLogin

    test_successful_login_from_main_page_enter_button — вход по кнопке
    «Войти в аккаунт» на главной,

    test_successful_login_from_main_page_LK_text_link — вход через кнопку
    «Личный кабинет»,

    test_successful_login_from_registerpage_enterclick — вход через кнопку
    в форме регистрации,

    test_successful_login_from_forgotpage_enterclick — вход через кнопку
    в форме восстановления пароля.


Личный кабинет — TESTS/test_personal_account.py, Класс TestPersonalAccount

    test_successful_redirect_to_LK_from_Main_page_by_LK_link — переход
    по клику на «Личный кабинет»,

    test_successful_redirect_from_LK_to_Main_page_by_Konstruktor_link —
    переход из кабинета в конструктор по клику на «Конструктор»,

    test_successful_redirect_from_LK_to_Main_page_by_logo_click — переход
    из кабинета на главную по клику на логотип Stellar Burgers,

    test_successful_logout_from_LK_by_Exit_link_click — выход из аккаунта
    по кнопке «Выход» в личном кабинете.


Раздел «Конструктор» — TESTS/test_constructor.py, Класс TestConstructor

    test_successful_move_to_buns_division — переход к разделу «Булки»,

    test_successful_move_to_sauces_division — переход к разделу «Соусы»,

    test_successful_move_to_fillings_division — переход к разделу «Начинки».
