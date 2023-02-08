from time import sleep
from behave import given, when, then
from datetime import datetime
import json
import random
import string

import boto3

eventBridge = boto3.client("events")
timeStream = boto3.client("timestream-query")


@given("a resource has been found non compliant")
def found_non_compliant(context):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    response = eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project request Event",
                "Detail": json.dumps(
                    {
                        "event_type": "ResourceFoundNonCompliant",
                        "container_id": "123456789012",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )

    assert response["FailedEntryCount"] == 0


@when("the resource is found compliant")
def found_compliant(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test project create Event",
                "Detail": json.dumps(
                    {
                        "event_type": "ResourceFoundCompliant",
                        "container_id": "123456789012",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@then("the compliance lead time is stored correctly")
def lead_time_stored(context):
    sleep(2)
    result = timeStream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = 'resource_compliance_lead_time'"
    )
    assert len(result["Rows"]) == 1