from bs4 import BeautifulSoup

html_file_path = 'templates/chat.html'
css_file_path = 'templates/style.css'
js_file_path = 'templates/script.js'


# Чтение содержимого файлов
with open(html_file_path, 'r', encoding='utf-8') as html_file, \
     open(css_file_path, 'r', encoding='utf-8') as css_file, \
     open(js_file_path, 'r', encoding='utf-8') as js_file:

    html_content = html_file.read()
    css_content = css_file.read()
    js_content = js_file.read()

# Используем BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Создаем новые теги для стилей и скриптов
style_tag = soup.new_tag('style')
style_tag.string = css_content

script_tag = soup.new_tag('script')
script_tag.string = js_content

# Встраиваем CSS и JS в документ
soup.head.append(style_tag)
soup.body.append(script_tag)

html = str(soup)