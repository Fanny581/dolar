import os
import telebot

bot = telebot.TeleBot('') #anadimos el token

@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def saludo(mensaje):
    bot.reply_to(mensaje, "Hola, soy fanny")
    print("Mandaron saludo")

@bot.message_handler(commands=['Dolar', ]) #definimos el comando
def nombre(mensaje):
    bot.reply_to(mensaje, "el dolar vale 24 lempiras")
    print("Mandaron Dolar")

@bot.message_handler(commands=['Euro', 'age'])
def edad(mensaje):
    bot.reply_to(mensaje, " el euro vale 28 lempiras")
    print("Mandaron edad")

@bot.message_handler(commands=['Oro', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "el precio del oro 43,097 lempiras")
    print("Mandaron oro")

@bot.message_handler(commands=['cafe', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "el precio del cafe es 3503 lempiras")
    print("Mandaron Direccion")

bot.polling()