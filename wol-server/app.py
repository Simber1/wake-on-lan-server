from litestar.response import Template
from litestar import Litestar, get
from pathlib import Path
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
import wakeonlan


@get("/")
async def index() -> Template:
    wakeonlan.send_magic_packet('08:BF:B8:12:EE:CE')
    return Template(template_name="index.html.jinja2")

template_config = TemplateConfig(directory=Path("templates"), engine=JinjaTemplateEngine)
app = Litestar([index], template_config=template_config)
print("Server running!")
