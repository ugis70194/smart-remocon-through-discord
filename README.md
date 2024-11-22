# smart-remocon-through-discord

## 概要

「リモコンどこいった？」をスマホをリモコン代わりにすることで解決する。  

## インターフェース

iosアプリのショートカットからHTTPリクエストを送信する。  
送信するメッセージの内容を事前に登録しておくことでワンタップで諸々の操作が可能。

## 初期化

1. `remocon/` 以下を raspberrypi 上にコピー
2. 必要な赤外線信号を irrp.py を使って登録
3. 必要な環境変数を `.env` に入力
4. crontab に自動化したい操作を記入
5. systemctl に remocon.service を登録して、service を起動する

## 詳細

raspberryPi Zero 上には赤外線送受信回路を実装されている。  
この回路を用いて、送信したい赤外線信号を事前に登録しておき、任意のタイミングで登録した赤外線信号を送信できるようにしておく。  

また、raspberryPi上にdiscord botサーバーを立ち上げておく。  
botを登録したチャンネルに対応するメッセージを送信することで、対応する赤外線信号を送信する仕組みが実装されている。  
加えて、raspberryPi起動時にdiscord botサーバーを自動起動するためにserviceファイルを記述してある。  

discordサーバーを用いる理由はwebhookを用いて、外部から簡単にraspberryPiにメッセージを送信できるためである。  


## 備考

WPA2-PSK/WPA3-SAEを使用している場合のWi-Fi設定は以下を参照。  

https://raspida.com/wi-fi-setting-env#index_id6

エアコンの信号が長すぎる場合の対応は以下を参照。  

https://korintje.com/archives/28  

http://www.neko.ne.jp/~freewing/raspberry_pi/raspberry_pi_gpio_pigpio_ir_remote_control/