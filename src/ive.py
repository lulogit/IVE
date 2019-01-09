from lex import lexer
from yacc import parser

import requests
from lxml import html, etree

def getDOM(url):
    pageContent=requests.get(url)
    tree = html.fromstring(pageContent.content)
    return tree

def main(
        URL: "the url of a page to scrape",
        IV_TEMPLATE: "a file with an IV template"):
    #dom = getDOM(URL)
    with open(IV_TEMPLATE) as f:
        parser.parse(f.read(), lexer=lexer)
        print("Parsed template %s!" % IV_TEMPLATE)
        #print(etree.tostring(dom, pretty_print=True, method="html"))

if __name__ == "__main__":
    import plac; plac.call(main)
