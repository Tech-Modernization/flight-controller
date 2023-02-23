from dataclasses import dataclass
from typing import Literal

from .base import BaseEvent, BaseMetric


@dataclass
class ResourceFoundNonCompliantPayload:
    container_id: str
    timestamp: float


@dataclass
class ResourceFoundNonCompliant(BaseEvent):
    payload: ResourceFoundNonCompliantPayload
    eventType: Literal["ResourceFoundNonCompliant"] = "ResourceFoundNonCompliant"


@dataclass
class ResourceFoundCompliantPayload:
    container_id: str
    timestamp: float


@dataclass
class ResourceFoundCompliant(BaseEvent):
    payload: ResourceFoundCompliantPayload
    eventType: Literal["ResourceFoundCompliant"] = "ResourceFoundCompliant"


@dataclass
class ResourceComplianceLeadTime(BaseMetric):
    lead_time: float
    metricType: Literal["ResourceComplianceLeadTime"] = "ResourceComplianceLeadTime"
