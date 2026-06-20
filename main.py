import os
import random
import time

def clear_screen():
    os.system('clear')

def generate_password(length=12):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-="
    return "".join(random.choice(chars) for _ in range(length))

def show_tips():
    tips = [
        "1. لا تشارك كلمات المرور الخاصة بك مع أي شخص مطلقاً.",
        "2. استخدم التحقق بخطوتين (2FA) لحماية حساباتك الأساسية.",
        "3. احذر من الروابط المجهولة التي تصلك عبر الواتساب أو التليجرام.",
        "4. قم بتحديث نظام تشغيل جوالك والتطبيقات بشكل دوري لسد الثغرات."
    ]
    print("\n=== نصائح السلامة الرقمية ===")
    for tip in tips:
        print(tip)
        time.sleep(1)

def main():
    while True:
        clear_screen()
        print("================================")
        print("   برنامج المستشار الأمني الرقمي   ")
        print("================================")
        print("[1] توليد كلمة مرور قوية")
        print("[2] عرض نصائح السلامة الرقمية")
        print("[3] الخروج من البرنامج")
        print("================================")
        
        choice = input("اختر رقماً من القائمة: ")
        
        if choice == '1':
            try:
                length_input = input("أدخل طول كلمة المرور (اضغط Enter للمقاس الافتراضي 12): ")
                length = int(length_input) if length_input.strip() else 12
                password = generate_password(length)
                print(f"\n+ كلمة المرور المقترحة: {password}")
            except ValueError:
                print("\n! خطأ: يرجى إدخال رقم صحيح.")
            input("\nاضغط Enter للعودة...")
            
        elif choice == '2':
            show_tips()
            input("\nاضغط Enter للعودة...")
            
        elif choice == '3':
            print("\nشكراً لاستخدامك المستشار الأمني. في أمان الله!")
            break
        else:
            print("\n! خيار غير صحيح، حاول مجدداً.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
