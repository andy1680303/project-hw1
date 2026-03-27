# 進行2進位、10進位，以及16進位之間的互相轉換
# 輸入數字範圍為正整數，可以超出255，不能負數
import tkinter as tk # 使用 Python 內建的 tkinter 模組來建立圖形化介面
from tkinter import messagebox # 使用到 tkinter 內建的 messagebox 模組

# ==========================================
# 一、轉換函式
# ==========================================
# 此部分為查找資料後自行撰寫
# 1. 十進位 轉換成 二進位 (Dec to Bin)
def dec_to_bin(n):                      # 輸入十進位表示的int
    if n == 0:                          # 輸入0，則函式直接回傳0
        return "0"
    result = []                         # 建立一個list來儲存每一位轉換結果
    while n > 0:                        # 任何數字皆可以寫成 An*2^n + An-1*2^n-1 + ... + A2*2^2 + A1*2^1
        remainder = n % 2               # 所以將此數字不斷除以2，並記錄每位餘數，就可以從最尾端依序得到每位數字
        result.append(str(remainder))   # 使用%取得n除以2的餘數並append進list內記錄，再用//取得n除以2後的整數
        n = n // 2                      # 用while loop重複上述步驟，記錄下每位餘數，直到n除以2後不是整數就會得到n=0，此時就會跳出while loop
    result.reverse()                    # 由於list內的數字排列最尾到頭是從左到右，但所求最尾到頭要從右到左，因此要將整個list做reverse
    return "".join(result)              # 再將整個list用空白join成一個二進位表示的數字str後回傳

# 2. 十進位 轉換成 十六進位 (Dec to Hex)
def dec_to_hex(n):                          # 輸入十進位表示的int
    if n == 0:                              # 輸入0，則函式直接回傳0
        return "0"
    hex_chars = "0123456789ABCDEF"          # 建立一個對照用的字串，索引序號可以對應到十六進位的各位數字
    result = []                             # 建立一個list來儲存每一位轉換結果
    while n > 0:                            # 任何數字皆可以寫成 An*16^n + An-1*16^n-1 + ... + A2*16^2 + A1*16^1
        remainder = n % 16                  # 所以將此數字不斷除以16，並記錄每位餘數，就可以從最尾端依序得到每位數字
        result.append(hex_chars[remainder]) # 將餘數作為索引序號，以取得十六進位對應到的數字，再append進list內記錄
        n = n // 16                         # 寫法同 dec_to_bin，最後回傳十六進位表示的str
    result.reverse()                        
    return "".join(result)

# 3. 二進位 轉換成 十進位 (Bin to Dec)
def bin_to_dec(bin_str):                    # 輸入二進位表示的str
    if bin_str == "0":                      # 輸入0，則函式直接回傳0
        return "0"
    digits = len(bin_str)                   # 取得這個二進位數字有幾位
    n = 0                                   # 宣告一個n來儲存計算完的十進位數字
    for i in range(digits):                 # An*2^n + An-1*2^n-1 + ... + A2*2^2 + A1*2^1
        current_char = bin_str[digits-(i+1)]# 用for loop作為索引序號，從最尾到最頭取得每一位數字An(str type)
        n += int(current_char) * (2**i)     # 先將每一位數字An從str轉成int，再乘以2的n次方，再加總起來
    return str(n)                           # 將十進位數字從int轉換成str後回傳

# 4. 十六進位 轉換成 十進位 (Hex to Dec)
def hex_to_dec(hex_str):                                    # 輸入十六進位表示的str
    if hex_str == "0":                                      # 輸入0，則函式直接回傳0
        return "0"
    digits = len(hex_str)                                   # 取得這個十六進位數字有幾位
    n = 0                                                   # 宣告一個n來儲存計算完的十進位數字
    hex_chars = "0123456789ABCDEF"                          # 建立一個對照用的字串，索引序號可以對應到十六進位的各位數字
    for i in range(digits):                                 # An*16^n + An-1*16^n-1 + ... + A2*16^2 + A1*16^1
        current_char = hex_str[digits-(i+1)].upper()        # 用for loop作為索引序號，從最尾到最頭取得每一位數字An，並將小寫一律轉大寫
        current_char_value = hex_chars.index(current_char)  # 用.index取得每一位數字An的索引序號，作為其所代表的值(int type)
        n += (current_char_value) * (16**i)                 # 將每一位數字An所代表的值乘以10的n次方，再加總起來
    return str(n)                                           # 將十進位數字從int轉換成str後回傳

