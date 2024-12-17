from typing import Literal

from cookit.pyd import field_validator
from nonebot import get_plugin_config
from nonebot_plugin_picstatus.templates.pw_render import resolve_file_url
from pydantic import BaseModel


class ConfigModel(BaseModel):
    ps_zhenxun_additional_css: list[str] = []
    ps_zhenxun_additional_script: list[str] = []
    ps_zhenxun_pic_format: Literal["jpeg", "png"] = "jpeg"

    @field_validator("ps_zhenxun_additional_css", "ps_zhenxun_additional_script")
    def resolve_script_url(cls, v: list[str]):  # noqa: N805
        return [resolve_file_url(x) for x in v]


config: ConfigModel = get_plugin_config(ConfigModel)
