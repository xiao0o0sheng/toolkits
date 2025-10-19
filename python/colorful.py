# -----------------------------------------------------------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Created Time:    2025/10/17
# @File:            colorful.py
# @Software:        Neovim 0.12.0
# @Author:          xiao0o0sheng
# @Email:           xiaosheng7@126.com
# @Version:         
# @Description:     
# -----------------------------------------------------------------



class Color:
    """颜色输出类"""

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

    @classmethod
    def red(cls, text: str) -> str:
        return f"{cls.RED}{text}{cls.END}"

    @classmethod
    def green(cls, text: str) -> str:
        return f"{cls.GREEN}{text}{cls.END}"

    @classmethod
    def yellow(cls, text: str) -> str:
        return f"{cls.YELLOW}{text}{cls.END}"

    @classmethod
    def blue(cls, text: str) -> str:
        return f"{cls.BLUE}{text}{cls.END}"

    @classmethod
    def magenta(cls, text: str) -> str:
        return f"{cls.MAGENTA}{text}{cls.END}"

    @classmethod
    def cyan(cls, text: str) -> str:
        return f"{cls.CYAN}{text}{cls.END}"

    @classmethod
    def bold(cls, text: str) -> str:
        return f"{cls.BOLD}{text}{cls.END}"

    @classmethod
    def underline(cls, text: str) -> str:
        return f"{cls.UNDERLINE}{text}{cls.END}"

    @classmethod
    def success(cls, text: str) -> str:
        """成功消息"""
        return cls.green(f"✅ {text}")

    @classmethod
    def error(cls, text: str) -> str:
        """错误消息"""
        return cls.red(f"❌ {text}")

    @classmethod
    def warning(cls, text: str) -> str:
        """警告消息"""
        return cls.yellow(f"⚠️  {text}")

    @classmethod
    def info(cls, text: str) -> str:
        """信息消息"""
        return cls.blue(f"ℹ️  {text}")

    @classmethod
    def debug(cls, text: str) -> str:
        """调试消息"""
        return cls.cyan(f"🐛 {text}")


if __name__ == "__main__":
    # 测试颜色输出
    print("颜色工具类测试:")
    print(Color.success("这是一个成功消息"))
    print(Color.error("这是一个错误消息"))
    print(Color.warning("这是一个警告消息"))
    print(Color.info("这是一个信息消息"))
    print(Color.debug("这是一个调试消息"))
    print()
    print(Color.red("红色文本"))
    print(Color.green("绿色文本"))
    print(Color.yellow("黄色文本"))
    print(Color.blue("蓝色文本"))
    print(Color.magenta("紫色文本"))
    print(Color.cyan("青色文本"))
    print(Color.bold("粗体文本"))
    print(Color.underline("下划线文本"))




