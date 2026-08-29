#!/usr/bin/env python3
# مجموعة أدوات النص العربي
# أداة تفاعلية: تشكيل/إصلاح إملاء/عكس نص/إحصاءات عربية Offline.
# أداة عربية مفتوحة المصدر (MIT) — جزء من سلسلة ArabianFox.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "ArabicUI"))
try:
    from arabic_ui import ArabicApp, PRIMARY, ACCENT, DANGER, FONT_AR, FONT_AR_TITLE
    import customtkinter as ctk
except ImportError:
    print("يلزم تثبيت: pip install customtkinter  (ومكتبة ArabicUI)")
    raise SystemExit(1)

APP_TITLE = "مجموعة أدوات النص العربي"

class App(ArabicApp):
    def __init__(self):
        super().__init__(APP_TITLE, (780, 560))
        self.header("مجموعة أدوات النص العربي", "أداة تفاعلية: تشكيل/إصلاح إملاء/عكس نص/إحصاءات عربية Offline.")
        body = self.card(pady=16)
        body.pack(fill="both", expand=True, padx=14, pady=10)
        ctk.CTkLabel(body, text="🔧 هذه الأداة قيد التطوير ضمن سلسلة ArabianFox.",
                     font=FONT_AR, text_color="#eaeaea", wraplength=620).pack(pady=20)
        ctk.CTkLabel(body, text="أداة تفاعلية: تشكيل/إصلاح إملاء/عكس نص/إحصاءات عربية Offline.", font=FONT_AR,
                     text_color="#cfcfcf", wraplength=620).pack(pady=10)
        self.btn = self.button(body, "ابدأ", self._start, "primary")
        self.btn.pack(pady=14)
        self.out = ctk.CTkTextbox(body, height=180, wrap="word",
                                  font=FONT_AR, fg_color="#0f3460",
                                  text_color="#eaeaea")
        self.out.pack(fill="both", expand=True, padx=10, pady=10)

    def _start(self):
        self.out.insert("end", "تم التشغيل بنجاح. طوّر هذه الأداة حسب حاجتك.\n")

def main():
    App().mainloop()

if __name__ == "__main__":
    main()
