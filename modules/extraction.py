import os
import openai


def call_llm(cfg, prompt):
    resp = openai.ChatCompletion.create(
        model=cfg.get('model'),
        messages=[{'role':'user','content':prompt}],
        max_tokens=cfg.get('max_output_tokens', 500)
    )
    return resp.choices[0].message.content.strip()


def extract_key_sentences(cfg, text):
    prompt = f"""任務說明：
請從文章中找出最能表達主要概念的三個句子。

文章內容：
{text}

請以條列方式列出三個關鍵句：
"""
    out = call_llm(cfg, prompt)
    # simple split by newline and take top 3 non-empty
    lines = [l.strip('1234567890. -') for l in out.splitlines() if l.strip()]
    return lines[:3]


def extract_events(cfg, text):
    prompt = f"""任務說明：
請從文章中擷取所有事件，並標註對應的時間（如果有）。

文章內容：
{text}

請以條列方式列出事件：
"""
    out = call_llm(cfg, prompt)
    events = []
    for line in out.splitlines():
        if not line.strip():
            continue
        # naive parse: split by '-' or ':'
        if '-' in line:
            parts = line.split('-')
            event = parts[0].strip('1234567890. ')
            time = parts[1].strip() if len(parts) > 1 else ''
        elif ':' in line:
            parts = line.split(':')
            event = parts[0].strip('1234567890. ')
            time = parts[1].strip() if len(parts) > 1 else ''
        else:
            event = line.strip('1234567890. ')
            time = ''
        events.append({'event': event, 'time': time})
    return events