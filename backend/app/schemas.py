"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ProjectEntry(BaseModel):
    """展会项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 展会名称
    field_2: str | None = None  # 主办单位
    field_3: str | None = None  # 展馆名称
    field_4: str | None = None  # 展出日期
    field_5: str | None = None  # 展位总数
    field_6: str | None = None  # 项目负责人
    field_7: str | None = None  # 项目状态

class BoothEntry(BaseModel):
    """展位明细结构。"""

    field_0: str | None = None  # 展位编号
    field_1: str | None = None  # 所属展会
    field_2: str | None = None  # 展馆区域
    field_3: str | None = None  # 展位面积
    field_4: str | None = None  # 展位类型
    field_5: str | None = None  # 参展单位
    field_6: str | None = None  # 分配人员
    field_7: str | None = None  # 展位状态

class ExhibitorEntry(BaseModel):
    """参展单位明细结构。"""

    field_0: str | None = None  # 单位编码
    field_1: str | None = None  # 单位名称
    field_2: str | None = None  # 单位类型
    field_3: str | None = None  # 联系人
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 参展面积
    field_6: str | None = None  # 展位数量
    field_7: str | None = None  # 单位状态

class DesignEntry(BaseModel):
    """设计图纸明细结构。"""

    field_0: str | None = None  # 图纸编号
    field_1: str | None = None  # 所属展位
    field_2: str | None = None  # 设计单位
    field_3: str | None = None  # 图纸版本
    field_4: str | None = None  # 提交日期
    field_5: str | None = None  # 审核人员
    field_6: str | None = None  # 审核意见
    field_7: str | None = None  # 图纸状态

class ConstructionEntry(BaseModel):
    """施工任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 所属展位
    field_2: str | None = None  # 承建单位
    field_3: str | None = None  # 施工内容
    field_4: str | None = None  # 进场日期
    field_5: str | None = None  # 完工日期
    field_6: str | None = None  # 现场负责人
    field_7: str | None = None  # 施工状态

class MaterialEntry(BaseModel):
    """租赁单明细结构。"""

    field_0: str | None = None  # 租赁单号
    field_1: str | None = None  # 展具名称
    field_2: str | None = None  # 展具规格
    field_3: str | None = None  # 租赁数量
    field_4: str | None = None  # 租用单位
    field_5: str | None = None  # 起租日期
    field_6: str | None = None  # 归还日期
    field_7: str | None = None  # 租赁状态

class PowerEntry(BaseModel):
    """用电申请单明细结构。"""

    field_0: str | None = None  # 申请单号
    field_1: str | None = None  # 所属展位
    field_2: str | None = None  # 用电容量
    field_3: str | None = None  # 用电设备
    field_4: str | None = None  # 申报人员
    field_5: str | None = None  # 接线方式
    field_6: str | None = None  # 审批日期
    field_7: str | None = None  # 申请状态

class FireEntry(BaseModel):
    """消防验收单明细结构。"""

    field_0: str | None = None  # 验收单号
    field_1: str | None = None  # 所属展位
    field_2: str | None = None  # 检查项目
    field_3: str | None = None  # 灭火器材
    field_4: str | None = None  # 疏散通道
    field_5: str | None = None  # 检查人员
    field_6: str | None = None  # 验收日期
    field_7: str | None = None  # 验收状态

class SafetyEntry(BaseModel):
    """安全巡查明细结构。"""

    field_0: str | None = None  # 巡查编号
    field_1: str | None = None  # 巡查区域
    field_2: str | None = None  # 巡查事项
    field_3: str | None = None  # 违规情形
    field_4: str | None = None  # 巡查人员
    field_5: str | None = None  # 巡查日期
    field_6: str | None = None  # 整改期限
    field_7: str | None = None  # 巡查状态

class SecurityEntry(BaseModel):
    """通行证件明细结构。"""

    field_0: str | None = None  # 证件编号
    field_1: str | None = None  # 持证人员
    field_2: str | None = None  # 所属单位
    field_3: str | None = None  # 通行区域
    field_4: str | None = None  # 有效期至
    field_5: str | None = None  # 发证人员
    field_6: str | None = None  # 发证日期
    field_7: str | None = None  # 证件状态

class LogisticsEntry(BaseModel):
    """运输任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 所属展位
    field_2: str | None = None  # 展品件数
    field_3: str | None = None  # 运输方式
    field_4: str | None = None  # 进场时段
    field_5: str | None = None  # 运输车辆
    field_6: str | None = None  # 押运人员
    field_7: str | None = None  # 运输状态

class CleaningEntry(BaseModel):
    """清运任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 所属展位
    field_2: str | None = None  # 清运内容
    field_3: str | None = None  # 垃圾量
    field_4: str | None = None  # 清运车辆
    field_5: str | None = None  # 作业班组
    field_6: str | None = None  # 完成时刻
    field_7: str | None = None  # 清运状态

class ScheduleEntry(BaseModel):
    """排期计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 所属展会
    field_2: str | None = None  # 施工阶段
    field_3: str | None = None  # 计划时段
    field_4: str | None = None  # 涉及区域
    field_5: str | None = None  # 编排人员
    field_6: str | None = None  # 计划日期
    field_7: str | None = None  # 计划状态

class FeeEntry(BaseModel):
    """收费单明细结构。"""

    field_0: str | None = None  # 收费单号
    field_1: str | None = None  # 参展单位
    field_2: str | None = None  # 收费项目
    field_3: str | None = None  # 计费面积
    field_4: str | None = None  # 应收金额
    field_5: str | None = None  # 已收金额
    field_6: str | None = None  # 开票状态
    field_7: str | None = None  # 收费状态

class ContractorEntry(BaseModel):
    """承建单位明细结构。"""

    field_0: str | None = None  # 单位编码
    field_1: str | None = None  # 单位名称
    field_2: str | None = None  # 资质等级
    field_3: str | None = None  # 联系人
    field_4: str | None = None  # 联系电话
    field_5: str | None = None  # 安全责任人
    field_6: str | None = None  # 合作年限
    field_7: str | None = None  # 单位状态

class ComplaintEntry(BaseModel):
    """投诉记录明细结构。"""

    field_0: str | None = None  # 投诉编号
    field_1: str | None = None  # 投诉单位
    field_2: str | None = None  # 投诉事由
    field_3: str | None = None  # 涉及展位
    field_4: str | None = None  # 受理人员
    field_5: str | None = None  # 处理措施
    field_6: str | None = None  # 处理期限
    field_7: str | None = None  # 投诉状态

class SettlementEntry(BaseModel):
    """结算单明细结构。"""

    field_0: str | None = None  # 结算单号
    field_1: str | None = None  # 参展单位
    field_2: str | None = None  # 结算周期
    field_3: str | None = None  # 结算项数
    field_4: str | None = None  # 应付金额
    field_5: str | None = None  # 已付金额
    field_6: str | None = None  # 审核人员
    field_7: str | None = None  # 结算状态

class ReviewEntry(BaseModel):
    """复盘记录明细结构。"""

    field_0: str | None = None  # 复盘编号
    field_1: str | None = None  # 所属展会
    field_2: str | None = None  # 复盘维度
    field_3: str | None = None  # 观众人数
    field_4: str | None = None  # 成交意向
    field_5: str | None = None  # 复盘人员
    field_6: str | None = None  # 复盘日期
    field_7: str | None = None  # 复盘状态
