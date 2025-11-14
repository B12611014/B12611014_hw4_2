import openai
import time
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def chapter_3_flow(cfg, data):
    print("\n[第3章] 神廟封印")
    print("--------------------------------")
    print("你踏入古老的神廟，昏暗的火炬閃爍著微光...")
    print("牆上刻著奇異的銘文，隱約散發著幽光。\n")
    time.sleep(2)

    text = data["temple_inscription.txt"]

    print("[任務] 解讀牆上銘文...\n")
    time.sleep(2)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一名考古學家，正在破解古代密碼。"},
            {"role": "user", "content": f"分析這段銘文，並揭示其中隱藏的訊息：\n{text}"}
        ]
    )

    decoded = response['choices'][0]['message']['content']
    print(f"解碼訊息：\n{decoded}\n")

    print("[提示] 也許答案藏在河流的名字或重生之年的紀年中...")

    # --- 只問一次 ---
    answer = input("\n請輸入重生之詞：").strip()

    # --- 定義可接受答案（大小寫及中英文） ---
    correct_words = ["River Thalen", "塔倫河"]

    # --- 檢查是否「完全相符」 ---
    if answer.lower() in [w.lower() for w in correct_words]:
        print("\n✨ 封印發出藍光... 神廟之門悄然開啟。")
        print("你踏步進入隱藏的密室。冒險繼續...\n")
    else:
        print("\n封印依然沉默，也許這不是正確的重生之詞。")