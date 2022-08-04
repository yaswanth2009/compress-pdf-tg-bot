from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
            InlineKeyboardButton('Update_Channel', url='t.me/DL_Bots_Update')
'),
            InlineKeyboardButton('Support_group', url='t.me/dl_bots_supports')
        ]
        ]

close = [
        [
            InlineKeyboardButton('Update_Channel', url='t.me/DL_Bots_Update'),
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        ]

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
