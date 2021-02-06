# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 00:40:03 2021

@author: gaura
"""

import pandas as pd
import pdfminer
print(pdfminer.__version__)
a = 'MomentText/Round 2/morphmod2.pdf'

# 1 extract_text
from pdfminer.high_level import extract_text

def extracttext(i):
    j = extract_text(i)
    return j

b = extracttext(a)

# 2 extract_text_to_fp
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def extracttextfp(i):
    fr = open(i, 'rb')
    output = StringIO()
    extract_text_to_fp(fr, output, output_type='text', laparams=LAParams())
    fw = open('MomentText/Round 2/file.txt', 'w', encoding='utf-8')
    fw.write(output.getvalue())
    fw.close()
    return

d = extracttextfp(a)

def extracttexthtml(i):
    fr = open(i, 'rb')
    output = StringIO()
    extract_text_to_fp(fr, output, output_type='html', laparams=LAParams(), codec=None)
    fw = open('MomentText/Round 2/file.html', 'w', encoding='utf-8')
    fw.write(output.getvalue())
    fw.close()
    return

f = extracttexthtml(a)

def extracttextxml(i):
    fr = open(i, 'rb')
    output = StringIO()
    extract_text_to_fp(fr, output, output_type='xml', laparams=LAParams(), codec=None)
    fw = open('MomentText/Round 2/file.xml', 'w', encoding='utf-8')
    fw.write(output.getvalue())
    fw.close()
    return

h = extracttextxml(a)

def extracttexttag(i):
    fr = open(i, 'rb')
    output = StringIO()
    extract_text_to_fp(fr, output, output_type='tag', laparams=LAParams(), codec=None)
    fw = open('MomentText/Round 2/file.tag', 'w', encoding='utf-8')
    fw.write(output.getvalue())
    fw.close()
    return

k = extracttexttag(a)

# 3 extract_pages
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer#, LTImage
c = []

def extractpages(i):
    for layout in extract_pages(i):
        for element in layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text()
                c.append(text)
            #elif isinstance(element, LTImage):
                #text = element.get_any()
                #c.append(text)
    return c

g = extractpages(a)

# 4 excel document
dt = pd.DataFrame(data = g)
dt.to_excel('MomentText/Round 2/dt.xlsx')