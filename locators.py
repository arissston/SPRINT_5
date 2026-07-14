from selenium.webdriver.common.by import By

# Оооооок. Все локаторы проекта хранятся тут и импортируются в тесты:
#
#       from locators import MainPageLocators
#
#       driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()


class MainPageLocators:
    # ===Локаторы главной страницы=== #
    # Кнопка «Войти в аккаунт»
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")

    # Ссылка «Личный Кабинет» в шапке
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[.//p='Личный Кабинет']")

    # Ссылка «Конструктор» в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[.//p='Конструктор']")

    # Логотип Stellar Burgers
    LOGO = (By.XPATH, ".//div[contains(@class,'logo')]/a")

    # Кнопка оформления заказа. Появляется только после успешного логина
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")


class LoginPageLocators:
    # ===Локаторы страницы входа=== #

    # Поле Email
    EMAIL_INPUT = (By.XPATH, ".//fieldset[.//label='Email']//input")

    # Поле Пароль
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")

    # Кнопка «Войти»
    SUBMIT_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти')]")

    # Ссылка «Зарегистрироваться»
    REGISTER_LINK = (By.XPATH, ".//a[contains(text(),'Зарегистрироваться')]")

    # Ссылка «Восстановить пароль»
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[contains(text(),'Восстановить пароль')]")


class RegistrationPageLocators:
    # ===Локаторы страницы регистрации=== #

    NAME_INPUT = (By.XPATH, ".//fieldset[.//label='Имя']//input")

    EMAIL_INPUT = (By.XPATH, ".//fieldset[.//label='Email']//input")

    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, ".//button[contains(text(),'Зарегистрироваться')]")

    # Ошибка при пароле короче 6 символов:
    # <p class="input__error text_type_main-default">Некорректный пароль</p>
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class,'error')]")

    # Ссылка «Войти» на странице регистрации
    LOGIN_LINK = (By.XPATH, ".//a[contains(text(),'Войти')]")


class ForgotPasswordPageLocators:
    # ===Локаторы страницы восстановления пароля=== #

    LOGIN_LINK = (By.XPATH, ".//a[contains(text(),'Войти')]")


class ProfilePageLocators:
    # ===Локаторы личного кабинета (/account/profile)=== #

    # Кнопка выхода
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    # Активный пункт бокового меню «Профиль»
    PROFILE_TITLE = (By.XPATH, ".//a[contains(@class,'link_active') and text()='Профиль']")


class ConstructorPageLocators:
    # ===Локаторы раздела «Конструктор»=== #

    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']")

    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']")

    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']")

    # Активные табы
    BUNS_ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_type_current')]//span[text()='Булки']")

    SAUCES_ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_type_current')]//span[text()='Соусы']")

    FILLINGS_ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_type_current')]//span[text()='Начинки']")
