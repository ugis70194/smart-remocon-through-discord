if __name__ == "__main__":
    import os

    import discord
    from datamodels.Aircon import Aircon, State
    from datamodels.Light import Light
    from dotenv import load_dotenv

    load_dotenv(".env")

    TOKEN = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    light = Light()
    aircon = Aircon()

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        command = message.content.split("_")
        if not (
            command[0] == "light" or command[0] == "aircon" or command[0] == "cleaner"
        ):
            return

        if command[0] == "light":
            if command[1] == "on":
                light.on()
            elif command[1] == "off":
                light.off()
            elif command[1] == "night":
                light.night()
            elif command[1] == "toBright":
                light.toBright()
            elif command[1] == "toDark":
                light.toDark()
            elif command[1] == "toWarm":
                light.toWarm()
            elif command[1] == "toCool":
                light.toCool()
            elif command[1] == "full":
                light.full()
            elif command[1] == "reset":
                light.reset()
        elif command[0] == "aircon":
            if command[1] == "cool":
                aircon.cool()
            elif command[1] == "warm":
                aircon.warm()
            elif command[1] == "off":
                aircon.off()
            elif command[1] == "down":
                if aircon.state == State.COOL:
                    aircon.tempDown_cool()
                elif aircon.state == State.WARM:
                    aircon.tempDown_warm()
            elif command[1] == "up":
                if aircon.state == State.COOL:
                    aircon.tempUp_cool()
                elif aircon.state == State.WARM:
                    aircon.tempUp_warm()

    client.run(TOKEN)
