from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from PIL import Image, ImageTk
from random import randint
from tkinter import Label, messagebox
from tkinter import *
from tkinter import filedialog
import mysql.connector
from datetime import date


def get_window():
    window = Tk()
    window.title("facebook lite")
    window.iconbitmap("res/facebook_icon.ico")
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    window.geometry(f"{screen_width - 10}x{screen_height - 80}+0+0")
    window.minsize(500, 500)
    window.withdraw()
    window.deiconify()
    window.state('zoomed')
    return window

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="facebook"
)
cursor = my_db.cursor()

def get_str(x):
    return "\"" + x + "\""

def reset_db():
    cursor.execute("delete from users")
    cursor.execute("delete from profiles")
    cursor.execute("delete from posts")
    cursor.execute("delete from reacted_posts")
    cursor.execute("delete from followers")
    cursor.execute("delete from variables")
    cursor.execute("INSERT INTO variables VALUES(1, 0)")
    my_db.commit()

def is_unique(table, column, value, str = 1):
    if str:
        value = get_str(value)
    cursor.execute(f"select * from {table} where {column} = {value}")
    res = cursor.fetchall()
    ln = 0
    for i in cursor:
        ln += 1
    return len(res) == 0

def sign_in(gmail, password):
    gmail = get_str(gmail)
    password = get_str(password)
    cursor.execute(f"select * from users where gmail = {gmail} and user_password = {password}")
    ln = 0
    for i in cursor:
        ln += 1
    return ln == 1

def sign_up(username, gmail, password):
    if not is_unique("users", "gmail", gmail):
        messagebox.showerror("Error", "This gmail account already exists!!")
        return
    gmail = get_str(gmail)
    username = get_str(username)
    password = get_str(password)
    cursor.execute(f"insert into users values ({gmail}, {password})")
    cursor.execute(f"insert into profiles values({gmail}, {username}, \"res/male_pic.png\", \"NA\", \"NA\", \"NA\", \"NA\")")
    my_db.commit()

