import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, ttk

# Hàm khởi tạo
def submit_data():
    for widget in root.winfo_children():
        widget.destroy()
    messagebox.showinfo("Notification!", "Saved all the data")
    root.quit()

# Cửa sổ chính
root = tk.Tk()
root.title("Thông tin nhân viên")
root.geometry("1000x400")
root.resizable(True, True)

# Frame chính
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Tiêu đề
tk.Label(main_frame, text="Thông tin nhân viên", font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=4, pady=10, sticky="w")

# Checkbox
chk_customer = tk.Checkbutton(main_frame, text="Là khách hàng", font=("cambria", 10))
chk_supplier = tk.Checkbutton(main_frame, text="Là nhà cung cấp", font=("cambria", 10))
chk_customer.grid(row=0, column=4, sticky="w", padx=10)
chk_supplier.grid(row=0, column=5, sticky="w", padx=10)

# Mã
tk.Label(main_frame, text="Mã", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_code = tk.Entry(main_frame, width=25, font=("Arial", 10))
entry_code.grid(row=1, column=1, padx=5, pady=5)

# Tên
tk.Label(main_frame, text="Tên", font=("Arial", 10)).grid(row=1, column=2, padx=5, pady=5, sticky="w")
entry_name = tk.Entry(main_frame, width=25, font=("Arial", 10))
entry_name.grid(row=1, column=3, padx=5, pady=5)

# Đơn vị
tk.Label(main_frame, text="Đơn vị", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
combo_unit = ttk.Combobox(main_frame, values=["Phân xưởng que hàn", "Phòng kỹ thuật", "Phòng kế toán"], font=("Arial", 10), width=23)
combo_unit.grid(row=2, column=1, padx=5, pady=5)
combo_unit.set("Phân xưởng que hàn")

# Ngày sinh
tk.Label(main_frame, text="Ngày sinh", font=("Arial", 10)).grid(row=2, column=2, padx=5, pady=5, sticky="w")
entry_dob = tk.Entry(main_frame, width=25, font=("Arial", 10))
entry_dob.grid(row=2, column=3, padx=5, pady=5)

# Giới tính
tk.Label(main_frame, text="Giới tính", font=("Arial", 10)).grid(row=2, column=4, padx=5, pady=5, sticky="w")
gender_var = tk.StringVar(value="Nam")
tk.Radiobutton(main_frame, text="Nam", variable=gender_var, value="Nam", font=("Arial", 10)).grid(row=2, column=5, sticky="w", padx=5)
tk.Radiobutton(main_frame, text="Nữ", variable=gender_var, value="Nữ", font=("Arial", 10)).grid(row=2, column=6, sticky="w", padx=5)

# Số CMND
tk.Label(main_frame, text="Số CMND", font=("Arial", 10)).grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_id = tk.Entry(main_frame, width=25, font=("Arial", 10))
entry_id.grid(row=3, column=1, padx=5, pady=5)

# Ngày cấp
tk.Label(main_frame, text="Ngày cấp", font=("Arial", 10)).grid(row=3, column=2, padx=5, pady=5, sticky="w")
entry_issue_date = tk.Entry(main_frame, width=25, font=("Arial", 10))
entry_issue_date.grid(row=3, column=3, padx=5, pady=5)

# Nơi cấp
tk.Label(main_frame, text="Nơi cấp", font=("Arial", 10)).grid(row=3, column=4, padx=5, pady=5, sticky="w")
entry_place = tk.Entry(main_frame, width=25, font=("Arial", 10))
entry_place.grid(row=3, column=5, padx=5, pady=5)

# Chức danh
tk.Label(main_frame, text="Chức danh", font=("Arial", 10)).grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_position = tk.Entry(main_frame, width=25, font=("Arial", 10))
entry_position.grid(row=4, column=1, padx=5, pady=5)

# Nút Lưu
save_button = tk.Button(main_frame, text="Lưu thông tin", bg="lightblue", font=("Arial", 12), command=submit_data)
save_button.grid(row=5, column=0, columnspan=4, pady=20)

# Chạy chương trình
root.mainloop()
