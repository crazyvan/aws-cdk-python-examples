#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hello_cdk.hello_cdk_stack import HelloCdkStack


app = cdk.App()

env_eu_west_2 = cdk.Environment(account="194086103172", region="eu-west-2")

HelloCdkStack(app, "HelloCdkStack", env=env_eu_west_2)

app.synth()
