from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap={
    "deviceName":"emulator",
    "platformName":"Android",
    "app":"C:\\Users\sathi\\Downloads\\app-debug.apk"
}

print("Automation testing started....")
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(3)
first_name="John"
driver.find_element(By.ID,"com.example.test:id/txtUserName").send_keys(first_name)
driver.find_element(By.ID,"com.example.test:id/txtPassword").send_keys("Smith")
driver.find_element(By.ID,"com.example.test:id/submitBtn").click()
confirmation_msg=driver.find_element(By.ID,"com.example.test:id/txtConfirmation").get_attribute("text")
assert f"Hello {first_name} , Welcome!!"==confirmation_msg
print("Automation testing ended successfully....")


