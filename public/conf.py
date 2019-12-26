import os
import sys
try:
    import MyLog
except ImportError as e:
    from . import MyLog


def Log():
    return MyLog.mylog().log()


class confClass(object):
    def __init__(self):
        path = os.path.dirname(os.path.dirname(__file__))
        self.conf_path = os.path.join(path, 'conf')
        self.filenam = 'conf.txt'
        self.conf_dic = {}

    def conf_info(self):
        file_path = os.path.join(self.conf_path, self.filenam)
        if os.path.isdir(self.conf_path):
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        conf_list = []
                        if '#' in line or '\n' == line:
                            continue
                        line_list = line.split('=')
                        conf_list = line_list[1].split(',')
                        conf_list=list(map(lambda x: x.strip(), conf_list))
                        self.conf_dic[line_list[0].strip()] = conf_list

            # print(self.conf_dic)
            # # MyLog().info(f.read())
            Log().info('conf file data：\n%s' % self.conf_dic)
            return self.conf_dic
        else:
            os.mkdir(self.conf_path)
            f = open(file_path, 'w', encoding='utf-8')
            f.close()
            Log().error('==conf.txt file created successfully,please edit!!!==')


if __name__ == '__main__':
    m = confClass()
    m.conf_info()
    # print(os.path.dirname(os.path.abspath("__file__")))
