import tkinter as tk
from PIL import Image, ImageTk
import logic as jjs
from characters import list_jss

# Update Function
def update_character():
    character = jjs.return_random_character()
    
    label_name.config(text=character["name"])
    label_game.config(text=character["name_game"])
    
    try:
        original_img = Image.open(character["real_url"])
        resize_img = original_img.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resize_img)
        
        label_img.config(image=photo)
        label_img.image = photo
        
    except Exception as e:
        print(f"Error in the charge: {e}")
        label_img.config(image="", text="Imagen not found")

# General
root = tk.Tk()
root.title("JJS Randomizer")
root.geometry("300x400")
root.configure(bg="#1a1a1a")

# Name of Character
label_name = tk.Label(root, fg="#aaaaaa", bg="#121212")
label_name.pack(pady=(20,0))

# Name in Game
label_game = tk.Label(root, fg="#ffffff", bg="#121212", font=("Arial", 18, "bold"))
label_game.pack(pady=3)

# Photo of Character
label_img = tk.Label(root)
label_img.pack()

# Button
btn_random = tk.Button(root, text="RANDOMIZER", command=update_character)
btn_random.pack(pady=20)

update_character()
root.mainloop()
