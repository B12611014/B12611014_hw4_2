# =================== modules/summary.py ===================
# Save as: modules/summary.py
"""
Functions:
- make_summary(cfg, key_sentences, decoded_text, events, reasoning_text)
"""


def make_summary(cfg, key_sentences, decoded_text, events, reasoning_text):
    parts = []
    parts.append('=== KEY SENTENCES ===')
    parts.extend(key_sentences)
    parts.append('\n=== DECODED TEXT (excerpt) ===')
    parts.append(decoded_text[:1500])
    parts.append('\n=== EVENTS ===')
    for e in events:
        parts.append(f"- {e.get('event')} ({e.get('time','unknown')})")
    parts.append('\n=== REASONING ===')
    parts.append(reasoning_text)
    return '\n'.join(parts)
