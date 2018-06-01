from datetime import datetime

with open('text.txt','w') as f:
    f.write('今天是')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('text.txt','r') as f:
    s=f.read()
    print('open for read...')
    print(s)

with open('text.txt','rb') as f:
    s=f.read()
    print('open as binary for read...')
    print(s)