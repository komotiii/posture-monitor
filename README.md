# posture-monitor

PC カメラを使って猫背を検知し、警告を出すアプリを目指すプロジェクトです。

まず第一段階として、MediaPipe を使った手（指）センシングを公開しています。

## Current Status

- Phase 1: 手・指トラッキング（公開対象）
        - ファイル: `finger_sensing.py`
        - 内容: Web カメラ映像から手のランドマークを検出して描画
- Phase 2: 猫背検知 + 警告（ローカル開発中・未公開）
        - 備考: しきい値調整と設計改善を進行中

## Demo (Phase 1)

`finger_sensing.py` でできること:

- 手のランドマークをリアルタイム表示
- 両手（最大 2 手）を同時に追跡
- `q` キーで終了

## Setup

1. Python 3.10+ をインストール
2. 依存関係をインストール

```bash
pip install -r requirements.txt
```

## Run

```bash
python finger_sensing.py
```

## Next Goal

次のステップでは、姿勢スコアの安定化と警告ロジックの改善を行い、
「猫背検知 + 通知」までを実装する予定です。

## Notes

- カメラデバイスが見つからない場合は、`cv2.VideoCapture(0)` の番号を調整してください。
- この公開では `nekoze.py` は含めません。

## Release Plan

1. Phase 1 (`finger_sensing.py`) を公開
2. 姿勢判定ロジックを改善
3. Phase 2 (猫背検知 + 警告) を公開

