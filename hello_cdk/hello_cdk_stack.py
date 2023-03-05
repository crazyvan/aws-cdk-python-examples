import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_lambda as aws_lambda

class HelloCdkStack(cdk.Stack):
    """Create a stack with a single S3 bucket and a lambda"""

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)
        # self.first_bucket = bucket

        first_lambda = aws_lambda.Function(
            self, 'HelloHandler',
            runtime = aws_lambda.Runtime.PYTHON_3_7,
            code = aws_lambda.Code.from_asset('hello_cdk/lambda'),
            handler = 'hello.handler',
        )
        self.first_lambda = first_lambda

