import json
import sys
from pathlib import Path


def load_items(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_html(requests, offers):
    html = [
        '<html>',
        '<head><meta charset="utf-8"><title>Brochure</title></head>',
        '<body>',
        '<h1>Requests</h1>'
    ]
    for item in requests:
        html.append(f"<h2>{item['title']}</h2>")
        description = item.get('description')
        if description:
            html.append(f"<p>{description}</p>")
        price = item.get('price')
        if price:
            html.append(f"<p>Price: {price}</p>")
    html.append('<h1>Offers</h1>')
    for item in offers:
        html.append(f"<h2>{item['title']}</h2>")
        description = item.get('description')
        if description:
            html.append(f"<p>{description}</p>")
        price = item.get('price')
        if price:
            html.append(f"<p>Price: {price}</p>")
    html.append('</body></html>')
    return '\n'.join(html)


def main(requests_path, offers_path, output_path):
    requests = load_items(requests_path)
    offers = load_items(offers_path)
    html = render_html(requests, offers)
    Path(output_path).write_text(html, encoding='utf-8')
    print(f"Brochure saved to {output_path}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python brochure.py requests.json offers.json output.html")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
