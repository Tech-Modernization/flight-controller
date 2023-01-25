import cdktf
import json
import os
import os.path as Path

from cdktf_cdktf_provider_aws import (
    iam_role,
    iam_role_policy_attachment,
    grafana_workspace,
    grafana_workspace_api_key,
)

from constructs import Construct

from cdktf import (
    TerraformAsset,
    AssetType,
)

from grafana_api import GrafanaFace

class GrafanaWithPermissionsStack(Construct):
    def __init__(self, scope: Construct, id: str, name: str):
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
            policy_arn="arn:aws:iam::aws:policy/AmazonTimestreamReadOnlyAccess",
            role=grafana_iam_role.name,
        )


        # Create a Grafana workspace
        self.grafana_workspace = grafana_workspace.GrafanaWorkspace(
            self,
            "grafana_flight_control",
            name=name,
            account_access_type="CURRENT_ACCOUNT",
            authentication_providers=["AWS_SSO"],
            permission_type="SERVICE_MANAGED",
            role_arn=grafana_iam_role.arn,
            data_sources=["TIMESTREAM"]
        )

        #Output the workspace ID
        output_grafana_workspace_id=cdktf.TerraformOutput(
            self,
            "workspace_id",
            value=self.grafana_workspace.id
        )


        #Create an API key for the admin role
        self.grafana_workspace_api_key = grafana_workspace_api_key.GrafanaWorkspaceApiKey(
            self,
            "grafana_workspace_api_key",
            key_name="flight-controller-grafana-api-key",
            key_role="ADMIN",
            workspace_id=self.grafana_workspace.id,
            seconds_to_live=86400
            )

        #Output API token for the dashboard role
        output_api_key=cdktf.TerraformOutput(
            self,
            "api_key",
            value=self.grafana_workspace_api_key.key,
        )

        # save_file=cdktf.FileProvisioner

        os.environ["GRAFANA_API_KEY"] = output_api_key.value

        
