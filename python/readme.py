# -----------------------------------------------------------------
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Created Time:    2026/07/29
# @File:            readme.py
# @Software:        Neovim 0.12.0
# @Author:          xiao0o0sheng
# @Email:           xiao0o0sheng@outlook.com
# @Version:         1.0.0
# @Description:     GitHub README header generator
# -----------------------------------------------------------------



import argparse
import sys

OUTPUT_FILE = "README.md"

LICENSES = {
    "MIT": (
        '<a href="https://opensource.org/licenses/MIT">'
        '<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>'
    ),
    "AGPL": (
        '<a href="https://www.gnu.org/licenses/agpl-3.0">'
        '<img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>'
    ),
}

SECTIONS = {
    "en": ("Introduction", "Features", "Quick Start"),
    "zh": ("项目介绍", "功能特性", "快速开始"),
}

SLOGANS = {
    "en": "If It Works, Don't Touch It",
    "zh": "相信我 · 这次真的没Bug",
}

TITLE_ICON = (
    '<img src="https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/icons/zap.svg"'
    ' width="24" height="24"'
    ' style="vertical-align: middle; color: #f59e0b;'
    ' filter: drop-shadow(0 0 2px #fbbf24) hue-rotate(45deg);">'
)


def generate_readme(repo: str, username: str, license_type: str, lang: str, private: bool = False) -> str:
    base = f"https://github.com/{username}/{repo}"
    license_badge = LICENSES[license_type]

    if private:
        badges_content = license_badge
    else:
        stars  = f'<a href="{base}/stargazers"><img src="https://img.shields.io/github/stars/{username}/{repo}?style=flat-square" alt="GitHub stars"></a>'
        forks  = f'<a href="{base}/network/members"><img src="https://img.shields.io/github/forks/{username}/{repo}?style=flat-square" alt="GitHub forks"></a>'
        issues = f'<a href="{base}/issues"><img src="https://img.shields.io/github/issues/{username}/{repo}" alt="GitHub issues"></a>'
        badges_content = f"{stars} {forks} {issues} {license_badge}"

    intro, features, quick_start = SECTIONS[lang]

    title  = f'<h1 align="center">{TITLE_ICON} {repo} {TITLE_ICON}</h1>'
    slogan = f'<p align="center"><em>{SLOGANS[lang]}</em></p>'
    badges = f'<p align="center">{badges_content}</p>'
    nav = (
        f'<p align="center">\n'
        f'  <a href="#{intro}">{intro}</a> &nbsp;|&nbsp;\n'
        f'  <a href="#{features}">{features}</a> &nbsp;|&nbsp;\n'
        f'  <a href="#{quick_start}">{quick_start}</a>\n'
        f'</p>'
    )
    hr = '<hr style="border: none; border-top: 1px solid #e1e4e8; margin: 24px 0;">'

    return (
        f"{title}\n\n"
        f"{slogan}\n\n"
        f"{badges}\n\n"
        f"{nav}\n\n"
        f"{hr}\n\n"
        f"# {intro}\n\n"
        f"# {features}\n\n"
        f"# {quick_start}\n"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a GitHub README header with badges.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  python readme.py my-repo\n"
            "  python readme.py my-repo --lang zh\n"
            "  python readme.py my-repo --license MIT --username johndoe\n"
            "  python readme.py my-repo --private\n"
            "  python readme.py my-repo --output"
        ),
    )
    parser.add_argument("repo", help="repository name")
    parser.add_argument(
        "--username", default="xiao0o0sheng",
        help="GitHub username (default: xiao0o0sheng)",
    )
    parser.add_argument(
        "--license", default="AGPL", choices=["MIT", "AGPL"],
        help="license type (default: AGPL)",
    )
    parser.add_argument(
        "--lang", default="en", choices=["en", "zh"],
        help="output language: en or zh (default: en)",
    )
    parser.add_argument(
        "--private", action="store_true",
        help="private repo: omit stars/forks/issues badges",
    )
    parser.add_argument(
        "--output", action="store_true",
        help=f"write output to {OUTPUT_FILE} instead of stdout",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    content = generate_readme(args.repo, args.username, args.license, args.lang, args.private)

    if args.output:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Written to {OUTPUT_FILE}")
    else:
        print(content)


if __name__ == "__main__":
    main()
