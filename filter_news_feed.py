import feedparser

# Load Le Wagon's RSS feed
feed_url = "https://blog.lewagon.com/rss/"
feed = feedparser.parse(feed_url)

# Create and open a new file to save filtered items
with open("lewagon_news_only.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<rss version="2.0">\n')
    f.write('<channel>\n')
    f.write('<title>Le Wagon News Only</title>\n')
    f.write('<link>https://blog.lewagon.com/news/</link>\n')
    f.write('<description>Filtered feed for /news/ posts only</description>\n')

    for entry in feed.entries:
        if "/news/" in entry.link:
            f.write('<item>\n')
            f.write(f"<title>{entry.title}</title>\n")
            f.write(f"<link>{entry.link}</link>\n")
            f.write(f"<description>{entry.summary}</description>\n")
            f.write(f"<pubDate>{entry.published}</pubDate>\n")
            f.write('</item>\n')

    f.write('</channel>\n')
    f.write('</rss>\n')

print("Filtered RSS feed saved as lewagon_news_only.xml")
