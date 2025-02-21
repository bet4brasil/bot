from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Substitua pelo seu token do BotFather
TOKEN = os.getenv('TOKEN')

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎰 Bem-vindo ao Cassino Bet4Brasil!\n\nDigite /info para saber mais sobre nossos serviços, /suporte para ajuda, /promocoes para ver as ofertas ou /faq para dúvidas frequentes."
    )

# Comando /info
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "ℹ️ Informações:\n\nAcesse nossos jogos em https://bet4brasil.online/home/game\n\nEstamos disponíveis 24/7 para garantir a sua diversão!"
    )

# Comando /suporte
async def suporte(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🛠️ Suporte:\n\nPara dúvidas ou problemas, entre em contato pelo e-mail: suporte@bet4brasil.online ou responda aqui mesmo e nossa equipe irá ajudá-lo."
    )

# Comando /promocoes
async def promocoes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎁 Promoções Ativas:\n\n- Bônus de boas-vindas de 100%!\n- Giros grátis toda sexta-feira!\n- Cashback de 10% em perdas semanais.\n\nAproveite agora mesmo em https://bet4brasil.online/home/game"
    )

# Comando /faq
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "❓ Perguntas Frequentes:\n\n1️⃣ Como faço para depositar?\n➡️ Acesse sua conta e clique em 'Depósito'.\n\n2️⃣ Como sacar meus ganhos?\n➡️ Vá até 'Saque' e siga as instruções.\n\n3️⃣ É seguro jogar aqui?\n➡️ Sim! Usamos tecnologia de criptografia avançada para proteger seus dados."
    )

# Resposta padrão para mensagens não reconhecidas
async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Desculpe, não entendi seu pedido. Tente /info, /suporte, /promocoes ou /faq."
    )

# Inicialização do bot
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Definindo comandos
    await app.bot.set_my_commands([
        BotCommand('start', 'Iniciar o bot'),
        BotCommand('info', 'Informações sobre o cassino'),
        BotCommand('suporte', 'Obter suporte'),
        BotCommand('promocoes', 'Ver promoções ativas'),
        BotCommand('faq', 'Perguntas frequentes')
    ])

    # Adicionando handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('info', info))
    app.add_handler(CommandHandler('suporte', suporte))
    app.add_handler(CommandHandler('promocoes', promocoes))
    app.add_handler(CommandHandler('faq', faq))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))

    print("Bot iniciado...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
