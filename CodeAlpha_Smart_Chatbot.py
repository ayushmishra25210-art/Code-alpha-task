import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import webbrowser
import ast
import operator
import json
import os


# -----------------------------------
# FILES
# -----------------------------------
USER_FILE = "chatbot_users.json"


# -----------------------------------
# USER DATA FUNCTIONS
# -----------------------------------
def load_users():
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}


def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


# -----------------------------------
# LOGIN PORTAL
# -----------------------------------
class LoginPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot Login Portal")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f172a")

        self.users = load_users()
        self.show_login_page()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # -----------------------------------
    # LOGIN PAGE
    # -----------------------------------
    def show_login_page(self):
        self.clear_window()

        left_frame = tk.Frame(self.root, bg="#020617", width=380)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        left_frame.pack_propagate(False)

        tk.Label(
            left_frame,
            text="Smart Chatbot",
            font=("Arial", 28, "bold"),
            bg="#020617",
            fg="white"
        ).pack(pady=(120, 10))

        tk.Label(
            left_frame,
            text="Login to continue your\nreal-life AI assistant",
            font=("Arial", 14),
            bg="#020617",
            fg="#94a3b8",
            justify="center"
        ).pack(pady=10)

        tk.Label(
            left_frame,
            text="â Study Help\nâ Calculations\nâ News & Wikipedia\nâ Search Assistant\nâ Chat History Style UI",
            font=("Arial", 13),
            bg="#020617",
            fg="#38bdf8",
            justify="left"
        ).pack(pady=40)

        right_frame = tk.Frame(self.root, bg="#0f172a")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(
            right_frame,
            text="Already Have Account?",
            font=("Arial", 24, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=(90, 20))

        # Username Entry with placeholder
        self.login_username = tk.Entry(
            right_frame,
            font=("Arial", 14),
            width=32,
            fg="gray",
            bg="white"
        )
        self.login_username.pack(pady=10, ipady=8)
        self.login_username.insert(0, "Username")
        self.login_username.bind("<FocusIn>", self.clear_username_placeholder)
        self.login_username.bind("<FocusOut>", self.add_username_placeholder)

        # Password Entry with placeholder
        self.login_password = tk.Entry(
            right_frame,
            font=("Arial", 14),
            width=32,
            fg="gray",
            bg="white"
        )
        self.login_password.pack(pady=10, ipady=8)
        self.login_password.insert(0, "Password")
        self.login_password.bind("<FocusIn>", self.clear_password_placeholder)
        self.login_password.bind("<FocusOut>", self.add_password_placeholder)

        tk.Button(
            right_frame,
            text="Login",
            font=("Arial", 13, "bold"),
            bg="#2563eb",
            fg="white",
            width=25,
            bd=0,
            command=self.login_user
        ).pack(pady=15, ipady=6)

        tk.Button(
            right_frame,
            text="Forgot Password?",
            font=("Arial", 11),
            bg="#0f172a",
            fg="#38bdf8",
            bd=0,
            command=self.show_forgot_page
        ).pack(pady=5)

        tk.Button(
            right_frame,
            text="Create New User Account",
            font=("Arial", 12, "bold"),
            bg="#16a34a",
            fg="white",
            width=25,
            bd=0,
            command=self.show_register_page
        ).pack(pady=20, ipady=6)

    # -----------------------------------
    # PLACEHOLDER FUNCTIONS
    # -----------------------------------
    def clear_username_placeholder(self, event):
        if self.login_username.get() == "Username":
            self.login_username.delete(0, tk.END)
            self.login_username.config(fg="black")

    def add_username_placeholder(self, event):
        if self.login_username.get() == "":
            self.login_username.insert(0, "Username")
            self.login_username.config(fg="gray")

    def clear_password_placeholder(self, event):
        if self.login_password.get() == "Password":
            self.login_password.delete(0, tk.END)
            self.login_password.config(fg="black", show="*")

    def add_password_placeholder(self, event):
        if self.login_password.get() == "":
            self.login_password.config(show="")
            self.login_password.insert(0, "Password")
            self.login_password.config(fg="gray")

    # -----------------------------------
    # REGISTER PAGE
    # -----------------------------------
    def show_register_page(self):
        self.clear_window()

        frame = tk.Frame(self.root, bg="#0f172a")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            frame,
            text="Create New Account",
            font=("Arial", 26, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=(50, 20))

        self.reg_name = tk.Entry(frame, font=("Arial", 14), width=35)
        self.reg_name.pack(pady=8, ipady=8)
        self.reg_name.insert(0, "Full Name")

        self.reg_username = tk.Entry(frame, font=("Arial", 14), width=35)
        self.reg_username.pack(pady=8, ipady=8)
        self.reg_username.insert(0, "Username")

        self.reg_password = tk.Entry(frame, font=("Arial", 14), width=35, show="*")
        self.reg_password.pack(pady=8, ipady=8)

        self.reg_answer = tk.Entry(frame, font=("Arial", 14), width=35)
        self.reg_answer.pack(pady=8, ipady=8)
        self.reg_answer.insert(0, "Security Answer: Favourite Color")

        tk.Button(
            frame,
            text="Register",
            font=("Arial", 13, "bold"),
            bg="#16a34a",
            fg="white",
            width=25,
            bd=0,
            command=self.register_user
        ).pack(pady=20, ipady=6)

        tk.Button(
            frame,
            text="Back to Login",
            font=("Arial", 12),
            bg="#334155",
            fg="white",
            width=20,
            bd=0,
            command=self.show_login_page
        ).pack(pady=5, ipady=5)

    # -----------------------------------
    # FORGOT PASSWORD PAGE
    # -----------------------------------
    def show_forgot_page(self):
        self.clear_window()

        frame = tk.Frame(self.root, bg="#0f172a")
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            frame,
            text="Forgot Password",
            font=("Arial", 26, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=(80, 20))

        tk.Label(
            frame,
            text="Enter username and your security answer",
            font=("Arial", 13),
            bg="#0f172a",
            fg="#94a3b8"
        ).pack(pady=5)

        self.forgot_username = tk.Entry(frame, font=("Arial", 14), width=35)
        self.forgot_username.pack(pady=10, ipady=8)
        self.forgot_username.insert(0, "Username")

        self.forgot_answer = tk.Entry(frame, font=("Arial", 14), width=35)
        self.forgot_answer.pack(pady=10, ipady=8)
        self.forgot_answer.insert(0, "Favourite Color")

        tk.Button(
            frame,
            text="Recover Password",
            font=("Arial", 13, "bold"),
            bg="#f59e0b",
            fg="white",
            width=25,
            bd=0,
            command=self.recover_password
        ).pack(pady=20, ipady=6)

        tk.Button(
            frame,
            text="Back to Login",
            font=("Arial", 12),
            bg="#334155",
            fg="white",
            width=20,
            bd=0,
            command=self.show_login_page
        ).pack(pady=5, ipady=5)

    # -----------------------------------
    # USER FUNCTIONS
    # -----------------------------------
    def register_user(self):
        name = self.reg_name.get().strip()
        username = self.reg_username.get().strip()
        password = self.reg_password.get().strip()
        answer = self.reg_answer.get().strip().lower()

        if (
            name == "" or username == "" or password == "" or answer == "" or
            name == "Full Name" or username == "Username" or
            answer == "security answer: favourite color"
        ):
            messagebox.showerror("Error", "Please fill all details.")
            return

        if username in self.users:
            messagebox.showerror("Error", "Username already exists.")
            return

        self.users[username] = {
            "name": name,
            "password": password,
            "security_answer": answer
        }

        save_users(self.users)
        messagebox.showinfo("Success", "Account created successfully.")
        self.show_login_page()

    def login_user(self):
        username = self.login_username.get().strip()
        password = self.login_password.get().strip()

        if username == "Username" or password == "Password" or username == "" or password == "":
            messagebox.showerror("Login Failed", "Please enter username and password.")
            return

        if username in self.users and self.users[username]["password"] == password:
            user_name = self.users[username]["name"]
            self.open_chatbot(user_name, username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def recover_password(self):
        username = self.forgot_username.get().strip()
        answer = self.forgot_answer.get().strip().lower()

        if username == "" or answer == "" or username == "Username" or answer == "favourite color":
            messagebox.showerror("Error", "Please fill all details.")
            return

        if username in self.users:
            if self.users[username]["security_answer"] == answer:
                password = self.users[username]["password"]
                messagebox.showinfo("Password Found", "Your password is: " + password)
            else:
                messagebox.showerror("Error", "Security answer is wrong.")
        else:
            messagebox.showerror("Error", "Username not found.")

    def open_chatbot(self, name, username):
        self.clear_window()
        SmartChatbotApp(self.root, name, username)


# -----------------------------------
# SMART CHATBOT APP
# -----------------------------------
class SmartChatbotApp:
    def __init__(self, root, user_name, username):
        self.root = root
        self.user_name = user_name
        self.username = username

        self.root.title("Smart Real-Life Chatbot")
        self.root.geometry("1050x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#111827")

        self.create_interface()

    # -----------------------------------
    # MAIN INTERFACE
    # -----------------------------------
    def create_interface(self):
        self.sidebar = tk.Frame(self.root, bg="#050505", width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)

        self.main_area = tk.Frame(self.root, bg="#111827")
        self.main_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_sidebar()
        self.create_chat_area()

    # -----------------------------------
    # SIDEBAR
    # -----------------------------------
    def create_sidebar(self):
        menu_items = [
            "â  New Chat",
            "â¥  Library",
            "â±  Projects",
            "â¦  Apps",
            "â  Explore GPTs",
            "â¯  More"
        ]

        for item in menu_items:
            if "New Chat" in item:
                command = self.new_chat
            else:
                command = self.sidebar_info

            tk.Button(
                self.sidebar,
                text=item,
                font=("Arial", 12),
                bg="#050505",
                fg="white",
                anchor="w",
                bd=0,
                padx=18,
                pady=10,
                activebackground="#1f2937",
                activeforeground="white",
                command=command
            ).pack(fill=tk.X, pady=2)

        tk.Label(
            self.sidebar,
            text="GPTs",
            font=("Arial", 11, "bold"),
            bg="#050505",
            fg="white",
            anchor="w",
            padx=18
        ).pack(fill=tk.X, pady=(25, 5))

        tk.Button(
            self.sidebar,
            text="ð¤  Basic Rule-Based Chatbot",
            font=("Arial", 11),
            bg="#2d2d2d",
            fg="white",
            anchor="w",
            bd=0,
            padx=18,
            pady=10
        ).pack(fill=tk.X, pady=3)

        tk.Label(
            self.sidebar,
            text="Recents",
            font=("Arial", 11, "bold"),
            bg="#050505",
            fg="white",
            anchor="w",
            padx=18
        ).pack(fill=tk.X, pady=(25, 5))

        recent_items = [
            "Basic Rule-Based Chatbot",
            "Study Explanation",
            "Calculation Chat",
            "Wikipedia Search"
        ]

        for item in recent_items:
            tk.Label(
                self.sidebar,
                text=item,
                font=("Arial", 10),
                bg="#050505",
                fg="#e5e7eb",
                anchor="w",
                padx=18,
                pady=6
            ).pack(fill=tk.X)

        bottom = tk.Frame(self.sidebar, bg="#050505")
        bottom.pack(side=tk.BOTTOM, fill=tk.X, pady=15)

        tk.Label(
            bottom,
            text="ð   " + self.user_name + "\n     Logged In",
            font=("Arial", 10),
            bg="#050505",
            fg="white",
            anchor="w",
            padx=15,
            justify="left"
        ).pack(fill=tk.X)

        tk.Button(
            bottom,
            text="Logout",
            font=("Arial", 10, "bold"),
            bg="#dc2626",
            fg="white",
            bd=0,
            command=self.logout
        ).pack(fill=tk.X, padx=15, pady=8)

    # -----------------------------------
    # CHAT AREA
    # -----------------------------------
    def create_chat_area(self):
        tk.Label(
            self.main_area,
            text="Smart Real-Life Chatbot",
            font=("Arial", 22, "bold"),
            bg="#111827",
            fg="white",
            pady=15
        ).pack(fill=tk.X)

        tk.Label(
            self.main_area,
            text="Ask me anything: study, calculation, news, Wikipedia, search, time and more",
            font=("Arial", 11),
            bg="#111827",
            fg="#9ca3af"
        ).pack()

        self.chat_area = scrolledtext.ScrolledText(
            self.main_area,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg="#1f2937",
            fg="white",
            insertbackground="white",
            state="disabled",
            padx=12,
            pady=12
        )
        self.chat_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        bottom_frame = tk.Frame(self.main_area, bg="#111827")
        bottom_frame.pack(fill=tk.X, padx=20, pady=12)

        self.user_entry = tk.Entry(
            bottom_frame,
            font=("Arial", 13),
            bg="#374151",
            fg="white",
            insertbackground="white",
            width=62,
            bd=0
        )
        self.user_entry.pack(side=tk.LEFT, padx=(0, 10), ipady=12)
        self.user_entry.bind("<Return>", self.send_message)

        tk.Button(
            bottom_frame,
            text="Send",
            font=("Arial", 12, "bold"),
            bg="#10a37f",
            fg="white",
            width=10,
            bd=0,
            command=self.send_message
        ).pack(side=tk.LEFT, padx=5, ipady=5)

        tk.Button(
            bottom_frame,
            text="Clear",
            font=("Arial", 12, "bold"),
            bg="#dc2626",
            fg="white",
            width=10,
            bd=0,
            command=self.clear_chat
        ).pack(side=tk.LEFT, padx=5, ipady=5)

        self.bot_message("Hello " + self.user_name + "! I am your smart chatbot.")
        self.bot_message("Type 'help' to see all commands.")

    # -----------------------------------
    # MESSAGE DISPLAY
    # -----------------------------------
    def user_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "You: " + message + "\n", "user")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def bot_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, "Bot: " + message + "\n\n", "bot")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def send_message(self, event=None):
        user_input = self.user_entry.get().strip()

        if user_input == "":
            return

        self.user_entry.delete(0, tk.END)
        self.user_message(user_input)

        response = self.get_response(user_input)
        self.bot_message(response)

    # -----------------------------------
    # BOT LOGIC
    # -----------------------------------
    def get_response(self, user_input):
        message = user_input.lower().strip()

        if message in ["hi", "hello", "hey", "hii"]:
            return "Hello " + self.user_name + "! How can I help you today?"

        elif message in ["how are you", "how are you?"]:
            return "I'm fine and ready to help you."

        elif message in ["thanks", "thank you"]:
            return "You're welcome!"

        elif message in ["bye", "exit", "quit"]:
            self.root.after(1000, self.root.destroy)
            return "Goodbye " + self.user_name + "! Have a great day."

        elif message == "help":
            return self.help_menu()

        elif message == "time":
            return "Current time is " + datetime.now().strftime("%I:%M %p")

        elif message == "date":
            return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

        elif message == "day":
            return "Today is " + datetime.now().strftime("%A")

        elif message.startswith("calculate"):
            expression = user_input.replace("calculate", "", 1).strip()
            return self.calculate(expression)

        elif self.looks_like_math(message):
            return self.calculate(user_input)

        elif message.startswith("explain"):
            topic = message.replace("explain", "", 1).strip()
            return self.explain_topic(topic)

        elif message.startswith("what is"):
            topic = message.replace("what is", "", 1).strip().replace("?", "")
            return self.answer_question(topic)

        elif message.startswith("search"):
            topic = user_input.replace("search", "", 1).strip()
            return self.open_google(topic)

        elif message.startswith("google"):
            topic = user_input.replace("google", "", 1).strip()
            return self.open_google(topic)

        elif message.startswith("wikipedia"):