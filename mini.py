import os
import json as js
from pprint import pprint

def MiniGenerate():
    print(os.sep)
    fileDir = os.path.abspath(os.path.dirname(__file__))
    for root, dirs, files in os.walk(fileDir):  
        print(fileDir)
        print('正在以下目录进行操作：')
        print(root)  
        print('检测到当前目录有以下文件：')
        print(files)
        print('')
        removelist=['mini.py','Generate.py','Waline.py','index.json','info.json']
        currentdir = root.replace('G:\Code\ValineCDN','.')
        if currentdir != '.' and ('.git' in currentdir) != True:
            for remove in removelist:
                print(remove)
                try:
                    files.remove(remove)
                except:
                    None
            print(currentdir)
            currentdir = currentdir[2:]
            print(currentdir)
            jsontamplatedict={"0": files}
            pprint(jsontamplatedict)
            with open('.\\'+ currentdir + '\index.json','w+') as f:
                f.writelines(str(js.dumps(str(jsontamplatedict)))
                .replace("\"{'0'",'{"0"')
                .replace(']}"',']}')
                .replace("'",'"'))
                f.close()
    os.remove(fileDir + "\index.json")
           
if __name__ == "__main__":
    MiniGenerate()  
