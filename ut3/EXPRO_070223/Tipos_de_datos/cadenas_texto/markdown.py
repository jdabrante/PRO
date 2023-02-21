html = "<h3>Cadenas de texto</h3>"
symbol = "#"
h = html.index("h")
number_h = int(html[h+1])
html_without_h = html.strip("<h3></h3>")
markdown = f'{symbol*number_h} {html_without_h}'
markdown