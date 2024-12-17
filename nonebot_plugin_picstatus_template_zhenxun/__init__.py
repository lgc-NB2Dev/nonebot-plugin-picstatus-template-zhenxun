# ruff: noqa: E402

from nonebot.plugin import PluginMetadata, inherit_supported_adapters, require

require("nonebot_plugin_picstatus")
require("nonebot_plugin_htmlrender")

from . import __main__ as __main__
from .config import ConfigModel

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="PicStatus Template ZhenXun",
    description="PicStatus 状态模板，复刻自绪山真寻 Bot",
    usage="一个状态模板",
    type="application",
    homepage="https://github.com/owner/nonebot-plugin-picstatus-template-zhenxun",
    config=ConfigModel,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_picstatus",
        "nonebot_plugin_htmlrender",
    ),
    extra={"License": "MIT", "Author": "student_2333"},
)
