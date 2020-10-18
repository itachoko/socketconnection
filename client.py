#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:48:15 2020

@author: reiya
"""

# クライアントを作成

import socket

i=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('127.0.0.1', 50008))
    # サーバにメッセージを送る
    while i<5:
        x = input("send message: ")
        s.sendall(x.encode())
        i+=1
