import os
import yaml
from datetime import datetime
import resend
from dotenv import load_dotenv

CAPSULES_FILE_PATH = "_data/capsules.yml"

load_dotenv()

def send_capsules_email():
    capsules = []
    try:
        with open(CAPSULES_FILE_PATH, "r", encoding="utf-8") as f:
            loaded_data = yaml.safe_load(f)
            if loaded_data:
                capsules = loaded_data
            
    except FileNotFoundError:
        print(f"File {CAPSULES_FILE_PATH} not found")
        return
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return
    
    if not capsules:
        print("No capsules found in _data/capsules.yml")
        return
    api_key = os.getenv("RESEND_API_KEY")
    if not api_key:
        raise ValueError("RESEND_API_KEY is not set")
    # Configure Resend Python SDK using module-level api_key per official docs
    resend.api_key = api_key
    today_str = datetime.now().strftime("%Y-%m-%d")
    from_address = os.getenv("RESEND_FROM")
    if not from_address:
        raise ValueError("RESEND_FROM is not set")
    is_modified = False

    for capsule in capsules:
        if capsule.get("status") == "scheduled":
            deliver_date_str = str(capsule.get("delivery_date"))

            if deliver_date_str <= today_str:
                print(f"检测到到期胶囊 (ID: {capsule.get('id')})，准备发送至 {capsule.get('email')}...")
                try:
                    subject_line = str(capsule.get("subject") or "一封来自过去的信件")
                    params = {
                        "from": from_address,  # 必须是你在Resend验证过的发件地址
                        "to": [capsule.get('email')],
                        "subject": subject_line,
                        "html": f"<p>{capsule.get('content', '').replace(os.linesep, '<br>')}</p>",
                    }
                    response = resend.Emails.send(params)
                    # 6. 发送成功后，更新状态
                    print(f"邮件发送成功！ Resend ID: {response['id']}")
                    capsule['status'] = 'sent'
                    is_modified = True
                except Exception as e:
                    # 7. 发送失败后，记录错误信息并更新状态
                    print(f"邮件发送失败: {e}")
                    capsule['status'] = f"error: {str(e)[:100]}" # 只记录部分错误信息
                    is_modified = True

    # 8. 如果文件内容有变动，则写回文件
    if is_modified:
        print("正在更新胶囊状态文件...")
        with open(CAPSULES_FILE_PATH, 'w', encoding='utf-8') as file:
            yaml.dump(capsules, file, allow_unicode=True)
        print("文件更新成功。")

if __name__ == "__main__":
    send_capsules_email()
    