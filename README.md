# HealthyLifeStyle
## About the Project
The project is a platform for choosing healthy food based on the Harvard Plate Method. The API allows users to create, modify, and delete plate halves, like favorite dishes, and write reviews. Dishes can be filtered and sorted by tags and categories. Additionally, administrators can post news and articles. Users register via a code that can be sent either via email or SMS.

__[Link](https://github.com/Healthy-lifestyle-team-1) to the project organization__

### Clone the repository from GitHub and navigate to the project directory
```commandline
git clone https://github.com/Healthy-lifestyle-team-1/Back
cd HealthyLifeStyle
```

### Create a `.env` file in the root folder and specify your variables for email and SMS services
```env
EMAIL_HOST=''
EMAIL_PORT=
EMAIL_HOST_USER=''
EMAIL_HOST_PASSWORD=''
DEFAULT_FROM_EMAIL=''

SMSC_LOGIN=''
SMSC_PASSWORD=''
```

### Activate the project's virtual environment
```commandline
pip install -r ../requirements.txt
```

### Run migrations
```commandline
python manage.py migrate
```

### Start the server

```commandline
python manage.py runserver
```
---


# Models

### ```admin/```
Access to the admin panel.

### ```category/```
VIEW: ALL

CREATE: ADMIN ONLY

Create and view categories.

Required arguments:
* ```name```

### ```tag/```
VIEW: ALL

CREATE: ADMIN ONLY

Create and view tags.

Required arguments:
* ```name```

### ```product/```
VIEW: ALL

CREATE: ADMIN ONLY

Create and view plates.

Required arguments:

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
VIEW: ALL

CREATE: ADMIN ONLY

Create and view ratings.

Required arguments:
* ```dishhalf```
* ```user```
* ```value```

### ```likes/```
VIEW: ALL

CREATE: USERS

Create and view allergies.

Required arguments:
* ```user```
* ```product```

### ```article/```
VIEW: ALL

CREATE: ADMIN ONLY

Create and view articles.

Required arguments:
* ```author```
* ```text```

### ```news/```
VIEW: ALL

CREATE: ADMIN ONLY

Create and view news.

Required arguments:
* ```author```
* ```text```

### ```cart/```
VIEW: AUTHENTICATED USERS

CREATE: AUTOMATICALLY UPON REGISTRATION

Create and view user carts.

Required arguments:
* ```user```
* ```created_at```

### ```cart_item/```
VIEW: AUTHENTICATED USERS

CREATE: AUTOMATICALLY UPON REGISTRATION

Create and view product items in the cart.

Required arguments:
* ```cart```
* ```product```
* ```quantity```

## User Registration & Authentication

### ```login/```
User registration and authentication.
Arguments:
* ```login```
* ```username```

### ```verify/```
Account verification.
Arguments:
* ```code```

### ```logout/```
Log out of the account. No arguments required.
