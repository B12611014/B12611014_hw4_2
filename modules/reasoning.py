# =================== modules/reasoning.py ===================
# Save as: modules/reasoning.py
"""
Functions:
- infer_cause(cfg, decoded_text, events): returns a text with reasoning about civilization decline
"""
import openai


def call_llm(cfg, prompt):
    resp = openai.ChatCompletion.create(
        model=cfg.get('model'),
        messages=[{'role':'user','content':prompt}],
        max_tokens=cfg.get('max_output_tokens', 500)
    )
    return resp.choices[0].message.content.strip()


def infer_cause(cfg, decoded_text, events):
    prompt = (
        f"任務說明：\n請根據解碼後的文字內容與列出的事件，推理可能導致該文明衰落的原因。\n\n"
        f"解碼文字內容：\n{decoded_text}\n\n事件列表：\n{events}\n\n"
        f"請逐步說明你的推理過程，最後給出一個簡短的結論。"
    )
    return call_llm(cfg, prompt)