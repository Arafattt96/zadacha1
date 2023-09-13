from selenium.webdriver import Keys
from datetime import datetime
from PageObjects.BasePageClass import BaseClass
from selenium.webdriver.common.by import By



class MainPage(BaseClass):

    def filling_out_the_form(self, first_name,
                             last_name,
                             email,
                             gender,
                             number,
                             date_of_birth,
                             subjects,
                             hobbies,
                             image,
                             current_address,
                             state,
                             city):
        self.contribute_first_name(self.get_element_with_xpath('//*[@id="firstName"]'), first_name)
        self.contribute_last_name(self.get_element_with_xpath('//*[@id="lastName"]'), last_name)
        self.contribute_email(self.get_element_with_xpath('//*[@id="userEmail"]'), email)
        self.select_gender(gender)
        self.contribute_mobile_phone(self.get_element_with_xpath('//*[@id="userNumber"]'), number)
        self.select_date_of_birth(date_of_birth)
        self.select_subjects(subjects)
        self.select_hobbies(hobbies)
        self.upload_image(self.get_element_with_xpath('//*[@id="uploadPicture"]'), image)
        self.contribute_current_address(self.get_element_with_xpath('//*[@id="currentAddress"]'), current_address)
        self.select_state(state)
        self.select_city(city)
        try:
            self.assert_correct_form_input()
            return True
        except AssertionError as error:
            return error.__str__()
        except:
            return False


    def get_element_with_xpath(self, xpath_locator):
        return self.driver.find_element(By.XPATH, xpath_locator)

    def contribute_first_name(self, element, first_name):
        element.send_keys(first_name)

    def contribute_last_name(self, element, last_name):
        element.send_keys(last_name)

    def contribute_email(self, element, email):
        element.send_keys(email)

    def select_gender(self, gender):
        if gender == 'Male':
            self.get_element_with_xpath('//*[@id="genterWrapper"]/div[2]/div[1]/label').click()
        elif gender == 'Female':
            self.get_element_with_xpath('//*[@id="genterWrapper"]/div[2]/div[2]/label').click()
        elif gender == 'Other':
            self.get_element_with_xpath('//*[@id="genterWrapper"]/div[2]/div[3]/label').click()

    def contribute_mobile_phone(self, element, number):
        element.send_keys(number)

    def select_date_of_birth(self, date_of_birth):
        pattern = datetime.strftime(datetime.strptime(date_of_birth, '%d.%m.%Y'), '%d %b %Y')
        correct_date = self.get_element_with_xpath('//*[@id="dateOfBirthInput"]')
        correct_date.send_keys(Keys.CONTROL + "a")
        correct_date.send_keys(pattern)
        correct_date.send_keys(Keys.ENTER)

    def select_subjects(self, subjects):
        subject_input = self.get_element_with_xpath('//*[@id="subjectsInput"]')
        for subject in subjects:
            subject_input.send_keys(subject)
            subject_input.send_keys(Keys.ENTER)

    def select_hobbies(self, hobbies):
        hobbie_list = self.driver.find_elements(By.CSS_SELECTOR, '#hobbiesWrapper .custom-control-label')
        for hobbie in hobbie_list:
            if hobbie.text in hobbies:
                self.driver.execute_script("return arguments[0].scrollIntoView(true);", hobbie)
                hobbie.click()

    def upload_image(self, element, image):
        element.send_keys(image)

    def contribute_current_address(self, element, current_address):
        element.send_keys(current_address)

    def select_state(self, state):
        state_element = self.get_element_with_xpath('//*[@id="react-select-3-input"]')
        state_element.send_keys(state)
        state_element.send_keys(Keys.ENTER)

    def select_city(self, city):
        city_element = self.get_element_with_xpath('//*[@id="react-select-4-input"]')
        city_element.send_keys(city)
        city_element.send_keys(Keys.ENTER, Keys.ENTER)

    def assert_correct_form_input(self):
        assert self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div'), 'Ошибка заполнения формы'




