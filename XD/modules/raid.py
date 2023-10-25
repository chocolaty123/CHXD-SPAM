import asyncio
import random
from telethon import events
from config import MK1, MK2, MK3, MK4, MK5 , MK6, MK7, MK8, MK9, MK10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltronX.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID, ALTRON

que = {}


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: ʀᴀɪᴅ\n  » {hl}raid <count> <Username of User>\n  » {hl}raid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(mkraid) == 2:
            message = str(mkraid[1])
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(mkraid[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = b.first_name
                counter = int(mkraid[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@MK1.on(events.NewMessage(incoming=True))
@MK2.on(events.NewMessage(incoming=True))
@MK3.on(events.NewMessage(incoming=True))
@MK4.on(events.NewMessage(incoming=True))
@MK5.on(events.NewMessage(incoming=True))
@MK6.on(events.NewMessage(incoming=True))
@MK7.on(events.NewMessage(incoming=True))
@MK8.on(events.NewMessage(incoming=True))
@MK9.on(events.NewMessage(incoming=True))
@MK10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    await asyncio.sleep(0.1)
    await event.client.send_message(
        entity=event.chat_id,
        message="""{}""".format(random.choice(REPLYRAID)),
        reply_to=event.message.id,
    )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: ʀᴇᴘʟʏʀᴀɪᴅ\n  » {hl}rraid <Username of User>\n  » {hl}rraid <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkrr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 11:
            message = str(mkrr[0])
            a = await e.client.get_entity(message)
            user_id = int(a.id)
            if int(user_id) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ʜᴇʜᴇ.. ᴀʙ ʀᴇᴘʟʏ ᴋʀɴᴇ ᴘʀ ɢᴀᴀʟɪʏᴀ ᴘᴀʀᴇɢɪ !! ✅", parse_mode=None, link_preview=None)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            user_id = int(b.id)
            if int(user_id) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) == OWNER_ID:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ ʙᴀᴀᴘ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(user_id) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                await e.reply("» ᴜғғ.. ᴀʙ ʀᴇᴘʟʏ ᴋʀɴᴇ ᴘʀ ɢᴀᴀʟɪʏᴀ ɴʜɪ ᴘᴀʀᴇɢɪ !! ✅", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def _(e):
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: ᴅʀᴇᴘʟʏʀᴀɪᴅ\n  » {hl}drraid <Username of User>\n  » {hl}drraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        AltX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(e.text) > 12:
            message = str(AltX[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ᴜғғ.. ᴀʙ ʀᴇᴘʟʏ ᴋʀɴᴇ ᴘʀ ɢᴀᴀʟɪʏᴀ ɴʜɪ ᴘᴀʀᴇɢɪ !! ✅", parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            await e.reply("» ᴜғғ.. ᴀʙ ʀᴇᴘʟʏ ᴋʀɴᴇ ᴘʀ ɢᴀᴀʟɪʏᴀ ɴʜɪ ᴘᴀʀᴇɢɪ !! ✅", parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: ᴍʀᴀɪᴅ\n  » {hl}mraid <count> <Username of User>\n  » {hl}mraid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkmr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(mkmr) == 2:
            message = str(mkmr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(mkmr[0])
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(mkmr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: sʀᴀɪᴅ\n  » {hl}sraid <count> <Username of User>\n  » {hl}sraid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        MKsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(MKsr) == 2:
            message = str(MKsr[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(MKsr[0])
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(MKsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(SRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ: ᴄʀᴀɪᴅ\n  » {hl}craid <count> <Username of User>\n  » {hl}craid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        MKsr = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(MKsr) == 2:
            message = str(MKsr[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(MKsr[0])
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(MKsr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(CRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
