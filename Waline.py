import os
import json as js
from pprint import pprint

def WalineGenerate():
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
        types = 'png'
        print(currentdir)
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
            jsontamplatedict={
                "name": "{}".format(currentdir.replace(".","")),
                "icon": "{}".format(files[0]),
                "items": files
            }
            pprint(jsontamplatedict)
            # jsontamplate = '''{
            #     "name": "{currentdir}",
            #     "prefix": "{currentdir}_",
            #     "type": "{types}",
            #     "icon": "{files[0]}",
            #     "items": {files}
            #     }'''.format(currentdir,currentdir,types,files[0],files)
            with open('.\\'+ currentdir + '\info.json','w+') as f:
                f.writelines(str(js.dumps(str(jsontamplatedict))).replace("': '",'": "')
                .replace("', '",'", "')
                .replace('"{\'','{"')
                .replace('}"','}')
                .replace("['","[\"")
                .replace('"items\'','"items"')
                .replace("']",'"]'))
                f.close()
    os.remove(fileDir + "\info.json")
           
if __name__ == "__main__":
    WalineGenerate()  
