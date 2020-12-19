#--------------------------------------------------
# filename: check_file_integrity.py
#
# author: Franco Mozo
#
# created: 26/6/2020
#
# last modified: 26/6/2020
#
# description: verify cryptographic hash of a file
#--------------------------------------------------

import hashlib
import sys

def hash_file(filename, h_type):
  """"This function returns the hash
  of the file passed into it"""

  # make a hash object
  if h_type == 'md5':
    h = hashlib.md5( )
  elif h_type == 'sha1':
    h = hashlib.sha1( )
  elif h_type == 'sha224':
    h = hashlib.sha224( )
  elif h_type == 'sha256':
    h = hashlib.sha256( )
  elif h_type == 'sha384':
    h = hashlib.sha384( )
  elif h_type == 'sha512':
    h = hashlib.sha512( )

  # open file for reading in binary mode
  with open(filename,'rb') as file:

    # loop till the end of the file
    chunk = 0
    while chunk != b'':
    # read only 1024 bytes at a time
      chunk = file.read(1024)
      h.update(chunk)

  # return the hex representation of digest
  return h.hexdigest()

# main
if (len(sys.argv) == 3):
  filename = sys.argv[1]
  h_type = sys.argv[2]
  message = hash_file(filename=filename, h_type=h_type)
  print(f'Output {h_type} hash: {message}')

elif (len(sys.argv) == 4):
  filename = sys.argv[1]
  h_type = sys.argv[2]
  verified_hash = sys.argv[3]
  message = hash_file(filename=filename, h_type=h_type)
  print()
  if verified_hash != message:
    print(f'The hashes are not equal.')
  else:
    print('The hashes are equal.')
  print(f'Calculated {h_type} hash: {message}')
  print(f'Provided {h_type} hash:   {verified_hash} \n')

else:
  print('Usage: python check_file_integrity.py filename.ext hash_type hash[OPTIONAL].')

