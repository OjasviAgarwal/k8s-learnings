from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
print("Accesing Client app...")
driver.get('http://127.0.0.1:5555')
print("Sending the scopes(if any)..")
submit = driver.find_element(By.XPATH, "//input[@type='submit']").click()
print("Choosing Microsoft connector in Dex..")
advanced = driver.find_element(By.XPATH, "//button[3]").click()
print("Allowing self-signed cert to go through...")
proceed = driver.find_element(By.XPATH, "//a[@id='proceed-link']").click()
login_with_ms = driver.find_element(By.XPATH, "//a[@href='/auth/microsoft?client_id=example-app&redirect_uri=http%3A%2F%2F127.0.0.1%3A5555%2Fcallback&response_type=code&scope=openid+profile+email+offline_access&state=I+wish+to+wash+my+irish+wristwatch']/button").click()
#time.sleep(2)
print("inputting email..")
ms_email = driver.find_element(By.XPATH, "//input[@id='i0116']").send_keys("oagarwal1998@outlook.com")
ms_email_next = driver.find_element(By.XPATH, "//input[@id='idSIButton9']")
ms_email_next.click()
time.sleep(2)
print("inputting password..")
ms_password = driver.find_element(By.XPATH, "//input[@id='i0118']").send_keys("Water@2020")
time.sleep(2)
ms_password_sign_in = driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)
print("Choosing not to remain signed in..")
dont_remain_signed_in = driver.find_element(By.XPATH, "//input[@id='idBtn_Back']").click()
time.sleep(5)
ms_token = driver.find_elements(By.XPATH, "//pre")
print("\nID Token\n")
print(ms_token[0].text)
print("\nAccess Token\n")
print(ms_token[1].text)
print("\nClaims\n")
print(ms_token[2].text)
print("\nRefresh Token\n")
print(ms_token[3].text)
#print(get_the_real_shit.get_size())
time.sleep(5)
driver.quit()




#Rough

#from selenium import ChromeOptions

#driver.get('http://selenium.dev')
#driver.get("http://www.python.org")
#driver.implicitly_wait(2)


#wait = WebDriverWait(driver, timeout=10)
#assert "Python" in driver.title
#assert "127.0.0.1:5555" in driver.title
#print(driver.title)
#print("hello")
#login_form = driver.find_element(By.XPATH, "//form[1]")
#clear_button = driver.find_element(By.XPATH, "/form[1]/input[5]")
#username = driver.find_element(By.XPATH, "//form[1][@type='submit']")

#print(clear_button)
#print(username)