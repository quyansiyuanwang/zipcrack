import itertools
import zipfile
import os
import sys


projectPath = os.path.split(os.path.abspath(__file__))[0]
exe_path = os.path.dirname(sys.executable)

os.system('chcp 65001>nul')

filename = None

def unzip(filename_zip, password_zip):
    try:
        with zipfile.ZipFile(filename_zip) as zip_:
            zip_.extractall('./', pwd=password_zip.encode("gbk18030"))
        return True
    except Exception:
        return False

def dictionary_crack():
    global filename
    dictionary_name = input('字典文件名：')
    dic_pf = projectPath + '/' + dictionary_name
    while not os.path.isfile(dic_pf):
        dic_pf = projectPath + '/' + dictionary_name
        print(dic_pf)
        print("文件不存在!请重新输入")
        dictionary_name = input('文件名：')
    print(f'dictionary字典文件路径{dic_pf}')

    with open(dic_pf, 'r', encoding='utf-8', errors='ignore') as dic_manager:
        password_list = dic_manager.readlines()
    total = len(password_list)
    count = 0
    step = int(input(f'总数：{total}, step:'))
    for password in password_list:
        count += 1
        if count % step == 0:
            print('yet try:' + password.strip('\n'), f'progress: {round(count * 100 / total, 5)}')
        if unzip(filename, password.strip('\n')):
            print('\n破解完成:password=', password)
            break
    else:
        print('not found!')
    return None

def strength_crack():
    global filename
    print('A:0-9\n'
          'B:a-z\n'
          'C:A-Z\n'
          'D:symbols')
    ch = input('请输入字串选择(例如AC)')
    num = '0123456789'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbol = ',.?!:/@.";\'~()<>([{<>}])*&\\`#%^_+-=|¥£€﹉–..´'
    chars = ''
    for i in ch:
        if i.upper() == 'A':
            chars += num
        elif i.upper() == 'B':
            chars += lower_letters
        elif i.upper() == 'C':
            chars += upper_letters
        elif i.upper() == 'D':
            chars += symbol
        else:
            continue
    print(f'破解字串:   {chars}')
    print('破解中...可能时间较长...')
    a = int(input('输入开始长度:'))
    b = int(input('输入末尾长度:'))
    
    count = 0
    total = 0
    length = len(chars)
    for n in range(a, b + 1):
        total += length ** n
    step = int(input(f'总数：{total}, step:'))
    found = False
    for n in range(a, b + 1):
        for c in itertools.product(chars, repeat=n):
            count += 1
            password = ''.join(c)
            if count % step == 0:
                print('yet try:' + password, '\t', f'progress:{round(count * 100 / total, 5)}%')
            if unzip(filename, password):
                print('\n破解完成:password=', password)
                found = True
                return
    if not found:
        print('not found!')
            
    return None

def main():
    global filename
    filename = input('文件名：')
    pf = projectPath + '/' + filename
    while not os.path.isfile(pf):
        pf = projectPath + '/' + filename
        print(pf)
        print("文件不存在!请重新输入")
        filename = input('文件名：')
    print(f'文件路径{pf}')

    flag = False
    while not flag:
        flag = True
        choice = input('1:暴力破解' +\
        '\n' + '2:字典破解' + '\n')
        if choice == '1':
            strength_crack()
        elif choice == '2':
            dictionary_crack()
        else:
            print('非法输入！请重新输入')
            flag = False
    return None


if __name__ == '__main__':
    main()
os.system('pause')
exit()
