if __package__ == 'lambdas':
    from lambdas.common import *
else:
    from common import *

started = False


def handler(event, ctx) -> None:
    global started
    if event.get('detail-type'):
        if not started:
            print('Starting ping-pong')
            started = True
            publish(ctx.invoked_function_arn, 'ping-topic', 'ping')
        else:
            print('Already started ping-pong')
    else:
        print(f'Received: {event}, sending ping to ping-topic')
        publish(ctx.invoked_function_arn, 'ping-topic', 'ping')

