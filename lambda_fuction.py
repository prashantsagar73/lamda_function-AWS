def lambda_handler(event, context):
    print('This is lambda function!')
    if event['fruits'] == 'apple':
        return 'yes it is'
    elif event['fruits'] == 'pen':
        return 'This is not a fruits'
    else: 
        return 'we do not recognize your argument'