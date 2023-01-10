# # Import the resource
# from grafana_cdk import grafana_workspace

# # Create the resource
# workspace = grafana_workspace.Workspace(
#     "my-workspace",
#     name="Dashboard",
# )

# # Output the workspace ID
# output = tf.Output(
#     "workspace_id",
#     value=workspace.id,
#     description="The ID of the Grafana workspace",
# )

# # Add the output to the app
# app.add_output(output)

import cdktf
import grafana_workspace
import grafana_dashboard
import grafana_panel
import grafana_row
import grafana_datasource
import json
import os
import os.path as Path

from cdktf_cdktf_provider_aws import (
    iam_role,
    iam_role_policy_attachment
)

from constructs import Construct

from cdktf import (
    TerraformAsset,
    AssetType,
)
# app = cdktf.App()

class GrafanaWithPermissionsStack(Construct):
    def __init__(self, scope: Construct, id: str, name: str, grafana_workspace: grafana_workspace.Workspace):
        super().__init__(scope, id)

        # CREATE roles

        grafana_iam_role = iam_role.IamRole(
            self,
            "iam_role_grafana",
            name="flight-controller-grafana-role",
            assume_role_policy=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": {
                        "Action": "sts:AssumeRole",
                        "Principal": {
                            "Service": "grafana.amazonaws.com",
                        },
                        "Effect": "Allow",
                        "Sid": "",
                    },
                }
            ),
            inline_policy=[
                iam_role.IamRoleInlinePolicy(
                    name="AllowTimestreamDB",
                    policy=json.dumps({
                        "Version": "2012-10-17",
                        "Statement":
                        {
                            "Action": [
                                "timestream:CancelQuery",
                                "timestream:DescribeDatabase",
                                "timestream:DescribeEndpoints",
                                "timestream:DescribeTable",
                                "timestream:ListDatabases",
                                "timestream:ListMeasures",
                                "timestream:ListTables",
                                "timestream:ListTagsForResource",
                                "timestream:Select",
                                "timestream:SelectValues",
                                "timestream:DescribeScheduledQuery",
                                "timestream:ListScheduledQueries"
                            ],
                            "Resource": "*",
                            "Effect": "Allow",
                        },
                    })
                )
            ]
        )

        iam_role_policy_attachment.IamRolePolicyAttachment(
            self,
            "policy_attachment",
            policy_arn="arn:aws:iam::099267815798:role/aws-service-role/grafana.amazonaws.com/AWSServiceRoleForAmazonGrafana",
            role=grafana_iam_role.name,
        )


        # Create a Grafana workspace
        self.grafana_workspace = grafana_workspace.Workspace(
            self,
            "grafana_flight_control",
            name=name,
            role=grafana_iam_role
        )


# # Create a Grafana workspace
# grafana_workspace = grafana_workspace.Workspace(
#     app, "my-workspace",
#     name="My Workspace",
# )

# # Create a Grafana dashboard
# dashboard = grafana_dashboard.Dashboard(
#     "my-dashboard",
#     title="My Dashboard",
# )

# # Create a Grafana panel
# panel = grafana_panel.Panel(
#     "my-panel",
#     title="My Panel",
#     type="graph",
#     data_source="my-datasource",
#     targets=[
#         {
#             "ref_id": "A",
#             "expr": "sum(rate(request_duration_seconds_count[5m])) by (le)"
#         }
#     ],
# )

# # Create a Grafana row
# row = grafana_row.Row(
#     "my-row",
#     title="My Row",
#     panels=[panel],
# )

# # Create a Grafana data source
# datasource = grafana_datasource.DataSource(
#     "my-datasource",
#     name="My Data Source",
#     type="prometheus",
#     url="http://localhost:9090",
# )

# # Add the dashboard, row, and data source to the workspace
# grafana_workspace.add_resources([dashboard, row, datasource])

# # Synthesize the CDK app
# app.synth()



  



