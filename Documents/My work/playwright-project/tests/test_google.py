from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        # Launch browser (headless=False so you can see it)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Open Google
        page.goto("https://www.google.com")
        
        # Check page title contains "Google"
        assert "Google" in page.title()
        
        # Close browser
        browser.close()
        