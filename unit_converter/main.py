import tkinter as tk
from tkinter import ttk

# 1000進位單位與對應倍數
SI_UNITS = ["Bytes", "KB", "MB", "GB", "TB"]
SI_FACTORS = [1, 1_000, 1_000_000, 1_000_000_000, 1_000_000_000_000]

# 1024進位單位與對應倍數
BINARY_UNITS = ["Bytes", "KiB", "MiB", "GiB", "TiB"]
BINARY_FACTORS = [1, 1024, 1024**2, 1024**3, 1024**4]

class UnitConverterApp:
    """
    單位轉換器主程式，負責建立 GUI 介面與單位換算邏輯
    """
    def __init__(self, root):
        self.root = root
        self.root.title("單位轉換器 Unit Converter")
        self.root.geometry("700x250")  # 視窗寬度加寬，確保內容完整顯示
        self.create_widgets()

    def create_widgets(self):
        """
        建立所有 GUI 元件（國際單位制與二進位制的欄位）
        """
        # 國際單位制區塊
        si_frame = ttk.LabelFrame(self.root, text="國際單位制 (1000進位)")
        si_frame.grid(row=0, column=0, padx=16, pady=12, sticky="ew")
        self.si_vars = [tk.StringVar() for _ in SI_UNITS]  # 儲存各單位的輸入值
        # TB, GB, MB 同一行
        for i, unit in enumerate(SI_UNITS[::-1][:-2]):
            idx = len(SI_UNITS) - 1 - i
            entry = ttk.Entry(si_frame, textvariable=self.si_vars[idx], width=18, font=("Consolas", 12))
            entry.grid(row=0, column=i*3, padx=(2,0), pady=8, sticky="ew")
            entry.bind('<KeyRelease>', lambda e, idx=idx: self.si_update(idx))  # 綁定輸入事件
            unit_label = ttk.Label(si_frame, text=unit, font=("Consolas", 12))
            unit_label.grid(row=0, column=i*3+1, padx=(2,4), sticky="w")
            if i != 0:
                eq_label = ttk.Label(si_frame, text="=", font=("Consolas", 12))
                eq_label.grid(row=0, column=i*3-1, padx=(0,2))
        # KB/Bytes 換行
        for i, unit in enumerate(SI_UNITS[1::-1]):
            idx = 1 - i
            entry = ttk.Entry(si_frame, textvariable=self.si_vars[idx], width=18, font=("Consolas", 12))
            entry.grid(row=1, column=i*3, padx=(2,0), pady=8, sticky="ew")
            entry.bind('<KeyRelease>', lambda e, idx=idx: self.si_update(idx))
            unit_label = ttk.Label(si_frame, text=unit, font=("Consolas", 12))
            unit_label.grid(row=1, column=i*3+1, padx=(2,4), sticky="w")
            if i != 0:
                eq_label = ttk.Label(si_frame, text="=", font=("Consolas", 12))
                eq_label.grid(row=1, column=i*3-1, padx=(0,2))

        # 二進位制區塊
        bin_frame = ttk.LabelFrame(self.root, text="二進位制 (1024進位)")
        bin_frame.grid(row=1, column=0, padx=16, pady=12, sticky="ew")
        self.bin_vars = [tk.StringVar() for _ in BINARY_UNITS]  # 儲存各單位的輸入值
        # TiB, GiB, MiB 同一行
        for i, unit in enumerate(BINARY_UNITS[::-1][:-2]):
            idx = len(BINARY_UNITS) - 1 - i
            entry = ttk.Entry(bin_frame, textvariable=self.bin_vars[idx], width=18, font=("Consolas", 12))
            entry.grid(row=0, column=i*3, padx=(2,0), pady=8, sticky="ew")
            entry.bind('<KeyRelease>', lambda e, idx=idx: self.bin_update(idx))
            unit_label = ttk.Label(bin_frame, text=unit, font=("Consolas", 12))
            unit_label.grid(row=0, column=i*3+1, padx=(2,4), sticky="w")
            if i != 0:
                eq_label = ttk.Label(bin_frame, text="=", font=("Consolas", 12))
                eq_label.grid(row=0, column=i*3-1, padx=(0,2))
        # KiB/Bytes 換行
        for i, unit in enumerate(BINARY_UNITS[1::-1]):
            idx = 1 - i
            entry = ttk.Entry(bin_frame, textvariable=self.bin_vars[idx], width=18, font=("Consolas", 12))
            entry.grid(row=1, column=i*3, padx=(2,0), pady=8, sticky="ew")
            entry.bind('<KeyRelease>', lambda e, idx=idx: self.bin_update(idx))
            unit_label = ttk.Label(bin_frame, text=unit, font=("Consolas", 12))
            unit_label.grid(row=1, column=i*3+1, padx=(2,4), sticky="w")
            if i != 0:
                eq_label = ttk.Label(bin_frame, text="=", font=("Consolas", 12))
                eq_label.grid(row=1, column=i*3-1, padx=(0,2))

    def si_update(self, idx):
        """
        處理國際單位制欄位的輸入事件，並自動換算其他單位
        idx: 目前被輸入的欄位索引
        """
        try:
            value = float(self.si_vars[idx].get().replace(',', ''))
        except ValueError:
            self.clear_vars(self.si_vars, except_idx=idx)
            return
        base = value * SI_FACTORS[idx]  # 先轉成 Bytes
        for i, factor in enumerate(SI_FACTORS):
            if i != idx:
                self.si_vars[i].set(f"{base / factor:,.0f}")

    def bin_update(self, idx):
        """
        處理二進位制欄位的輸入事件，並自動換算其他單位
        idx: 目前被輸入的欄位索引
        """
        try:
            value = float(self.bin_vars[idx].get().replace(',', ''))
        except ValueError:
            self.clear_vars(self.bin_vars, except_idx=idx)
            return
        base = value * BINARY_FACTORS[idx]  # 先轉成 Bytes
        for i, factor in enumerate(BINARY_FACTORS):
            if i != idx:
                self.bin_vars[i].set(f"{base / factor:,.0f}")

    def clear_vars(self, vars_list, except_idx):
        """
        清除同一單位制下，除了目前輸入欄位以外的所有欄位內容
        """
        for i, var in enumerate(vars_list):
            if i != except_idx:
                var.set("")

if __name__ == "__main__":
    # 啟動主程式
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop() 