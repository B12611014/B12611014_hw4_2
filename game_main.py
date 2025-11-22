# =================== game_main_zh.py ===================
# Save as: game_main_zh.py
"""
Main controller for the Lost Civilization game (繁體中文版).
Run: python3 game_main_zh.py
It will ask for your OpenAI API key and then guide you through Chapter 1.
"""
import os
import json
import openai
import time
import logging
from modules import extraction, decoding, reasoning, dialogue, summary
from chapters.chapter3 import chapter_3_flow
import time
from modules import extraction, decoding, reasoning, dialogue
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
CONFIG_PATH = 'config.json'


def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_data():
    data = {}
    folder = "data"
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            with open(os.path.join(folder, fname), "r", encoding="utf-8") as f:
                data[fname] = f.read()
    return data


def save_output(filename, text):
    os.makedirs('output', exist_ok=True)
    path = os.path.join('output', filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    logging.info(f'已將輸出存檔至 {path}')


def chapter_1_flow(cfg, data):
    print('\n--- 第1章：遺跡探索 ---\n')
    print(data['ruins_description.txt'])

    # --- 1. Key Sentences ---
    print('\n[任務] 從考古學家日誌中擷取關鍵句...')
    key_sents = extraction.extract_key_sentences(cfg, data['archaeologist_log.txt'])
    save_output('chapter1_key_sentences.txt', '\n'.join(key_sents))

    print("\n--- Key Sentences ---")
    for i, s in enumerate(key_sents, 1):
        print(f"{i}. {s}")

    # --- 2. Decoding ---
    print('\n[任務] 解讀古代石板片段...')
    decoded = decoding.decode_tablet(cfg, data['ancient_tablet.txt'])
    save_output('chapter1_decoded_text.txt', decoded)

    print("\n--- Decoded Tablet ---")
    print(decoded)

    # --- 3. Events Extraction ---
    print('\n[任務] 從解碼文本中擷取事件與時間線...')
    events = extraction.extract_events(cfg, decoded)
    save_output(
        'chapter1_events.txt',
        '\n'.join([f"{i+1}. {e['event']} - {e.get('time','未知')}" for i, e in enumerate(events)])
    )

    print("\n--- Events ---")
    for i, e in enumerate(events, 1):
        print(f"{i}. 事件: {e['event']} | 時間: {e.get('time', '未知')}")

    # --- 4. Reasoning ---
    print('\n[任務] 根據現有線索推理文明發展...')
    reasoning_text = reasoning.infer_cause(cfg, decoded, events)
    save_output('chapter1_reasoning.txt', reasoning_text)

    print("\n--- Reasoning ---")
    print(reasoning_text)

    # --- 5. Dialogue ---
    print('\n[任務] 與古代 AI 對話（模擬）...')
    dialog = dialogue.talk_to_ancient(cfg, decoded)
    save_output('chapter1_dialogue.txt', dialog)

    print("\n--- Ancient Dialogue ---")
    print(dialog)

    # --- 6. Summary ---
    final_summary = summary.make_summary(cfg, key_sents, decoded, events, reasoning_text)
    save_output('summary_1.txt', final_summary)

    print("\n--- Final Summary ---")
    print(final_summary)

    print('\n第1章完成！輸出檔案已存於 output/。\n')


def chapter_2_flow(cfg, data):
    print("\n--- 第2章：解讀石碑 ---\n")
    print("你發現一塊覆滿灰塵的石碑，上面刻滿古老文字，似乎記錄了王國的興衰。")

    print("\n[任務] 從石碑中擷取事件時間...\n")
    from modules import event_time
    events = event_time.extract_event_times(cfg, data["stone_tablet.txt"])

    # 中文化漂亮輸出
    print("\n以下是石碑中所有事件的摘要：\n")
    for i, e in enumerate(events, 1):
        print(f"事件 {i}:")
        print(f"  原始句子：{e.get('sentence','')}")
        print(f"  時間表達：{e.get('time','')}")
        print(f"  事件描述：{e.get('description','')}")
        print(f"  相對順序：{e.get('relative_order','')}")
        print('-'*40)

    # 儲存 JSON
    import json
    os.makedirs("output", exist_ok=True)
    with open("output/chapter2_event_times.txt", "w", encoding="utf-8") as f:
        f.write(json.dumps(events, ensure_ascii=False, indent=2))

    print("\n結果已存至 output/chapter2_event_times.txt")


def chapter_4_flow(cfg, data):

    print("\n--- 第4章：失落文明的寶庫 ---\n")
    print("你踏入失落文明的寶庫入口，四周刻滿古老符號與神祕圖紋。")
    print("每一步都彷彿踩在歷史脈動之上，空氣中傳來若有似無的低語——")
    print("那些是古人留下的警告，或是指引？你尚且不得而知。\n")
    time.sleep(2)

    # 1️⃣ 提取關鍵句子
    print("[任務] 擷取寶庫筆記中的關鍵線索...\n")
    key_sents = extraction.extract_key_sentences(cfg, data['treasure_notes.txt'])
    for i, s in enumerate(key_sents, 1):
        print(f"{i}. {s}")
    print()
    os.makedirs('output', exist_ok=True)
    with open("output/chapter4_key_sentences.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(key_sents))

    # 2️⃣ 提取事件與時間
    print("[任務] 分析寶庫歷史事件與時間順序...\n")
    events_text = extraction.extract_events(cfg, data['treasure_notes.txt'])
    for idx, e in enumerate(events_text, 1):
        print(f"{idx}. {e['event']} - {e.get('time','未知')}")
    with open("output/chapter4_events.txt", "w", encoding="utf-8") as f:
        for e in events_text:
            f.write(f"{e['event']} - {e.get('time','未知')}\n")

    # 3️⃣ 推理寶庫秘密
    print("\n[任務] 推理寶庫所隱藏的真正意義...\n")
    reasoning_text = reasoning.infer_cause(cfg, data['treasure_notes.txt'], events_text)
    print(reasoning_text)
    with open("output/chapter4_reasoning.txt", "w", encoding="utf-8") as f:
        f.write(reasoning_text)

    # 4️⃣ 與古文明智慧對話
    print("\n[任務] 試圖與古文明智慧產生共鳴，取得開啟寶庫的提示...\n")
    hint_text = dialogue.treasure_hint(cfg, data['treasure_notes.txt'])
    print(hint_text)
    with open("output/chapter4_dialogue.txt", "w", encoding="utf-8") as f:
        f.write(hint_text)

    # 5️⃣ 玩家輸入密碼
    print("\n寶庫石門浮現一道金色文字，等待你說出關鍵詞方可開啟...")
    answer = input("請輸入寶庫外層密碼：").strip().lower()

    # 判斷密碼
    correct_answers = ["智慧", "wisdom"]
    if answer in correct_answers:
        print("\n✨ 石門微微震動，象徵外層封印已鬆動。")
        print("你看見深處的光芒閃爍，那裡才是真正的寶庫核心……")
    else:
        print("\n石門紋絲不動，似乎還需要更正確的線索。")

    print("\n第4章完成，所有輸出已存於 output/ 目錄中。")

def chapter_5_flow(cfg, data):

    print("\n--- 第5章：古文明的最終智慧 ---\n")
    print("你走進古文明最深處的秘密圖書館。")
    print("四周堆滿古老卷軸、石板與未解的符文，彷彿每一塊石頭都")
    print("藏著一段文明的心跳與遺憾。\n")
    time.sleep(2)

    # 1️⃣ 提取關鍵句子
    print("[任務] 擷取古文明筆記的核心線索...\n")
    key_sents = extraction.extract_key_sentences(cfg, data['ancient_final_notes.txt'])
    for i, s in enumerate(key_sents, 1):
        print(f"{i}. {s}")
    print()
    os.makedirs('output', exist_ok=True)
    with open("output/chapter5_key_sentences.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(key_sents))

    # 2️⃣ 提取事件與時間
    print("[任務] 分析古文明的歷史脈絡...\n")
    events_text = extraction.extract_events(cfg, data['ancient_final_notes.txt'])
    for idx, e in enumerate(events_text, 1):
        print(f"{idx}. {e['event']} - {e.get('time','未知')}")
    with open("output/chapter5_events.txt", "w", encoding="utf-8") as f:
        for e in events_text:
            f.write(f"{e['event']} - {e.get('time','未知')}\n")

    # 3️⃣ 推理文明秘密
    print("\n[任務] 詮釋古文明留下的最終價值與教誨...\n")
    reasoning_text = reasoning.infer_cause(cfg, data['ancient_final_notes.txt'], events_text)
    print(reasoning_text)
    with open("output/chapter5_reasoning.txt", "w", encoding="utf-8") as f:
        f.write(reasoning_text)

    # 4️⃣ 與古人智慧交談
    print("\n[任務] 與古文明之靈進行對話，以獲得最後啟示...\n")
    dialog = dialogue.talk_to_ancient(cfg, data['ancient_final_notes.txt'])
    print(dialog)
    with open("output/chapter5_dialogue.txt", "w", encoding="utf-8") as f:
        f.write(dialog)

    # 5️⃣ 玩家輸入最終密碼
    print("\n在寶庫最深處，一枚古老印記發出微光。")
    print("它等待你說出古文明最珍視的核心價值……\n")
    answer = input("請輸入寶庫最終密碼：").strip().lower()

    correct_answers = ["傳承", "珍惜", "延續"]
    if answer in correct_answers:
        print("\n✨ 最終封印破裂！")
        print("金光灑落，你步入文明之心，見證千年智慧的真正意義。")
        print("你不只是發現寶藏，而是接下了文明的火焰。🔥")
    else:
        print("\n封印仍未解開，古文明尚未向你完全敞開心門。")

    print("\n第5章完成，所有輸出已存入 output/。")

def main():
    cfg = load_config()
    if "OPENAI_API_KEY" not in os.environ:
        api_key = input("請輸入你的 OpenAI API 金鑰：").strip()
        openai.api_key = api_key
    else:
        openai.api_key = os.getenv("OPENAI_API_KEY")

    data = read_data()

    while True:
        print('\n歡迎來到《失落文明：語言學家》')
        print('(1) 開始新的探險')
        print('(2) 進入失落文明的寶庫')
        print('(3) 去文明深處尋找秘密')
        print('(4) 離開遊戲')
        print("(5) 查看 output/ 中的檔案")
        choice = input('請選擇：').strip()

        if choice == '1':
            chapter_1_flow(cfg, data)
            chapter_2_flow(cfg, data)
            chapter_3_flow(cfg, data)  # 確保 chapter_3_flow 內只呼叫一次 input()
        elif choice == '2':
            # Chapter 4 容錯：先確認檔案是否存在
            if 'treasure_notes.txt' in data:
                chapter_4_flow(cfg, data)
            else:
                print("缺少 treasure_notes.txt，請先放入 data/ 資料夾")
        elif choice == '3':
            chapter_5_flow(cfg, data)
        elif choice == '4':
            print('再見！')
            break
        elif choice == '5':
            print('\n輸出檔案列表：')
            for f in os.listdir('output') if os.path.exists('output') else []:
                print(' -', f)
        else:
            print('輸入錯誤，請重新選擇。')


if __name__ == '__main__':
    main()