import pandas as pd 
import tkinter as tk
from tkinter import filedialog
import re
import matplotlib.pyplot as plt
import seaborn as sns
from y1_inference.constant import Constant 

def open_file():
    file_path = filedialog.askopenfilename()
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
    class_data, feedback_data = process_file(file_path)
    
    class_teacher_dict = class_data.set_index(Constant.COLUMN_MALOPHOC)[Constant.COLUMN_MAGIANGVIEN].to_dict()

    feedback_data['Mã lớp học chuẩn hóa'] = feedback_data[Constant.COLUMN_LOPHOC].apply(normalize_class_code)
    feedback_data = feedback_data.dropna(subset=['Mã lớp học chuẩn hóa'])
    feedback_count_by_class = feedback_data['Mã lớp học chuẩn hóa'].value_counts().reset_index()
    feedback_count_by_class.columns = ['Lớp', 'Số phản hồi']
    feedback_count_by_class['Giảng viên'] = feedback_count_by_class['Lớp'].map(class_teacher_dict)
    feedback_count_by_class = feedback_count_by_class[['Lớp', 'Giảng viên', 'Số phản hồi']]
    
    print(feedback_count_by_class)
    
    # biểu đồ số phản hồi theo từng lớp
    plt.figure(figsize=(10, 6))
    sns.barplot(data=feedback_count_by_class, x='Lớp', y='Số phản hồi')
    plt.xticks(rotation=90)
    plt.title('Số phản hồi theo từng lớp')
    plt.xlabel('Lớp')
    plt.ylabel('Số phản hồi')
    plt.tight_layout()
    plt.show()
    
    # Biểu đồ số phản hồi theo từng giảng viên
    feedback_by_teacher = feedback_count_by_class.groupby('Giảng viên')['Số phản hồi'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=feedback_by_teacher, x='Giảng viên', y='Số phản hồi')
    plt.xticks(rotation=90)
    plt.title('Số phản hồi theo từng giảng viên')
    plt.xlabel('Giảng viên')
    plt.ylabel('Số phản hồi')
    plt.tight_layout()
    plt.show()

#dedign ui
root = tk.Tk()
root.title("Công cụ thống kê số phản hồi")
root.geometry("1000x400")
frame = tk.Frame(root, padx=20, pady=20, bg='#98FB98')
frame.pack(expand=True)
label = tk.Label(frame, text="Chọn một tệp Excel để bắt đầu thống kê dữ liệu", font=("Helvetica", 24), bg='#f1f0f0')
label.pack(pady=10)
open_button = tk.Button(frame, text="Mở Tệp Excel", command=open_file, font=("Helvetica", 12), bg='#4CAF50', fg='white', relief=tk.RAISED)
open_button.pack(pady=10)
root.mainloop()
