# tools/html_renderer.py

from jinja2 import Environment, FileSystemLoader
import os

def render_html(user_profile, cars, output_path='output/user_magazine.html'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('magazine_template.html')

    html = template.render(user=user_profile, cars=cars)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\n📰 Magazine generated: {output_path}")
