import pandas as pd
import tkinter as tk
from tkinter import filedialog
import re
import matplotlib.pyplot as plt
from y1_inference.constant import Constant 

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        process_and_plot(file_path)

def process_file(file_path):
    df_class = pd.read_excel(file_path, sheet_name=Constant.SHEET_NAME_CLASS)
    df_raw = pd.read_excel(file_path, sheet_name=Constant.SHEET_NAME_RAW)
    return df_class, df_raw

def normalize_class_code(class_code):
    result = re.search(r'(WD|SD)\d{5}', class_code)
    return result.group(0) if result else None


def process_and_plot(file_path):
    feedback_data = process_file(file_path)
    #class_teacher_dict = class_data.set_index('Mã lớp học')['Mã giảng viên'].to_dict()
    
    feedback_data['Normalized Class Code'] = feedback_data['Bạn học lớp nào? (Ví dụ: SD19300)'].apply(normalize_class_code)
    feedback_data = feedback_data.dropna(subset=['Normalized Class Code'])
    feedback_data['Ngày'] = pd.to_datetime(feedback_data['Timestamp']).dt.day
    feedback_count_by_day_class = feedback_data.groupby(['Ngày', 'Normalized Class Code']).size().unstack(fill_value=0)
    
    print(feedback_count_by_day_class)
    
    # Vẽ biểu đồ 
    ax = plt.subplots(figsize=(10, 12))  
    feedback_count_by_day_class.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel('Ngày')
    ax.set_ylabel('Số phản hồi')
    ax.legend(title='Mã lớp học chuẩn hóa', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    ax.set_xticklabels(feedback_count_by_day_class.index, rotation=0, ha='center')
    ax.grid(axis='y', linestyle='--', alpha=0.7)  
    ax.set_title('Số phản hồi theo từng ngày cho từng lớp', pad=5)  
    plt.tight_layout()
    plt.show()



# design ui
root = tk.Tk()
root.title("Công cụ thống kê số phản hồi")
root.geometry("800x400")
frame = tk.Frame(root, padx=20, pady=20, bg='#98FB98')
frame.pack(expand=True)
label = tk.Label(frame, text="Chọn một tệp Excel để bắt đầu thống kê dữ liệu", font=("Helvetica", 18), bg='#f1f0f0')
label.pack(pady=10)
open_button = tk.Button(frame, text="Mở Tệp Excel", command=open_file, font=("Helvetica", 14), bg='#4CAF50', fg='white', relief=tk.RAISED)
open_button.pack(pady=10)
root.mainloop()
