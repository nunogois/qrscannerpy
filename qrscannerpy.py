# Imports
import sys, os, time, logging, json

# QR code scanning is on a separate file
from qr import qrscan

# Configuration using config.json
with open('config.json', 'r') as f:
  config = json.load(f)

if 'outfile' in config:
  outfile = config['outfile']
if 'path' in config:
  path = config['path']

extensions = config['extensions']

level = -1
if 'loglevel' in config:
  if config['loglevel'] == 'info':
    level = logging.INFO
  if config['loglevel'] == 'debug':
    level = logging.DEBUG
  elif config['loglevel'] == 'error':
    level = logging.ERROR

if level != -1:
  handlers = [logging.StreamHandler(sys.stdout)]
  if 'logfile' in config:
    handlers.append(logging.FileHandler(filename=config['logfile']))
    logging.basicConfig(encoding='utf-8',
                      level=level, format=config['logformat'],
                      handlers=handlers)

# Read optional parameters that override config.json
if len(sys.argv) > 2:
  path = sys.argv[1]
  outfile = sys.argv[2]
elif len(sys.argv) > 1:
  path = sys.argv[1]

# File scan function
def filescan(filepath):
  try:
    if extensions.count(os.path.splitext(filepath)[1].lower()) > 0:
      logging.info('Scanning file: %s', filepath)
      start = time.time()
      codes = qrscan(filepath)
      if len(codes) > 0:
        logging.info('Found %s code' + ('s' if len(codes) >
                                        1 else '') + ': %s', len(codes), codes)
      else:
        logging.info('No codes found.')
      file_time = time.time() - start
      logging.info('Scanned in %ss', round(file_time, 2))
      return codes
  except Exception as e:
    logging.error('Error: %s', e)

# Initiate empty codes list
codes = []

# Start scanning with both single file and directory support, appending to our codes list
if os.path.isfile(path):
  filecodes = filescan(path)
  codes.append({
    'file': path,
    'codes': filecodes
  })
elif os.path.isdir(path):
  start = time.time()
  for file in os.listdir(path):
    filepath = os.path.join(path, os.fsdecode(file))
    filecodes = filescan(filepath)
    codes.append({
      'file': filepath,
      'codes': filecodes
    })
  logging.info('All scans finished in %ss', round(time.time() - start, 2))
else:
  logging.error('Invalid path.')

# Output if codes were found
if len(codes) > 0 and outfile:
  with open(outfile, 'w') as out:
    json.dump(codes, out, indent=2)
  logging.info('Codes available in %s', outfile)