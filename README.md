# HealthyLifeStyle
## О проекте
Проект представляет из себя платформу для выбора здоровой еды по методу Гарвардской тарелки. API дает возможность создания, изменения и удаления половинок тарелок; лайкать понравившиеся блюда, писать рецензии. Блюда можно фильтровать и сортировать по тегам и категориям. Кроме того, администраторы имеют возможность писать новости и статьи. Пользователь регистрируется через код, который быть отправлен как по электронной почте, так и по SMS. 

__[Ссылка](https://github.com/Healthy-lifestyle-team-1) на организацию проекта__

### Клонируйте репозиторий с GitHub и переключитесь на директорию проекта
```commandline
git clone https://github.com/Healthy-lifestyle-team-1/Back
cd HealthyLifeStyle
```

### Создайте файл .env в корневой папке и укажите свои переменные для почтовых и СМС отправлений:
```env
EMAIL_HOST=''
EMAIL_PORT=
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
DEFAULT_FROM_EMAIL=''

SMSC_LOGIN=''
SMSC_PASSWORD=''
```

### Активируйте виртуальное окружение проекта:
```commandline
pip install -r ../requirements.txt
```

### Сделайте миграции:
```commandline
python manage.py migrate
```

### Запустите сервер:

```commandline
python manage.py runserver
```
---


# Модели

## ```admin/```
Вход в админ панель.

### ```category/```
ПРОСМОТР: ВСЕ   
СОЗДАНИЕ: ТОЛЬКО АДМИН   
Создание и просмотр категорий.   
Запрашивает такие аргументы как:
* ```name```

### ```tag/```
ПРОСМОТР: ВСЕ   
СОЗДАНИЕ: ТОЛЬКО АДМИН   
Создание и просмотр тег.   
Запрашивает такие аргументы как:
* ```name```

### ```product/```
ПРОСМОТР: ВСЕ   
СОЗДАНИЕ: ТОЛЬКО АДМИН   
Создание и просмотр тарелок.   
Запрашивает такие аргументы как:
* ```title```
* ```subtitle```
* ```category```
* ```tag```
* ```image```
* ```image_extra```
* ```calories```
* ```proteins```
* ```fats```
* ```carbs```
* ```price```
* ```description```
* ```cooking_method```
* ```weight```
* ```ingredients```
* ```is_prepared```

### ```rating/```
ПРОСМОТР: ВСЕ   
СОЗДАНИЕ: ТОЛЬКО АДМИН   
Создание и просмотр рейтинга.   
Запрашивает такие аргументы как:
* ```dishhalf```
* ```user```
* ```value```

### ```likes/```
ПРОСМОТР: ВСЕ   
СОЗДАНИЕ: ПОЛЬЗОВАТЕЛИ   
Создание и просмотр аллергий.   
Запрашивает такие аргументы как:
* ```user```
* ```product```

### ```article/```
ПРОСМОТР: ВСЕ   
СОЗДАНИЕ: ТОЛЬКО АДМИН   
Создание и просмотр статьи.   
Запрашивает такие аргументы как:
* ```author```
* ```text```

### ```news/```
ПРОСМОТР: ВСЕ   
СОЗДАНИЕ: ТОЛЬКО АДМИН   
Создание и просмотр новостей.   
Запрашивает такие аргументы как:
* ```author```
* ```text```

### ```cart/```
ПРОСМОТР: АУДЕНТИФИЦИРОВАННЫЙ ПОЛЬЗОВАТЕЛЬ   
СОЗДАНИЕ: АВТОМАТИЧЕСКИ ПРИ РЕГИСТРАЦИИ   
Создание и просмотр корзины пользователя.   
Запрашивает такие аргументы как:
* ```user```
* ```created_at```

### ```cart_item/```
ПРОСМОТР: АУДЕНТИФИЦИРОВАННЫЙ ПОЛЬЗОВАТЕЛЬ   
СОЗДАНИЕ: АВТОМАТИЧЕСКИ ПРИ РЕГИСТРАЦИИ   
Создание и просмотр позиции продукта в корзине.   
Запрашивает такие аргументы как:
* ```cart```
* ```product```
* ```quantity```

## Регистрация и учётные данные пользователя

### ```login/```
Регистрация и аутентификация пользователя.   
Аргументы:
* ```login```
* ```username```

### ```verify/```
Подтверждение учетной записи.   
Аргументы:
* ```code```

### ```logout/```
Выход из учетной записи. Не запрашивает аргументов.

### ```user/```
Просмотр и изменение информации пользователя.   
Аргументы:
* ```username```
* ```phone```
* ```email```