# ==========================================
# 二、執行函式
# ==========================================
# 此部分與AI協作，並加入自己的想法
def perform_conversion():
    # 取得輸入框的文字，以及使用者選擇的進位制
    input_str = input_field.get().strip()   # 防呆：把字串最前面和最後面的空白鍵自動刪掉，避免使用者不小心多按了一個空白
    from_base = from_var.get()              # 取得使用者現在勾選了哪一種進位制
    to_base = to_var.get()

    # 除錯防呆，彈出錯誤視窗
    # 1. 未輸入東西 (用 showwarning 顯示黃色三角形警告)
    if not input_str:
        messagebox.showwarning("輸入警告", "請輸入數字！")  # 彈出一個錯誤警告視窗 (標題, 內容)
        return  # 結束函式

    # 2. 開頭多餘的零 (用 showerror 顯示紅色叉叉錯誤)
    if len(input_str) > 1 and input_str[0] == "0":
        messagebox.showerror("格式錯誤", "數字開頭不能包含多餘的零！")
        return

    # 3. 檢查輸入格式 (用 showerror 顯示紅色叉叉錯誤)
    # 檢查輸入的每一個字，是不是都符合該進位制的規定
    if from_base == 2:
        for char in input_str:
            if char not in "01":
                messagebox.showerror("格式錯誤", "輸入了非二進位的數字！")
                return
                
    elif from_base == 10:
        for char in input_str:
            if char not in "0123456789":
                messagebox.showerror("格式錯誤", "輸入了非十進位的數字！")
                return
                
    elif from_base == 16:
        for char in input_str.upper():  # 統一轉大寫來檢查
            if char not in "0123456789ABCDEF":
                messagebox.showerror("格式錯誤", "輸入了非十六進位的數字！")
                return

    try:
        # 第一步：全部先轉成十進位的整數int
        dec_num = 0
        if from_base == 10:
            dec_num = int(input_str)
        elif from_base == 2:
            dec_num = int(bin_to_dec(input_str))    # 呼叫函式，並把回傳的字串轉成可計算的整數
        elif from_base == 16:
            dec_num = int(hex_to_dec(input_str))    # 呼叫函式，並把回傳的字串轉成可計算的整數
            
        # 第二步：把十進位的整數int轉換成目標進位制
        final_result = ""
        if to_base == 10:
            final_result = str(dec_num)
        elif to_base == 2:
            final_result = dec_to_bin(dec_num)
        elif to_base == 16:
            final_result = dec_to_hex(dec_num)
            
        # 第三步：顯示結果 (成功的話就會正常顯示藍字，不會彈出視窗)
        result_label.config(text=f"轉換結果：{final_result}", fg="blue")    # 更新標籤的文字內容與顏色

    # 例外處理：任何未知的錯誤，也會彈出錯誤視窗
    except Exception as e:  # 如有錯誤可以 print(e) 來除錯
        messagebox.showerror("未知錯誤", "發生未知的轉換錯誤！")

def clear_data():
    # 1. 清空輸入框：從第 0 個位置刪除到最後 (tk.END)
    input_field.delete(0, tk.END)
    
    # 2. 把結果標籤恢復成預設狀態
    result_label.config(text="等待轉換...", fg="black")     # 更新標籤的文字內容與顏色
    
    # 3. 把進位制選項也恢復到預設值
    from_var.set(10)
    to_var.set(2)

# ==========================================
# 三、圖形化介面 (GUI) 排版設計
# ==========================================
# 此部分與AI協作，並加入自己的想法

window = tk.Tk()               # 宣告建立一個主視窗
window.title("進位轉換器")      # 設定視窗左上角的標題文字。
window.geometry("800x500")     # 設定視窗的初始大小

# 1. 輸入區
tk.Label(window, text="請輸入數字：", font=("Arial", 12)).pack(pady=5)   # 文字標籤與格式，提示使用者
input_field = tk.Entry(window, font=("Arial", 14), justify="center")    # 單行輸入框，輸入數字置中顯示
input_field.pack(pady=5)    # 排版指令

# 2. 選擇來源進位制
tk.Label(window, text="目前的進位制是：", font=("Arial", 10)).pack(pady=5)  # 文字標籤與格式，提示使用者
from_var = tk.IntVar(value=10) # 預設選擇 10 進位
tk.Radiobutton(window, text="2 進位", variable=from_var, value=2).pack(anchor="center")     # 單選按鈕
tk.Radiobutton(window, text="10 進位", variable=from_var, value=10).pack(anchor="center")
tk.Radiobutton(window, text="16 進位", variable=from_var, value=16).pack(anchor="center")

# 3. 選擇目標進位制
tk.Label(window, text="想要轉換成：", font=("Arial", 10)).pack(pady=5)  # 文字標籤與格式，提示使用者
to_var = tk.IntVar(value=2) # 預設選擇 2 進位
tk.Radiobutton(window, text="2 進位", variable=to_var, value=2).pack(anchor="center")   # 單選按鈕
tk.Radiobutton(window, text="10 進位", variable=to_var, value=10).pack(anchor="center")
tk.Radiobutton(window, text="16 進位", variable=to_var, value=16).pack(anchor="center")

# 4. 轉換按鈕
convert_btn = tk.Button(window, text="開始轉換", font=("Arial", 12, "bold"), bg="lightgray", command=perform_conversion)
convert_btn.pack(pady=15)   # 排版指令

# 5. 清除按鈕
clear_btn = tk.Button(window, text="清除全部", font=("Arial", 12, "bold"), bg="lightgray", command=clear_data)
clear_btn.pack(pady=5)

# 6. 結果顯示
result_label = tk.Label(window, text="等待轉換...", font=("Arial", 14, "bold")) # 結果顯示標籤，可更新文字內容與顏色
result_label.pack(pady=20)  # 排版指令

# 7. 啟動應用程式
window.mainloop()   # 保持視窗顯示狀態