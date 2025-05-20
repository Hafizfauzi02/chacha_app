import tkinter as tk
from encryption import encrypt_message, decrypt_message
from database import init_db, save_message, get_all_messages

init_db()

def encrypt_and_save():
    msg = entry.get()
    if not msg.strip():
        result_label.config(text="Please enter a message first!")
        return
    encrypted, nonce = encrypt_message(msg)
    save_message(encrypted, nonce)
    entry.delete(0, tk.END)
    update_listbox()
    result_label.config(text="Message encrypted and saved successfully!")

def update_listbox():
    listbox.delete(0, tk.END)
    for i, (msg_id, _, _) in enumerate(get_all_messages()):
        listbox.insert(i, f"Message ID: {msg_id}")

def show_decrypted():
    try:
        index = listbox.curselection()[0]
        data = get_all_messages()[index]
        decrypted = decrypt_message(data[1], data[2])
        result_label.config(text="Decrypted Message: " + decrypted)
    except:
        result_label.config(text="Please select a valid message.")

# Create the main window
root = tk.Tk()
root.title("ChaCha20 Encryption App")
root.geometry("600x400")  # Set window size
root.configure(bg='#f0f0f0')  # Light gray background

# Create a frame for better organization
main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20, bd=2, relief=tk.RIDGE)
main_frame.pack(expand=True, fill='both', padx=40, pady=40)

# Title label
title_label = tk.Label(main_frame, text="Secure Message Encryption", font=('Helvetica', 16, 'bold'), bg='#f0f0f0')
title_label.pack(pady=(0, 20))

# Entry field with label
entry_label = tk.Label(main_frame, text="Enter your message:", bg='#f0f0f0')
entry_label.pack()
entry = tk.Entry(main_frame, width=50, font=('Helvetica', 12))
entry.pack(pady=5)

# Encrypt button
encrypt_btn = tk.Button(main_frame, text="Encrypt & Save", command=encrypt_and_save,
                       bg='#4CAF50', fg='white', font=('Helvetica', 12))
encrypt_btn.pack(pady=10)

# Listbox with label
listbox_label = tk.Label(main_frame, text="Saved Messages:", bg='#f0f0f0')
listbox_label.pack()
listbox = tk.Listbox(main_frame, width=50, height=5, font=('Helvetica', 12))
listbox.pack(pady=5)

# Decrypt button
decrypt_btn = tk.Button(main_frame, text="Decrypt Selected Message", command=show_decrypted,
                       bg='#2196F3', fg='white', font=('Helvetica', 12))
decrypt_btn.pack(pady=10)

# Result label
result_label = tk.Label(main_frame, text="", wraplength=500, bg='#f0f0f0', font=('Helvetica', 12))
result_label.pack(pady=10)

# Update the listbox with existing messages
update_listbox()

# Debug prints to verify widget creation
print("All widgets created and packed.")

# Start the application
root.mainloop()
