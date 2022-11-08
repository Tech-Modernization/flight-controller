import random
import string
from datetime import datetime
from dateutil import parser
from uuid import uuid4

from src.adapters.controller import handle_event
from src.entities.projects import (
    ProjectCreated,
    ProjectAssigned,
    ProjectCreatedPayload,
    ProjectRequested,
    ProjectRequestedPayload,
    ProjectLeadTime,
    ProjectAssignedLeadTime
)

correlation_id = "".join(random.choices(string.ascii_letters, k=12))

project_requested_payload = {
    "correlation_id": correlation_id,
    "time": datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
    "event_type": "ProjectRequested",
}

project_assigned_payload = {
    "correlation_id": correlation_id,
    "time": datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
    "event_type": "ProjectAssigned",
}

project_created_payload = {
    "correlation_id": correlation_id,
    "time": datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
    "event_type": "ProjectCreated",
}


def test_project_requested_returns_no_metrics():
    assert (
        handle_event(
            project_requested_payload,
            [],
        )[1]
        == []
    )


def test_project_requested_returns_correct_event():
    assert isinstance(
        handle_event(
            project_requested_payload,
            [],
        )[0],
        ProjectRequested,
    )


def test_project_created_returns_correct_event():
    requested_event = ProjectRequested(
        correlation_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )
    assert isinstance(
        handle_event(
            project_created_payload,
            [requested_event],
        )[0],
        ProjectCreated,
    )

def test_project_assigned_returns_correct_event():
    requested_event = ProjectRequested(
        correlation_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )
    assert isinstance(
        handle_event(
            project_assigned_payload,
            [requested_event],
        )[0],
        ProjectAssigned,
    )


def test_project_created_returns_lead_time():
    requested_event = ProjectRequested(
        correlation_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )
    assert handle_event(project_created_payload, [requested_event])[1] == [
        ProjectLeadTime(
            correlation_id,
            0
        )
    ]

def test_project_assigned_returns_lead_time():
    requested_event = ProjectRequested(
        correlation_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )
    assert handle_event(project_assigned_payload, [requested_event])[1] == [
        ProjectAssignedLeadTime(
            correlation_id,
            0
        )
    ]

def test_project_assigned_returns_lead_time_with_multiple_aggregates():
    requested_event = ProjectRequested(
        correlation_id,
        "Project",
        1,
        uuid4(),
        1,
        ProjectRequestedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )

    created_event = ProjectCreated(
        correlation_id,
        "Project",
        2,
        uuid4(),
        1,
        ProjectCreatedPayload(correlation_id, datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")),
    )
    assert handle_event(project_assigned_payload, [created_event,requested_event])[1] == [
        ProjectAssignedLeadTime(
            correlation_id,
            0
        )
    ]

def test_project_created_handles_no_project_requested():
    assert isinstance(handle_event(project_created_payload, [])[0], ProjectCreated)

def test_project_assigned_handles_no_project_requested():
    assert isinstance(handle_event(project_assigned_payload, [])[0], ProjectAssigned)


def test_project_created_returns_no_metric_with_no_project_requested():
    assert handle_event(project_created_payload, [])[1] == []

def test_project_assigned_returns_no_metric_with_no_project_requested():
    assert handle_event(project_assigned_payload, [])[1] == []

def test_project_assigned_returns_no_metric_with_no_project_requested():
    assert handle_event(project_assigned_payload, [])[1] == []


def test_project_handles_unknown_event():
    assert isinstance(
        handle_event(
            {
                "requested_time": 1659656680.789246,
                "correlation_id": "the-armitagency",
                "event_type": "NotAnEvent",
            },
            [],
        ),
        Exception,
    )


def test_project_handles_malformed_event():
    assert isinstance(
        handle_event(
            {
                "requested_time": 1659656680.789246,
                "correlation_id": "the-armitagency",
            },
            [],
        ),
        Exception,
    )
