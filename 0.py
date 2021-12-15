from random import random, randint 
from typing import Any 
from requests import get 
from pagermaid.listener import listener 
from pagermaid.utils import alias_command 
from os import remove, stat_result 
 
 
@listener(is_plugin=True, outgoing=True, command=alias_command("pic"), 
          description="图片接口整合插件\n当参数是'1'时，获取随机东方project图片\n当参数是'2'时，获取随机Pixiv图片\n当参数是'3'时，获取随机二刺猿小姐姐图片\n当参数是'4'时，获取自然风景图片\n当参数是'5'时，获取NSFW色图\n当参数是'6'时，获取随机图片(随到啥未知)\n若不带参数，则从以上随机获取一张图", parameters='<num> 随意内容') 
async def pic(context): 
    status = False 
    filename = "Project" + str(random())[2:] + ".png" 
    if len(context.parameter) == 0: 
        a = str(randint(0,6)) 
    else: 
        a = context.parameter 
    for _ in range (3): 
        try: 
            if a[0] == '1': 
                await context.edit("正在获取东方Project图片") 
                img = get("https://img.paulzzh.com/touhou/random?size=all&site=all") 
            elif a[0] == '2': 
                await context.edit("正在获取Pixiv图片") 
                img = get("https://pximg.rainchan.win/rawimg") 
            elif a[0] == '3': 
                await context.edit("正在获取二刺猿小姐姐图片") 
                img = get("https://api.ixiaowai.cn/api/api.php") 
            elif a[0] == '4': 
                await context.edit("正在获取自然风景图片") 
                img = get("https://api.ixiaowai.cn/gqapi/gqapi.php") 
            elif a[0] == '5': 
                await context.edit("正在获取色图") 
                img = get("https://se.jiba.xyz/api.php") 
            elif a[0] == '6': 
                await context.edit("正在获取随机图片") 
                img = get("https://unsplash.it/1600/900?random") 
            else: 
                status = True 
                await context.edit("呜呜呜~参数不对喔~~~") 
                break 
        except: 
            try: 
                remove(filename) 
            except: 
                pass 
                continue 
        try: 
            if img.status_code == 200: 
                with open(filename, 'wb') as f: 
                    f.write(img.content) 
                    await context.edit("上传中 . . .") 
            if a[0] == '5': 
                await context.client.send_file(context.chat_id,filename,caption="#NSFW 色图警告😈😈") 
                status = True 
                break 
            else: 
                await context.client.send_file(context.chat_id,filename,caption="美图来咯😍😍~~~") 
                status = True 
                break 
        except: 
            await context.edit ("呜呜呜~上传失败了喔~~~") 
    try: 
        remove(filename) 
    except: 
        pass 
    try: 
        await context.delete() 
    except: 
        pass 
    if not status: 
        await context.client.send_message(context.chat_id,"出错了呜呜呜 ~ 试了好多好多次都无法访问到服务器")
