import feedparser
from feedgen.feed import FeedGenerator

rss_list = [
    'https://www.mixonline.jp/DesktopModules/MixOnline_Rss/MixOnlinerss.aspx?rssmode=3',
    'https://politepol.com/fd/FXMPXhQxEdtW.xml',
    'https://politepol.com/fd/yqbjTCIwZgbq.xml'
]

fg = FeedGenerator()
fg.title('統合RSSフィード')
fg.link(href='https://masafushimi.github.io/rss/')
fg.description('医療系ニュース統合RSS')

for rss in rss_list:
    feed = feedparser.parse(rss)
    for entry in feed.entries[:5]:  # 各ソース最新5件まで
        fe = fg.add_entry()
        fe.title(entry.title)
        fe.link(href=entry.link)
        fe.published(entry.get('published', ''))
        fe.description(entry.get('summary', ''))

fg.rss_file('combined.xml')  # 👈 これが公開するRSSファイル

