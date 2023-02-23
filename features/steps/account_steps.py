from time import sleep
from behave import given, when, then
from datetime import datetime
import json
import random
import string
import boto3

from src.entities.accounts import AccountLeadTime

eventBridge = boto3.client("events")
timeStream = boto3.client('timestream-query')


@given("an account has been requested")
def request_account(context):
    context.aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
    requested_time = int(round(datetime.utcnow().timestamp()))

    response = eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test account request Event",
                "Detail": json.dumps(
                    {
                        "event_type": "AccountRequested",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )

    assert response["FailedEntryCount"] == 0



@when("the account has been created")
def assing_account(context):
    sleep(3)
    requested_time = int(round(datetime.utcnow().timestamp()))
    eventBridge.put_events(
        Entries=[
            {
                "Source": "contino.custom",
                "DetailType": "Test account create Event",
                "Detail": json.dumps(
                    {
                        "event_type": "AccountCreated",
                        "aggregate_id": f"{context.aggregate_id}",
                        "time": f"{requested_time}",
                    }
                ),
                "EventBusName": "main_lambda_bus_cdktf",
            }
        ]
    )


@then("the account created lead time is stored correctly")
def lead_time_stored(context):
    sleep(2)
    result = timeStream.query(
        QueryString=f"select * from core_timestream_db.metrics_table where aggregate_id = '{context.aggregate_id}' and measure_name = '{AccountLeadTime.metricType}'"
    )
    assert len(result["Rows"]) == 1