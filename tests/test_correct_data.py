import json
import os
import time
from PageObjects.MainPageClass import MainPage
from conftest import driver
import pytest

@pytest.mark.smoke
def test_correct_data(driver):
    page = MainPage(driver)
    page.open_browser('https://demoqa.com/automation-practice-form')
    with open(os.path.abspath('./data.json'), 'r') as file:
        data = json.load(file)
        page.filling_out_the_form(data["first_name"],
                              data["last_name"],
                              data["email"],
                              data["gender"],
                              data["mobile_phone"],
                              data["date_of_birth"],
                              data["subjects"],
                              data["hobbies"],
                              os.path.abspath(data["image"]),
                              data["current_address"],
                              data["state"],
                              data["city"])
    time.sleep(3)
