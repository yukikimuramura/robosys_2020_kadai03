# robosys_2020_kadai03

### 概要
ques.pyを実行すると「質問を書こう」が出てくるため「欲しいものは?」「なんでも願いが叶うなら?」と打つとans.pyを実行した端末に答えが返ってきます.
この答えに私の涙の思いを乗せました.

### 動作環境
- Rasberry Pi Model 3B+
- Ubuntu18.04
- Ros Noetic

### 実行手順
```
1.ディレクトリに入る
$cd ~/catkin_ws/src
2.リポジトリをクローンする
$git clone https://github.com/yukikimuramura/robosys_2020_kadai03.git
3.一つ前のリポジトリに戻る
$cd ..
4.コンパイルする
$catkin_make
5.rosを起動する
$roscore
6.ディレクトリに入る
$cd ~/catkin_ws/src/robosys_2020_kadai03/spricts
7.実行できるようにそれぞれのプログラムのパーミッションを設定する
$chmod 755 ques.py       
$chmod 755 ans.py     
8.それぞれ別の端末でques.py,ans.pyを実行する
$rosrun mypkg ques.py
$rosrun mypkg ans.py

```
### Demo
こちらが実際に動かした動画のURLです.
https://www.youtube.com/watch?v=ttH49wwj92c&feature=youtu.be
