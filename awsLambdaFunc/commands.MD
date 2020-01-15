 
 ```
 aws lambda create-function --function-name  CreateTableAddRecordsAndRead --runtime python3.8 \
--zip-file fileb://app.zip --handler app.handler \
--role arn:aws:iam::127503254852:role/lambda-vpc-role \
--vpc-config SubnetIds=subnet-3ff41662,SecurityGroupIds=sg-0501236ade10d905d
```
 
 Returns:
 aws lambda create-function --function-name  CreateTableAddRecordsAndRead --runtime python3.8 --zip-file fileb://app.zip --handler app.handler --role arn:aws:iam::<iam_id>:role/lambda-vpc-role --vpc-config SubnetIds=<in: https://us-west-2.console.aws.amazon.com/vpc/home?region=us-west-2#dashboard:>,SecurityGroupIds=<in: https://us-west-2.console.aws.amazon.com/vpc/home?region=us-west-2#dashboard:>
{
    "FunctionName": "CreateTableAddRecordsAndRead",
    "FunctionArn": "arn:aws:lambda:us-west-2:<iam_id>function:CreateTableAddRecordsAndRead",
    "Runtime": "python3.8",
    "Role": "arn:aws:iam::<iam_id>:role/lambda-vpc-role",
    "Handler": "app.handler",
    "CodeSize": 24213124,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": "2020-01-15T18:20:38.323+0000",
    "CodeSha256": "xqTDhRik/UlNh4pNCOMtOq8JSG3Xx0BKTwIZ6GYZy8E=",
    "Version": "$LATEST",
    "VpcConfig": {
        "SubnetIds": [
            "<in: https://us-west-2.console.aws.amazon.com/vpc/home?region=us-west-2#dashboard:>"
        ],
        "SecurityGroupIds": [
            "<in: https://us-west-2.console.aws.amazon.com/vpc/home?region=us-west-2#dashboard:>"
        ],
        "VpcId": "vpc-6281071a"
    },
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "558f2794-7333-4a65-b468-3a0e78ab6f33",
    "State": "Active",
    "LastUpdateStatus": "Successful"
}
