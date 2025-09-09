# ruff: noqa: E402

from nonebot.plugin import PluginMetadata, inherit_supported_adapters, require

require("nonebot_plugin_picstatus")
require("nonebot_plugin_htmlrender")

from . import __main__ as __main__
from .config import ConfigModel

__version__ = "0.2.0"
__plugin_meta__ = PluginMetadata(
    name="PicStatus Template ZhenXun",
    description="一个衍生自绪山真寻 Bot 的 PicStatus 状态模板",
    usage="一个衍生自绪山真寻 Bot 的 PicStatus 状态模板",
    type="application",
    homepage="https://github.com/lgc-NB2Dev/nonebot-plugin-picstatus-template-zhenxun",
    config=ConfigModel,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_picstatus",
        "nonebot_plugin_htmlrender",
    ),
    extra={"License": "AGPL-3.0-or-later", "Author": "LgCookie"},
)
