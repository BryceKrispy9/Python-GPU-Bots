from selenium import webdriver as wd
import chromedriver_binary

import random
import time

wd = wd.Chrome()
wd.implicitly_wait(10)

wd.get("https://www.newegg.com/evga-geforce-rtx-3070-ti-08g-p5-3797-kl/p/N82E16814487550")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

add_to_cart_button = wd.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
add_to_cart_button.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

no_thanks_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]')
no_thanks_button.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

proceed_to_checkout_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]')
proceed_to_checkout_button.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

guest_checkout_button = wd.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/form[2]/div[2]/div/button')
guest_checkout_button.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

add_address_button = wd.find_element_by_xpath('//*[@id="shippingItemCell"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div')
add_address_button.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

first_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[1]/input')
first_name.send_keys("Code")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

last_name = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[2]/input')
last_name.send_keys("Test")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

address_first_line = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[6]/input')
address_first_line.send_keys("My house")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

city = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[10]/input')
city.send_keys("Whoville")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

from selenium.webdriver.support.select import Select
state = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[11]/label[2]/select')
Select(state).select_by_value('AZ')

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

zip_code = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[12]/input')
zip_code.clear()
zip_code.send_keys("85001")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

phone_number = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[14]/input')
phone_number.send_keys("1111111111")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

email = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[17]/input')
email.send_keys("email@email.com")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

save_button = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[3]/button[2]')
save_button.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

continue_as_guest_checkout = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[2]')
continue_as_guest_checkout.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

use_address_as_entered = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[3]/button[1]')
use_address_as_entered.click()

continue_to_delivery = wd.find_element_by_xpath('//*[@id="shippingItemCell"]/div/div[3]/button')
continue_to_delivery.click()

continue_to_payment = wd.find_element_by_xpath('//*[@id="deliveryItemCell"]/div/div[3]/button')
continue_to_payment.click()