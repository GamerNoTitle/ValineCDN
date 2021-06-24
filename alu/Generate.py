import os
remotepath = 'https://valinecdn.bili33.top/'
prefix= input("请输入前缀：")
FilePath="."
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f!='Generate.py' and f!='index.json' and f!='mini.py' and f!='info.json':
                yield f

def walkFile(FilePath):
    print("正在生成MiniValine所需的index.json文件")
    S='''{"0":['''
    for root, dirs, files in os.walk(FilePath):
        for f in files:
            if f!='Generate.py':
                Path=os.path.join(root, f)
                S+='"'+f+'",'
    S+="]}"
    S=S.replace(",]}", "]}")
    print("正在写入文件，这通常不会太久...")
    with open("./index.json","wb") as ff:
        ff.write(S.encode("utf-8"))
    print("恭喜，已成功完成")


def main():
    base = './'
    linklist=[]
    num=1
    print('# {}'.format(prefix))
    print('MiniValine/Waline:')
    print('> https://valinecdn.bili33.top/{}'.format(prefix))
    print('```json')
    print('{')
    for i in findAllFile(base):
        if i!='Generate.py':
            print('\"{}{}\": \"{}/{}\",'.format(prefix,num,prefix,i))
            num=num+1
    print('}')
    print('```')
    num=1
    for i in findAllFile(base):
        if i!='Generate.py':
            print('![{}{}]({}{}/{})'.format(prefix,num,remotepath,prefix,i))
            num=num+1
    WalineTamplate='''{
    name: "{prefix}",
    folder: "{remotepath}prefix",
    prefix: "{prefix}_",
    type: "png",
    icon: "{}",
    items: {}
    }'''.format(linklist[0],str(linklist).replace('.png',''))



if __name__ == '__main__':
    main()
    print("请坐和放宽，我们正帮你搞定一切......")
    try:
        walkFile(FilePath)
    except Exception as e:
        print("生成失败！我们都有不顺利的时候.")
        print(e)
    with open('./info.json','w+',encoding='utf8') as f:
        f.write(WalineTamplate)
        f.close
