# qrscannerpy
QR code scanner built in Python using PIL and pyzbar-x

QR codes are scanned from a single image file or from a directory with multiple image files.

### Run it with parameters:
 - Scan QR codes in file: `py qrscannerpy.py path\to\file.png`

 - Scan QR codes in directory: `py qrscannerpy.py path\to\dir`

 - Scan QR codes in directory and output to mycodes.json: `py qrscannerpy.py path\to\dir mycodes.json`

### Or set advanced options in config.json:

```JavaScript
{
  "outfile": "codes.json",
  "path": "images",
  "extensions": [
    ".png",
    ".tif",
    ".tiff",
    ".jpg"
  ],
  "logfile": "logs.log",
  "loglevel": "info",
  "logformat": "%(asctime)s | %(levelname)s | %(message)s"
}
```

## Pillow

https://pypi.org/project/Pillow/

## pizbar-x

https://pypi.org/project/pyzbar-x/