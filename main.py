from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class CyberGuideApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # العنوان
        title = Label(text="مستشار الأمن السيبراني", font_size='24sp', size_hint_y=None, height=50)
        layout.add_widget(title)
        
        # النص الاستشاري داخل واجهة قابلة للتمرير
        scroll = ScrollView()
        advice_text = (
            "=== نصائح السلامة الرقمية ===\n\n"
            "1. تفعيل التحقق الثنائي (2FA) لحماية الحسابات الأساسية.\n"
            "2. احذر من الروابط المجهولة التي تصلك عبر الواتساب أو التليجرام.\n"
            "3. تحديث نظام تشغيل جوالك والتطبيقات بشكل دوري لسد الثغرات.\n"
            "4. لا تشارك كلمات المرور الخاصة بك مع أي شخص مطلقاً."
        )
        content = Label(text=advice_text, font_size='18sp', size_hint_y=None, text_size=(400, None), halign='center')
        content.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        return layout

if __name__ == '__main__':
    CyberGuideApp().run()
