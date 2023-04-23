import customtkinter as tk


class MainApplication(tk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x820")
        self.title("Recogni Pilajara")

        # Set up main page
        self.mainpage = tk.CTkFrame(self)
        self.mainpage.grid(row=0, column=0, sticky="nsew")

        self.top_left_frame = tk.CTkFrame(self.mainpage, fg_color="red")
        self.top_left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.top_left_label = tk.CTkLabel(self.top_left_frame, text="Top Left Frame")
        self.top_left_label.pack(pady=20)

        self.bottom_right_frame = tk.CTkFrame(self.mainpage, fg_color="blue")
        self.bottom_right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.bottom_right_label = tk.CTkLabel(self.bottom_right_frame, text="Bottom Right Frame")
        self.bottom_right_label.pack(pady=20)

        self.main_button = tk.CTkButton(self.mainpage, text="Go to Second Page", command=self.show_second_page)
        self.main_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Set up second page
        self.second_frame = tk.CTkFrame(self)
        self.second_frame.grid(row=0, column=0, sticky="nsew")

        self.top_frame = tk.CTkFrame(self.second_frame, fg_color="green")
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.top_label = tk.CTkLabel(self.top_frame, text="Top Frame")
        self.top_label.pack(pady=20)

        self.bottom_frame = tk.CTkFrame(self.second_frame, fg_color="yellow")
        self.bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.bottom_label = tk.CTkLabel(self.bottom_frame, text="Bottom Frame")
        self.bottom_label.pack(pady=20)

        self.second_button = tk.CTkButton(self.bottom_frame, text="Go to Main Page", command=self.show_main_page)
        self.second_button.pack(pady=10)

        self.second_widget = tk.CTkLabel(self.top_frame, text="Second Widget")
        self.second_widget.pack(pady=10)

        # Set grid weights to make widgets expandable
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.mainpage.rowconfigure(0, weight=1)
        self.mainpage.columnconfigure(0, weight=1)
        self.mainpage.columnconfigure(1, weight=1)
        self.second_frame.rowconfigure(0, weight=1)
        self.second_frame.columnconfigure(0, weight=1)

        # Show main page initially
        self.show_main_page()

    def show_main_page(self):
        self.second_frame.grid_forget()
        self.mainpage.grid(row=0, column=0, sticky="nsew")

    def show_second_page(self):
        self.mainpage.grid_forget()
        self.second_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()
