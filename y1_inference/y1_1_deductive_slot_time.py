import pandas as pd 
import tkinter as tk 
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from constant import Constant 
from tabulate import tabulate 

def deductive_slot_function(timestamp):
    for slot, (start, end) in Constant.CA_TIMES.items():
        if start <= timestamp.time() < end:
            return slot
    return Constant.OUT_OF_HOUR

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            df = process_file(file_path)
            display_result(df)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi xử lý tệp: {e}")

def process_file(file_path):
    df = pd.read_excel(file_path, sheet_name=Constant.SHEET_NAME_RAW)
    df[Constant.COLUMN_TIMESTAMP] = pd.to_datetime(df[Constant.COLUMN_TIMESTAMP], format=Constant.FORMAT_TIME)
    df['CaHoc'] = df[Constant.COLUMN_TIMESTAMP].apply(deductive_slot_function)
    return df


def display_result(df):   
    result_window = tk.Toplevel(root)
    result_window.title("Kết quả suy luận")

    text = ScrolledText(result_window, wrap=tk.WORD, width=100, height=30, font=("Courier New", 10))
    text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    df['STT'] = range(1, len(df) + 1)
    df_filtered = df[['STT', Constant.COLUMN_TIMESTAMP, 'CaHoc', 'Bạn học lớp nào? (Ví dụ: SD19300)', 'Thầy/Cô nào đang dạy bạn nhỉ? (Ví dụ: DungNA29)']]
    table_str = tabulate(df_filtered, headers='keys', tablefmt='grid', showindex=False)
    text.insert(tk.END, table_str)

# design ui
root = tk.Tk()
root.title("Ca học suy luận từ nhật ký")
root.geometry("1000x400")
frame = tk.Frame(root, padx=20, pady=20, bg='#98FB98')
frame.pack(expand=True)
label = tk.Label(frame, text="Chọn một tệp Excel để bắt đầu suy luận thông tin ca học", font=("Helvetica", 24), bg='#f0f0f0')
label.pack(pady=10)
open_button = tk.Button(frame, text="Open Excel File", command=open_file, font=("Helvetica", 12), bg='#4CAF50', fg='white', relief=tk.RAISED)
open_button.pack(pady=10)
root.mainloop()
