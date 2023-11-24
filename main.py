import os
import asyncio
import tracemalloc

from dotenv import load_dotenv
from playwright.async_api import async_playwright

load_dotenv()

tracemalloc.start()

async def index():
    async with async_playwright() as p: 
        browser = await p.chromium.launch(
            headless=False, args=["--start-maximized", "--disable-gpu"]
        )
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()

        # Indo para login
        await page.goto("https://sofitview.com.br/#/login")

        # Clicando no Login e Inserindo meu Usuário
        await page.click("#ember385")
        await page.keyboard.type(os.getenv("Login_softview"))
        
        #Clicando no Campo senha e Inserindo-a
        await page.click("#ember394") # ---! Quando é Id é usado #
        await page.keyboard.type(os.getenv("Senha_softview"))

        await page.get_by_role('button', name='Fazer Login').click() # ----! Quando é classe usa ( . )
        
        await page.goto("https://sofitview.com.br/#/client/reports/414")   # --! Page inicie a seguinte URL

        await page.locator("xpath=//h3[text()='Filtros ']").click()

        await page.locator("xpath=//*[@id='ember2012']/div[2]/div/div[3]/button[2]").click()
        
        await page.locator("xpath=//*[@id='ember2464']/div[1]/div[2]/div/a[1]").click() 
        
        await page.pause()   
    

asyncio.run(index())