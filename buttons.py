import discord, facts

class GenerateRandomAgain(discord.ui.View):
    @discord.ui.button(label="Generate again!", style=discord.ButtonStyle.primary, emoji="🐕")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message(facts.generateRandomFact(), ephemeral=True)