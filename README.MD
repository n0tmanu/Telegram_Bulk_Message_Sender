## Use This Script Responsibly. If You'll Use This To Spam And Get banned, It's On You.

### What does it do?
It basically has two functionalities

 - Scrape users from channels you have joined
 - Send messages to every user you have scraped 

### Initialization

[Download Python](https://www.python.org/downloads/)


First Install the requirements using
    
    pip install -r requirements.txt

Now you are going to need the API ID and API Hash for your telegram application. You can get it [Here](https://my.telegram.org)

Look into [this](https://core.telegram.org/api/obtaining_api_id) tutorial by telegram for more info about acquiring the api id and hash 

 - Once you have the API access, paste the ID and the Hash in config.py
 - Also write the message you want to send in config.py

### Usage

Running the script is pretty straight forward. Assuming you have python installed already, Run

    python main.py

The script is pretty self-explanatory. The Users you scrape from channels will be stored in a csv file named <_channel_name_>_users.csv inside the users directory.

#### You Must Scrape the Users Before Sending Messages

### Avoiding Telegram's Flood Restrictions

To avoid getting your account limited by telegram, I have added a wait between every message. You can adjust it in config.py

To make it more natural, the sleep time will be randomized every time. 

The default wait time is 5 - 10 seconds but the more you can wait, lesser the risk of getting your account banned


