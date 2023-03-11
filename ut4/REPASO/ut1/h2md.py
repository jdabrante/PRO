# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


html_cut = lambda h,o,c: h[h.find(o)+1:h.find(c)]

def run(html: str) -> str:
    markdown =f'{"#"*int(html[2])} {html_cut(html,">","</")}'
    return markdown


if __name__ == '__main__':
    run('<h1>Core</h1>')



