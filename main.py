from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
import database
import razorpay

# Initialize Razorpay
client = razorpay.Client(auth=(config.RAZORPAY_KEY, config.RAZORPAY_SECRET))

# Start command
async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("🏠 Lister", callback_data="role_lister")],
        [InlineKeyboardButton("👀 Viewer", callback_data="role_viewer")]
    ]
    await update.message.reply_text(
        "Choose your role:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Handle role selection
async def role_selection(update: Update, context):
    query = update.callback_query
    role = query.data.split("_")[1]  # "lister" or "viewer"
    
    # Save to database (simplified)
    database.save_user(query.message.chat_id, role)
    
    await query.edit_message_text(f"✅ Registered as {role}!")

# Razorpay payment handler
async def create_payment(update: Update, context):
    chat_id = update.message.chat_id
    payment = client.order.create({
        "amount": 10000,  # ₹100 in paise
        "currency": "INR",
        "receipt": f"receipt_{chat_id}",
    })
    await update.message.reply_text(
        f"Pay ₹100: {payment['id']}\n"
        "After payment, send screenshot to @AdminBot"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(role_selection, pattern="^role_"))
    app.add_handler(CommandHandler("pay", create_payment))
    
    app.run_polling()

if __name__ == "__main__":
    main()
