import boto3
import time

client = boto3.client('sns')

def _publish(region: str, account: str, topic: str, msg: str) -> None:
    "publish a message to sns"
    client.publish(TopicArn=f'arn:aws:sns:{region}:{account}:{topic}', Message=msg)

def publish(ctx, topic, msg) -> None:
    "publish a message to sns"
    region, account = determine_region_and_account(ctx)
    delay(1)
    _publish(region, account, topic, msg)

def delay(x: int) -> None:
    "sleep for x seconds, to slow down the game a little"
    time.sleep(x)

def determine_region_and_account(arn: str) -> (str, str):
    "returns the region and account from a given arn"
    xs = arn.split(':')
    return xs[3], xs[4]

def dump_context(ctx) -> None:
    "Logs the lambda context"
    print(
        f"""
        function_name: {ctx.function_name}
        function_version: {ctx.function_version}
        invoked_function_arn: {ctx.invoked_function_arn}
        memory_limit_in_mb: {ctx. memory_limit_in_mb}
        aws_request_id: {ctx.aws_request_id}
        log_group_name: {ctx.log_group_name}
        log_stream_name: {ctx.log_stream_name}
        identity: {ctx.identity}
        """)

