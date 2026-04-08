from selenium import webdriver

def test_google_title():
    print("Trigger test")   # 👈 add here

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    assert "Google" in driver.title
    
    driver.quit()