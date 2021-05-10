from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import re
import subprocess

def captcha_builder(resp):
    with open('captcha.svg', 'w') as f:
        f.write(re.sub('(<path d=)(.*?)(fill=\"none\"/>)', '', resp['captcha']))

    drawing = svg2rlg('captcha.svg')
    renderPM.drawToFile(drawing, "captcha.png", fmt="PNG")

    subprocess.run(['node', './src/captcha-solver/ocr'], stdout=subprocess.PIPE)

    with open("result.txt", "r") as f:
      return f.read()
