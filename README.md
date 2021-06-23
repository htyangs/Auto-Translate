# 即時翻譯軟體 (適用任何語言)
### 特點
* 一鍵自動查詢單字、翻譯、輸入、發音
* 適用於網站、pdf、word、onenote等各式各樣程式
* 可翻譯單字與段落 (英文、日文、韓文、西班牙文等等任何語言)
* 可用於迅速查詢論文單字、外文小說，不拖累閱讀速度
* 一鍵製作txt單字本，包含中文以及英文，用於後續單字複習
# 安裝方法 
### Win 10
##### 方法一、 下載程式後並解壓縮，打開dist/pdf2.exe後即可以直接運行
##### 方法二、 於anaconda建立python 3.7環境，在下載資料夾輸入 pip install -r requirements.txt，運行pdf2.py
### Mac/Linux
##### 方法一、 於anaconda建立python 3.7環境，在下載資料夾輸入 pip install -r requirements.txt，運行pdf2.py(需修改Key，比如將crtl 換到 cmd等等)
# 主要按鍵
由於某些快捷鍵已經被程式定義(比如f3在瀏覽器上被定義過了，會造成翻譯失敗)，因此會有兩個可用快捷鍵，可自行選用適合的
* F1 or F3 : 用在網站、PDF檔案或任何可以反白的文字，顯示翻譯在浮動視窗 (F1:網站/F3:Adobe reader pdf)
* F2 : 用在Word檔案、txt檔案、onenote等可以輸入文字的軟體，反白要翻譯的部分後會自動插入翻譯在單字後面
* F4 : 用在不能輸入文字，但可以貼上文字的軟體，比如Drawboard，與F2類似但是利用貼上作為輸出
* F6 or F8 : 同F1，在顯示完後發音 (兩個按鍵為了配合非定義過的快捷鍵)
* F9 : 反白想要翻譯的單字後會自動儲存翻譯txt檔案中，作為後續復習用的單字本，txt檔案會存在與pdf2.exe同資料夾，名為vocabulary.txt
# 自行修改方法
* 自定義快速按鍵 : 於pdf2.py檔案，修改key == keyboard.Key.f1即可以修改快捷鍵
* 軟體打包成.exe : 利用pyinstaller對pdf2.py打包即可以形成.exe檔案 
# Auto-Translate
### Automatically translate English into Chinese, with .exe package running on Windows directly and .py file.
### Available in all kinds of file Ex: pdf, word, txt, browser
# Key function
* F2 : use primarily in word or txt file where you can type word directly
* F4 : use primarily in file that cannot key in any words but can paste words into it (crtl+v). Ex: Drawboard
* F9 : save the vocabulary in another txt which can be used to review those words.
* F8 : use another windows do display the tranlation, which can be used in pdf file or internet
