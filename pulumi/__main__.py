#!/bin/env python3

# import pulumi
# import pulumi_aws as aws

# # Enable AWS Security Hub
# security_hub = aws.securityhub.Account("security-hub")

# # Export the Security Hub ARN
# pulumi.export("security_hub_arn", security_hub.id)

import tb_pulumi
import tb_pulumi.securityhub
import tb_pulumi.guardduty
import tb_pulumi.cfg
# import tb_pulumi.network


# Create a project to aggregate resources. This will allow consistent tagging, resource protection,
# etc. The naming is derived from the currently selected Pulumi project/stack. A configuration file
# called `config.$stack.yaml` is loaded from the current directory. See config.stack.yaml.example.
project = tb_pulumi.ThunderbirdPulumiProject()

# Pull the "resources" config mapping
resources = project.config.get("resources")

# Security Hub Configuration
securityhub_account = resources["tb:securityhub:SecurityHubAccount"]
security_hub_account_opts = securityhub_account["options"]
security_hub_account = tb_pulumi.securityhub.SecurityHubAccount(
    f"{project.name_prefix}",
    project,
)

# GuardDuty Configuration
guardduty_configuration_opts = resources["tb:securityhub:GuardDutyConfiguration"]
guardduty_configuration_features = guardduty_configuration_opts["features"]
guardduty_configuration = tb_pulumi.guardduty.GuardDutyAccount(
    f"{project.name_prefix}",
    project,
    features=guardduty_configuration_features,
    # opts=guardduty_configuration_opts["opts"],
)

# AWS Config Configuration
# aws_config_configuration_opts = resources["tb:securityhub:AWSConfigConfiguration"]
aws_config_account = tb_pulumi.cfg.AwsConfigAccount(
    f"{project.name_prefix}",
    project,
    # opts=aws_config_configuration_opts["opts"],
)
