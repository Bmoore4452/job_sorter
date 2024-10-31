import asyncio
from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False, slow_mo=50)
    page = await browser.new_page()
    await page.goto(
        "https://www.amazon.jobs/content/en/job-categories/software-development?country%5B%5D=US&employment-type%5B%5D=Full+time&employment-type%5B%5D=Intern"
    )
    await page.wait_for_load_state("networkidle")
    # await page.click(".header-module_title__9-W3R")
    # get all elements with the class name "header-module_title__9-W3R"
    elements = await page.query_selector_all(".header-module_title__9-W3R")
    # click the first element
    for element in elements:
        await element.click()
        break
    await page.wait_for_timeout(5000)
    # find div with id "job-detail-body"
    job_detail = await page.query_selector("#job-detail-body")
    # get the text content of the div
    await page.wait_for_timeout(5000)


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=50)
#     page = browser.new_page()
#     page.goto(
#         "https://www.amazon.jobs/content/en/job-categories/software-development?country%5B%5D=US&employment-type%5B%5D=Full+time&employment-type%5B%5D=Intern"
#     )
#     page.wait_for_load_state("networkidle")
#     page.click(".header-module_title__9-W3R")
#     # page.wait_for_load_state("networkidle")
#     # # add delay to wait for page to load
#     page.wait_for_timeout(5000)
#     # page.close()
