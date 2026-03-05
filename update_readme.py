#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import urllib.parse
from pathlib import Path

def scan_directory(dir_path, base_path):
    """扫描目录并生成文档链接"""
    items = []
    if not os.path.exists(dir_path):
        return items
    
    for item in sorted(os.listdir(dir_path)):
        if item.startswith('.'):
            continue
            
        item_path = os.path.join(dir_path, item)
        relative_path = os.path.relpath(item_path, base_path)
        
        if os.path.isfile(item_path) and item.endswith('.md'):
            # 文件名去掉 .md 后缀作为显示名
            display_name = os.path.splitext(item)[0]
            # URL 编码文件名
            encoded_path = urllib.parse.quote(relative_path, safe='/')
            items.append(f"- [{display_name}]({encoded_path})")
            
        elif os.path.isdir(item_path):
            # 子目录
            sub_items = scan_directory(item_path, base_path)
            if sub_items:
                items.append(f"\n### {item}")
                items.extend(sub_items)
    
    return items

def generate_readme():
    """生成 README 文档"""
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    content = [
        "# Novena - 个人技术知识库",
        "",
        "系统化整理的技术知识库，涵盖项目经验总结、核心技术栈深度分析以及英文面试准备资料。",
        "",
        "> 📖 **在线阅读**：[https://kyleexu.github.io/novena](https://kyleexu.github.io/novena)",
        "",
        "---",
        ""
    ]
    
    # 扫描各个目录
    directories = [
        ("project", "🚀 项目经验"),
        ("repository", "📚 技术知识库"), 
        # ("english", "🌍 英文面试准备"),
        ("jobs", "🎯 岗位描述"),
        ("interview", "📄 面试总结"),
        ("resume", "📝 个人简历"),
    ]
    
    for dir_name, title in directories:
        dir_path = os.path.join(base_path, dir_name)
        if os.path.exists(dir_path):
            content.append(f"## {title}")
            content.append("")
            
            items = scan_directory(dir_path, base_path)
            if items:
                content.extend(items)
            else:
                content.append("暂无文档")
            
            content.append("")
            content.append("---")
            content.append("")
    
    # 添加尾部
    content.extend([
        "## 🔧 本地预览",
        "",
        "```bash",
        "# 安装 docsify-cli",
        "npm i docsify-cli -g",
        "",
        "# 启动本地服务", 
        "docsify serve .",
        "",
        "# 访问 http://localhost:3000",
        "```",
        "",
        "---",
        "",
        "## 📜 License",
        "",
        "本项目仅用于个人学习和技术分享。",
        "",
        "---",
        "",
        "**Last Updated:** March 2026"
    ])
    
    # 写入 README.md
    readme_path = os.path.join(base_path, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    print(f"✅ README.md 已更新 ({len([x for x in content if x.startswith('- [')])} 个文档)")

if __name__ == "__main__":
    generate_readme()