from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from load_django import *
from app.models import VacancyLink, Vacancy


class VacancyDescription:
    def __init__(self):
        service = Service()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.DEBUG = True

    def get_info(self):
        for vac in VacancyLink.objects.filter(status="New"):
            url = vac.link
            self.driver.get(url)

            try:
                title_element = self.driver.find_element(By.CLASS_NAME, "jobsearch-JobInfoHeader-title-container")
                title = title_element.text.strip()
            except NoSuchElementException:
                title = None

            try:
                description_element = self.driver.find_element(By.ID, "jobDescriptionText")
                description = description_element.text.strip()
            except NoSuchElementException:
                description = None

            try:
                name_company_element = self.driver.find_element(By.CSS_SELECTOR, "div[data-company-name='true']")
                employer = name_company_element.text.strip()
            except NoSuchElementException:
                employer = None

            try:
                date_publication_element = self.driver.find_element(By.CLASS_NAME, "css-5vsc1i.eu4oa1w0")
                date_publication = date_publication_element.text.strip()
            except NoSuchElementException:
                date_publication = None

            if self.DEBUG:
                print(employer)
                print(title)
                print(description)
                print(date_publication)

            defaults = {
                'employer': employer,
                'title': title,
                'description': description,
                'date_publication': date_publication,
            }
            obj, created = Vacancy.objects.get_or_create(
                link=url,
                defaults=defaults,
            )
            if created:
                vac.status = "Done"
                vac.save()


vacancy = VacancyDescription()
vacancy.get_info()
