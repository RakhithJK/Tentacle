#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'orleven'
import platform
import logging
import os
import sys
import time
from lib.core.enums import CUSTOM_LOGGING
from lib.utils.colorer import ColoredFormatter
# from lib.utils.colorer import _AnsiColorStreamHandler
class logger:
    def __init__(self, set_level=CUSTOM_LOGGING.SYSINFO,
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 log_name=time.strftime("%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "log"),
                 use_console=True):
        '''
            set_level： 设置日志的打印级别，默认为DEBUG
            name： 日志中将会打印的name，默认为运行程序的name
            log_name： 日志文件的名字，默认为当前时间（年-月-日.log）
            log_path： 日志文件夹的路径，默认为logger.py同级目录中的log文件夹
            use_console： 是否在控制台打印，默认为True
        '''
        logging.addLevelName(CUSTOM_LOGGING.SYSINFO, "*")
        logging.addLevelName(CUSTOM_LOGGING.SUCCESS, "+")
        logging.addLevelName(CUSTOM_LOGGING.ERROR, "-")
        logging.addLevelName(CUSTOM_LOGGING.WARNING, "!")
        logging.addLevelName(CUSTOM_LOGGING.DEBUG, "DEBUG")

        self.logger = logging.getLogger(name)
        self.set_level(set_level)

        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file_path = os.path.join(log_path, log_name)
        log_handler = logging.FileHandler(log_file_path)
        log_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S"))
        self.logger.addHandler(log_handler)

        # if use_console:
        #     try:
        #         from thirdparty.ansistrm.ansistrm import ColorizingStreamHandler
        #         # if True:
        #         try:
        #             self.console_handler = ColorizingStreamHandler(sys.stdout)
        #             self.console_handler.level_map = {}
        #             self.console_handler.level_map[logging.getLevelName("*")] = (None, "cyan", False)
        #             self.console_handler.level_map[logging.getLevelName("+")] = (None, "green", False)
        #             self.console_handler.level_map[logging.getLevelName("-")] = (None, "red", False)
        #             self.console_handler.level_map[logging.getLevelName("!")] = (None, "yellow", False)
        #             self.console_handler.level_map[logging.getLevelName("DEBUG")] = (None, "white", False)
        #
        #         except Exception:
        #             self.console_handler = logging.StreamHandler(sys.stdout)
        #
        #     except ImportError:
        #         self.console_handler = logging.StreamHandler(sys.stdout)
        #
        #     # console_handler = logging.StreamHandler()
        #     self.console_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S"))
        #     self.logger.addHandler(self.console_handler)
        self.console_handler = logging.StreamHandler(stream=sys.stdout)
        colors = {
            CUSTOM_LOGGING.SYSINFO: 34,  # Blue
            CUSTOM_LOGGING.SUCCESS: 32,  # Green
            CUSTOM_LOGGING.WARNING: 33,  # Yellow
            CUSTOM_LOGGING.ERROR: 31,  # Red
            CUSTOM_LOGGING.DEBUG: 35,  # burgundy
        }
        self.console_handler.setFormatter(ColoredFormatter(fmt = "%(color)s[%(asctime)s] [%(levelname)s] %(message)s%(end_color)s",  datefmt = "%H:%M:%S",colors =colors ))
        # self.console_handler.setFormatter()
        self.logger.addHandler(self.console_handler)
            # log = logging.getLogger()
            # log.addFilter(log_filter())
            # //hdlr = logging.StreamHandler()
            # //hdlr.setFormatter(formatter())

    def set_level(self,set_level):
        self.logger.setLevel(set_level)


        # if set_level.lower() == "critical":
        #     self.logger.setLevel(logging.CRITICAL)
        # elif set_level.lower() == "error":
        #     self.logger.setLevel(logging.ERROR)
        # elif set_level.lower() == "warning":
        #     self.logger.setLevel(logging.WARNING)
        # elif set_level.lower() == "info":
        #     self.logger.setLevel(logging.INFO)
        # elif set_level.lower() == "debug":
        #     self.logger.setLevel(logging.DEBUG)
        # else:
        #     self.logger.setLevel(logging.NOTSET)

    def addHandler(self, hdlr):
        self.logger.addHandler(hdlr)

    def removeHandler(self, hdlr):
        self.logger.removeHandler(hdlr)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    # def warning(self, msg, *args, **kwargs):
    #     self.logger.warning(msg, *args, **kwargs)
    #
    # def error(self, msg, *args, **kwargs):
    #     self.logger.error(msg, *args, **kwargs)

    # def debug(self, msg, *args, **kwargs):
    #     self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def log(self, level, msg, *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)

    def sysinfo(self, msg, *args, **kwargs):
        self.logger.log(CUSTOM_LOGGING.SYSINFO, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.log(CUSTOM_LOGGING.ERROR, msg, *args, **kwargs)

    def success(self, msg, *args, **kwargs):
        self.logger.log(CUSTOM_LOGGING.SUCCESS, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.log(CUSTOM_LOGGING.WARNING, msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self.logger.log(CUSTOM_LOGGING.DEBUG, msg, *args, **kwargs)




    # from logging.handlers import TimedRotatingFileHandler
# from logging.handlers import RotatingFileHandler
# from lib.core.enums import CUSTOM_LOGGING
#
# logging.addLevelName(CUSTOM_LOGGING.SYSINFO, "*")
# logging.addLevelName(CUSTOM_LOGGING.SUCCESS, "+")
# logging.addLevelName(CUSTOM_LOGGING.ERROR, "-")
# logging.addLevelName(CUSTOM_LOGGING.WARNING, "!")
# logging.addLevelName(CUSTOM_LOGGING.DEBUG, "DEBUG")
# LOGGER = logging.getLogger("Tentacle")
#
#
LOGGER_HANDLER = None
LOGGER_FILE_HANDLER = None
#
# try:
#     from thirdparty.ansistrm.ansistrm import ColorizingStreamHandler
#
#     # disableColor = False
#     #
#     # for argument in sys.argv:
#     #     if "disable-col" in argument:
#     #         disableColor = True
#     #         break
#
#     # if disableColor:
#     #     LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
#     # else:
#     #     LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
#         # LOGGER_HANDLER.level_map[logging.getLevelName("Task")] = (None, "cyan", False)
#         # LOGGER_HANDLER.level_map[logging.getLevelName("TRAFFIC OUT")] = (None, "magenta", False)
#         # LOGGER_HANDLER.level_map[logging.getLevelName("TRAFFIC IN")] = ("magenta", None, False)
#     try:
#         LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
#         LOGGER_HANDLER.level_map[logging.getLevelName("*")] = (None, "cyan", False)
#         LOGGER_HANDLER.level_map[logging.getLevelName("+")] = (None, "green", False)
#         LOGGER_HANDLER.level_map[logging.getLevelName("-")] = (None, "red", False)
#         LOGGER_HANDLER.level_map[logging.getLevelName("!")] = (None, "yellow", False)
#         LOGGER_HANDLER.level_map[logging.getLevelName("DEBUG")] = (None, "white", False)
#     except Exception:
#         LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
#
# except ImportError:
#     LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
#
# FORMATTER = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")
# LOGGER_HANDLER.setFormatter(FORMATTER)
# LOGGER.addHandler(LOGGER_HANDLER)
#
# log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),'log')
# if not os.path.exists(log_dir):
#     os.mkdir(log_dir)
#
# LOGGER_FILE_HANDLER = logging.handlers.RotatingFileHandler(filename=os.path.join(log_dir,'logs.log'), maxBytes=10*1024*1024)
# LOGGER_FILE_HANDLER.setLevel(logging.INFO)
# LOGGER_FILE_HANDLER.setFormatter(FORMATTER)
# LOGGER.addHandler(LOGGER_FILE_HANDLER)
# LOGGER.setLevel(logging.INFO)
#
#
# class MY_LOGGER:
#     @staticmethod
#     def success(msg):
#         return LOGGER.log(CUSTOM_LOGGING.SUCCESS, msg)
#
#     @staticmethod
#     def info(msg):
#         return LOGGER.log(CUSTOM_LOGGING.SYSINFO, msg)
#
#     @staticmethod
#     def warning(msg):
#         return LOGGER.log(CUSTOM_LOGGING.WARNING, msg)
#
#     @staticmethod
#     def error(msg):
#         return LOGGER.log(CUSTOM_LOGGING.ERROR, msg)
#
#     @staticmethod
#     def critical(msg):
#         return LOGGER.log(CUSTOM_LOGGING.ERROR, msg)
#
#     @staticmethod
#     def debug(msg):
#         return LOGGER.log(CUSTOM_LOGGING.DEBUG, msg)

    # @staticmethod
    # def security_note(msg, k=''):
    #     MY_LOGGER.info(msg)
    #
    # @staticmethod
    # def security_warning(msg, k=''):
    #     MY_LOGGER.warning(msg)
    #
    # @staticmethod
    # def security_hole(msg, k=''):
    #     MY_LOGGER.success(msg)
    #
    # @staticmethod
    # def security_info(msg, k=''):
    #     MY_LOGGER.info(msg)

