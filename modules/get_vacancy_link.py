from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from load_django import *
from app.models import Options, VacancyLink


class VacancyLinks:
    def __init__(self):
        service = Service()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.DEBUG = True

    def get_vacancy_links(self):
        for opt in Options.objects.filter(status="New"):
            country = opt.country
            position = opt.position

            self.driver.get(f"https://ua.indeed.com/jobs?q={position}&l={country}")

            try:
                cookie_agreement = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
                cookie_agreement.click()
            except NoSuchElementException:
                pass

            while True:
                links = self.driver.find_elements(By.CSS_SELECTOR, "h2.jobTitle a")
                for link in links:
                    url = link.get_attribute("href")
                    vacancy_name = link.text

                    if self.DEBUG:
                        print(url)
                        print(vacancy_name)

                    defaults = {
                        'name': vacancy_name,
                    }

                    VacancyLink.objects.get_or_create(
                        link=url,
                        defaults=defaults,
                    )

                try:
                    authorization_popup = self.driver.find_element(By.CLASS_NAME, "icl-CloseButton.icl-Card-close")
                    authorization_popup.click()
                    mailing_popup = self.driver.find_element(By.CLASS_NAME, "icl-CloseButton.icl-Modal-close")
                    mailing_popup.click()
                except NoSuchElementException:
                    pass

                try:
                    button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="pagination-page-next"]')
                    action_chains = ActionChains(self.driver)
                    action_chains.move_to_element(button).click().perform()
                except NoSuchElementException:
                    break

            opt.status = "Done"
            opt.save()


vacancy_link = VacancyLinks()
vacancy_link.get_vacancy_links()
