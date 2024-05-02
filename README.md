# Автоматизация тестирования: frontend - OpenCart, backend - Swagger Petstore

## Swagger Petstore

Подготовка для запуска: 

1. Склоннировать репозиторий  
`git clone https://github.com/Ann1010/otus_test_project.git`
2. Установить содержимое requirements.txt  
`pip install -r requirements.txt`

[https://petstore.swagger.io](https://petstore.swagger.io)

Тесты для **Swagger Petstore** располагаются в каталоге
**api_tests/tests**

Для запуска тестов необходимо выполнить команду: 

`pytest -m api -n 2 api_tests/`

##### Дополнительные атрибуты: 
* --api_url - адрес Swagger Petstore, по умолчанию - https://petstore.swagger.io/v2/

##### Тэги для запуска отдельных тестовых классов:  

api - все тесты для Swagger Petstore  
pet - тесты для раздела Pet  
store - тесты для раздела Store  
user - тесты для раздела User  

## OpenCart 
Для запуска тестов должен быть развернут контейнер с OpenCart.
[Ссылка с инструкцией](https://gist.github.com/konflic/ecd93a4bf7666d97d62bcecbe2713e55)

Тесты для **OpenCart** располагаются в каталоге
**front_tests/tests**

Для запуска тестов необходимо выполнить команду: 

`pytest -m front -n 2 front_tests/`

##### Дополнительные атрибуты:

* --browser_name - браузер (safari, chrome, firefox), по умолчанию - chrome
* --headless - запуск в безоконном режиме, по умолчанию - True 
* --executor - local или через selenoid 
* --url - ip адрес и порт для развернутого OpenCart

##### Тэги для запуска отдельных тестовых классов:  

front - все тесты для OpenCart  
change_password - тесты для страницы Change Password   
my_account - тесты для для страницы My Account   
orders - тесты для для страницы Orders  
wish_list - тесты для для страницы Wish List  

## Запуск через Dockerfile 

1. Собрать образ  
`docker build -t tests_project .`  
2. Запустить контейнер. Пример:  
`docker run --rm tests_project -ti -m api api_tests/`

