import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

#Don't be a thief 
print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

if __name__ == "__main__":
    #------------------------------------------------------------------------------------------------------
    import threading
    from flask import Flask
    import os
    
    # Your existing bot code goes here...
    
    # Start a fake web server to keep Render happy
    def start_fake_web_server():
        app = Flask(__name__)
    
        @app.route('/')
        def home():
            return 'Bot is running!', 200
    
        port = int(os.environ.get("PORT", 10000))
        app.run(host="0.0.0.0", port=port)
    
    # Run the fake server in a separate thread
    threading.Thread(target=start_fake_web_server).start()
    #------------------------------------------------------------------------------------------------------

    bot.run_until_disconnected()
