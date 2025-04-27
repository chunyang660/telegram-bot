import logging
     from telegram import Update
     from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

     # 设置日志
     logging.basicConfig(
         format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
         level=logging.INFO
     )

     async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
         await update.message.reply_text(
             "欢迎使用即时聊天机器人！请输入您的消息，我们会即时回应。"
         )

     async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
         user_message = update.message.text
         await update.message.reply_text(f"您说: {user_message}")

     def main():
         import os
         BOT_TOKEN = os.getenv("BOT_TOKEN")  # 从环境变量中读取 Bot Token
         if not BOT_TOKEN:
             raise ValueError("请在环境变量中设置 BOT_TOKEN")

         application = ApplicationBuilder().token(BOT_TOKEN).build()

         application.add_handler(CommandHandler("start", start))
         application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

         application.run_polling()

     if __name__ == "__main__":
         main()