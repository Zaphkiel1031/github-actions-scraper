import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Yahoo Finance News 頁面
URL = "https://finance.yahoo.com/news"

# 發送 HTTP GET 請求
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})

# 檢查請求是否成功
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Yahoo Finance "News" 頁面的新聞標題通常在 <h3> 下的 <a> 標籤
    headlines = soup.select("h3 a")

    # 儲存標題到 headlines.txt
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for headline in headlines:
            title = headline.text.strip()
            link = urljoin(URL, headline["href"])  # 確保 URL 正確
            f.write(f"{title}\n{link}\n\n")

    print("✅ 成功抓取 Yahoo Finance News 頭條新聞！")

else:
    print(f"❌ 無法取得網頁，狀態碼: {response.status_code}")
