from balethon.objects import InlineKeyboard, ReplyKeyboard
#KEYBORD
inline_buttons = InlineKeyboard(
    [("📌 بخش کاربردی و ابزاری", "tools")],
    [("🎯 بخش سرگرمی و علمی", "fun_science")],
    [("🤖 بخش هوش مصنوعی", "ai_services")],
    [("ℹ️ درباره ما", "info"), ("راهنما 🧬", "help")]
)

tools_buttons = InlineKeyboard(
    [("اعلام زمان ⏰", "time"), ("فونت ساز", "font")],
    [("دریافت نرخ طلا و سکه 💰", "gold_rate")],
    [("وضعیت آب و هوا ⛅️", "w_i")],
    [("بازی های امروز ⚽️", "fo")],
    [("پیگیری مرسوله تیپاکس 📦", "track_parcel")],
    [("جستجوی گوشی 📱", "mobi")],
    [("جستجو در آپارات 🎥", "apa")],
    [("جستجو در دیجی کالا 🗣️", "kala")],
    [("جستجو آهنگ 🎵", "mu")],
    [("محاسبه سن 🎂", "calculate_age")],
    [("بازگشت به منو اصلی 🏠", "return_to_main_menu")]
)

fun_science_buttons = InlineKeyboard(
    [("جوک تصادفی 😂", "random_joke"), ("دانستنی‌ها 🧠", "facts")],
    [("حدیث 📖", "hadis")],
    [("سخن بزرگان", "so"), ("ذکر این هفته", "zekr")],
    [("بازگشت به منو اصلی 🏠", "return_to_main_menu")]
)

ai_services_buttons = InlineKeyboard(
    [("هوش مصنوعی حافظه دار 🧠", "gpt1")],
    [("دستیار مومن 🤖", "ai_chat")],
    [("وکیل ⚖️", "lawyer")],
    [("روانشناس 🧠", "psychologist")],
    [("ChatGPT-4o 🧩", "gpt")],
    [("تولید تصویر 🤳", "p")],
    [("مترجم انگلیسی 📝", "translate")],
    [("بازگشت به منو اصلی 🏠", "return_to_main_menu")]
)
return_to_main_menu_button = InlineKeyboard([("بازگشت به منو اصلی 🏠", "return_to_main_menu")])
join = InlineKeyboard([InlineKeyboardButton("🔗 عضویت در کانال", url="https://ble.ir/shafag_tm")])
Ai_back = InlineKeyboard([("🔙", "Ai_b")])
