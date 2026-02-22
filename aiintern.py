import tkinter as tk
from tkinter import messagebox,ttk,scrolledtext
main= tk.Tk()
main.geometry("1920x1080")
main.configure(background="black")
main.title("Chatbot")

#to create multiple pages
container=tk.Frame(main,bg="black")
container.place(x=0,y=0,width=1920,height=1080)


welcome_page=tk.Frame(container,bg="gray")
chatbot_page=tk.Frame(container,bg="light blue")


for page in (welcome_page,chatbot_page):
    page.place(x=0,y=0,width=1920,height=1080)

#switch page fun
def sp(page):
    page.tkraise()
#welcome page
tk.Label(welcome_page,text="Welcome Buddy!",font=("Arial",20),bg="lightblue").pack(pady=20)

user_name=tk.Entry(welcome_page,font=("Arial",14)).pack(pady=10)
tk.Button(welcome_page,text="Ready to chat",command=lambda:sp(chatbot_page)).pack(pady=10)

tk.Label(chatbot_page,text="chatbot ready....search here").pack(pady=20)
tk.Button(chatbot_page,text="back",command=lambda:sp(welcome_page)).pack(pady=10)

sp(welcome_page)

main.mainloop()




