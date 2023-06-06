# Job Scraper
This Django application allows you to scrape job information from Indeed based on the specified country and position. It utilizes Selenium to automate the process of retrieving job details and saves them into the database.


## Installation
Change the Django settings in settings.py to match your environment and database configuration.

```shell
git clone https://github.com/Ilyakson/VacancyPars.git
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
