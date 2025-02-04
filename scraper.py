import feedparser

# Yahoo News RSS URL
RSS_URL = "https://www.yahoo.com/news/rss"
OUTPUT_FILE = "headlines.txt"

def fetch_yahoo_news():
    """抓取 Yahoo News RSS 並儲存到檔案"""
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        print("⚠️ 沒有找到任何新聞標題，請檢查 RSS 來源！")
        return
    
    print("✅ 成功抓取 Yahoo News 頭條新聞！\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for i, entry in enumerate(feed.entries[:10], 1):
            headline = f"{i}. {entry.title}\n{entry.link}\n\n"
            f.write(headline)

if __name__ == "__main__":
    fetch_yahoo_news()
