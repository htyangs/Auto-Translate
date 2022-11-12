# Auto-Translate
### Automatically translate English(or any language) into Chinese, with .exe package running on Windows directly and .py file.
### Available in all kinds of file Ex: pdf, word, txt, browser
### Check the definition of WIKI

# 即時翻譯 (一鍵查詢定義、插入單字、製作單字本)
### 特點
* 一鍵自動查詢單字翻譯/wiki定義、發音、自動插入/貼上翻譯結果/製作成單字本/懸浮視窗顯示
* 適用於網站、pdf、word、onenote等各式各樣程式
* 可翻譯單字與段落 (英文、日文、韓文、西班牙文等等任何語言)
* 可用於迅速查詢論文單字、外文小說的翻譯/維基百科定義，不拖累閱讀速度
* 一鍵製作txt單字本，包含中文以及英文，用於後續單字複習
* 如果好用請在右上方給一個star，非常感謝XD
### 更新
* wiki查詢單詞定義，可用來查詢專有名詞之定義並顯示在視窗上、複製在剪貼簿中
### DEMO 
<table>
  <tr>
    <td align="center"> F1 視窗顯示</td>
     <td align="center">F2 插入顯示</td>
  </tr>
  <tr>
  <td align="center"><img src="https://user-images.githubusercontent.com/29053630/124051289-c73e8680-da4e-11eb-9886-0b1b0fbadc64.gif" width="6000">
  <td align="center"><img src="https://user-images.githubusercontent.com/29053630/124052280-b727a680-da50-11eb-9366-34f79be02118.gif" width="6000">
  </tr>
 </table>
 
<table>
  <tr>
    <td align="center"> F8 Wiki定義</td>
     <td align="center">F9 製作單字本</td>
  </tr>
  <tr>
    <td style="text-align: center; vertical-align: middle;"><img src="https://user-images.githubusercontent.com/29053630/124051451-1edcf200-da4f-11eb-9106-9cad426d3a47.gif" width="600"/>
    <td style="text-align: center; vertical-align: middle;"><img src="https://user-images.githubusercontent.com/29053630/124051457-200e1f00-da4f-11eb-9a43-a08be8e2205b.gif" width="600"/>
  </tr>
 </table>
 


# 安裝方法 
### Win 10
##### 方法一、 下載程式後並解壓縮，打開dist/pdf2.exe後即可以直接運行
##### 方法二、 於anaconda建立python 3.7環境，在下載資料夾輸入 pip install -r requirements.txt，運行pdf2.py
### Mac/Linux
##### 方法一、 於anaconda建立python 3.7環境，在下載資料夾輸入 pip install -r requirements.txt，運行pdf2.py(需修改Key，比如將crtl 換到 cmd等等)
# 主要按鍵
由於某些快捷鍵已經被程式定義(比如f3在瀏覽器上被定義過了，會造成翻譯失敗)，因此會有兩個可用快捷鍵，可自行選用適合的
#### 反白要翻譯的文字後按下下面按鍵
* F1 or F3 : 用在網站、PDF檔案或任何可以反白的文字，顯示翻譯在浮動視窗 (F1:網站/F3:Adobe reader pdf)
* F2 : 用在Word檔案、txt檔案、onenote等可以輸入文字的軟體，反白要翻譯的部分後會自動插入翻譯在單字後面
* F4 : 用在不能輸入文字，但可以貼上文字的軟體，比如Drawboard，與F2類似但是利用貼上作為輸出
* F5 : 單純發音，不能用在網站
* F6 : 同F1，在顯示完後發音
* F8 : 查詢wiki對於單字(專有名詞)的定義，顯示在視窗並且複製在剪貼簿
* F9 : 反白想要翻譯的單字後會自動儲存翻譯txt檔案中，作為後續復習用的單字本，txt檔案會存在與pdf2.exe同資料夾，名為vocabulary.txt

# 自行修改方法
* 自定義快速按鍵 : 於pdf2.py檔案，修改key == keyboard.Key.f1即可以修改快捷鍵
* 軟體打包成.exe : 利用pyinstaller對pdf2.py打包即可以形成.exe檔案 

