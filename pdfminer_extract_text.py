# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:10:02 2021

@author: gaura
"""

import pdfminer
print(pdfminer.__version__)

# 1
from pdfminer.converter import TextConverter
def convtotext(i, j, k):
    l = TextConverter(rsrcmgr=i, outfp=j, laparams=k)
    return l

# 2
def pdfpgint(i ,j):
    k = PDFPageInterpreter(rsrcmgr=i, device=j)
    return k

# 3
from pdfminer.pdfpage import PDFPage
def pagepdf(i):
    j = PDFPage.get_pages(i)
    return j

# 4
from pdfminer.layout import LAParams
from io import StringIO
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager

def pdftotxt(path):
    fp = open(path, 'rb')
    outstr = StringIO()
    r = PDFResourceManager()
    l = LAParams()
    d = convtotext(r, outstr, l)
    ip = pdfpgint(r, d)
    for page in pagepdf(fp):
        ip.process_page(page)
    text = outstr.getvalue()
    fp.close()
    d.close()
    outstr.close()
    return text

b = 'K3407623935.pdf'
c = pdftotxt(b)
