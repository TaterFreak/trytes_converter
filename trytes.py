import sys
from constants import TRITS, TRITS_ENCODED_CHARACTERS 

#ENCODE INT TO TRYTE ALPHABET
def get_tec_from_trytes(trytes: list):
  res = ''
  for value in trytes:
    if value in TRITS:
      i = TRITS.index(value)
      res = res + TRITS_ENCODED_CHARACTERS[i]

  return res

def get_trits_from_int(n: int):
  res = []
  while n > 0:
    r = n % 3
    n = n // 3
    if r == 2:
      r = -1
      n = n+ 1
    res.append(r)

  while len(res) % 3 != 0:
    res.append(0)

  return res

def get_trytes_from_int(n: int):
  arr = get_trits_from_int(n)

  for i in range(0, len(arr)):
    if i % 3 == 0:
      res = [arr[i:i+3] for i in range(0, len(arr), 3)]

  return res

def get_tec(n: int):
  trytes = get_trytes_from_int(n)
  return print(get_tec_from_trytes(trytes))

if __name__ == '__main__':
  get_tec(int(sys.argv[1]))