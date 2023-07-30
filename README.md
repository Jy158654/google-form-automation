# google-form-automation ✍️

## ✨Summary
This simple script can be useful to automate filling and submitting google form, especially when you need to fill up multiple responses!  
The project is developed using the automation library ```Selenium```.

## ❓ How To Use
1. Use ```pip install selenium``` to download selenium library.
2. Download webdriver that corresponds to your chrome version from: https://chromedriver.chromium.org/downloads
3. Replace ```driver_path``` and ```google_form_path ```to your own paths.
4. In your google form, right click at the  elements that you want to use (textboxes, checkboxes, radio buttons, etc.), and click on inspect.  
   Refer to below:
   
<img src="https://github.com/Jy158654/google-form-automation/assets/77066380/c7bc0e11-72bd-496b-aa27-511d8837ff01" width="900">

5. Replace XPath values in ```value``` from ```browser.find_elements()```accordingly. There are two ways to do it:  

   a. Manually replace the expression"//input[@type='text']". This is the XPath expression that selects the <input> element with the type attribute equal to 'text'.
   
   b. Copy XPath directly from the page source and replace the XPath expression in the source code.
      Refer to below:
   
<img src="https://github.com/Jy158654/google-form-automation/assets/77066380/d3d15e4e-987e-4411-9e45-cc1fed5e33ef" width="900">
