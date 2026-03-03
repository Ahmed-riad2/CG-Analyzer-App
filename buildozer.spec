[app]

# (str) Title of your application
title = CG Analyzer

# (str) Package name
package.name = cganalyzer

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (تأكدنا من وجود kv هنا)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تم إصلاح السطر وإضافة sqlite3 للتعامل مع قاعدة بيانات المستخدمين
requirements = python3, kivy==2.3.0, kivymd==1.1.1, sqlite3, pillow

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API (يفضل 33 للأجهزة الحديثة)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

[buildozer]

# (int) Log level (2 = debug لإظهار كل التفاصيل في حالة الخطأ)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1