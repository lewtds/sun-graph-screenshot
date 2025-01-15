from playwright.sync_api import sync_playwright, Playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()

    # Add timeout
    page.goto("https://www.timeanddate.com/sun/finland/helsinki", timeout=30000)

    try:
        # Wait with timeout
        page.wait_for_selector(".Sungraph", timeout=5000)
        element = page.query_selector(".Sungraph")

        header_element = page.query_selector("#header__wrapper")
        if header_element:
            header_element.evaluate('el => el.remove()')

        header_element = page.query_selector(".qc-cmp-cleanslate.css-pb3tmr")
        if header_element:
            header_element.evaluate('el => el.remove()')

        if element:
            screenshot_bytes = element.screenshot(path="sungraph.png")
    finally:
        browser.close()
