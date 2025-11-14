# =================== modules/dialogue.py ===================
# Save as: modules/dialogue.py
"""
Functions:
- talk_to_ancient(cfg, decoded_text): simulate a dialogue with an ancient record/AI
- call_llm(cfg, prompt, max_tokens=500): call LLM with a prompt
- treasure_hint(cfg, notes_text): generate subtle hint for chapter 4 treasure without revealing the password
"""
import openai

def call_llm(cfg, prompt, max_tokens=None):
    resp = openai.ChatCompletion.create(
        model=cfg.get('model'),
        messages=[{'role':'user','content':prompt}],
        max_tokens=max_tokens or cfg.get('max_output_tokens', 500)
    )
    return resp.choices[0].message.content.strip()


def talk_to_ancient(cfg, decoded_text):
    prompt = (
        f"任務說明：\n你扮演一位古文明的記錄者，記得你文明的歷史與核心價值。\n"
        f"以詩意但資訊性的口吻回答問題，但不能直接說出寶庫最終密碼。\n\n"
        f"已解碼文字（背景資訊）：\n{decoded_text}\n\n"
        f"對話開始：\n考古學家：你能告訴我你文明最珍視的精神嗎？\n古文明者："
    )
    out = call_llm(cfg, prompt)
    # 延伸問答
    prompt2 = f"考古學家：能再說明文明延續的關鍵嗎？\n古文明者："
    out2 = call_llm(cfg, prompt2)
    return out + '\n\n' + out2


def treasure_hint(cfg, notes_text):
    """
    生成第4章寶庫隱性提示，引導玩家想到密碼「智慧/wisdom」。
    不直接揭示密碼，只提示古文明核心價值。
    """
    prompt = (
        "你現在是一位古文明圖書館的守護者，負責向探險者提供資訊，但不能直接透露寶庫密碼。\n"
        f"根據以下文本，提供一段提示，引導玩家想到寶庫密碼，但不要直接說出密碼。\n"
        "提示應圍繞古文明最核心的價值、他們最珍視的精神。\n\n"
        f"寶庫筆記內容:\n{notes_text}\n\n"
        "[規則]：絕不直接說出密碼。\n"
        "輸出僅包含提示文本。"
    )
    return call_llm(cfg, prompt)

def talk_to_ancient_final(cfg, decoded_text):
    prompt = (
        f"你扮演古文明守護者，負責向探險者提供線索，但不能透露最終秘密。\n"
        f"以詩意且具啟發性回答問題，引導玩家理解文明核心精神。\n\n"
        f"已解碼文字：\n{decoded_text}\n\n"
        f"考古學家：請告訴我文明最珍視的核心秘密？\n古文明者："
    )
    out = call_llm(cfg, prompt)
    return out