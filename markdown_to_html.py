#markdown_to_html.py
import markdown

text = input("Enter markdown: ")
html = markdown.markdown(text)

print(html)
