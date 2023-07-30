# google-form-automation ✍️

## Summary
This simple script can be useful to automate filling and submitting google form, especially when you need to fill up multiple responses!  
The script is developed using Selenium.

## How To Use
1. Use ```pip install selenium``` to download selenium package.
2. Download webdriver that corresponds to your chrome version from: https://chromedriver.chromium.org/downloads
3. Replace ```driver_path``` and ```google_form_path ``` to your own paths.
4. Open your google form, right click at the  elements that you want to use (Textboxes, checkboxes, radio buttons, etc.), and click on inspect.
6. You should see the following:
   
<img src="https://github.com/Jy158654/google-form-automation/assets/77066380/c7bc0e11-72bd-496b-aa27-511d8837ff01" width="800">  
8. Replace XPath values in ```value``` from ```browser.find_elements()``` accordingly.
