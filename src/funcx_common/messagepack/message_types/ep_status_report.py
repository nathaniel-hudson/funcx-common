from __future__ import annotations

import typing as t
import uuid
from dataclasses import dataclass

from ..common import Message


@dataclass
class EPStatusReport(Message):
    """
    Status report for an endpoint, sent from Endpoint to Forwarder.

    Includes EP-wide info such as utilization, as well as per-task status information.
    """

    message_type = "ep_status_report"
    endpoint_id: str | uuid.UUID
    ep_status_report: t.Dict[str, t.Any]
    task_statuses: t.Dict[str, t.Any]
