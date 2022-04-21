import os 
import discord
from discord.ext import commands, tasks
import os
import discord
from discord.ext import commands, tasks
import random
import configparser
import time
from datetime import date
from datetime import datetime
import sys
import requests
import uuid
import shutil
import glob
import time 
from dotenv import load_dotenv
load_dotenv()

TOAKEN=os.getenv('discord_key')

dirname = os.path.join(os.path.dirname(__file__))

UPLOAD_PATH = os.path.join(dirname,'yolov5\\runs\\detect')
print(UPLOAD_PATH)
UNCHECKED_PATH = os.path.join(dirname,'datasets\\Endangered-Animals-1\\test\\images')


def main():
    client = commands.Bot(command_prefix='!')
    message = "Yolov5 Bot Sequence Activated"
    @client.event
    async def on_ready():
        print('Bot is ready !')
        channel = client.get_channel(931292221335023743)
        await channel.send(message)
        
    @client.event
    async def on_message(message_ctx):
        # print(message_ctx)
        # print(message_ctx.content)

        if message_ctx.content.lower() == '!usage':
            usage_string = '!result : display result \n!nanodetect : execute Yolo \n!smalldetect : execute Yolo \n!upload : - include image files <3 \n\!clear_result : clear both unchecked_picture and result '
            await message_ctx.channel.send(usage_string)

        if message_ctx.content.lower() == "!result" :

            for root, dirs, files in os.walk(UPLOAD_PATH):
                for file in files:
                    if file.endswith('.jpg') :
                        img_path = os.path.join(root, file)
                        print(img_path)
                        with open(img_path,'rb') as f :
                            pic = discord.File(f)
                            await message_ctx.channel.send(file=pic)

        if message_ctx.content.lower()== '!upload' :
            try :
                url = message_ctx.attachments[0].url
            except IndexError:
                print('Error: No attachments ')
                await message_ctx.channel.send('Error ! no attachment :( ')
            else :
                if url[0:26] == "https://cdn.discordapp.com":
                    r = requests.get(url,stream = True)
                    imageName = str(uuid.uuid4()) + '.jpg'
                    try :
                        with open(imageName, 'wb') as out_file:
                            print('Saving image ' + imageName)
                            shutil.copyfileobj(r.raw, out_file)

                            saving_message_string = 'Images successfully saved to unchecked folder !\nRun \n!smalldetect or !nanodetect to analyze'
                            await message_ctx.channel.send(saving_message_string)
                        shutil.move(os.path.join(dirname,imageName),os.path.join(UNCHECKED_PATH,imageName))
                    except :
                        await message_ctx.channel.send("something went wrong :( ")
        
        if message_ctx.content.lower() == '!nanodetect' :
            await message_ctx.channel.send("YOLO nano is working it's magic ...... ! ")
            await message_ctx.channel.send("It could take maybe like a few minutes !")
            os.chdir(os.path.join(dirname,'yolov5'))
            start = time.time()
            
            os.system('python yolomango.py nano')
            end = time.time()
            elaspe = end - start 
            await message_ctx.channel.send('It took me %0.2f seconds ! ' % elaspe)
            await message_ctx.channel.send('Done ! use the reuslt command to see the images !')
            os.chdir('../')
        
        if message_ctx.content.lower() == '!smalldetect' :
            await message_ctx.channel.send("YOLO nano is working it's magic ...... ! ")
            await message_ctx.channel.send("It could take maybe like a few minutes !")
            os.chdir(os.path.join(dirname,'yolov5'))
            start = time.time()
            
            os.system('python yolomango.py small')
            end = time.time()
            elaspe = end - start 
            await message_ctx.channel.send('It took me %0.2f seconds ! ' % elaspe)
            await message_ctx.channel.send('Done ! use the reuslt command to see the images !')
            os.chdir('../')

        if message_ctx.content.lower() == '!clear_result' :
            if message_ctx.author.name != 'dukebao':
                await message_ctx.channel.send("your trial period has ended, please consider to subscribe Yolov5 premium service")
                await message_ctx.channel.send(f'paypal me $5 https://paypal.me/dukebao?country.x=CA&locale.x=en_US to activate your premium service ')
            else :
                await message_ctx.channel.send("Deleting result directory ...")
                for file in os.listdir(UPLOAD_PATH):
  
                    shutil.rmtree(os.path.join(UPLOAD_PATH,file))
                for file in os.listdir(UNCHECKED_PATH):

                    os.remove(os.path.join(UNCHECKED_PATH,file))
                
                await message_ctx.channel.send("Done !")
        if message_ctx.content.lower() == '!where' :
            current_dir = os.getcwd()
            await message_ctx.channel.send(current_dir)
    client.run(TOAKEN)

if __name__ =="__main__":
    main()