from .jrrp_command import JrrpCommand
from .dnd_command import UtilsDNDCommand
from .coc_command import UtilsCOCCommand
from .statistics_cmd import StatisticsCommand

# 防止无log情况下无法运行
try:
    from .log_command import LogCommand
except:
    print("Log系统未安装，已取消加载。")

from .test_command import NewTestCommand