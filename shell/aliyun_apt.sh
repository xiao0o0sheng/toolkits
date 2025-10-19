# -----------------------------------------------------------------
# !/usr/bin/bash
# -*- coding: utf-8 -*-
# @Created Time:    2025/10/15
# @File:            yuan.sh
# @Software:        Neovim 0.12.0
# @Author:          xiao0o0sheng
# @Email:           xiaosheng7@126.com
# @Version:         
# @Description:     
# -----------------------------------------------------------------





# 自动获取 Ubuntu 版本代号（如 focal、jammy、noble）
UBUNTU_CODENAME=$(lsb_release -cs)
echo "检测到 Ubuntu 版本代号: $UBUNTU_CODENAME"

# 备份原有源
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
echo "已备份原 sources.list 到 sources.list.bak"

# 写入阿里云镜像源
sudo tee /etc/apt/sources.list > /dev/null <<EOF
deb http://mirrors.aliyun.com/ubuntu/ $UBUNTU_CODENAME main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ $UBUNTU_CODENAME-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ $UBUNTU_CODENAME-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ $UBUNTU_CODENAME-backports main restricted universe multiverse
EOF

echo "阿里云镜像源已写入 /etc/apt/sources.list"

# 更新软件包列表
sudo apt update

echo "更新完成，可以使用新的阿里云源安装软件"
