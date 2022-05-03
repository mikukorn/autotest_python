# autotest_python
Тестовый проект написания автотестов на python для ТЗ на сайт http://teamcapybara.github.io/capybara/


Какие проверки были реализованы: 
1.  Проверка на корректное отображение главной страницы и элементов.
1.2 Проверка на корректный переход по ссылке Ruby
2.  Проверка блока menu
2.2 Проверка перехода по ссылкам в разделе меню
3.  Проверка блока install
4.  Проверка блока Get started
4.2 Проверка ReadMe
5.  Проверка футера ellabs


### ТЗ:
Есть небольшая страница - http://teamcapybara.github.io/capybara/
1) Нужно написать автотесты, которые проверяют корректность страницы.
При реализации автотестов можно использовать python. Обязательно использовать шаблон PageObject.
2) Проект выложить на github и прислать ссылочку на него.
3) В свободном формате написать тест кейсы, которые реализованы в проекте и приложить их в проект.
4) Время на выполнение неделя.
5) Плюсом будет написание docker-compose для локального запуска тестов.


### Памятка по запуску и работе с проектом 
"pip freeze" - зафикисровать requirements.txt
"python -m pytest -s --alluredir=allure_test_results/" запустить тесты с отчетом allure 
"allure serve C:\Users\{user}\PycharmProjects\autotest_python\allure_test_results"
"docker build -t pytest_runner ." -контейнер docker
"docker run --rm --mount type=bind,src=C:\Users\mikuk\PycharmProjects\autotest_python,target=/test_project/ pytest_runner"
"docker-compose up --build" -запустить тесты в докере