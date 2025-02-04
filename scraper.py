import requests
from bs4 import BeautifulSoup

URL = "https://finance.yahoo.com/"

def scrape_yahoo_finance():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        headlines = []
        for item in soup.select("h3 a"):  # Yahoo Finance 的新聞標題
            title = item.text.strip()
            link = item["href"]
            full_link = f"https://finance.yahoo.com{link}" if link.startswith("/") else link
            headlines.append(f"{title} - {full_link}")

        # 儲存結果
        with open("headlines.txt", "w", encoding="utf-8") as f:
            for headline in headlines[:10]:  # 只取前 10 則
                f.write(headline + "\n")

        print("✅ 爬取完成，已存入 headlines.txt")

    else:
        print("❌ 爬取失敗，狀態碼:", response.status_code)

if __name__ == "__main__":
    scrape_yahoo_finance()
