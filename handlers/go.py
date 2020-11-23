from app import *
from main.functions import Action

keyboard1 = types.InlineKeyboardMarkup(row_width=2)
a = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Dx50 List", use_aliases=True), callback_data="list")
keyboard1.add(a)

keyboard2 = types.InlineKeyboardMarkup(row_width=1)
a = types.InlineKeyboardButton(text=emoji.emojize(":memo: Activate Subscriber", use_aliases=True), callback_data="activate")
b = types.InlineKeyboardButton(text=emoji.emojize(":scroll: Send Advertisement", use_aliases=True), callback_data="ad")
c = types.InlineKeyboardButton(text=emoji.emojize(":memo: Deactivate Subscriber", use_aliases=True), callback_data="deactivate")
keyboard2.add(a,c,b)

keyboard3 = types.InlineKeyboardMarkup(row_width=1)
a = types.InlineKeyboardButton(text=emoji.emojize(":memo: Read Guide", use_aliases=True), callback_data="rules")
keyboard3.add(a)


@bot.message_handler()
def echo(msg):
    """
    Checking The User's Message Within The Licensed Group
    """

    message_format = "Dx50 @instatravel.lifestyle https://www.instagram.com/p/CCk4PN9sz4S/"

    if msg.chat.type == "group" or msg.chat.type == "supergroup":

        #Check the message format
        text = msg.text

        message = text.split(" ")

        if len(message) != 3:
            reply = bot.reply_to(
                msg,
                f"""
Wrong Format! The right format is
{message_format}
                """,
                disable_web_page_preview=True
            )            

        elif len(message[2].strip("/").split("/")) == 5:

            link = message[2]

            username = message[1].strip("@")

            action = Action(username, link)
            
            # action.get_user_id()
            post = action.get_media_id()

            if post is None:
                reply = bot.reply_to(
                    msg,
                    f"This post was not found in {username}'s timeline feed"
                )
            else:
            
                ####CHECK IF USER HAS PERFORMED LIKE ACTIONS
                # action.check_likes()
                # action.check_comments()

                status = action.get_status()

                if status != True:
                    reply = bot.reply_to(
                        msg,
                        emoji.emojize(f":x: {status}", use_aliases=True),
                        reply_markup=keyboard3
                    )
                else:
                    bot.reply_to(
                        msg,
                        emoji.emojize(f"@{msg.from_user.first_name} :heavy_check_mark: Approved", use_aliases=True)
                    )
                    action.add_to_list()

        else:
            reply = bot.reply_to(
                msg,
                f"""
Wrong Format! The right format is
{message_format}
                """,
                disable_web_page_preview=True
            )


    elif msg.chat.type == "private" and msg.text != '/panel':
        
                
        message = """
<b>:bangbang: STOP Liking & Commenting :bangbang:</b>
:raising_hand: Join the Premium Subscribers and post without engaging back or get auto comments every time you post to our pods :raising_hand:
:point_right: Contact admin:
@theonegrow
"""

        reply = bot.reply_to(
            msg,
            emoji.emojize(message, use_aliases=True),
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=keyboard1
        )

    elif msg.chat.type == "private" and msg.text == '/panel':

        if msg.from_user.id == int(ADMIN_ID):

            reply = bot.send_message(
                msg.chat.id,
                f"""
    Welcome Back {msg.from_user.username},
                
        <b>Dx15 Group Administrative Panel.</b>""",
                reply_markup=keyboard2,
                parse_mode=telegram.ParseMode.HTML
            )
        else:
            pass


    else:    
        pass


    try:
        bot.delete_message(msg.chat.id, msg.message_id)
        time.sleep(30)

        bot.delete_message(msg.chat.id, reply.message_id)
    except:
        pass
    



