"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import project as router_project
from app.routers import booth as router_booth
from app.routers import exhibitor as router_exhibitor
from app.routers import design as router_design
from app.routers import construction as router_construction
from app.routers import material as router_material
from app.routers import power as router_power
from app.routers import fire as router_fire
from app.routers import safety as router_safety
from app.routers import security as router_security
from app.routers import logistics as router_logistics
from app.routers import cleaning as router_cleaning
from app.routers import schedule as router_schedule
from app.routers import fee as router_fee
from app.routers import contractor as router_contractor
from app.routers import complaint as router_complaint
from app.routers import settlement as router_settlement
from app.routers import review as router_review

ROUTERS = [router_project, router_booth, router_exhibitor, router_design, router_construction, router_material, router_power, router_fire, router_safety, router_security, router_logistics, router_cleaning, router_schedule, router_fee, router_contractor, router_complaint, router_settlement, router_review]
