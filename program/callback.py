"""
Video + Music Stream Telegram Bot
Copyright (c) 2022-present levina=lab <https://github.com/levina-lab>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but without any warranty; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/licenses.html>
"""


from driver.core import me_bot, me_user
from driver.queues import QUEUE
from driver.decorators import check_blacklist
from program.utils.inline import menu_markup, stream_markup

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
@check_blacklist()
async def start_set(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        """
⋆ مرحبا بك ياروحي ⤌⤈
𓆩  {message.from_user.mention()} 𓆪
ꔹ━━━━━ꔹ
⋆ في بوت تشغيل الاغاني في المكالمات •
[𓆩 قناة السورس 𓆪](t.me/BANDA1M)
ꔹ━━━━━ꔹ
⋆ لمعرفة اوامر البوت اضغط على ⤌⤈
[ 𓆩 اوامر التشغيل 𓆪](https://www.youtube.com/@ull)
ꔹ━━━━━ꔹ
⋆ لمعرفة طريقة التفعيل اضغط علي ⤌⤈
[𓆩 طريقة التفعيل 𓆪](https://www.youtube.com/@ull)
ꔹ━━━━━ꔹ
لصنع بوت مثل هذا البوت مجانا ⤌⤈
[𓆩  اضغط هنا 𓆪](https://www.youtube.com/@ull)
ꔹ━━━━━ꔹ
⋆ لمساعدتك تواصل مع المطور •
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("♡اضف البوت الى مجموعتك♡", url=f"https://t.me/{me_bot.username}?startgroup=true")
                ],[
                   InlineKeyboardButton("⋆ مطور البوت •", url=f"https://t.me/{OWNER_USERNAME}")                    
                ],[
                    InlineKeyboardButton("⋆ اوامر التشغيل •", callback_data="command_list"),
                    InlineKeyboardButton("⋆ طريقة التفعيل •", callback_data="user_guide")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
@check_blacklist()
async def guide_set(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""
⋆ ʷᵉˡᶜᵒᵐᵉ ᵗᵒ ᵗʰᵉ ᵃᶻᵃᶻʸ ˢᵒᵘʳᶜᵉ ⤈⤌
⋆ تفضل طريقة تشغيل البوت ⤌⤈
1⤌أولا أضفني الى مجموعتك •
2⤌بعد ذالك قم برفع البوت مشرف •
3⤌بعد ذالك اكتب .تحديث •
4⤌ضيف الحساب المساعد فجررب •
𓆩 @{me_user.username} 𓆪
5⤌او اكتب .انضم لدعوة المساعد •
6⤌اذ لم تستطيع اضافة المساعد او واجهت مشاكل تحدث مع مطور البوت  •
ꔹ━━━━━ꔹ
♚ ملحوظه هامة يجب عليك كتابه نقطه (.)قبل الامر مثلا .تشغيل .ايقاق .تخطي لازم (نقطه(.) قبل الامر 
ꔹ━━━━━ꔹ
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⋆ رجوع •", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
@check_blacklist()
async def commands_set(_, query: CallbackQuery):
    user_id = query.from_user.id
    await query.answer("⋆ قائمة الاوامر •")
    await query.edit_message_text(
        f"""- تابع الازرار في الاسفل ↓

يمديك تشوف كل اوامر البوت عن طريق زر اوامر البوت""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⋆ اوامر التشغيل •", callback_data="user_command"),
                ],[             
                    InlineKeyboardButton("⋆ رجوع •", callback_data="home_start")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
@check_blacklist()
async def user_set(_, query: CallbackQuery):
    await query.answer("⋆ اوامر التشغيل •")
    await query.edit_message_text(
        f"""
⋆ ʷᵉˡᶜᵒᵐᵉ ᵗᵒ ᵗʰᵉ ᵃᶻᵃᶻʸ ˢᵒᵘʳᶜᵉ ⤈⤌
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪
| - اوامر تشغيل البوت في الجروبات والقنوات  •
| - الاوامر تعمل بشرط استخدام (نقطه(.) قبل الامر •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪
⋆ ╖ .شغل - بالرد على ملف صوتي 
⋆ ╢ .اصعد - لصعود الحساب للمكالمه
⋆ ╢ .انزل - لنزول المساعد من المكالمة
⋆ ╢ .تخطي - لتخطي اغنية في التشغيل
⋆ ╢ .ايقاف - لايقاف تشغيل جميع الاغاني
⋆ ╢ .اضبط - لضبط صوت حساب المساعد
⋆ ╢ .فيديو - بالرد على مقطع فيديو 
⋆ ╢ .الانتضار - لرؤية قائمة الانتضار التشغيل
⋆ ╢ .ابحثلي - لبحث عن فيديو من اليوتيوب
⋆ ╢ .بحث - لتحميل اغنية من اليوتيوب
⋆ ╢ .كتم - لكتم صوت المساعد 
⋆ ╢ .بنك - لإضهار بنك البوت
⋆ ╜ .انضم - لدعوة حساب المساعد
 """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("⋆ رجوع •", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
@check_blacklist()
async def at_set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⋆ هذه الاومر ليست لك ياروحي •", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("⋆ تم فتح لوحة التحكم •")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("⋆ مفيش حاجه شغاله اصلا •", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
@check_blacklist()
async def is_set_home_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⋆ هذه الاومر ليست لك ياروحي •", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
@check_blacklist()
async def on_close_menu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⋆ هذه الاومر ليست لك ياروحي •", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
@check_blacklist()
async def in_close_panel(_, query: CallbackQuery):
    await query.message.delete()
