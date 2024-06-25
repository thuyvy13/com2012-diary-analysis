from datetime import time

class Constant:
    CA_TIMES = {
        "Ca 1": (time(7, 15), time(9, 15)),
        "Ca 2": (time(9, 25), time(11, 25)),
        "Ca 3": (time(12, 0), time(14, 0)),
        "Ca 4": (time(14, 10), time(16, 10)),
        "Ca 5": (time(16, 20), time(18, 20)),
        "Ca 6": (time(18, 30), time(20, 30))
    }

    OUT_OF_HOURS = "Ngoài giờ học"
    
    #Format time
    FORMAT_TIME = '%d/%m/%Y %H:%M:%S'
    
    #sheet class, raw, lecturer
    SHEET_NAME_CLASS = 'class'
    SHEET_NAME_RAW = 'raw'
    SHEET_NAME_LECTURER = 'lecturer'
    
    #column
    COLUMN_TIMESTAMP = 'Timestamp'
    COLUMN_MAGIANGVIEN = 'Mã giảng viên'
    COLUMN_TENGIANGVIEN = 'Tên giảng viên'
    COLUMN_LOPHOC = 'Bạn học lớp nào? (Ví dụ: SD19300)'
    COLUMN_KIENTHUCBAIHOC = 'Hôm nay thầy/cô giảng về kiến thức nào thế?'
    COLUMN_MALOPHOC = 'Mã lớp học'
    
    
    #Từ điển các bài học và các từ khoá liên quan đến bài học
    LESSONS_KEYWORDS = {
        'Bài 1': ['giới thiệu', 'msssql', 'server', 'sql'],
        'Bài 2': ['truy vấn', 'dữ liệu', 'bảng'],
        'Bài 3': ['lọc dữ liệu'],
        'Bài 4': ['truy vấn', 'nhiều bảng'],
        'Bài 5': ['truy vấn con'],
        'Bài 6': ['pivot', 'kết nối', 'excel'],
        'Bài 7': ['data definition', 'modifying data'],
        'Bài 8': ['kế hoạch', 'chiến lược', 'sao lưu', 'phục hồi', 'csdl']
    }
    
    #Thứ tự bài học
    LESSON_ORDER = {
        'Bài 1': 1,
        'Bài 2': 2,
        'Bài 3': 3,
        'Bài 4': 4,
        'Bài 5': 5,
        'Bài 6': 6,
        'Bài 7': 7,
        'Bài 8': 8,
        'Không thuộc tám bài học': 9
    }