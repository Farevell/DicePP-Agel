"""
命令模板, 复制到新创建的文件里修改
"""

from typing import List, Tuple, Any

import bot_config
from bot_core import Bot
from command.command_config import *
from command.dicepp_command import UserCommandBase, custom_user_command, MessageMetaData
from command.bot_command import BotCommandBase, PrivateMessagePort, GroupMessagePort, BotSendMsgCommand

LOC_TEMP = "template_loc"

CFG_TEMP = "template_config"

# 增加自定义DataChunk
# @custom_data_chunk(identifier="DATA_CHUNK_ID")
# class _(DataChunkBase):
#     def __init__(self):
#         super().__init__()


# 使用之前取消注释掉下面几行
# @custom_user_command(priority=DPP_COMMAND_PRIORITY_DEFAULT)
class HelpCommand(UserCommandBase):
    """
    模板命令, 不要使用
    """

    def __init__(self, bot: Bot):
        super().__init__(bot)
        bot.loc_helper.register_loc_text(LOC_TEMP, "内容", "注释")
        bot.cfg_helper.register_config(CFG_TEMP, "内容", "注释")

    def delay_init(self) -> List[str]:
        return []

    def can_process_msg(self, msg_str: str, meta: MessageMetaData) -> Tuple[bool, bool, Any]:
        should_proc: bool = msg_str.startswith(".xxx")
        should_pass: bool = False
        return should_proc, should_pass, msg_str[4:].strip()

    def process_msg(self, msg_str: str, meta: MessageMetaData, hint: Any) -> List[BotCommandBase]:
        port = GroupMessagePort(meta.group_id) if meta.group_id else PrivateMessagePort(meta.user_id)
        # 解析语句
        arg_str = hint
        feedback: str = ""

        return [BotSendMsgCommand(self.bot.account, feedback, [port])]

    def get_help(self, keyword: str, meta: MessageMetaData) -> str:
        if keyword == "TMP":  # help后的接着的内容
            feedback: str = ""
            return feedback
        return ""

    def get_description(self) -> str:
        return ".help 查看帮助"  # help指令中返回的内容
