# What About Kawaii-Term
kawaii-termは主にエンジニアに対して適切に精神的な癒しを与えることで、ストレスを低減するものです　　

この世界が可愛ければ戦争は無くなるのに  

**めちゃくちゃ変更しました。**

## 機能一覧
- 顔文字の表示
- 空きメモリの表示
- 時間の表示

## サポートしているOS
- Ubuntu Linux (zesty, x86_64, armhf, arm64)
- Debian Linux (sid, armhf, arm64)
- Arch Linux (x86_64)

## Requrements
python3が以下のパスに通っている必要があります  
```console
$ which python3
/usr/bin/python3
```

Ubuntu Linux, Debian Linuxでは以下のようにインストールしてください
```console
$ sudo apt install python3
```

curlもインストールされている必要があります
```console
$ which curl
/usr/bin/curl
```

Ubuntu Linux, Debian Linuxでは以下のようにインストールしてください
```console
$ sudo apt install curl
```

## Install 
任意ディレクトリにクローンできます。
```console
$ git clone https://github.com/GINK03/kawaii-term
```
template.bashrcを~/.bashrcに追加します（アップデート時は計算時間が無駄にならないように適切に、重複等を消すなどして、軽くしてください）
```
$ cd kawaii-term
$ cat templte.bashrc  >> ~/.bashrc
```

## ライセンス
Copyright (C) 2021 Viterum(Satsuki Akiba).
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
