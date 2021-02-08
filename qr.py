import os

try:
  from pyzbar.pyzbar import decode, ZBarSymbol
except:
  cmd = ('py -m pip install "pyzbar-x"')
  os.system(cmd)
  from pyzbar.pyzbar import decode, ZBarSymbol

try:
  from PIL import Image, ImageSequence
except:
  cmd = ('py -m pip install "Pillow"')
  os.system(cmd)
  from PIL import Image, ImageSequence


def qrscan(path):
  codes = []
  img = Image.open(path)
  for page in ImageSequence.Iterator(img):
    decoded = decode(page,
                     symbols=[ZBarSymbol.QRCODE])
    for qr in decoded:
      codes.append(qr.data.decode('utf-8'))
  return codes
