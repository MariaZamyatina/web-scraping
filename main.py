from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def main(url, f):
    driver = webdriver.Chrome()
    driver.get(url)
    vacancies = driver.find_element(By.CLASS_NAME, "vacancy-serp-content").find_elements(By.CLASS_NAME, "serp-item")
    dict = {
        "company": "",
        "position": "",
        "link": "",
        "city": "",
        "salary": ""
    }
    with open(f, "w", encoding="utf-8") as file:
        for element in vacancies:
            salary_content = element.find_element(By.CLASS_NAME, "vacancy-serp-item-body__main-info")
            if salary_content is not None and "USD" in salary_content.text:
                salary = salary_content.find_element(By.CSS_SELECTOR,
                                                     "span[data-qa='vacancy-serp__vacancy-compensation']")\
                    .text.replace(" ", " ")
                position = element.find_element(By.CLASS_NAME, "serp-item__title").text
                link = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                company = element.find_element(By.CLASS_NAME, "bloko-link_kind-tertiary").text
                city = element.find_element(By.CLASS_NAME, "vacancy-serp-item__info").find_element(
                    By.CSS_SELECTOR, "div[data-qa='vacancy-serp__vacancy-address']").text

                dict["position"] = position
                dict["link"] = link
                dict["company"] = company
                dict["city"] = city
                dict["salary"] = salary
                json.dump(dict, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    url = "https://spb.hh.ru/search/vacancy?text=python%2Cdjango%2Cflask&from=suggest_post&salary=&clusters=true&area=1&area=2&ored_clusters=true&enable_snippets=true"
    main(url, "data.json")
