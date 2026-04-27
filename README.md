# posture-monitor

PC カメラを使って姿勢をセンシングし、猫背を検知して警告を出すことを目的とした Python プロジェクトです。

このリポジトリでは、段階的に機能を公開しています。

## What This Project Does

1. 手・指トラッキング
- スクリプト: `finger_sensing.py`
- MediaPipe Hands で手のランドマークをリアルタイム描画

2. 猫背検知 + 警告
- スクリプト: `nekoze.py`
- 顔と肩の位置関係から姿勢を判定し、状態を表示
- 条件に応じて警告音を再生

## Requirements

- Python 3.10 以上
- Web カメラ

## Setup

```bash
pip install -r requirements.txt
```

## Usage

### 1) Finger Sensing

```bash
python finger_sensing.py
```

- 終了キー: `q`

### 2) Posture Detection

```bash
python nekoze.py
```

- 終了キー: `q`
- 警告音は `nekoze.py` と同じフォルダに `be.mp3` がある場合に再生

## Project Status

- v0.1: 手・指トラッキングの公開
- v0.2: 猫背検知 + 警告機能の公開

## Known Limitations

- 姿勢判定しきい値は環境により調整が必要
- カメラの角度や座る位置で判定が変わる
- 現在はシンプルな判定ロジックで実験中

## Roadmap

- 判定ロジックの安定化
- 個人差に合わせたキャリブレーション
- 通知方式の改善（音以外の通知など）

## Troubleshooting

- カメラが起動しない場合: `cv2.VideoCapture(0)` の番号を `1` などに変更
- 警告音が鳴らない場合: `be.mp3` の配置と音量設定を確認
