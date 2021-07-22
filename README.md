# NTU選課小幫手 
### 特點
* 針對能上課的時間，一次將通識課、體育課、學程系上必修選修列出來，自動匯出excel
* 排除關鍵詞搜尋(比如排除專題討論、服務學習)
* 解決"明明只有6 7節有空堂，但選課網只能給你6 7 8 or 7 8 9的課程"
* 如果好用請在右上方給一個star，非常感謝~
### DEMO 

https://user-images.githubusercontent.com/29053630/126666340-3021d788-ee8f-4dbc-bc37-eee54a6467ae.mp4

# 安裝方法 
### Win 10
##### 方法一、 下載程式後並解壓縮，打開dist/my_class.exe後即可以直接運行
##### 方法二、 於anaconda建立python 3.7環境，在下載資料夾輸入 pip install -r requirements.txt，運行pdf2.py
### Mac/Linux
##### 方法一、 於anaconda建立python 3.7環境，在下載資料夾輸入 pip install -r requirements.txt，運行pdf2.py(需修改Key，比如將crtl 換到 cmd等等)
# 使用方法
##### 一、 選擇學期後，可以針對1.開課的學院/學系 2.體育課 3.學程課 4.通識課 做一次性的選擇(選擇為聯集)
##### 二、 針對課程關鍵詞，建立在上方的課程中篩選出含有此關鍵詞的課程
##### 三、 針對不想要的課程關鍵詞，可在輸入後排除含有此關鍵詞的課程，(利用空白做分隔)
##### 四、 針對可以上課的時間，列出以上的課程(時間需要完全符合)
##### 五、 自動於同exe檔案的資料夾生成名為class_info.xls的excel檔案，並且顯示出excel表格
