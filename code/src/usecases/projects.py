from dateutil import parser

from src.entities.projects import (
    ProjectCreated,
    ProjectAssigned,
    ProjectAssignedLeadTime,
    ProjectLeadTime,
    ProjectRequested,
)

def handle_project_assigned(
    project_requested: ProjectRequested, project_assigned: ProjectAssigned
) -> ProjectAssignedLeadTime:
    return ProjectAssignedLeadTime(
        project_requested.payload.project_id,
        (parser.parse(project_assigned.payload.assigned_time) - parser.parse(project_requested.payload.requested_time)).total_seconds(),
    )


def handle_project_created(
    project_requested: ProjectRequested, project_created: ProjectCreated
) -> ProjectLeadTime:
    return ProjectLeadTime(
        project_requested.payload.project_id,
        (parser.parse(project_created.payload.created_time) - parser.parse(project_requested.payload.requested_time)).total_seconds(),
    )
