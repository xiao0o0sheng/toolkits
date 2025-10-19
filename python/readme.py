# -----------------------------------------------------------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Created Time:    2025/10/19
# @File:            readme.py
# @Software:        Neovim 0.12.0
# @Author:          xiao0o0sheng
# @Email:           xiaosheng7@126.com
# @Version:         
# @Description:     
# -----------------------------------------------------------------



import sys


def generate_badges(repo_name, language=0, license="AGPL", username="xiao0o0sheng"):
    """
    自动生成 github 的 README 结构
    :param repo_name: str, 仓库名
    :param language: 语言，0(默认): English, 1: 中文
    :param license: str, 许可证类型，MIT 或 AGPL，默认为 AGPL 3.0
    :param username: str, GitHub用户名，默认为xiao0o0sheng
    :return: str, README.md 基本信息
    """

    # 使用纯 HTML 格式的徽章
    # stars_badge = f'<a href="https://github.com/{username}/{repo_name}/stargazers"><img src="https://img.shields.io/github/stars/{username}/{repo_name}" alt="GitHub stars"></a>'
    # forks_badge = f'<a href="https://github.com/{username}/{repo_name}/network/members"><img src="https://img.shields.io/github/forks/{username}/{repo_name}" alt="GitHub forks"></a>'
    stars_badge = f'<a href="https://github.com/{username}/{repo_name}/stargazers"><img src="https://img.shields.io/github/stars/{username}/{repo_name}?style=flat-square" alt="GitHub stars"></a>'
    forks_badge = f'<a href="https://github.com/{username}/{repo_name}/network/members"><img src="https://img.shields.io/github/forks/{username}/{repo_name}?style=flat-square" alt="GitHub forks"></a>'
    issues_badge = f'<a href="https://github.com/{username}/{repo_name}/issues"><img src="https://img.shields.io/github/issues/{username}/{repo_name}" alt="GitHub issues"></a>'

    if license.upper() == "MIT":
        license_badge = '<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>'
    else:
        license_badge = '<a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>'

    badges_line = f"{stars_badge} {forks_badge} {issues_badge} {license_badge}"

    # 标题图标方案
    title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24) hue-rotate(45deg);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24) hue-rotate(45deg);"></h1>'
    # title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24);"></h1>'
    # title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #8b5cf6; filter: drop-shadow(0 0 2px #a78bfa);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #8b5cf6; filter: drop-shadow(0 0 2px #a78bfa);"></h1>'
    # title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #10b981; filter: drop-shadow(0 0 2px #34d399);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #10b981; filter: drop-shadow(0 0 2px #34d399);"></h1>'

    if language != 0:
        slogan = '<p align="center"><em>相信我 · 这次真的没Bug</em></p>'
        # slogan = '<p align="center"><em>理论上可行 · 实际上也能跑</em></p>'
        # slogan = '<p align="center"><em>随缘更新 · 有缘Star · 无缘Fork</em></p>'
        # slogan = '<p align="center"><em>简洁 · 优雅 · 高效 · 实用</em></p>'
        introduction = "项目介绍"
        fearure = "功能特性"
        quick_start = "快速开始"
    else:
        slogan = '<p align="center"><em>If It Works, Don\'t Touch It</em></p>'
        # slogan = '<p align="center"><em>Simple, Elegant, Efficient</em></p>'
        # slogan = '<p align="center"><em>Where Ideas Meet Implementation</em></p>'
        # slogan = '<p align="center"><em>Pushing the Boundaries of Possibility</em></p>'
        # slogan = '<p align="center"><em>Innovation at Your Fingertips</em></p>'
        # slogan = '<p align="center"><em>Simplifying Complexity with Elegance</em></p>'
        # slogan = '<p align="center"><em>Where Vision Becomes Reality</em></p>'
        introduction = "Introduction"
        fearure = "Features"
        quick_start = "Quick Start"

    header_content = f"""{title_icon}

{slogan}

<p align="center">{badges_line}</p>

<p align="center">
  <a href="#{introduction}">{introduction}</a> &nbsp;|&nbsp;
  <a href="#{fearure}">{fearure}</a> &nbsp;|&nbsp;
  <a href="#{quick_start}">{quick_start}</a>
</p>

<hr style="border: none; border-top: 1px solid #e1e4e8; margin: 24px 0;">

# {introduction}
# {fearure}
# {quick_start}

"""

    return header_content


def parse_arguments() -> tuple[str, str, str, int]:
    """
    解析命令行参数
    Returns:
        tuple: (repo_name, username, license, language)
    """
    if len(sys.argv) < 2:
        print("使用方法: python generate_badges.py <仓库名> [语言] [许可证类型] [用户名]")
        print("示例: python generate_badges.py my-repo")
        print("示例: python generate_badges.py my-repo 1")
        print("示例: python generate_badges.py my-repo 0 MIT")
        print("示例: python generate_badges.py my-repo 1 AGPL your-username")
        sys.exit(1)

    repo_name = sys.argv[1]

    # 设置默认值
    language = 0
    license = "AGPL"
    username = "xiao0o0sheng"

    # 根据参数数量逐步解析
    if len(sys.argv) > 2:
        try:
            language = int(sys.argv[2])
        except ValueError:
            print(f"警告: 无效的语言类型 '{sys.argv[2]}', 使用默认值 (0)")

    if len(sys.argv) > 3:
        license = sys.argv[3].upper()  # 统一转为大写

    if len(sys.argv) > 4:
        username = sys.argv[4]

    return repo_name, username, license, language


def validate_arguments(repo_name: str, username: str, license: str, language: int) -> None:
    """
    验证参数有效性
    """
    if not repo_name or not repo_name.strip():
        raise ValueError("仓库名不能为空")

    if not username or not username.strip():
        raise ValueError("用户名不能为空")

    valid_licenses = {"MIT", "AGPL"}
    if license not in valid_licenses:
        raise ValueError(f"许可证必须是 {valid_licenses} 之一, 但得到的是 '{license}'")

    if language not in {0, 1}:
        raise ValueError("语言必须是 0 (英文) 或 1 (中文)")


def main():
    try:
        # 解析和验证参数
        repo_name, username, license, language = parse_arguments()
        validate_arguments(repo_name, username, license, language)

        # 生成徽章内容
        badges = generate_badges(repo_name, language, license, username)
        print(f"\n{badges}")

    except ValueError as e:
        print(f"错误: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"意外错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
