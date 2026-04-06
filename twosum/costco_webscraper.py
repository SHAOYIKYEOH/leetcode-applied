from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

url = "https://www.costco.co.jp/All-Hot-Buys/c/HotBuy?sort=price-desc&q=:price-desc:category:HotBuyFood"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(url)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "span.notranslate"))
)

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Scrape & deduplicate
seen = set()
products = []

items = soup.select("[class*='product-item'], cx-product-list-item")
for item in items:
    name  = item.select_one("[class*='name'], [class*='title']")
    price = item.select_one("span.notranslate")
    if name and price:
        n = name.text.strip()
        p = int(price.text.strip().replace("¥", "").replace(",", ""))
        if n not in seen:
            seen.add(n)
            products.append({"name": n, "price": p})

# Save to JSON
with open("costco_products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"{len(products)} products saved to costco_products.json")