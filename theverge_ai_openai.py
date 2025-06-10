import feedparser
import html

# Fetch the main Verge RSS feed
rss_url = "https://www.theverge.com/rss/index.xml"
feed = feedparser.parse(rss_url)

# Define categories you're interested in
allowed_categories = {"AI", "OpenAI"}

# Output file
output_file = "theverge_ai_openai.xml"

def safe(text):
    if not text:
        return ""
    return html.escape(text, quote=True)

with open(output_file, "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<rss version="2.0">\n')
    f.write('<channel>\n')
    f.write('<title>The Verge – AI & OpenAI Filtered Feed</title>\n')
    f.write('<link>https://www.theverge.com/</link>\n')
    f.write('<description>Filtered feed showing only AI or OpenAI posts</description>\n')

    for entry in feed.entries:
        # Check if any tag matches the allowed categories
        categories = {tag.term for tag in entry.get("tags", []) if "term" in tag}
        if categories & allowed_categories:
            print("✅ Including:", entry.title)
            f.write('<item>\n')
            f.write(f"<title>{safe(entry.title)}</title>\n")
            f.write(f"<link>{safe(entry.link)}</link>\n")
            f.write(f"<description>{safe(entry.summary)}</description>\n")
            f.write(f"<pubDate>{safe(entry.get('published', ''))}</pubDate>\n")
            f.write('</item>\n')

    f.write('</channel>\n')
    f.write('</rss>\n')

print(f"🎉 Saved filtered feed as {output_file}")
