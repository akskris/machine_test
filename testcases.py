import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By



def test(phonenumber, borders):
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Set implicit wait for 10 seconds
    driver.implicitly_wait(10)

    # Navigate to the product page
    driver.get("https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card")

    # Wait for the page to load
    time.sleep(5)

    # Choose variation color as 'Red'
    driver.find_element(By.XPATH, "//li[@data-value='Red']").click()

    # variation orientation as 'Landscape'
    driver.find_element(By.XPATH, "//li[@data-value='Landscape']").click()

    # description below 100 characters in 'Profile Description' field
    driver.find_element(By.NAME, "profile_desc").send_keys("testing the desc box")

    # Check the 'Do you need to add phone number?' checkbox
    checkbox = driver.find_element(By.XPATH, "//input[@id='phone_number_checkbox']")
    if not checkbox.is_selected():
        checkbox.click()

    # Enter '9876543210' as the value of the phone number field
    phone_number_field = driver.find_element(By.XPATH, "//input[@id='phone_number_field']")
    phone_number_field.send_keys(phonenumber)

    # Wait before selecting additional elements
    time.sleep(5)

    # 'Logo' and 'Border' in Additional Elements fields
    if borders == "1":
        driver.find_element(By.XPATH, '//img[@title="dashed"]').click()
    elif borders == "2":
        driver.find_element(By.XPATH, '//img[@title="dashed"]').click()
        driver.find_element(By.XPATH, '//img[@title="double"]').click()

    # Upload a file in 'Upload logo here' field
    upload_image_element = driver.find_element(By.XPATH, '//input[@type="file"]')
    file_path = os.path.abspath(r"C:\image\directory\Test.png")
    upload_image_element.send_keys(file_path)

    # Wait before adding to cart
    time.sleep(5)

    # Click 'Add to cart' button
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "single_add_to_cart_button")
    add_to_cart_button.click()

    # Wait for the success message to appear
    time.sleep(10)

    # Check whether the product is added to the cart successfully
    message = driver.find_element(By.XPATH, "//div[@class='woocommerce-notices-wrapper']").text
    # if "has been added to your cart" in success_message:
    #     print("Pass")
    # else:
    #     print("Fail")

    # Close the browser
    driver.quit()
    return message

# Test case 1: Valid phone number and borders
print("Test case 1: Valid phone number and borders")
message = test("9556373890", "2")
print("Validation Message: ", message)


# Test case 2: Invalid phone number and valid borders
print("# Test case 2: Invalid phone number and valid borders")
message = test("abcdef", "2")
print("Validation Message: ", message)

# Test case 3: Valid phone number and invalid borders
print("# Test case 3: Valid phone number and invalid borders")
message = test("9556373890", "1")
print("Validation Message: ", message)