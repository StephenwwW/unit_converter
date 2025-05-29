# 單位轉換器 Unit Converter

本專案是一款以 Python 製作，並帶有 GUI 介面的單位轉換工具，支援國際單位制與二進位制的容量換算。

## 支援單位
- 國際單位制（1000進位）：Bytes、KB、MB、GB、TB
- 二進位制（1024進位）：Bytes、KiB、MiB、GiB、TiB

## 功能特色
- 任意單位輸入數值，其他單位自動換算
- 兩種單位制分開顯示，並以 `=` 連接
- 直覺易用的圖形化介面
- 支援千分位顯示，數字一目了然
- 支援 Bytes 欄位，換算更完整

## 介面截圖
> ![介面截圖](screenshot.png)

## 執行方式
1. 安裝依賴：`pip install -r requirements.txt`
2. 執行主程式：`python main.py`

## 檔案說明
- `main.py`：主程式，含 GUI 與單位轉換邏輯
- `requirements.txt`：依賴說明
- `README.md`：專案說明文件

## 授權
本專案採用 MIT License。
