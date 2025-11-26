"""
Abertura de arquivos usando try e excepts...
"""

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()
