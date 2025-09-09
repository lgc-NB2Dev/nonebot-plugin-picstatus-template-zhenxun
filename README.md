<!-- markdownlint-disable MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# NoneBot-Plugin-PicStatus-Template-ZhenXun

_✨ 一个衍生自绪山真寻 Bot 的 PicStatus 状态模板 ✨_

<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/uv">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
</a>
<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/5a3b2aa7-f878-4304-a92c-cbb018c57bed">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/5a3b2aa7-f878-4304-a92c-cbb018c57bed.svg" alt="wakatime">
</a>

<br />

<a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/pyd-v1-or-v2.json" alt="Pydantic Version 1 Or 2" >
</a>
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-picstatus-template-zhenxun.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-picstatus-template-zhenxun">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-picstatus-template-zhenxun.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-picstatus-template-zhenxun">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-picstatus-template-zhenxun" alt="pypi download">
</a>

<br />

<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-picstatus-template-zhenxun:nonebot_plugin_picstatus_template_zhenxun">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-picstatus-template-zhenxun" alt="NoneBot Registry">
</a>
<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-picstatus-template-zhenxun:nonebot_plugin_picstatus_template_zhenxun">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-picstatus-template-zhenxun" alt="Supported Adapters">
</a>

</div>

## 📖 介绍

一个衍生自绪山真寻 Bot 的 PicStatus 状态模板

### 效果图

<details>
  <summary>点击展开</summary>

![example](https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/picstatus/zhenxun/example.jpg)

</details>

## 💿 安装

以下提到的方法 任选**其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-picstatus-template-zhenxun
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-picstatus-template-zhenxun
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-picstatus-template-zhenxun
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-picstatus-template-zhenxun
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-picstatus-template-zhenxun
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_picstatus_template_zhenxun"
]
```

</details>

## 🎉 使用

在 nonebot2 项目的 `.env` 文件中添加如下配置

```properties
PS_TEMPLATE=zhenxun
PS_BG_PROVIDER=zhenxun_banner
PS_BG_PRELOAD_COUNT=1
```

且在加载 PicStatus 插件的同时加载本插件

## ⚙️ 额外配置

在 nonebot2 项目的 `.env` 文件中添加下表中的必填配置

|             配置项             | 必填 | 默认值 |                说明                 |
| :----------------------------: | :--: | :----: | :---------------------------------: |
|  `PS_ZHENXUN_ADDITIONAL_CSS`   |  否  |  `[]`  |   向模板中附加的 CSS 脚本路径列表   |
| `PS_ZHENXUN_ADDITIONAL_SCRIPT` |  否  |  `[]`  |   向模板中附加的 JS 脚本路径列表    |
|    `PS_ZHENXUN_PIC_FORMAT`     |  否  | `jpeg` | 输出的图片格式，可选：`jpeg`、`png` |

## 📞 联系

QQ：3076823485  
Telegram：[@lgc2333](https://t.me/lgc2333)  
吹水群：[168603371](https://qm.qq.com/q/EikuZ5sP4G)  
邮箱：<lgc2333@126.com>

## 💡 鸣谢

### [HibiKier/zhenxun_bot](https://github.com/HibiKier/zhenxun_bot)

- 模板样式来源，真寻酱可爱！

## 💰 赞助

**[赞助我](https://blog.lgc2333.top/donate)**

感谢大家的赞助！你们的赞助将是我继续创作的动力！

## 📝 更新日志

### 0.2.0

- 适配 PicStatus 2.2.0 的 API 变动
