import discord
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY

# Define the bot
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Dictionary to store user progress
user_story_progress = {}

async def generate_story(prompt):
    """Generates a continuation of the story using OpenAI API"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an interactive storytelling AI."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore bot messages

    user_id = str(message.author.id)

    if message.content.lower().startswith("/start_story"):
        genre = message.content.split(" ", 1)[1] if len(message.content.split()) > 1 else "fantasy"
        story_prompt = f"Start a {genre} adventure where the user is the protagonist."
        story = await generate_story(story_prompt)

        user_story_progress[user_id] = story
        await message.channel.send(f"**Your story begins...**\n\n{story}\n\nType your next action!")

    elif user_id in user_story_progress:
        user_choice = message.content
        story_prompt = f"{user_story_progress[user_id]}\n\nUser chooses: {user_choice}\n\nContinue the story."
        next_part = await generate_story(story_prompt)

        user_story_progress[user_id] = next_part
        await message.channel.send(f"{next_part}\n\nWhat happens next?")

client.run(DISCORD_TOKEN)
