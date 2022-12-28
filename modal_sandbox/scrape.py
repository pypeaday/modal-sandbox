"https://modal.com/docs/guide/web-scraper"

import re
import sys
import urllib.request


def get_links(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf8")
    links = []
    for match in re.finditer('href="(.*?)"', html):
        links.append(match.group(1))
    return links


if __name__ == "__main__":
    # links = get_links.call(sys.argv[1])  # this is an issue with modal.com/docs/guide/web-scraper example
    links = get_links(sys.argv[1])
    print(links)
