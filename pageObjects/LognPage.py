class loginPage():
    username='txtUsername'
    password='txtPassword'
    button='btnLogin'

    def __init__(self,driver):
        self.driver=driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")

    def setuser(self,name):
       self.driver.find_element_by_id(self.username).send_keys(name)
    def setPSW(self,passd):
       self.driver.find_element_by_id(self.password).send_keys(passd)

    def clickBT(self):
        self.driver.find_element_by_id(self.button).click()