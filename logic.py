import math
import sqlite3
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel

def show_msg(text):
    snackbar = Snackbar()
    snackbar.add_widget(MDLabel(text=text, theme_text_color="Custom", text_color=(1,1,1,1), bold=True))
    snackbar.open()

class LoginScreen(Screen):
    def authenticate(self):
        user, pw = self.ids.user.text.strip(), self.ids.password.text.strip()
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("SELECT is_admin FROM users WHERE username=? AND password=?", (user, pw))
        res = cur.fetchone()
        conn.close()
        if res:
            MDApp.get_running_app().is_admin = res[0]
            self.manager.current = 'calc'
        else:
            show_msg("Invalid Login")

class SignUpScreen(Screen):
    def register_user(self):
        user, pw = self.ids.new_user.text.strip(), self.ids.new_pw.text.strip()
        is_admin = 1 if self.ids.admin_key.text == "1234" else 0
        try:
            conn = sqlite3.connect('users.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO users VALUES (?, ?, ?)", (user, pw, is_admin))
            conn.commit()
            conn.close()
            show_msg("Registered!")
            self.manager.current = 'login'
        except:
            show_msg("User exists")

class CalcScreen(Screen):
    def compute(self):
        try:
            # 1. سحب البيانات بدقة
            W = float(self.ids.w.text)       # 4200
            WB = float(self.ids.wb.text)     # 2.5
            F2 = float(self.ids.f2.text)     # 1380
            F3 = float(self.ids.f3.text)     # 1250
            alpha_deg = float(self.ids.alpha.text) # 25
            
            # 2. تحويل الزاوية للراديان
            a_rad = math.radians(alpha_deg)

            # 3. حساب Xcg (المعادلة 1.1)
            # Xcg = (F2 * WB) / W
            xcg = (F2 * WB) / W

            # 4. حساب Ycg (المعادلة 1.3) مع مراعاة الأقواس بدقة هندسية
            # 
            # تم تقسيم المعادلة لثلاث خطوات لضمان عدم حدوث خطأ في الترتيب
            part1 = F3 * WB * math.cos( a_rad)
            part2 = W * xcg * math.cos(  a_rad)
            numerator = part1 - part2
            denominator = W * math.sin( a_rad)
            
            # if abs(denominator) < 1e-9:
            #     show_msg("Angle error: Division by zero")
            #     return
                
             
            ycg = numerator/denominator

            # 5. عرض النتائج النهائية (0.82 و 0.73)
            self.ids.res_label.text = f"Xcg = {xcg:.2f} m  |  Ycg = {ycg:.2f} m"
            
        except Exception as e:
            show_msg("Please check your numbers")

    def check_admin(self):
        if MDApp.get_running_app().is_admin: self.manager.current = 'admin'
        else: show_msg("Admin Only")

    def logout(self): self.manager.current = 'login'

class AdminScreen(Screen):
    def on_enter(self):
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        self.ids.admin_info.text = f"Total Users: {cur.fetchone()[0]}"
        conn.close()