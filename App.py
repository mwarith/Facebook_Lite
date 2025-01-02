from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageOps
import functions
import shutil


signedin_gmail = ""


def upload_Image(window, path):
    img = Image.open(path)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.pack(fill="both", expand=True)
    panel.place(x=0, y=0, relwidth=1, relheight=1)


class startWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#F0F2F5")
        upload_Image(self.window, "res/wallpaperflarecom_wallpaper.jpg")

        welcome = Label(
            self.window,
            text="Welcome to Facebook Lite.",
            bg="#7f98ce",
            fg="#1877F2",
            font=("Helvetica", 20, "bold"),
        )
        welcome.place(x=600 - 50, y=100)

        def c1():
            self.destroy()
            login_window.open()

        sign_in = Button(
            self.window,
            command=c1,
            text="Sign in",
            bg="#0861F2",
            fg="white",
            height=1,
            width=15,
            font=("Helvetica", 16, "bold"),
        )
        sign_in.place(x=630, y=200)

        def c2():
            self.destroy()
            register_window.open()

        sign_up = Button(
            self.window,
            text="Sign up",
            command=c2,
            bg="green",
            fg="white",
            height=1,
            width=15,
            font=("Helvetica", 16, "bold"),
        )
        sign_up.place(x=630, y=250)


class loginWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#F0F2F5")
        upload_Image(self.window, "res/wallpaperflarecom_wallpaper.jpg")

        welcome = Label(
            self.window,
            text="Facebook Lite",
            bg="#7f98ce",
            fg="#1877F2",
            font=("Helvetica", 20, "bold"),
        )
        welcome.place(x=600, y=100)

        Gmail = Label(
            self.window,
            text="Gmail:",
            bg="#7f9cd0",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        Gmail.place(x=500 - 50, y=150)
        password = Label(
            self.window,
            text="password:",
            bg="#849fd4",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        password.place(x=500 - 50, y=200)

        Gmailtb = Entry(self.window, font=("Helvetica", 16))
        Gmailtb.place(x=600 - 10, y=150)
        passwordtb = Entry(self.window, font=("Helvetica", 16), show="*")
        passwordtb.place(x=600 - 10, y=200)

        def c1():
            g = Gmailtb.get()
            p = passwordtb.get()
            # g = "waheed@gmail.com"
            # p = "root"
            if not len(g) or not len(p):
                messagebox.showerror("Error", "Please fill out all the fields.")
                return
            if functions.sign_in(g, p):
                global signedin_gmail
                signedin_gmail = g
                self.destroy()
                profile_window.open(g)
            else:
                messagebox.showerror("Error", "Either gmail or password is wrong.")

        sign_in = Button(
            self.window,
            text="Sign in",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=15,
            font=("Helvetica", 16, "bold"),
        )
        sign_in.place(x=630 + 50 + 10 + 10, y=300 - 10 - 10)

        def c2():
            self.destroy()
            start_window.open()

        back = Button(
            self.window,
            text="back",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=15,
            font=("Helvetica", 16, "bold"),
        )
        back.place(x=530 - 50 - 10, y=300 - 10 - 10)


class registerWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#F0F2F5")
        upload_Image(self.window, "res/wallpaperflarecom_wallpaper.jpg")
        welcome = Label(
            self.window,
            text="facebook lite",
            bg="#7f98ce",
            fg="#1877F2",
            font=("Helvetica", 20, "bold"),
        )
        welcome.place(x=600, y=100 - 40)

        username = Label(
            self.window,
            text="username:",
            bg="#7f9cd0",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        username.place(x=500 - 100, y=150 - 40)
        gmail = Label(
            self.window,
            text="gmail:",
            bg="#849fd4",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        gmail.place(x=500 - 100, y=200 - 40)
        password = Label(
            self.window,
            text="password:",
            bg="#87a2d6",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        password.place(x=500 - 100, y=250 - 40)
        comfirm = Label(
            self.window,
            text="confirm password:",
            bg="#88a3d8",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        comfirm.place(x=500 - 100, y=300 - 40)

        usernametb = Entry(self.window, font=("Helvetica", 16))
        usernametb.place(x=600, y=150 - 40)
        gmailtb = Entry(self.window, font=("Helvetica", 16))
        gmailtb.place(x=600, y=200 - 40)
        passwordtb = Entry(self.window, font=("Helvetica", 16), show="*")
        passwordtb.place(x=600, y=250 - 40)
        confirmtb = Entry(self.window, font=("Helvetica", 16), show="*")
        confirmtb.place(x=600, y=300 - 40)

        def c1():
            g = gmailtb.get()
            p = passwordtb.get()
            u = usernametb.get()
            if p != confirmtb.get():
                messagebox.showerror(
                    "Error",
                    "Please make sure password is the same as confirm password.",
                )
                return
            if not (len(g) and len(p) and len(u)):
                messagebox.showerror("Error", "Please fill out all the fields.")
                return
            if not functions.is_unique("users", "gmail", g):
                messagebox.showerror("Error", "This gmail account was used before.")
                return
            global signedin_gmail
            signedin_gmail = g
            functions.sign_up(u, g, p)
            self.destroy()
            profile_window.open(g)

        sign_up = Button(
            self.window,
            text="Sign up",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=15,
            font=("Helvetica", 16, "bold"),
        )
        sign_up.place(x=630 + 50, y=380 + 100)

        def c2():
            self.destroy()
            start_window.open()

        back = Button(
            self.window,
            text="back",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=15,
            font=("Helvetica", 16, "bold"),
        )
        back.place(x=530 - 50 - 40, y=380 + 100)


def make_circle(image_path):
    # Open the input image as an image object
    image = Image.open(image_path).convert("RGBA")

    # Create a mask to create a circle
    size = min(image.size)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Resize the image to fit the mask
    output = ImageOps.fit(image, (size, size))
    output.putalpha(mask)

    return output


class profileWindow:
    def destroy(self):
        self.window.destroy()
        self.gmail = ""

    def open(self, gmail):
        self.window = functions.get_window()
        self.gmail = gmail
        self.fill()

    def fill(self):
        self.window.configure(bg="#F0F2F5")

        # Create a canvas
        canvas = Canvas(self.window, bg="#F0F2F5")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a scrollbar
        scrollbar = Scrollbar(self.window, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Create a frame inside the canvas
        frame = Frame(canvas, bg="#F0F2F5")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Scroll function
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Bind the mouse wheel event to the scroll function
        self.window.bind_all("<MouseWheel>", on_mousewheel)

        def c1():
            self.destroy()
            self.open(signedin_gmail)

        profileb = Button(
            frame,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            timeline_window.open()
            self.destroy()

        timelineb = Button(
            frame,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            search_window.open([])
            self.destroy()

        searchb = Button(
            frame,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            setting_window.open()
            self.destroy()

        settingsb = Button(
            frame,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        img = make_circle(functions.get_profile_pic(self.gmail))
        # img = Image.open(functions.get_profile_pic(self.gmail))
        img = img.resize((320, 320), Image.Resampling.LANCZOS)

        tk_image = ImageTk.PhotoImage(img, master=self.window)
        pic = Label(frame, height=320, width=320, image=tk_image, bg="#F0F2F5")
        pic.image = tk_image
        pic.grid(row=1, column=0, pady=25, rowspan=4)

        user = Label(
            frame,
            text=functions.get_username(self.gmail),
            bg="#F0F2F5",
            fg="#1877F2",
            font=("Helvetica", 20, "bold"),
        )
        user.grid(row=5, column=0, padx=35 + 10 + 20 + 30 + 20, pady=20, sticky="w")

        phone = Label(
            frame,
            text="Phone Number: " + functions.get_phone(self.gmail),
            bg="#F0F2F5",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        phone.grid(row=1, column=1, padx=10, pady=0, sticky="ws")

        gender = Label(
            frame,
            text="Gender: " + functions.get_gender(self.gmail),
            bg="#F0F2F5",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        gender.grid(row=2, column=1, padx=10, pady=0, sticky="ws")

        birthday = Label(
            frame,
            text="BirthDay: " + functions.get_birth(self.gmail),
            bg="#F0F2F5",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        birthday.grid(row=3, column=1, padx=10, pady=0, sticky="ws")

        education = Label(
            frame,
            text="Education: " + functions.get_edu(self.gmail),
            bg="#F0F2F5",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        education.grid(row=4, column=1, padx=10, pady=0, sticky="ws")

        follower = Label(
            frame,
            text="followers: " + str(len(functions.get_followers(self.gmail))),
            bg="#F0F2F5",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        follower.grid(row=1, column=3, padx=10, pady=10, sticky="ws")

        following = Label(
            frame,
            text="following: " + str(len(functions.get_following(self.gmail))),
            bg="#F0F2F5",
            fg="#1877F2",
            font=("Helvetica", 16, "bold"),
        )
        following.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        if self.gmail == signedin_gmail:

            def c5():
                post_window.open()
                self.destroy()

            create_post = Button(
                frame,
                text="Create Post",
                command=c5,
                bg="#0861F2",
                fg="white",
                height=1,
                width=20,
                font=("Helvetica", 16),
            )
            create_post.grid(
                row=6, column=0, padx=50, pady=0, sticky="nw", columnspan=2
            )
        else:
            t = ""
            if functions.is_follow(signedin_gmail, self.gmail):
                t = "Unfollow"
            else:
                t = "Follow"

            follow = Button(
                frame,
                text=t,
                bg="#0861F2",
                fg="white",
                height=1,
                width=20,
                font=("Helvetica", 16),
            )

            def c11(f):
                if not functions.is_follow(signedin_gmail, self.gmail):
                    functions.follow(signedin_gmail, self.gmail)
                    f.configure(text="Unfollow")
                else:
                    functions.unfollow(signedin_gmail, self.gmail)
                    f.configure(text="Follow")

            follow.configure(command=lambda e=follow: c11(e))
            follow.grid(row=6, column=0, padx=50, pady=0, sticky="nw", columnspan=2)

        posts = functions.get_posts(self.gmail)
        for i in range(len(posts)):
            usr = Label(
                frame,
                text=functions.get_username(posts[i][1]) + " . " + posts[i][2],
                bg="#F0F2F5",
                fg="#1877F2",
                font=("Helvetica", 16, "bold"),
            )
            usr.grid(
                row=7 + i * 4,
                column=0,
                padx=400,
                pady=(10, 0),
                sticky="w",
                columnspan=4,
            )

            post = Label(
                frame,
                text=posts[i][3],
                height=10,
                width=100,
                bg="#B5D7F2",
                fg="black",
                font=("Helvetica", 9, "bold"),
            )
            post.grid(
                row=8 + i * 4, column=0, padx=400, pady=0, sticky="w", columnspan=4
            )

            t = "red" if functions.is_react(signedin_gmail, posts[i][0]) else "#1877F2"
            love = Button(
                frame,
                text="Love",
                bg=t,
                fg="white",
                height=1,
                width=15,
                font=("Helvetica", 7),
            )
            love.grid(
                row=9 + i * 4, column=0, padx=400, pady=0, sticky="w", columnspan=4
            )

            react = Label(
                frame,
                text=str(posts[i][4]),
                bg="black",
                fg="white",
                font=("Helvetica", 7),
            )

            def c12(e, id, r):
                if functions.is_react(signedin_gmail, id):
                    functions.unreact(signedin_gmail, id)
                    e.configure(bg="#1877F2")
                else:
                    functions.react(signedin_gmail, id)
                    e.configure(bg="red")
                r.configure(text=str(functions.get_reacts(id)))

            love.configure(
                command=lambda e=love, id=posts[i][0], r=react: c12(e, id, r)
            )
            react.grid(
                row=9 + i * 4, column=0, padx=500, pady=0, sticky="w", columnspan=4
            )


class timelineWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#F0F2F5")

        # Create a canvas
        canvas = Canvas(self.window, bg="#F0F2F5")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a scrollbar
        scrollbar = Scrollbar(self.window, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Create a frame inside the canvas
        frame = Frame(canvas, bg="#F0F2F5")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Scroll function
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Bind the mouse wheel event to the scroll function
        self.window.bind_all("<MouseWheel>", on_mousewheel)

        def c1():
            profile_window.open(signedin_gmail)
            self.destroy()

        profileb = Button(
            frame,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            self.destroy()
            self.open()

        timelineb = Button(
            frame,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            search_window.open([])
            self.destroy()

        searchb = Button(
            frame,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            setting_window.open()
            self.destroy()

        settingsb = Button(
            frame,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        posts = functions.create_timeline(signedin_gmail)
        for i in range(len(posts)):
            usr = Label(
                frame,
                text=functions.get_username(posts[i][1]) + " . " + posts[i][2],
                bg="#F0F2F5",
                fg="#1877F2",
                font=("Helvetica", 16, "bold"),
            )
            usr.grid(
                row=7 + i * 3, column=0, padx=400, pady=0, sticky="w", columnspan=4
            )
            post = Label(
                frame,
                text=posts[i][3],
                height=10,
                width=100,
                bg="#B5D7F2",
                fg="black",
                font=("Helvetica", 9, "bold"),
            )
            post.grid(
                row=8 + i * 3, column=0, padx=400, pady=0, sticky="w", columnspan=4
            )
            t = ""
            if functions.is_react(signedin_gmail, posts[i][0]):
                t = "red"
            else:
                t = "#1877F2"
            love = Button(
                frame,
                text="Love",
                bg=t,
                fg="white",
                height=1,
                width=15,
                font=("Helvetica", 7),
            )
            love.grid(
                row=9 + i * 3, column=0, padx=400, pady=0, sticky="w", columnspan=4
            )
            react = Label(
                frame,
                text=str(posts[i][4]),
                bg="black",
                fg="white",
                font=("Helvetica", 7),
            )

            def c(e, id, r):
                if functions.is_react(signedin_gmail, id):
                    functions.unreact(signedin_gmail, id)
                    e.configure(bg="#1877F2")
                else:
                    functions.react(signedin_gmail, id)
                    e.configure(bg="red")
                r.configure(text=str(functions.get_reacts(id)))

            love.configure(command=lambda e=love, id=posts[i][0], r=react: c(e, id, r))
            react.grid(
                row=9 + i * 3, column=0, padx=500, pady=0, sticky="w", columnspan=4
            )


class postWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#F0F2F5")

        def c1():
            profile_window.open(signedin_gmail)
            self.destroy()

        profileb = Button(
            self.window,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            timeline_window.open()
            self.destroy()

        timelineb = Button(
            self.window,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            search_window.open([])
            self.destroy()

        searchb = Button(
            self.window,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            setting_window.open()
            self.destroy()

        settingsb = Button(
            self.window,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        posttb = Text(self.window, font=("Helvetica", 16), width=85, height=20)
        posttb.place(x=250, y=150)

        def c5():
            if len(posttb.get("1.0", "end-1c").strip()) == 0:
                messagebox.showerror("Error", "Please type something before posting.")
                return
            functions.create_post(signedin_gmail, posttb.get("1.0", "end-1c").strip())
            profile_window.open(signedin_gmail)
            self.destroy()

        postB = Button(
            self.window,
            command=c5,
            text="Post",
            bg="#0861F2",
            fg="white",
            font=("Helvetica", 16, "bold"),
        )
        postB.place(x=1200, y=650)


class settingWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#B5D7F2")

        def c1():
            profile_window.open(signedin_gmail)
            self.destroy()

        profileb = Button(
            self.window,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            timeline_window.open()
            self.destroy()

        timelineb = Button(
            self.window,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            search_window.open([])
            self.destroy()

        searchb = Button(
            self.window,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            self.destroy()
            self.open()

        settingsb = Button(
            self.window,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        def c5():
            changeUsr_window.open()
            self.destroy()

        changeUser = Button(
            self.window,
            command=c5,
            text="Change username",
            bg="#0861F2",
            fg="white",
            width=31,
            font=("Helvetica", 16, "bold"),
        )
        changeUser.place(x=500, y=100)

        def c6():
            changeImage_window.open()
            self.destroy()

        changepi = Button(
            self.window,
            command=c6,
            text="Change profile image",
            bg="#0861F2",
            fg="white",
            width=31,
            font=("Helvetica", 16, "bold"),
        )
        changepi.place(x=500, y=200)

        def c7():
            editInfo_window.open()
            self.destroy()

        editinfo = Button(
            self.window,
            command=c7,
            text="Edit profile info",
            bg="#0861F2",
            fg="white",
            width=31,
            font=("Helvetica", 16, "bold"),
        )
        editinfo.place(x=500, y=300)

        def c8():
            response = messagebox.askyesno(
                "Delete account permenantly", "Do you want to proceed?"
            )
            if response:
                functions.delete_account(signedin_gmail)
                start_window.open()
                self.destroy()

        deleteaccount = Button(
            self.window,
            command=c8,
            text="Delete account",
            bg="#0861F2",
            fg="white",
            width=31,
            font=("Helvetica", 16, "bold"),
        )
        deleteaccount.place(x=500, y=400)

        def c9():
            self.destroy()
            start_window.open()

        logout = Button(
            self.window,
            command=c9,
            text="log out",
            bg="#0861F2",
            fg="white",
            width=31,
            font=("Helvetica", 16, "bold"),
        )
        logout.place(x=500, y=500)


class searchWindow:
    def destroy(self):
        self.window.destroy()

    def open(self, usersL):
        self.window = functions.get_window()
        self.fill(usersL)

    def fill(self, usersL):
        self.window.configure(bg="#B5D7F2")

        # Create a canvas
        canvas = Canvas(self.window, bg="#B5D7F2")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a scrollbar
        scrollbar = Scrollbar(self.window, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Create a frame inside the canvas
        frame = Frame(canvas, bg="#B5D7F2")
        canvas.create_window((0, 0), window=frame, anchor="nw")

        # Scroll function
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        # Bind the mouse wheel event to the scroll function
        self.window.bind_all("<MouseWheel>", on_mousewheel)

        def c1():
            profile_window.open(signedin_gmail)
            self.destroy()

        profileb = Button(
            frame,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            timeline_window.open()
            self.destroy()

        timelineb = Button(
            frame,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            self.destroy()
            self.open()

        searchb = Button(
            frame,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            setting_window.open()
            self.destroy()

        settingsb = Button(
            frame,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        posttb = Entry(frame, font=("Helvetica", 16), width=30)
        posttb.grid(row=1, column=1, pady=50, sticky="se")

        def c5():
            usersL = functions.search(posttb.get())
            self.destroy()
            self.open(usersL)

        postB = Button(
            frame,
            command=c5,
            text="search",
            bg="#0861F2",
            fg="white",
            font=("Helvetica", 11, "bold"),
        )
        postB.grid(row=1, column=2, pady=50, padx=10, sticky="sw")
        for i in range(len(usersL)):
            usr = Label(
                frame,
                text=usersL[i][1],
                bg="#B5D7F2",
                fg="#1877F2",
                font=("Helvetica", 16),
            )
            usr.grid(
                row=7 + i * 2, column=0, padx=400, pady=0, sticky="w", columnspan=4
            )
            profile = Button(
                frame,
                text="View profile",
                bg="#0861F2",
                fg="white",
                height=1,
                width=15,
                font=("Helvetica", 7),
            )

            def c(e, g):
                profile_window.open(g)
                self.destroy()

            profile.configure(command=lambda e=profile, g=usersL[i][0]: c(e, g))
            profile.grid(
                row=7 + i * 2, column=1, padx=400, pady=0, sticky="w", columnspan=4
            )


class changeUsrWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#B5D7F2")

        def c1():
            profile_window.open(signedin_gmail)
            self.destroy()

        profileb = Button(
            self.window,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            timeline_window.open()
            self.destroy()

        timelineb = Button(
            self.window,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            search_window.open([])
            self.destroy()

        searchb = Button(
            self.window,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            setting_window.open()
            self.destroy()

        settingsb = Button(
            self.window,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        changeL = Label(
            self.window,
            text="New username:",
            bg="#B5D7F2",
            fg="#1877F2",
            font=("Helvetica", 16),
        )
        changeL.place(x=200 + 200, y=150)

        changetb = Entry(self.window, font=("Helvetica", 16))
        changetb.place(x=350 + 200, y=150)

        def c5():
            if len(changetb.get()) == 0:
                messagebox.showerror("Error", "Please type the new username.")
                return
            functions.change_username(signedin_gmail, changetb.get())
            messagebox.showinfo("", f"Your new username is {changetb.get()}.")
            setting_window.open()
            self.destroy()

        changeB = Button(
            self.window,
            command=c5,
            text="Change username",
            bg="#0861F2",
            fg="white",
            font=("Helvetica", 11),
        )
        changeB.place(x=600 + 200, y=150)


class changeImageWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.path = ""
        self.fill()

    def fill(self):
        self.window.configure(bg="#B5D7F2")

        def c1():
            profile_window.open(signedin_gmail)
            self.destroy()

        profileb = Button(
            self.window,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            timeline_window.open()
            self.destroy()

        timelineb = Button(
            self.window,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            search_window.open([])
            self.destroy()

        searchb = Button(
            self.window,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            setting_window.open()
            self.destroy()

        settingsb = Button(
            self.window,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        def c5():
            self.path = functions.choose_profile_pic()

        changetb = Button(
            self.window,
            command=c5,
            text="Select photo",
            width=15,
            height=2,
            bg="#0861F2",
            fg="white",
            font=("Helvetica", 11, "bold"),
        )
        changetb.place(x=700, y=150 + 150)

        def c6():
            dst_path = "res/"
            self.path = self.path[::-1]
            temp = ""
            for i in self.path:
                if i == "/":
                    break
                temp += i
            temp = temp[::-1]
            dst_path += temp
            self.path = self.path[::-1]
            shutil.copy(self.path, dst_path)
            functions.change_profile_pic(signedin_gmail, dst_path)
            self.destroy()
            setting_window.open()

        changeB = Button(
            self.window,
            command=c6,
            text="Change",
            width=15,
            height=2,
            bg="#0861F2",
            fg="white",
            font=("Helvetica", 11, "bold"),
        )
        changeB.place(x=700, y=250 + 150)


class editInfoWindow:
    def destroy(self):
        self.window.destroy()

    def open(self):
        self.window = functions.get_window()
        self.fill()

    def fill(self):
        self.window.configure(bg="#B5D7F2")

        def c1():
            profile_window.open(signedin_gmail)
            self.destroy()

        profileb = Button(
            self.window,
            text="Profile",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        profileb.grid(row=0, column=0, padx=0, pady=0)

        def c2():
            timeline_window.open()
            self.destroy()

        timelineb = Button(
            self.window,
            text="Timeline",
            command=c2,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        timelineb.grid(row=0, column=1, padx=0, pady=0)

        def c3():
            search_window.open([])
            self.destroy()

        searchb = Button(
            self.window,
            text="Search",
            command=c3,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        searchb.grid(row=0, column=2, padx=0, pady=0)

        def c4():
            setting_window.open()
            self.destroy()

        settingsb = Button(
            self.window,
            text="Settings",
            command=c4,
            bg="#0861F2",
            fg="white",
            height=1,
            width=31,
            font=("Helvetica", 16),
        )
        settingsb.grid(row=0, column=3, padx=0, pady=0)

        edu = Label(
            self.window,
            text="Education:",
            bg="#B5D7F2",
            fg="#1877F2",
            font=("Helvetica", 16),
        )
        edu.place(x=500 - 100, y=150)
        gender = Label(
            self.window,
            text="Gender:",
            bg="#B5D7F2",
            fg="#1877F2",
            font=("Helvetica", 16),
        )
        gender.place(x=500 - 100, y=200)
        phone = Label(
            self.window,
            text="Phone:",
            bg="#B5D7F2",
            fg="#1877F2",
            font=("Helvetica", 16),
        )
        phone.place(x=500 - 100, y=250)
        birth = Label(
            self.window,
            text="BirthDay:",
            bg="#B5D7F2",
            fg="#1877F2",
            font=("Helvetica", 16),
        )
        birth.place(x=500 - 100, y=300)

        edutb = Entry(self.window, font=("Helvetica", 16))
        edutb.place(x=600, y=150)
        gendertb = Entry(self.window, font=("Helvetica", 16))
        gendertb.place(x=600, y=200)
        phonetb = Entry(self.window, font=("Helvetica", 16))
        phonetb.place(x=600, y=250)
        birthtb = Entry(self.window, font=("Helvetica", 16))
        birthtb.place(x=600, y=300)

        def c1():
            print(edutb.get(), gendertb.get(), phonetb.get(), birthtb.get())
            functions.edit_profile_info(
                signedin_gmail,
                edutb.get(),
                gendertb.get(),
                phonetb.get(),
                birthtb.get(),
            )
            setting_window.open()
            self.destroy()

        ok = Button(
            self.window,
            text="OK",
            command=c1,
            bg="#0861F2",
            fg="white",
            height=1,
            width=15,
            font=("Helvetica", 16),
        )
        ok.place(x=600, y=380)


start_window = startWindow()
login_window = loginWindow()
register_window = registerWindow()
profile_window = profileWindow()
timeline_window = timelineWindow()
post_window = postWindow()
setting_window = settingWindow()
search_window = searchWindow()
changeUsr_window = changeUsrWindow()
changeImage_window = changeImageWindow()
editInfo_window = editInfoWindow()

start_window.open()
mainloop()
