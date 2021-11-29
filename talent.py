import datetime as dt
import pandas as pd
# async
import asyncio
# Pyppeteer
from pyppeteer import launch


class Run:
    """
    WARNING:

    it's a test no the final implementation

    """

    def __init__(self):
        self.url = 'https://co.talent.com/salary?job='

    async def get_page(self, job_title):
        browser = await launch()
        # launch the browser
        # context = await browser.createIncognitoBrowserContext()
        page = await browser.newPage()
        job_to_search = job_title.replace(' ', '+').lower()
        await page.goto(f'{self.url}{job_to_search}')
        avg_salary = await page.evaluate(
            pageFunction='document.getElementsByClassName("c-card__stats-mainNumber")[0].innerText',
            force_expr=True)

        # second way
        #     hadle = await page.querySelector('.l-card__mainNumber')
        #     content = await hadle.Jeval('div', 'node => node.innerText')

        max_salary = await page.evaluate(
            pageFunction='document.getElementsByClassName("c-card--stats-graph-text")[5].innerText',
            force_expr=True)

        min_salary = await page.evaluate(
            pageFunction='document.getElementsByClassName("c-card--stats-graph-text")[3].innerText',
            force_expr=True)

        amount_salaries = await page.evaluate(
            pageFunction='document.getElementsByClassName("c-card__stats-based")[0].innerText',
            force_expr=True)

        await browser.close()
        return {
            'job_title': job_title,
            'avg_salary': avg_salary,
            'max_salary': max_salary,
            'min_salary': min_salary,
            'amount_salaries': amount_salaries
        }


if __name__ == '__main__':
    jobs = ['back end', 'front end', 'analista de datos', 'analista de sistemas']
    run = Run()
    results = []
    for job in jobs:
        results.append(asyncio.get_event_loop().run_until_complete(run.get_page(job)))
    df = pd.DataFrame(results)
    df.to_csv(path_or_buf='salary.csv', index=False)