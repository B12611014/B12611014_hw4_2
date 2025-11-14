# =================== modules/decoding.py ===================
# Save as: modules/decoding.py
"""
Functions:
- decode_tablet(cfg, raw_tablet_text): returns a decoded/translated text
"""
import openai


def call_llm(cfg, prompt):
    resp = openai.ChatCompletion.create(
        model=cfg.get('model'),
        messages=[{'role':'user','content':prompt}],
        max_tokens=cfg.get('max_output_tokens', 500)
    )
    return resp.choices[0].message.content.strip()


def decode_tablet(cfg, raw_tablet_text):
    prompt = (
        f"任務說明：\n你是一位專精於古文字的考古學家。以下是一片未知文字的古代石板。\n"
        f"請提供合理的翻譯／意涵，用清楚的繁體中文描述，並逐步說明你的推理過程。\n\n"
        f"石板內容：\n{raw_tablet_text}\n\n回答："
    )
    out = call_llm(cfg, prompt)
    # return entire output; later modules will parse as needed
    return out