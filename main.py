import os
from dotenv import load_dotenv
from github_op import create_issue, cls_issue, get_all_repos
from discord.ext import commands
import discord
from util import is_mkissue, get_issue_info, is_clsissue

load_dotenv()

DISCORD_API_TOKEN =  os.getenv("DISCORD_API_TOKEN")

intents = discord.Intents.default()
intents.members = True # メンバー管理の権限
intents.message_content = True # メッセージの内容を取得する権限


# Botをインスタンス化
bot = commands.Bot(
    command_prefix="!", # $コマンド名　でコマンドを実行できるようになる
    case_insensitive=True, # コマンドの大文字小文字を区別しない ($hello も $Hello も同じ!)
    intents=intents # 権限を設定
)

@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.event
async def on_message(message: discord.Message):

    if message.author.bot: # ボットのメッセージは無視
        return
    
    if is_mkissue(message.content):
        await message.channel.send("issueを作成します")
        issue_info = get_issue_info(message.content)
        issue = create_issue(issue_info)
        print(issue)
        if issue:
            await message.channel.send(f"issueを作成しました")
        else:
            await message.channel.send("issueの作成に失敗しました")

    if is_clsissue(message.content):
        await message.channel.send("issueをクローズします")
        issue_info = get_issue_info(message.content)
        repo_name = issue_info["repository"]
        issue_title = issue_info["title"]
        if cls_issue(repo_name, issue_title):
            await message.channel.send("issueをクローズしました")
        else:
            await message.channel.send("issueのクローズに失敗しました")

    if message.content == "!repos":
        await message.channel.send("リポジトリ一覧を取得します")
        repo_list = get_all_repos()
        if repo_list:
            text = "\n".join(repo_list)
            await message.channel.send(text)
        else:
            await message.channel.send("リポジトリ一覧の取得に失敗しました")


bot.run(DISCORD_API_TOKEN) # Botの起動