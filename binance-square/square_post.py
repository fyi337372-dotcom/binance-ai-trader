#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests

API_KEY = "ead750e55b1b4a0c8992766992df8e12"
URL = "https://www.binance.com/bapi/composite/v1/public/pgc/openApi/content/add"

def post_to_square(content):
    headers = {
        "Content-Type": "application/json",
        "X-Square-OpenAPI-Key": API_KEY,
        "clienttype": "binanceSkill"
    }
    payload = {"bodyTextOnly": content}
    
    try:
        r = requests.post(URL, headers=headers, json=payload, timeout=30)
        print("Status:", r.status_code)
        print("Response:", r.text)
        
        data = r.json()
        if data.get("code") == "000000":
            post_id = data.get("data", {}).get("id")
            if post_id:
                print("OK! Post ID:", post_id)
                print("Post URL: https://www.binance.com/square/post/" + str(post_id))
            else:
                print("[OK] Post may succeeded but no ID returned")
        else:
            print("[FAIL] Error:", data.get("message"))
            
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        post_to_square(sys.argv[1])
    else:
        print("Usage: python square_post.py <content>")