def get_username(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select username from profiles where gmail = {gmail}")
    res = cursor.fetchall()
    return res[0][0]

def change_username(gmail, new_username):
    gmail = get_str(gmail)
    new_username = get_str(new_username)
    cursor.execute(f"update profiles set username = {new_username} where gmail = {gmail}")
    my_db.commit()

def get_profile_pic(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select profile_image_path from profiles where gmail = {gmail}")
    res = cursor.fetchall()
    return res[0][0]

def choose_profile_pic():
    file_path = filedialog.askopenfilename()
    return file_path

def change_profile_pic(gmail, image_path):
    gmail = get_str(gmail)
    image_path = get_str(image_path)
    cursor.execute(f"update profiles set profile_image_path = {image_path} where gmail = {gmail}")
    my_db.commit()

def get_birth(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select birthday from profiles where gmail = {gmail}")
    res = cursor.fetchall()
    return res[0][0]

def get_phone(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select phone from profiles where gmail = {gmail}")
    res = cursor.fetchall()
    return res[0][0]

def get_gender(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select gender from profiles where gmail = {gmail}")
    res = cursor.fetchall()
    return res[0][0]

def get_edu(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select education from profiles where gmail = {gmail}")
    res = cursor.fetchall()
    return res[0][0]

def edit_profile_info(gmail, education, gender, phone, birthday):
    gmail = get_str(gmail)
    education = get_str(education)
    gender = get_str(gender)
    phone = get_str(phone)
    birthday = get_str(birthday)
    
    cursor.execute(f"update profiles set education = {education}, gender = {gender}, phone = {phone}, birthday = {birthday} where gmail = {gmail}")
    my_db.commit()

def search(username):
    username = get_str('%' + username + '%')
    cursor.execute(f"select gmail,username from profiles where username like {username}")

    l = []
    for i in cursor:
        p = []
        for j in i:
            p.append(j)
        l.append(p)
    return l

def is_follow(follower, followed):
    follower = get_str(follower)
    followed = get_str(followed)
    cursor.execute(f"select * from followers where follower_gmail = {follower} and followed_gmail = {followed}")
    res = cursor.fetchall()
    return len(res) != 0

def follow(follower, followed):
    if (is_follow(follower, followed)):
        return
    follower = get_str(follower)
    followed = get_str(followed)
    cursor.execute(f"insert into followers values({follower}, {followed})")
    my_db.commit()

def unfollow(follower, followed):
    follower = get_str(follower)
    followed = get_str(followed)
    cursor.execute(f"delete from followers where follower_gmail = {follower} and followed_gmail = {followed}")
    my_db.commit()

def get_followers(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select follower_gmail from followers where followed_gmail = {gmail}")
    l = []
    for i in cursor:
        for j in i:
            l.append(j)
    return l

def get_following(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select followed_gmail from followers where follower_gmail = {gmail}")
    l = []
    for i in cursor:
        for j in i:
            l.append(j)
    return l

def react(gmail, post_id):
    gmail = get_str(gmail)
    cursor.execute(f"insert into reacted_posts values({post_id}, {gmail})")
    cursor.execute(f"update posts set react_number = react_number + 1 where post_id = {post_id}")
    my_db.commit()


def unreact(gmail, post_id):
    gmail = get_str(gmail)
    cursor.execute(f"delete from reacted_posts where post_id = {post_id} and gmail = {gmail}")
    cursor.execute(f"update posts set react_number = react_number - 1 where post_id = {post_id}")
    my_db.commit()

def is_react(gmail, post_id):
    gmail = get_str(gmail)
    cursor.execute(f"select * from reacted_posts where gmail = {gmail} and post_id = {post_id}")
    res = cursor.fetchall()
    return len(res) != 0

def create_post(sender_gmail, content):
    cursor.execute(f"select post_number from variables where id = 1")
    res = cursor.fetchall()
    post_id = res[0][0] + 1
    sender_gmail = get_str(sender_gmail)
    send_date = get_str(str(date.today()))
    content = get_str(content)
    cursor.execute(f"update variables set post_number = {res[0][0]+1} where id = 1")
    cursor.execute(f"insert into posts values({post_id}, {sender_gmail}, {send_date}, {content}, 0)")
    my_db.commit()

def get_posts(gmail):
    gmail = get_str(gmail)
    cursor.execute(f"select * from posts where sender_gmail = {gmail} order by post_id")
    res = cursor.fetchall()
    res.reverse()
    return res

def get_reacts(post_id):
    cursor.execute(f"select react_number from posts where post_id = {post_id}")
    res = cursor.fetchall()
    return res[0][0]

def delete_account(gmail):
    cursor.execute(f"select post_id from reacted_posts where gmail = {get_str(gmail)}")
    res = cursor.fetchall()
    for i in res:
        unreact(gmail, i[0])
        
    cursor.execute(f"select followed_gmail from followers where follower_gmail = {get_str(gmail)}")
    res = cursor.fetchall()
    for i in res:
        unfollow(gmail, i[0])

    cursor.execute(f"select follower_gmail from followers where followed_gmail = {get_str(gmail)}")
    res = cursor.fetchall()
    for i in res:
        unfollow(i[0], gmail)

    cursor.execute(f"select * from posts where sender_gmail = {get_str(gmail)}")
    res = cursor.fetchall()
    for i in res:
        cursor.execute(f"delete from reacted_posts where post_id = {i[0]}")
        my_db.commit()
    cursor.execute(f"delete from users where gmail = {get_str(gmail)}")
    cursor.execute(f"delete from profiles where gmail = {get_str(gmail)}")
    cursor.execute(f"delete from posts where sender_gmail = {get_str(gmail)}")
    my_db.commit()

def create_timeline(gmail):
    res = get_following(gmail)
    gmail = get_str(gmail)
    posts = []
    for followed in res:
        p = get_posts(followed)
        for i in p:
            posts.append(i)
    posts.sort(key=lambda x: x[0])
    posts.reverse()
    return posts
# edit_profile_info("joo@gmail.com", "a", "b", "c", "d")
# reset_db()
# print(get_following("mohamed@gmail.com"))
# print(create_timeline("mohamed@gmail.com"))

# follow("mohamed@gmail.com","root@gmail.com")

# sign_up("waheed", "waheed@gmail.com", "root")
# create_post("root@gmail.com", "third")
# follow("waheed@gmail.com", "root@gmail.com")
# follow("root@gmail.com", "waheed@gmail.com")
