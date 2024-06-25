import pandas as pd 
import tkinter as tk 
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from constant import Constant 

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            df = process_file(file_path)
            show_result_of_process_file(df)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi xử lý tệp: {e}")


def process_file(file_path):
    df_raw = pd.read_excel(file_path, sheet_name=Constant.SHEET_NAME_RAW)
    
    def infer_lesson(description):
        description_lower = description.lower()
        for lesson, keywords in Constant.LESSONS_KEYWORDS.items():
            for keyword in keywords:
                if keyword in description_lower:
                    return lesson
        return "Không thuộc tám bài học"
    
    df_raw[Constant.SHEET_NAME_CLASS] = df_raw[Constant.COLUMN_LOPHOC]
    df_raw['Bài học'] = df_raw[Constant.COLUMN_KIENTHUCBAIHOC].apply(infer_lesson)
    df_raw['Thứ tự bài học'] = df_raw['Bài học'].apply(lambda x: Constant.LESSON_ORDER[x])
    df_raw = df_raw.sort_values(by='Thứ tự bài học')
    return df_raw


def show_result_of_process_file(df):
    result_window = tk.Toplevel(root)
    result_window.title("Kết quả suy luận")
    
    text = ScrolledText(result_window, wrap=tk.WORD, width=120, height=30, font=("Consolas", 12))
    text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    df_filtered = df[[Constant.COLUMN_KIENTHUCBAIHOC, 'Class', 'Bài học']]
    
    table_str = df_filtered.to_string(index=False)
    text.insert(tk.END, table_str)
    text.config(state=tk.DISABLED)

# design ui
root = tk.Tk()
root.title("Suy luận thông tin chủ đề buổi học")
root.geometry("1000x400")
frame = tk.Frame(root, padx=20, pady=20, bg='#98FB98')
frame.pack(expand=True)
label = tk.Label(frame, text="Chọn một tệp Excel để bắt đầu suy luận thông tin chủ đề buổi học", font=("Helvetica", 24), bg='#f0f0f0')
label.pack(pady=10)
open_button = tk.Button(frame, text="Open Excel File", command=open_file, font=("Helvetica", 12), bg='#4CAF50', fg='white', relief=tk.RAISED)
open_button.pack(pady=10)
root.mainloop()
