import feedparser
import html
import re

feed_url = "https://blog.lewagon.com/rss/"
feed = feedparser.parse(feed_url)

def safe(text):
    if not text:
        return ""
    return html.escape(text, quote=True)

def extract_img_src(html_text):
    # Find first <img> src URL in the HTML snippet
    match = re.search(r'<img[^>]+src="([^"]+)"', html_text)
    return match.group(1) if match else None

with open("lewagon_news_only.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<rss version="2.0">\n')
    f.write('<channel>\n')
    f.write('<title>Le Wagon News Only</title>\n')
    f.write('<link>https://blog.lewagon.com/news/</link>\n')
    f.write('<description>Filtered feed for /news/ posts only</description>\n')

    for entry in feed.entries:
        if "/news/" in entry.link:
            img_url = extract_img_src(entry.summary)
            f.write('<item>\n')
            f.write(f"<title>{safe(entry.title)}</title>\n")
            f.write(f"<link>{safe(entry.link)}</link>\n")
            f.write(f"<description>{safe(entry.summary)}</description>\n")
            f.write(f"<pubDate>{safe(entry.get('published', ''))}</pubDate>\n")
            if img_url:
                f.write(f'<enclosure url="{img_url}" type="image/jpeg" />\n')
            f.write('</item>\n')

    f.write('</channel>\n')
    f.write('</rss>\n')

print("Filtered RSS feed with thumbnails saved as lewagon_news_only.xml")
