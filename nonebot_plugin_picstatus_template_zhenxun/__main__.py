from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any

import jinja2 as jj
from cookit.pw.router import make_real_path_router
from nonebot import get_loaded_plugins
from nonebot.matcher import current_bot
from nonebot_plugin_htmlrender import get_new_page
from nonebot_plugin_picstatus.bg_provider import BgBytesData, BgFileData, bg_provider
from nonebot_plugin_picstatus.collectors import first_time_collector, normal_collector
from nonebot_plugin_picstatus.collectors.bot import get_bot_status
from nonebot_plugin_picstatus.templates import pic_template
from nonebot_plugin_picstatus.templates.pw_render import (
    ROUTE_URL,
    add_background_router,
    add_root_router,
    base_router_group,
    register_global_filter_to,
)
from nonebot_plugin_picstatus.util import debug

from .config import config

if TYPE_CHECKING:
    from yarl import URL

RES_DIR = Path(__file__).parent / "res"


@bg_provider()
async def zhenxun_banner(num: int):
    for _ in range(num):
        yield BgFileData(
            path=RES_DIR / "top.jpg",
            mime="image/jpeg",
        )


@normal_collector("current_bot")
async def current_bot_collector():
    now_time = datetime.now().astimezone()
    return await get_bot_status(current_bot.get(), now_time)


@normal_collector()
async def zhenxun_version():
    path = Path.cwd() / "__version__"
    if not path.is_file():
        return None
    return path.read_text().strip().split(":")[-1]


@normal_collector()
async def plugin_count():
    return len(get_loaded_plugins())


@first_time_collector()
async def template_version():
    from . import __version__

    return __version__


template_env = jj.Environment(
    loader=jj.FileSystemLoader(RES_DIR),
    autoescape=True,
    enable_async=True,
)
register_global_filter_to(template_env)


template_router_group = base_router_group.copy()


@template_router_group.router(f"{ROUTE_URL}/res/**/*", priority=99)
@make_real_path_router
async def _(url: "URL", **_):
    return RES_DIR.joinpath(*url.parts[2:])


@pic_template(
    collecting={
        "current_bot",
        "network_connection",
        "cpu_percent",
        "cpu_freq",
        "cpu_count",
        "memory_stat",
        "swap_stat",
        "disk_usage",
        "cpu_brand",
        "system_name",
        "zhenxun_version",
        "python_version",
        "nonebot_version",
        "plugin_count",
        "ps_version",
        "template_version",
        "time",
    },
)
async def zhenxun(collected: dict[str, Any], bg: "BgBytesData", **_):
    template = template_env.get_template("index.html.jinja")
    html = await template.render_async(d=collected, config=config)

    if debug.enabled:
        debug.write(html, "{time}.html")

    router_group = template_router_group.copy()
    add_root_router(router_group, html)
    add_background_router(router_group, bg)

    async with get_new_page() as page:
        await router_group.apply(page)
        await page.goto(f"{ROUTE_URL}/", wait_until="load")
        elem = await page.wait_for_selector("div.wrapper")
        assert elem
        return await elem.screenshot(type=config.ps_zhenxun_pic_format)
