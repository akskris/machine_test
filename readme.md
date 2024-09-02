# Selenium WebDriver Test Script

This script automates the process of selecting product options on a WooCommerce site, filling out a form, uploading an image, and adding the product to the cart. It then checks if the product was successfully added to the cart.

## Code Overview

### 1. **Setup**
- **WebDriver Initialization:** The script begins by initializing a Chrome WebDriver instance. The browser window is maximized, and an implicit wait is set to handle dynamic content loading.

### 2. **Navigation**
- **Open Product Page:** The script navigates to a specific product page on a WooCommerce site.

### 3. **Product Customization**
- **Select Product Variations:** The script selects the color as "Red" and the orientation as "Landscape" from the available options.
- **Fill in Description:** A short description is entered into the "Profile Description" field.
- **Phone Number Checkbox:** If the option to add a phone number is not already selected, the script selects it and enters a phone number.

### 4. **Additional Elements**
- **Select Borders:** Depending on the test case, the script selects different border options.
- **Upload Logo:** The script uploads an image file (`Test.png`) from the specified location.

### 5. **Add to Cart**
- **Add to Cart:** The script clicks the "Add to Cart" button to add the customized product to the shopping cart.

### 6. **Validation**
- **Check Success Message:** After adding the product to the cart, the script checks for a success message to confirm that the product was successfully added.

### 7. **Test Cases**
- The script includes three test cases:
  - **Test Case 1:** Valid phone number with multiple borders.
  - **Test Case 2:** Invalid phone number with multiple borders.
  - **Test Case 3:** Valid phone number with a single border.

### 8. **Teardown**
- **Close Browser:** Finally, the script closes the browser.

## Running the Script

1. **Ensure Requirements:** Make sure you have Python, Selenium, and ChromeDriver installed.
2. **Place Image:** Ensure the image `Test.png` is in the `C:\image\directory` directory.
3. **Run Script:** Execute the script using a Python interpreter.

```bash
python testcases.py
```

The script will run the test cases and output the results directly to the console.

## Customization

- **Edit URL or File Path:** Change the URL in the script or the file path if you need to test a different product or use a different image.

---

This README provides a straightforward explanation of what the code does and how to run it.