import openai
import json

def call_llm(cfg, prompt):
    resp = openai.ChatCompletion.create(
        model=cfg.get("model"),
        messages=[{"role": "user", "content": prompt}],
        max_tokens=cfg.get("max_output_tokens", 500)
    )
    return resp["choices"][0]["message"]["content"].strip()


def extract_event_times(cfg, text):
    prompt = f"""
你是一個嚴格的 JSON 輸出機器。

任務：從以下文章中擷取事件，依時間順序整理。

⚠️ 僅輸出「純 JSON」！
⚠️ 不要加入註解、不需要使用 ```json、不要加文字敘述。
⚠️ JSON 結構必須是 list，格式如下：

[
  {{
    "sentence": "原句",
    "time": "時間表達(若無填空字串)",
    "description": "事件描述",
    "relative_order": "1,2,3..."
  }}
]

文章如下：
{text}
"""

    out = call_llm(cfg, prompt)

    import json

    # 1️⃣ 先嘗試直接解析（最理想）
    try:
        return json.loads(out)
    except:
        pass

    # 2️⃣ 如果開頭有 markdown 區塊，自動清理
    cleaned = out.strip().replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(cleaned)
    except:
        # 3️⃣ 最後手段：回傳空 list（或擋住錯誤）
        print("⚠️ 無法解析模型輸出的 JSON，請檢查 prompt。")
        return []