import sqlite3
import telebot
from telebot import types

TOKEN = "9220675051:AAFw1otCXbd-4vsrLzJPpqtkiSHycKL8S64"
bot = telebot.TeleBot(TOKEN)

# --- ИНИЦИАЛИЗА БАЗЫ ДАННЫХ SQLITE ---
def init_db():
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    # Создаем таблицу для транзакций, если ее еще нет
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()

# Запускаем создание базы данных при старте
init_db()

# --- ФУНКЦИИ ДЛЯ РАБОТЫ С БД ---
def add_transaction(user_id, category, amount):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (user_id, category, amount) VALUES (?, ?, ?)",
        (user_id, category, amount)
    )
    conn.commit()
    conn.close()

def get_user_stats(user_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND category = 'income'", (user_id,))
    incomes = cursor.fetchone()[0] or 0.0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND category = 'fixed'", (user_id,))
    fixed = cursor.fetchone()[0] or 0.0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND category = 'expense'", (user_id,))
    expenses = cursor.fetchone()[0] or 0.0

    conn.close()
    return incomes, fixed, expenses

# --- КЛАВИАТУРЫ ---
def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("💰 Добавить доход")
    item2 = types.KeyboardButton("📌 Постоянный платеж")
    item3 = types.KeyboardButton("🛒 Обычный расход")
    item4 = types.KeyboardButton("📊 Итоговый баланс")
    markup.add(item1, item2, item3, item4)
    return markup

# --- ОБРАБОТЧИКИ КОМАНД И ТЕКСТА ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я твой финансовый менеджер с базой данных SQLite.\nВыбери действие:",
        reply_markup=get_main_keyboard()
    )

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_id = message.from_user.id
    text = message.text

    if text == "💰 Добавить доход":
        msg = bot.send_message(message.chat.id, "Введите сумму дохода:")
        bot.register_next_step_handler(msg, process_amount, 'income')
    elif text == "📌 Постоянный платеж":
        msg = bot.send_message(message.chat.id, "Введите сумму постоянного платежа:")
        bot.register_next_step_handler(msg, process_amount, 'fixed')
    elif text == "🛒 Обычный расход":
        msg = bot.send_message(message.chat.id, "Введите сумму расхода:")
        bot.register_next_step_handler(msg, process_amount, 'expense')
    elif text == "📊 Итоговый баланс":
        incomes, fixed, expenses = get_user_stats(user_id)
        balance = incomes - fixed - expenses
        response = (
            f"📈 **Финансовый отчет:**\n\n"
            f"💰 Всего доходов: {incomes} ₸\n"
            f"📌 Постоянные расходы: {fixed} ₸\n"
            f"🛒 Обычные расходы: {expenses} ₸\n"
            f"───────────────────\n"
            f"💵 **Чистый баланс:** {balance} ₸"
        )
        bot.send_message(message.chat.id, response, parse_mode="Markdown")

def process_amount(message, category):
    try:
        amount = float(message.text)
        add_transaction(message.from_user.id, category, amount)
        bot.send_message(message.chat.id, f"Успешно сохранено в базу данных! Сумма: {amount} ₸")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Пожалуйста, введите число.")

print("Бот с поддержкой SQLite запущен...")
bot.polling(none_stop=True)