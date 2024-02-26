import time
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import UserInvalidError
import config
import asyncio
from telethon.tl.types import Channel
from colorama import Fore, Style
import csv
import os
import sys

client = TelegramClient(
    "silly_",
    api_id=config.TELEGRAM_API_ID,
    api_hash=config.TELEGRAM_API_HASH
)


client.start()


async def get_channels():

    try:
        dialogs = await client.get_dialogs()
        filtered_channels = [obj for obj in dialogs if isinstance(obj.entity, Channel)]
        channels = []
        for channel in filtered_channels:
            channels.append(channel)
        return channels

    except Exception as e:
        print(e)


async def scrape_channels():
    channels = await get_channels()
    for index, channel in enumerate(channels):
        print(Fore.RED, index, end=" - ")
        print(Fore.BLUE, channel.name)
    print(Fore.RED, 99, Fore.RED, "Main Menu")
    print(Style.RESET_ALL)
    channel_index = int(input("Select the number of the channel : "))
    if channel_index == 99:
        clear_terminal()
        await main()
    try:
        print(Fore.BLUE, channels[channel_index].name, Fore.GREEN, "Selected")
        channel = channels[channel_index]
        participants = await client.get_participants(channel)

        with open(f"users/{channel.name}_users.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['User ID', 'Username', 'First Name', 'Last Name'])
            for user in participants:
                writer.writerow([user.id, user.username, user.first_name, user.last_name])

        print(Fore.RED, f"Saved users to users/{channel.name}_users.csv")

        clear_terminal()

        await main()

    except Exception as e:
        print(e)


async def send_messages():
    clear_terminal()
    files = os.listdir("users")
    if not files:
        print(Fore.RED, "Please Scrape the users first")
        print(Style.RESET_ALL)
        await main()

    for index, file in enumerate(files):
        print(Fore.RED, index, Fore.BLUE, file)
    print(Fore.RED, 99, Fore.RED, "Main Menu")

    print(Style.RESET_ALL)

    file_index = int(input("Please Select a File : "))
    if file_index == 99:
        clear_terminal()
        await main()
    try:
        file = files[file_index]
        print(Fore.BLUE, file, Fore.GREEN, "Selected")
        print(Style.RESET_ALL)
        clear_terminal()

        message = input("Please Enter a message to send : ")

        with open(f"users/{file}", "r", newline="", encoding="utf-8") as users:
            reader = csv.reader(users)
            next(reader)
            clear_terminal()
            for row in reader:
                user_id, _, _, _ = row

                try:
                    await client.send_message(int(user_id), message)
                    print(Fore.YELLOW, f"Message sent to {user_id}")
                    time.sleep(config.sleep_time)

                except UserInvalidError:
                    print(f"Error Sending the message to {user_id}. User Likely a bot")

            print(Fore.RED, "Finished Sending Messages")

    except Exception as e:
        print(e)
    finally:
        await main()


async def main():
    print(Fore.RED, 1, Fore.BLUE, "Scrape Users")
    print(Fore.RED, 2, Fore.BLUE, "Send Messages")
    print(Fore.RED, 0, Fore.RED, "Exit")
    print(Style.RESET_ALL)

    answer = int(input("Select an option : "))
    clear_terminal()
    if answer == 1:
        await scrape_channels()
    elif answer == 2:
        await send_messages()
    elif answer == 0:
        sys.exit()
    else:
        print(Fore.RED, "Invalid Selection")


def clear_terminal():
    # Clear the terminal screen
    if os.name == 'posix':  # For Unix/Linux/MacOS
        _ = os.system('clear')
    elif os.name == 'nt':   # For Windows
        _ = os.system('cls')


if __name__ == '__main__':
    print(Fore.RED, """
    Check config.py For Settings. 
    The Default Sleep Time Is 5 Seconds. 
    Increase It If You have a Large Number Of Messages To Send""")
    print(Style.RESET_ALL)

    asyncio.get_event_loop().run_until_complete(main())





