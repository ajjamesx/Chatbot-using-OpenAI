import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

client = OpenAI(api_key="") # Input your API key from https://platform.openai.com/docs/api-reference/introduction

def get_bot_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, witty assistant named PyBot."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error fetching response: {str(e)}]"

# GUI behavior
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, f"You: {user_input}\n")
    entry.delete(0, tk.END)
    window.update()

    bot_response = get_bot_response(user_input)
    chat_window.insert(tk.END, f"PyBot: {bot_response}\n\n")
    chat_window.see(tk.END)

# GUI setup
window = tk.Tk()
window.title("PyBot Chat (GPT-Powered)")
window.geometry("460x540")

chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Consolas", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry_frame = tk.Frame(window)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, font=("Consolas", 12), width=34)
entry.pack(side=tk.LEFT, padx=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

window.mainloop()