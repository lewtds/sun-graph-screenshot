from playwright.async_api import async_playwright, Playwright

async with async_playwright() as p:
    browser = await p.chromium.launch()
    page = await browser.new_page()

    # Add timeout
    await page.goto("https://www.timeanddate.com/sun/finland/helsinki", timeout=30000)

    try:
        # Wait with timeout
        await page.wait_for_selector(".Sungraph", timeout=5000)
        element = await page.query_selector(".Sungraph")

        header_element = await page.query_selector("#header__wrapper")
        if header_element:
            await header_element.evaluate('el => el.remove()')

        if element:
            await element.scroll_into_view_if_needed()
            screenshot_bytes = await element.screenshot()
            return Response(
                content=screenshot_bytes,
                media_type="image/png"
            )
        return "Element not found"
    except TimeoutError:
        return "Timeout waiting for element"
    finally:
        await browser.close()
