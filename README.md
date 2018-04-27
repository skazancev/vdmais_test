## Калькулятор сервисов.

На странице есть форма с параметрами (в виде селекторов):
- Number power clients			(1-35)
- Number of external systems		(50-1000, step = 50)
- Number of cores in processor / RAM	(2CPU/2Gb | 2CPU/4Gb | 4CPU/8Gb | 8CPU/16Gb)

При изменении параметров - пользователь видит стоимость, которая вычисляется по формуле.
Пользователь не должен никаким образом увидеть саму формулу или добраться до неё.

Пользователь может добавить еще одну форму с такими же параметрами (а потом еще одну и еще...) 
и получить общий расчет по обеим. Значения селекторов в каждой форме могут быть разными (разумеется)

формула:

- Number power clients			= A
- Number of external systems		= B
- Number of cores in processor / RAM	= C

AMOUNT_MIN = 200
power = {"2gb": 100, "4gb": 200: "8gb": 500, "16gb": 900}

server_amount = AMOUNT_MIN + 10 * (pow(B, 0.25) + 50 * pow(A, 0.5) + power[C]


## Установка
`bower i`

`cp main/.env_sample main/.env`

Измените файл `.env` под себя 

`python manage.py migrate`
`python manage.py runserver`
