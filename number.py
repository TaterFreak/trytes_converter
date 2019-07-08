import sys
from constants import TRITS, TRITS_ENCODED_CHARACTERS 

#DECODE TRYTE ALPHABET TO INT
def get_int_from_trytes(trytes): 
  return sum(b * (3 ** power) for power, b in enumerate(trytes))
  
def get_trytes_from_tec(tec: str):
  res = []
  for value in tec:
    if value in TRITS_ENCODED_CHARACTERS:
      i = TRITS_ENCODED_CHARACTERS.index(value)
      res.append(TRITS[i])
      
  flat=[]
  for i in res:
    for j in i:
      flat.append(j)

  return (flat)

def get_int(t: str):
  trytes = get_trytes_from_tec(t)
  return print(get_int_from_trytes(trytes))

if __name__ == '__main__':
  get_int(sys.argv[1])