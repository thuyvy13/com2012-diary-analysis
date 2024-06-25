import pandas as pd 
import tkinter as tk 
from tkinter import filedialog, messagebox, scrolledtext
from tabulate import tabulate 
from constant import Constant

def open_File():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            df = process_file(file_path)
            show_result_of_process_file(df)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi xử lý tệp: {e}")


def process_file(file_path):
    df_class = pd.read_excel(file_path, sheet_name=Constant.SHEET_NAME_RAW)
    df_lecturer = pd.read_excel(file_path, sheet_name=Constant.SHEET_NAME_LECTURER)
    
    lecturer_mapping = df_lecturer.set_index(Constant.COLUMN_MAGIANGVIEN)[Constant.COLUMN_TENGIANGVIEN].to_dict()
    df_class[Constant.COLUMN_TENGIANGVIEN] = df_class[Constant.COLUMN_MAGIANGVIEN].map(lecturer_mapping)
    return df_class


def show_result_of_process_file(df):
    result_window = tk.Toplevel(root)
    result_window.title("Dữ liệu đã chuẩn hóa")
    
    text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=100, height=30, font=("Consolas", 12))
    text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    df['STT'] = range(1, len(df) + 1)
    df_filtered = df[['STT','Mã lớp học', Constant.COLUMN_MAGIANGVIEN, Constant.COLUMN_TENGIANGVIEN]]
    table_str = tabulate(df_filtered, headers='keys', tablefmt='grid', showindex=False)
    text.insert(tk.END, table_str)

# design ui
root = tk.Tk()
root.title("Công cụ chuẩn hoá dữ liệu")
root.geometry("1000x400")
frame = tk.Frame(root, padx=20, pady=20, bg='#98FB98')
frame.pack(expand=True)
label = tk.Label(frame, text="Chọn một tệp Excel để bắt đầu chuẩn hoá dữ liệu", font=("Helvetica", 24), bg='#f1f0f0')
label.pack(pady=10)
open_button = tk.Button(frame, text="Mở Tệp Excel", command=open_File, font=("Helvetica", 12), bg='#4CAF50', fg='white', relief=tk.RAISED)
open_button.pack(pady=10)
root.mainloop()
