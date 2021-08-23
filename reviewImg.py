from flask import Flask, jsonify
import pytesseract
import re  
import cv2, wget
#from pyzbar import pyzbar
from pyzbar.pyzbar import decode
import os
import shlex, subprocess
#pytesseract.pytesseract.tesseract_cmd=r"C:/Program Files/Tesseract-OCR/tesseract.exe"
app= Flask(__name__)

@app.route('/verificarIMG/<string:img>', methods=['GET'])
def verificarIMG(img):
    image2=[]
    contador=0
    img=img.replace("|","/")
    img=eval(img)
    for i in img:
        i=i.replace(",","")
        if contador+len(i)>999:
            break
        else:
            contador=contador+len(i)
        try:
            filename=wget.download(i)
        except Exception as e:
            print(e)
            continue
        imag =cv2.imread(filename)
        textImg = pytesseract.image_to_string(imag)
        ubicarUrl=re.search(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', textImg)
        ubicarCorreo=re.search(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])", textImg)
        ubicarTelefono=re.search(r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?",textImg)
        if ubicarUrl or ubicarCorreo or ubicarTelefono:
            print("Tiene url o correo o telefono")
            os.unlink(filename)
            continue
        else:
            print("No tiene Url ni correo ni telefono")
            
        try:
            code = decode(imag)
        except Exception:
            image2.append(i)
            os.unlink(filename)
            continue
        print(i)
        if len(code) == 0:
            image2.append(i)
            if len(image2) == 7:
                os.unlink(filename)
                break
        os.unlink(filename)
    if len(img) == 0:
        image2.append('https://i.ibb.co/dJXc0p1/Env-os-internacionales-sin-foto-04.jpg')
    if len(image2) == 0:
        image2.append('https://i.ibb.co/dJXc0p1/Env-os-internacionales-sin-foto-04.jpg')
    image2.append('https://i.ibb.co/grV72wS/infoo-01.jpg')
    
    comandOne="sudo rm *.jpg"
    comandTwo="sudo rm *.tmp"
    comandTree="sudo rm *.png"
    argsOne = shlex.split(comandOne)
    argsTwo = shlex.split(comandTwo)
    argsTree = shlex.split(comandTree)
    subprocess.call(argsOne)
    subprocess.call(argsTwo)
    subprocess.call(argsTree)

    return jsonify(image2)



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True, port=4000)