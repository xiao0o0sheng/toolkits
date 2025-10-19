# -----------------------------------------------------------------
# !/usr/bin/bash
# -*- coding: utf-8 -*-
# @Created Time:    2025/10/03
# @File:            ssh_pub_upload.sh
# @Software:        Neovim 0.12.0
# @Author:          xiao0o0sheng
# @Email:           xiaosheng7@126.com
# @Version:         
# @Description:     
# -----------------------------------------------------------------



# 提示输入用户名、IP、密码
read -p "请输入IP地址: " ip_address
read -p "请输入用户名: " username
read -s -p "请输入密码: " password
echo ""

# 检查输入是否为空
if [ -z "$username" ] || [ -z "$ip_address" ] || [ -z "$password" ]; then
    echo "错误：用户名、IP地址或密码不能为空。"
    exit 1
fi

# 设置密钥文件路径（使用ed25519类型）
key_file="$HOME/.ssh/id_ed25519"

# 检查密钥是否已存在
if [ ! -f "$key_file" ] || [ ! -f "${key_file}.pub" ]; then
    echo "未找到SSH密钥，准备生成新的Ed25519密钥..."
    read -p "请输入邮箱地址（用于密钥注释）: " email
    
    # 检查邮箱是否为空
    if [ -z "$email" ]; then
        echo "错误：邮箱地址不能为空。"
        exit 1
    fi
    
    # 检查邮箱格式（简单验证）
    if ! echo "$email" | grep -q "@"; then
        echo "警告：邮箱地址格式可能不正确，但将继续执行..."
    fi
    
    echo "使用邮箱: $email"
    echo "正在生成密钥..."
    ssh-keygen -t ed25519 -f "$key_file" -C "$email" -N ""
    echo "Ed25519密钥生成完成！"
else
    echo "检测到现有SSH Ed25519密钥，跳过生成步骤。"
fi

# 检查公钥是否存在（确保密钥生成成功）
if [ ! -f "${key_file}.pub" ]; then
    echo "错误：SSH公钥不存在，无法继续。"
    echo "注意：检测到私钥文件存在但公钥文件缺失，为避免覆盖现有密钥，请手动处理。"
    exit 1
fi

# 显示公钥内容（可选，用于调试）
echo "使用的公钥内容："
cat "${key_file}.pub"
echo ""

# 使用 sshpass 复制公钥
echo "正在将公钥复制到目标主机 $username@$ip_address..."
sshpass -p "$password" ssh-copy-id -i "${key_file}.pub" "$username@$ip_address"

# 检查是否成功
if [ $? -eq 0 ]; then
    echo "成功设置SSH免密登录到 $username@$ip_address"
    echo "使用的密钥类型: Ed25519"
else
    echo "错误：SSH公钥复制失败。请检查："
    echo "1. 目标主机是否开启SSH服务？"
    echo "2. 用户名/密码是否正确？"
    echo "3. 网络是否可达？"
    exit 1
fi
