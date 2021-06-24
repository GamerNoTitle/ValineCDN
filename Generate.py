import os
remotepath = 'https://valinecdn.bili33.top/'
prefix= input("请输入前缀：")
FilePath="."
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f!='Generate.py' and f!='index.json' and f!='mini.py' and f!='info.json':
                yield f

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
        if f!='Generate.py' and f!='index.json' and f!='mini.py' and f!='info.json':
            print('\"{}{}\": \"{}/{}\",'.format(prefix,num,prefix,i))
            num=num+1
    print('}')
    print('```')
    num=1
    for i in findAllFile(base):
        if f!='Generate.py' and f!='index.json' and f!='mini.py' and f!='info.json':
            print('![{}{}]({}{}/{})'.format(prefix,num,remotepath,prefix,i))
            num=num+1



if __name__ == '__main__':
    main()