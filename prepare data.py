import os
with open('opfileA.txt','w',encoding='utf-8') as f:
    try:
        for dir in os.walk('a:\\'):
            f.write(str(dir).lower()+'\n')
    except Exception as exception:
        print(exception)