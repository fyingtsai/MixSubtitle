# MixSubtitle
用途：合併中英文字幕檔為雙字幕，供學習英文為用

##注意事項
1. 程式目前支援UTF-8，請注意先將中文字幕檔做轉檔
2. 程式以中英文相同時間做合併，若時間不同步可自行修改(將判斷式改為判斷檔案id)

##使用方式
可用shell script，參數傳遞請依照:
./mixSub.py 中文檔路徑 英文檔路徑 輸出檔路徑

##執行結果範例
![chs](https://cloud.githubusercontent.com/assets/10824338/6057633/e4725560-ad5a-11e4-8fd3-207c14fc9de2.png)
![eng](https://cloud.githubusercontent.com/assets/10824338/6057634/e474c688-ad5a-11e4-9300-9fa3152c631f.png)
![mix](https://cloud.githubusercontent.com/assets/10824338/6057635/e47854a6-ad5a-11e4-9584-a16a3ebd3dc1.png)
