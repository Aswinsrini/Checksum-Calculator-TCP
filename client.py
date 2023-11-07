import socket
import tkinter as tk
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect(('localhost', 12345))
buffer_size = 2004


def calculate():
    tcp.send(entry.get().encode())
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    res = tcp.recv(buffer_size).decode()
    print("The received checksum from the server is ", res)
    result_text.insert(tk.END, res)
    result_text.config(state=tk.DISABLED)


def close_window():
    tcp.send("close".encode())
    window.destroy()


def validate_input(P):
    if len(P) <= int(entry1.get()):
        return True
    else:
        return False


window = tk.Tk()
window.geometry("800x700")
window.title("TCP Checksum Calculator(client)")


label2 = tk.Label(window, text="TCP Checksum Calculator(Client)",
                  font=("Times New Roman", 22))
label2.pack(pady=20)
label1 = tk.Label(
    window, text="Enter the number of character to calculate checksum", font=("Times New Roman", 16))
label1.pack(pady=20)
entry1 = tk.Entry(window, font=("Times New Roman", 16))
entry1.pack()


label = tk.Label(window, text="Enter the data ", font=("Times New Roman", 16))
label.pack(pady=20)
entry = tk.Entry(window, font=("Times New Roman", 16))
entry.pack()

calculate_button = tk.Button(
    window, text="Calculate Checksum", command=calculate, font=("Times New Roman", 16))
calculate_button.pack(pady=20)

label2 = tk.Label(window, text="Received Checksum from the sever",
                  font=("Times New Roman", 16))
label2.pack(pady=20)

result_text = tk.Text(window, height=1, width=10,
                      font=("Times New Roman", 16), state=tk.DISABLED)
result_text.pack(pady=20)

validate_input_func = window.register(validate_input)
entry.config(validate="key", validatecommand=(validate_input_func, "%P"))

close_button = tk.Button(
    window, text="close the application", command=close_window, font=("Times New Roman", 16))
close_button.pack(pady=15)
window.mainloop()


tcp.close()
