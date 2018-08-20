import os


def srt2str(source_name, target_name):
    print('open_source')
    file = open(source_name)
    print('target_source')

    f = open(target_name, 'a')
    source = file.read()
    print('readed')
    splitted = source.split('\n')
    # print(splitted)

    arrow = False
    for s in splitted:
        if arrow:
            if s:
                # print(s)
                f.write(' ' + s)

            else:
                arrow = False
        if s.find('-->') > 0:
            arrow = True


def main():
    path = '/home/dmitry/Desktop/friends/Friends_S01_DVDRip'
    lf = os.listdir(path)
    i = 0
    # print(len(lf))
    for l in lf:
        i = i + 1
        filename = path + '/' + l
        print(filename)
        print(i)
        srt2str(filename,'target.txt')



if __name__ == '__main__':
    main()
