# -----------------------------------------------------------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Created Time:    2025/10/17
# @File:            readme.py
# @Software:        Neovim 0.12.0
# @Author:          xiao0o0sheng
# @Email:           xiaosheng7@126.com
# @Version:         
# @Description:     generate github README.md
# -----------------------------------------------------------------



import sys


def generate_badges(repo_name, username="xiao0o0sheng", license_type="AGPL"):
    """
    自动生成 github 的 README 结构
    :param repo_name: str, 仓库名
    :param username: str, GitHub用户名，默认为xiao0o0sheng
    :param license_type: str, 许可证类型，MIT 或 AGPL，默认为 AGPL 3.0
    :return: str, README.md 基本信息
    """

    # 使用纯 HTML 格式的徽章
    # stars_badge = f'<a href="https://github.com/{username}/{repo_name}/stargazers"><img src="https://img.shields.io/github/stars/{username}/{repo_name}" alt="GitHub stars"></a>'
    # forks_badge = f'<a href="https://github.com/{username}/{repo_name}/network/members"><img src="https://img.shields.io/github/forks/{username}/{repo_name}" alt="GitHub forks"></a>'
    stars_badge = f'<a href="https://github.com/{username}/{repo_name}/stargazers"><img src="https://img.shields.io/github/stars/{username}/{repo_name}?style=flat-square" alt="GitHub stars"></a>'
    forks_badge = f'<a href="https://github.com/{username}/{repo_name}/network/members"><img src="https://img.shields.io/github/forks/{username}/{repo_name}?style=flat-square" alt="GitHub forks"></a>'
    issues_badge = f'<a href="https://github.com/{username}/{repo_name}/issues"><img src="https://img.shields.io/github/issues/{username}/{repo_name}" alt="GitHub issues"></a>'

    if license_type.upper() == "MIT":
        license_badge = '<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>'
    else:
        license_badge = '<a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>'

    badges_line = f"{stars_badge} {forks_badge} {issues_badge} {license_badge}"

    # 标题图标方案
    title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24) hue-rotate(45deg);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24) hue-rotate(45deg);"></h1>'
    # title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #f59e0b; filter: drop-shadow(0 0 2px #fbbf24);"></h1>'
    # title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #8b5cf6; filter: drop-shadow(0 0 2px #a78bfa);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #8b5cf6; filter: drop-shadow(0 0 2px #a78bfa);"></h1>'
    # title_icon = f'<h1 align="center"><img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #10b981; filter: drop-shadow(0 0 2px #34d399);"> {repo_name} <img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg" width="24" height="24" style="vertical-align: middle; color: #10b981; filter: drop-shadow(0 0 2px #34d399);"></h1>'

    # 标语
    slogan = '<p align="center"><em>相信我 · 这次真的没Bug</em></p>'
    # slogan = '<p align="center"><em>理论上可行 · 实际上也能跑</em></p>'
    # slogan = '<p align="center"><em>随缘更新 · 有缘Star · 无缘Fork</em></p>'
    # slogan = '<p align="center"><em>简洁 · 优雅 · 高效 · 实用</em></p>'

    header_content = f"""{title_icon}

{slogan}

<p align="center">{badges_line}</p>

<p align="center">
  <a href="#项目介绍">项目介绍</a> &nbsp;|&nbsp;
  <a href="#功能特性">功能特性</a> &nbsp;|&nbsp;
  <a href="#快速开始">快速开始</a>
</p>

<hr style="border: none; border-top: 1px solid #e1e4e8; margin: 24px 0;">

# 项目介绍
# 功能特性
# 快速开始

"""

    return header_content


def main():
    if len(sys.argv) < 2:
        print("使用方法: python generate_badges.py <仓库名> [用户名] [许可证类型]")
        print("示例: python generate_badges.py my-repo")
        print("示例: python generate_badges.py my-repo your-username")
        print("示例: python generate_badges.py my-repo your-username MIT")
        sys.exit(1)

    repo_name = sys.argv[1]
    username = sys.argv[2] if len(sys.argv) > 2 else "xiao0o0sheng"
    license_type = sys.argv[3] if len(sys.argv) > 3 else "AGPL"

    badges = generate_badges(repo_name, username, license_type)
    print(f"\n{badges}")


if __name__ == "__main__":
    main()





