import os
import sys
import logging
import datetime


class mylog(object):
    '''    
    # ERROR    
    # WARNING  
    # INFO    
    # DEBUG
    '''

    def __init__(self):
        path = os.path.dirname(os.path.dirname(__file__))
        version = datetime.datetime.now().strftime("%Y-%m-%dH%H")
        self.logname = 'all_%s.log' % version  # all.log
        self.log_path = "temp"
        self.logger = logging.getLogger("logger")
        self.tem_path = os.path.join(path, self.log_path)
        self.log_path = os.path.join(self.tem_path, self.logname)

    def log_name(self):
        return self.log_path

    def log(self):
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s: %(message)s")
        #tem_path  = os.path.join(os.path.dirname(os.getcwd()),self.log_path)
        #log_path = os.path.join(self.tem_path,self.logname)
        if not os.path.isdir(self.tem_path) or not os.path.isfile(self.log_path):
            try:
                os.mkdir(self.tem_path)
            except FileExistsError as e:
                pass
            with open(self.log_path, 'w', encoding='utf-8') as f:
                pass

        if not self.logger.handlers:
            # 文件日志
            file_handler = logging.FileHandler(self.log_path)
            file_handler.setLevel(logging.INFO)  # 指定日志的最低输出级别，默认为WARN级别
            file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

            # 控制台日志
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.DEBUG)  # 指定日志的最低输出级别，默认为WARN级别
            console_handler.formatter = formatter  # 也可以直接给formatter赋值

            # 为logger添加的日志处理器
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

            # 指定日志的最低输出级别，默认为WARN级别
            self.logger.setLevel(logging.INFO)

        return self.logger


if __name__ == '__main__':
    # l = log()
    # l.info('1234566789')
    m = mylog()
    m.log().info('8888888888888')
    # for i in range(0,500):
    #     m.info(i)
    print(m.log_name())
