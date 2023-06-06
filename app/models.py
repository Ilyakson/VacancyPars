import os

from django.db import models


class Settings(models.Model):
    country = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        f = open("write_your_path/{}.py".format(self.position), "w+", encoding="UTF-8")
        f.write(
            """import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from app.models import Info


country = "{country}"
position = "{position}"


def parse_links():
    service = Service()

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://ua.indeed.com/jobs?q={position}&l={country}")
    links = []

    closer3 = driver.find_element(By.ID, "onetrust-reject-all-handler")
    closer3.click()

    while True:
        elements = driver.find_elements(By.CSS_SELECTOR, "h2.jobTitle a")

        for element in elements:
            links.append(element.get_property("href"))

        try:
            closer1 = driver.find_element(By.CLASS_NAME, "icl-CloseButton.icl-Card-close")
            closer1.click()
            closer2 = driver.find_element(By.CLASS_NAME, "icl-CloseButton.icl-Modal-close")
            closer2.click()
        except:
            pass

        try:
            button = driver.find_element(By.CSS_SELECTOR, '[data-testid="pagination-page-next"]')
            action_chains = ActionChains(driver)
            action_chains.move_to_element(button).click().perform()
        except Exception as e:
            break
        time.sleep(3)

    for link in links:
        driver.get(link)
        vacancy_name = driver.find_element(By.CLASS_NAME, "jobsearch-JobInfoHeader-title-container")
        text = driver.find_element(By.ID, "jobDescriptionText")
        name_company = driver.find_element(By.CSS_SELECTOR, "div[data-company-name='true']")
        date = driver.find_element(By.CLASS_NAME, "css-5vsc1i.eu4oa1w0")
        var = Info.objects.create(
            company_name=name_company.text,
            vacancy_name=vacancy_name.text,
            position=position,
            description=text.text,
            date_publication=date.text,
            link=link
        )
        var.save()
        time.sleep(2)


parse_links()
""".format(
                country=self.country, position=self.position
            )
        )
        f.close()
        os.system("python manage.py runscript {}.py".format(self.position))
        os.remove("write_your_path/{}.py".format(self.position))
        super(Settings, self).save(*args, **kwargs)


class Info(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    vacancy_name = models.CharField(max_length=255)
    description = models.TextField()
    date_publication = models.CharField(max_length=255)
    link = models.URLField()
