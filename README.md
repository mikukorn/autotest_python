# autotest_python
Тестовый проект написания автотестов на python для ТЗ на сайт http://teamcapybara.github.io/capybara/

### ТЗ:
Есть небольшая страница - http://teamcapybara.github.io/capybara/
1) Нужно написать автотесты, которые проверяют корректность страницы.
При реализации автотестов можно использовать python. Обязательно использовать шаблон PageObject.
2) Проект выложить на github и прислать ссылочку на него.
3) В свободном формате написать тест кейсы, которые реализованы в проекте и приложить их в проект.
4) Время на выполнение неделя.
5) Плюсом будет написание docker-compose для локального запуска тестов.


### Какие проверки были реализованы: 
1.  Проверка на корректное отображение главной страницы и элементов
1.2 Проверка на корректный переход по ссылкам 
2.  Проверка блока menu
3.  Проверка блока install
4.  Проверка блока intro
5.  Проверка футера ellabs

### Тест-кейсы 
Название: 1. Проверка главной страницы http://teamcapybara.github.io/capybara/
1) Перейти на сайт http://teamcapybara.github.io/capybara/
2) Проверить отображение блоков: Описание, Меню, блок с установкой фреймворка, блок Get Started
ОР: Блоки отображаются, информация корректна. 
3) Проверить корректность перехода на ресурсы и отображения ссылок на главной, а именно: 
- Ссылка на главную страницу Ruby  (ОР: выполнен переход на главную страницу http://www.ruby-lang.org/ru/)
- Блок меню. Ссылка на добавление в группу outlook ruby-capybara(ОР: выполнен переход на http://groups.google.com/group/ruby-capybara)
- Блок меню. Ссылка на документацию api  (ОР: выполнен переход на https://rubydoc.info/github/teamcapybara/capybara/master)
- Блок меню. Ссылка на проект github (ОР: выполнен переход на https://github.com/teamcapybara/capybara)
- Ссылка на README (ОР: выполнен переход на https://rubydoc.info/github/teamcapybara/capybara)
4) Проверить корректность отображения блока с командой установки. 
ОР: Отображена команда "  gem install capybara"
 

### Памятка по запуску и работе с проектом 
"pip freeze" - зафикисровать requirements.txt
"python -m pytest -s --alluredir=allure_test_results/" запустить тесты с отчетом allure 
"allure serve C:\Users\{user}\PycharmProjects\autotest_python\allure_test_results"
"docker build -t pytest_runner ." -контейнер docker
"docker run --rm --mount type=bind,src=C:\Users\mikuk\PycharmProjects\autotest_python,target=/test_project/ pytest_runner"
"docker-compose up --build" -запустить тесты в докере