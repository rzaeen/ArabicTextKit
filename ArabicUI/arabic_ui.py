#!/usr/bin/env python3
# =============================================================================
# arabic_ui.py — مكتبة واجهة عربية حديثة مشتركة (ArabianFox)
# تعتمد customtkinter لتوفير تصميم عصري (داكن/فاتح، زوايا منحنية، RTL).
# تُستخدم من كل أدوات ArabianFox لضمان اتساق بصري وجودة 2026.
# =============================================================================
import customtkinter as ctk

# ألوان العلامة العربية (هوية موحّدة)
PRIMARY = "#2a9d8f"      # أخضر فيروزي
ACCENT = "#e9c46a"       # ذهبي
DANGER = "#e76f51"
BG_DARK = "#1a1a2e"
CARD = "#16213e"
TEXT = "#eaeaea"

FONT = ("Segoe UI", 13)
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_AR = ("Tahoma", 13)
FONT_AR_TITLE = ("Tahoma", 20, "bold")


def setup_theme():
    """يضبط سمة customtkinter للوضع الداكن العربي."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")


class ArabicApp(ctk.CTk):
    """نافذة أساس عربية باتجاه RTL وجاهزة للتمديد."""

    def __init__(self, title="أداة عربية", size=(900, 640)):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.configure(fg_color=BG_DARK)
        # تفعيل RTL حيثما أمكن
        try:
            self.tk.call("wm", "attributes", ".", "-rtl", True)
        except Exception:  # noqa: BLE001
            pass
        self.grid_columnconfigure(0, weight=1)

    def header(self, text, subtitle=None):
        """شريط علوي بعنوان كبير."""
        frame = ctk.CTkFrame(self, fg_color=CARD, corner_radius=12)
        frame.pack(fill="x", padx=14, pady=12)
        ctk.CTkLabel(frame, text=text, font=FONT_AR_TITLE,
                     text_color=PRIMARY).pack(side="right", padx=14, pady=10)
        if subtitle:
            ctk.CTkLabel(frame, text=subtitle, font=FONT_AR,
                         text_color=TEXT).pack(side="right", padx=8)
        return frame

    def card(self, parent=None, **kw):
        """بطاقة محتوى بزوايا منحنية."""
        parent = parent or self
        # customtkinter لا يقبل padx/pady في constructor — نزيلها ونطبّقها لاحقاً
        kw.pop("padx", None)
        kw.pop("pady", None)
        return ctk.CTkFrame(parent, fg_color=CARD, corner_radius=14, **kw)

    def button(self, parent, text, command, style="primary"):
        color = {"primary": PRIMARY, "accent": ACCENT,
                 "danger": DANGER}.get(style, PRIMARY)
        return ctk.CTkButton(parent, text=text, command=command,
                             fg_color=color, hover_color=color,
                             font=FONT_AR, corner_radius=10, height=38)

    def toast(self, msg, kind="info"):
        """رسالة منبثقة أنيقة (شريط سفلي)."""
        color = {"info": PRIMARY, "error": DANGER, "ok": ACCENT}.get(kind, PRIMARY)
        bar = ctk.CTkLabel(self, text=msg, font=FONT_AR, text_color="#fff",
                          fg_color=color, corner_radius=8, height=30)
        bar.pack(side="bottom", fill="x", padx=10, pady=6)
        self.after(3500, bar.destroy)
