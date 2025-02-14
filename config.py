from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "12986357"))
API_HASH = getenv("API_HASH", "94160b9fb6b79b005ffd23d358fe2392")
BOT_TOKEN = getenv("BOT_TOKEN", "5548381739:AAGZ7VbILBzFAWqlImlD0RiZPrswuiEbWzw")
SESSION_NAME = getenv("SESSION_NAME", "AgCbDbiWolWCUIqhOzrD7L7ZCwWihsfRShd2GFwoykn6afqpwOTXELTNSHSgwJTVJzfjg1PKl66xAIdL0AsEpMtKO1lU4tPQiDTRiP6YCWUf9NG2sXRutqo12lXDIffET5uJuI_iwvf7Dl1NFG0PZFqHJ8zak6ygMXt31JkIVKCPEVZu2vSwWpUvP3Mk9ud8fa-CZf29g8Ez45wUAlMrFYBJjTdtNdewWWcRhl47piSiw9fHQKDOovktVf6iSKqPAq2U5oUI9EQBQLYDt9M5mhctHn5ArcJsEpN5iSxFmQvGtD4jNPSwvIZY0vHsm83z8o13rKaxKQEB4_xYiIxCTtUEeQosDQA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "alazizy")
ALIVE_NAME = getenv("ALIVE_NAME", "sonng")
BOT_USERNAME = getenv("BOT_USERNAME", "hsjsbsssjdhdbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rr8r9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1183747742").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1183747742").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
