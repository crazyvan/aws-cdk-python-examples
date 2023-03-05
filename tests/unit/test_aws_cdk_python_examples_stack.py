import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_python_examples.aws_cdk_python_examples_stack import AwsCdkPythonExamplesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_python_examples/aws_cdk_python_examples_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkPythonExamplesStack(app, "aws-cdk-python-examples")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })