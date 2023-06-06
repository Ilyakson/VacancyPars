# Job Scraper
This Django application allows you to scrape job information from Indeed based on the specified country and position. It utilizes Selenium to automate the process of retrieving job details and saves them into the database.


## Installation
Change the Django settings in settings.py to match your environment and database configuration. 
And also write the path to the file in the file models.py on lines 11 and 84


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
## Instruction
Specify the country and position for the job scraping in the web form.

Click the "Save" button to trigger the scraping process.

The application will generate a Python script based on the provided inputs, execute it, and store the job information in the database.

View the scraped job information by accessing the appropriate URLs or by querying the Info model in Django.






