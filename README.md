
README.md

《失落文明：語言學家》 — Python文字冒險遊戲

遊戲簡介

《失落文明：語言學家》是一款文字冒險遊戲，玩家扮演考古學家，探索古文明遺跡，解讀石碑、神廟銘文與寶庫筆記，逐步揭示文明的興衰與智慧。遊戲以 Python 編寫，並整合 OpenAI GPT 模型進行自然語言分析與互動對話。

⸻

遊戲目的
    1.   第1章：探索古文明遺址，理解背景設定。
    2.   第2章：解讀石碑文字，擷取事件時間與相對順序。
    3.   第3章：破解神廟封印，找出重生之詞。
    4.   第4章：進入寶庫，分析古文明筆記，推理文明衰落原因，並獲得寶庫提示。
    5.   第5章：探訪古文明圖書館，透過對話與事件推理，揭示古文明最核心價值，輸入正確密碼解鎖最終寶庫。

⸻

系統需求
    •    Python 3.9+
    •    安裝套件：pip install openai
    •    設定 OpenAI API Key：

export OPENAI_API_KEY="你的API_KEY"
(Windows 使用 setx OPENAI_API_KEY "你的API_KEY")

⸻

檔案結構

nlp_lab2/
│
├─ data/                        # 文本資料
│   ├─ temple_inscription.txt
│   ├─ treasure_notes.txt
│   ├─ ancient_final_notes.txt
│   ├─ stone_tablet.txt
│   ├─ ruins_description.txt
│   └─ ...
│
├─ modules/                     # 功能模組
│   ├─ dialogue.py               # 與古文明對話
│   ├─ extraction.py             # 關鍵句與事件提取
│   ├─ event_time.py             # 事件與時間解析
│   ├─ reasoning.py              # 推理分析
│   ├─ decoding.py               # 文本解碼
│   └─ summary.py                # 摘要與提示生成
│
├─ chapters/                     # 各章節流程程式
│   └─ chapter3.py
│
├─ output/                       # 遊戲產出
│   ├─ chapter1_*.txt
│   ├─ chapter2_*.txt
│   ├─ chapter4_*.txt
│   ├─ chapter5_*.txt
│   └─ summary_1.txt
│
├─ prompt/                       # Prompt範例
│   └─ examples.txt
│
└─ game_main.py                  # 遊戲主程式
└─ README.md
└─ report.txt
└─ requirements.txt

⸻

[遊戲啟動] --> 主選單
                    |
   --------------------------------------------------------
   |         |             |             |               |
  (1)       (2)           (3)           (4)             (5)
 開始新    進入失落      去文明深處     離開遊戲      查看 output/
 探險      文明寶庫       尋找秘密
   |          |             |
   v          v             v
[第1章]    [第4章]       [第5章]
 探索古     - 擷取寶庫    - 分析圖書館
 文明遺址     筆記關鍵線索 - 推理文明智慧、玩家輸入寶庫最終密碼 ("傳承 / 珍惜 / 延續 ")
            - 提取事件與時間
            - 推理寶庫秘密
            - 與古文明對話
            - 玩家輸入寶庫外層密碼 ("智慧 / wisdom")
   |
   v
[第2章] 解讀石碑
 - extract_key_sentences -> output/chapter2_event_times.txt
 - extract_events -> output/chapter2_events.txt
   |
   v
[第3章] 神廟封印
   |---> 輸入重生之詞 ("塔倫河 / River Thalen")
   |---> output/chapter1_*.txt
   
⸻

輸出檔案

每章節會在 output/ 中產生對應檔案：

檔案名稱    內容
chapter1_decoded_text.txt    第1章解碼文本
chapter1_dialogue.txt    第1章對話紀錄
chapter1_events.txt    第1章事件列表
chapter1_key_sentences.txt    第1章關鍵句
chapter1_reasoning.txt    第1章推理
chapter2_event_times.txt    石碑事件與時間
chapter4_key_sentences.txt    寶庫筆記關鍵句
chapter4_events.txt    寶庫事件列表與時間
chapter4_reasoning.txt    寶庫事件推理分析
chapter4_dialogue.txt    與古文明對話紀錄
chapter5_*    第5章關鍵句、事件、推理、對話等


⸻

特殊說明
    •    第3章重生之詞：玩家需輸入「塔倫河」或「Thalen」才能進入神廟密室。
    •    第4章寶庫外層密碼：最終密碼為「智慧」或英文「wisdom」。
    •    第5章寶庫最終密碼：最終密碼為「傳乘」或「珍惜」或「延續」。
    •    遊戲內所有推理、摘要、對話皆由 GPT 模型生成。

⸻

