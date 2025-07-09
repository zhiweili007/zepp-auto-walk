import os
import json
import random
import time

def log(msg):
    print(f"[刷步日志] {msg}")

def load_config():
    raw = os.environ.get("CONFIG")
    if not raw:
        raise ValueError("未检测到 CONFIG，请前往 Secrets 添加环境变量")

    try:
        config = json.loads(raw)
        return config if isinstance(config, list) else [config]
    except Exception as e:
        raise ValueError(f"CONFIG 格式错误：{e}")

def simulate_login(user, pwd):
    return "@" in user or len(user) >= 6  # 简单模拟登录成功条件

def simulate_upload(user, step):
    log(f"{user} 上传步数：{step}")
    return True

def run(cfg):
    user = cfg.get("USER")
    pwd = cfg.get("PWD")
    min_step = int(cfg.get("MIN_STEP", 8000))
    max_step = int(cfg.get("MAX_STEP", 12000))
    sleep_gap = int(cfg.get("SLEEP_GAP", 3))

    if not user or not pwd:
        log("账号或密码缺失，跳过")
        return

    if not simulate_login(user, pwd):
        log(f"❌ 登录失败：{user}")
        return

    step = random.randint(min_step, max_step)
    if simulate_upload(user, step):
        log(f"✅ 步数上传成功：{step}")
    else:
        log(f"❌ 上传失败")

    time.sleep(sleep_gap)

def main():
    configs = load_config()
    for cfg in configs:
        run(cfg)

if __name__ == "__main__":
    main()
