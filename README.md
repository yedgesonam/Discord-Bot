**AI Storyteller Bot**

Welcome to the AI Storyteller Bot! This bot creates interactive and dynamic stories where users can make decisions that shape the plot. It uses OpenAI's GPT-4 to generate storylines, allowing users to become the protagonists in a world of their own creation.

**Features**

Interactive Storytelling: Users start a story and continue it by typing decisions or actions.
Customizable Genres: Choose your preferred genre (e.g., fantasy, sci-fi, adventure) to set the tone of the story.
AI-Generated Narrative: Powered by OpenAI's GPT-4, the bot generates a unique and engaging storyline based on user input.
Single-User Experience: Each user can have their own story running separately from others.

**How It Works**

Start a Story: Type /start_story <genre> to begin your adventure. If no genre is specified, the default genre is fantasy.
Make Decisions: Respond with choices or actions to shape the storyline. Each input from the user will update the story.
Continue the Journey: The bot will generate the next part of the story based on your input, guiding you through your unique adventure.
Requirements
Python 3.9+ (Recommended)
Discord account
OpenAI API key

**Libraries**

discord.py: A Python library to interact with the Discord API.
openai: A Python wrapper for OpenAI's GPT-4 model.
python-dotenv: To manage environment variables securely.
Setup Guide
**1. Create a Discord Bot**

Go to the Discord Developer Portal.
Create a new application and navigate to the Bot section.
Add a bot to the application and copy the Bot Token.
Under the OAuth2 section, select the bot and applications.commands permissions, then copy the generated invite link to invite the bot to your server.
**2. Create OpenAI Account**

Sign up on OpenAI's platform if you haven't already.
Create a new API key from your OpenAI account dashboard.
**3. Install Dependencies**

Ensure Python is installed on your system, then install the required libraries:


pip install discord openai python-dotenv
**4. Set Up Environment Variables**

Create a .env file in the project directory with the following content:


DISCORD_BOT_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
Replace your_discord_bot_token_here and your_openai_api_key_here with the credentials you got in steps 1 and 2.

**5. Run the Bot**

Run the bot by executing:
python bot.py

**Commands**

/start_story <genre>: Start a new story with your chosen genre (e.g., /start_story fantasy).
Your choices: Respond with actions or decisions that will guide the story forward (e.g., "I choose to explore the cave").

**Example Interaction**

User: /start_story fantasy
Bot: Your story begins...
"You're standing at the edge of a dense forest, with the sounds of wildlife echoing in the distance. The path ahead is shrouded in mist. What will you do?"
User: "I decide to step into the forest."
Bot: You step into the forest and immediately feel the temperature drop. A shadowy figure appears in front of you, holding a map. What do you do next?
User: "I ask the figure for directions."
Bot: The figure hands you the map and gestures towards a nearby village...

