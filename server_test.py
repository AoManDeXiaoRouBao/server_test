import requests
import time
import os

def test_server_chan():
    # 1. 填入你的 SendKey (从 https://sct.ftqq.com/ 获取)
    SEND_KEY = os.getenv("SERVER_CHAN_KEY")

    if not SEND_KEY:
        print("❌ 错误：未找到 SERVER_CHAN_KEY 环境变量。请检查 GitHub Secrets 设置。")
        return
    
    # 2. 构建请求 URL
    url = f"https://sctapi.ftqq.com/{SEND_KEY}.send"

    # 3. 准备参数 
    title = "NGA 监控脚本测试消息"
    content = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - 这是一条测试消息，说明 Server 酱配置正确，脚本可以正常发送请求。"

    params = {
        'title': title,
        'desp': content,
    }

    print(f"📤 正在发送消息到 Server 酱...")
    try:
        response = requests.post(url, data=params, timeout=10)
        result = response.json()
        
        if result.get('code') == 0:
            print("✅ 发送成功！请查看微信。")
        else:
            print(f"❌ 发送失败：{result.get('message')}")
    except Exception as e:
        print(f"❌ 发生异常：{e}")

if __name__ == "__main__":

    test_server_chan()
    print("\n测试完成。")
