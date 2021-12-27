class Constants:
    HELP_MESSAGE = (
        f"\n\nThis bot will send you a random memory at every midday from your memory vault."
        f"\n- You can join my system by writing, *join* or */join*"
        f"\n- You leave my system by, *leave*"
        f"\n- You can get a random memory by, *send*"
        f"\n- You can get your status information by, *status*"
        f"\n- You can list memories by, *list*"
        f"\n- You delete a memory with command, *delete id*. You can get the memory id with the command, *list*"
        f"\n*Example*:"
        f"\n*delete 2*"
        f"\n- You can add memories to your memory vault with command,  *add Sentence*"
        f"\n*Example*:"
        f"\n*add Time does not come back*"
        f"\n\n- You can set your timezone with command, *gmt timezone*. Default timezone is GMT0."
        f"\n*Examples*:"
        f"\nGMT+3: *gmt 3*"
        f"\nGMT0: *gmt 0*"
        f"\nGMT-5: *gmt -5*"
        f"\n\nYou can use me in groups as well, just can add me to the group and make me admin. Also you can have multiple memory vaults by using groups."
    )
    BROADCAST_CHAT_ID = -1001786782026

    @staticmethod
    def start_message(name: str = "") -> str:
        return (
            f"Welcome onboard {name} "
            f"\nThis bot stores your memories in the memory vault and sends a random memory every midday."
            f"\n\nKeeping note of beautiful & important stuff that we come across throughout the life and remembering those memories is quite challenging. "
            f"\nThis bot solves this problem with a very simple "
            f"approach, as complex methods makes it harder to keep it them in our life."
            f"\nSincerely thanks to my wife Seyyide for the beautiful idea."
            f"\n\n- You can join my system by writing, *join*. "
            f"\n- You can get more detailed information by writing, *help*."
        )
