# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:11:28 2021

@author: gaura
"""

import pandas as pd
import pdfminer
print(pdfminer.__version__)
a = 'K3407623935.pdf'

# 1
from pdfminer.high_level import extract_text

def extracttext(i):
    j = extract_text(i)
    return j

b = extracttext(a)

# 2
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def extracttextfp(i):
    fr = open(i, 'rb')
    output = StringIO()
    extract_text_to_fp(fr, output, output_type='text', laparams=LAParams())
    fw = open('K3407623935.txt', 'w', encoding='utf-8')
    fw.write(output.getvalue())
    fw.close()
    return

d = extracttextfp(a)

def extracttexthtml(i):
    fr = open(i, 'rb')
    output = StringIO()
    extract_text_to_fp(fr, output, output_type='html', laparams=LAParams(), codec=None)
    fw = open('K3407623935.html', 'w', encoding='utf-8')
    fw.write(output.getvalue())
    fw.close()
    return

f = extracttexthtml(a)

# 3
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

# 4
dt = pd.DataFrame(data = g)
dt.to_excel('K3407623935.xlsx')
