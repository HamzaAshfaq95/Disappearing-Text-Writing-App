from tkinter import *
import time

window = Tk()
window.title("Dangerous Writing App")
window.minsize(width=1000, height=600)
window.config(padx=10)

# Variable to keep track of whether a key is pressed
typing = False
last_key_time = time.time()

def key_is_pressed(event):
    global typing, last_key_time
    typing = True
    last_key_time = time.time()

def check_typing():
    global typing, last_key_time
    if typing:
        update = time.time() - last_key_time
        if int(update) == 5:
            update = "Time Over"
        else:
            update = int(update)
        update_time.config(text=update)

    # Check if there has been no key press for 5 seconds
    if typing and (time.time() - last_key_time > 5):
        typing = False
        text_area.delete("1.0", END)

    # Schedule the next check
    window.after(100, check_typing)

def save_text():
    saved_text = text_area.get("1.0", END)
    if not len(saved_text) == 1:
        save_text.config(state="normal")
        save_text.delete("1.0", END)
        save_text.insert(END, saved_text)
        save_text.config(state="disabled")

main_label = Label(text="The Most Dangerous Writing App", font=("Arial", 18, "bold"))
main_label.grid(row=0, column=0, columnspan=2)

time_label = Label(text="Time When Last Key is Pressed:", font=("Arial", 14, "normal"))
time_label.grid(row=1, column=0)

update_time = Label(text="", font=("Arial", 12, "normal"))
update_time.grid(row=1, column=1)

text_area = Text(width=122, height=15)
text_area.focus()
text_area.grid(row=2, column=0, columnspan=2)
# Bind key press events
text_area.bind("<KeyPress>", key_is_pressed)

save_button = Button(text="Save Writing", command=save_text)
save_button.grid(row=3, column=0, columnspan=2)

save_text = Text(width=122, height=15)
save_text.insert(END, "Your Saved Text will show here")
save_text.config(state="disabled")
save_text.grid(row=4, column=0, columnspan=2)

# Start checking for typing
check_typing()

window.mainloop()