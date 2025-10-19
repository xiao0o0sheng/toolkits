# -----------------------------------------------------------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Created Time:    2025/10/17
# @File:            custom_logger.py
# @Software:        Neovim 0.12.0
# @Author:          xiao0o0sheng
# @Email:           xiaosheng7@126.com
# @Version:         
# @Description:     
# -----------------------------------------------------------------



import logging
import os
import sys


class Logger:
    """日志工具类"""

    # 定义日志级别常量，避免外部导入 logging
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, name, log_dir="logs", console_level=INFO, file_level=DEBUG):
        """
        初始化日志器

        :param name: 日志器名称，通常使用主机名或模块名
        :param log_dir: 日志文件目录
        :param console_level: 控制台输出级别，默认 INFO
        :param file_level: 文件记录级别，默认 DEBUG
        """
        self.name = name
        self.log_dir = log_dir
        self.console_level = console_level
        self.file_level = file_level

        # 创建日志器 - 设置为最低级别 DEBUG，让处理器各自过滤
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 避免重复添加处理器
        if not self.logger.handlers:
            self._setup_handlers()

    def _setup_handlers(self):
        """设置日志处理器"""
        # 创建日志目录
        os.makedirs(self.log_dir, exist_ok=True)

        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_format = logging.Formatter(
            ">>> %(levelname)-8s - %(asctime)s - %(message)s"
        )
        console_handler.setLevel(self.console_level)
        console_handler.setFormatter(console_format)

        # 文件处理器
        log_file = os.path.join(self.log_dir, f"{self.name}.log")
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_format = logging.Formatter(
            "%(levelname)-8s - %(asctime)s - %(name)s - %(message)s"
        )
        file_handler.setLevel(self.file_level)
        file_handler.setFormatter(file_format)

        # 添加处理器
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    @classmethod
    def create_logger(cls, name, log_dir="logs", console_level=INFO, file_level=DEBUG):
        """创建日志器的类方法"""
        return cls(name, log_dir, console_level, file_level)

    def setLevel(self, level):
        """同时设置控制台和文件记录级别"""
        self.set_console_level(level)
        self.set_file_level(level)

    def set_console_level(self, level):
        """设置控制台输出级别"""
        self.console_level = level
        for handler in self.logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                handler.setLevel(level)

    def set_file_level(self, level):
        """设置文件记录级别"""
        self.file_level = level
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                handler.setLevel(level)

    # 标准日志方法
    def info(self, message):
        """信息级别日志"""
        self.logger.info(message)

    def error(self, message):
        """错误级别日志"""
        self.logger.error(message)

    def warning(self, message):
        """警告级别日志"""
        self.logger.warning(message)

    def debug(self, message):
        """调试级别日志"""
        self.logger.debug(message)

    def critical(self, message):
        """严重错误级别日志"""
        self.logger.critical(message)

    def get_console_level(self):
        """获取当前控制台输出级别"""
        return self.console_level

    def get_file_level(self):
        """获取当前文件记录级别"""
        return self.file_level


if __name__ == "__main__":
    print("=== 测试：控制台 INFO，文件 DEBUG ===")
    logger = Logger.create_logger("test_logger", console_level=Logger.INFO, file_level=Logger.DEBUG)

    print("控制台级别: INFO (只显示INFO及以上)")
    print("文件级别: DEBUG (记录DEBUG及以上)")
    print()

    # 测试各种级别的日志
    logger.debug("DEBUG信息 - ❌ 控制台不显示，✅ 文件记录")
    logger.info("INFO信息 - ✅ 控制台显示，✅ 文件记录")
    logger.warning("WARNING信息 - ✅ 控制台显示，✅ 文件记录")
    logger.error("ERROR信息 - ✅ 控制台显示，✅ 文件记录")

    print("\n=== 测试：控制台 ERROR，文件 INFO ===")
    logger.set_console_level(Logger.ERROR)
    logger.set_file_level(Logger.INFO)

    print("控制台级别: ERROR (只显示ERROR及以上)")
    print("文件级别: INFO (只记录INFO及以上)")
    print()

    logger.debug("DEBUG信息 - ❌ 控制台不显示，❌ 文件不记录")
    logger.info("INFO信息 - ❌ 控制台不显示，✅ 文件记录")
    logger.warning("WARNING信息 - ❌ 控制台不显示，✅ 文件记录")
    logger.error("ERROR信息 - ✅ 控制台显示，✅ 文件记录")



