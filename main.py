import discord, buttons, facts, keep_alive

bot = discord.Bot('Get random fun facts of dogs or cats!')

betaTesterServers = [1004514844319428608, 937444366505615390, 1007408288675143761]

@bot.event
async def on_ready():
    print("I'm ready!")

@bot.command(description="Get a random fact of dogs or cats!")
async def fact(ctx):
    await ctx.respond(facts.generateRandomFact(), view=buttons.GenerateRandomAgain(), ephemeral=False)

keep_alive.keep_alive()
bot.run('MTA0MDY5NzY2NDAyODgwMzEzMw.GGPqZY.D2FbNfwLnr102exKDTR0oJpUUKI3dBrNyVYl5I')