import discord
import CONFIG

async def ex(args, message, client, invoke):
    msg = "``` --- Help ---\n\n"
    cmd_list = [
            "clear [args/number]",
            "ping",
            "say [args/text]",
            "type [args/text]"
                ]
    for element in cmd_list:
        msg += "    " + CONFIG.PREFIX + element + "\n"
    msg += "\n```"
    await client.delete_message(message)
    #await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description=msg))
    await client.send_message(message.channel, msg)
