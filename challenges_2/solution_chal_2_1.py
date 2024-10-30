def xor_string(input_bytes, key):
  result_bytes = bytes([b ^ key for b in input_bytes])
  result_string = result_bytes.decode('utf-8')
  return result_string

encrypted = 0x0C060B0D670F231E07303F20053A043D13092F2F383C1B070C252E7A22271002090A.to_bytes(34, 'big')

for key in range(255):
    result = xor_string(encrypted, key)
    if result.startswith('FLAG-'):
      print(f"Key = {key}, flag = {result[:-1]}")
      exit()
