if __package__ == 'lambdas':
    from lambdas.common import *
else:
    from common import *

def handler(event, ctx):
    print(f'Received event: {event}, sending pong to pong-topic')
    publish(ctx.invoked_function_arn, 'pong-topic', 'pong')

