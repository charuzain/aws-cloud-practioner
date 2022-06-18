def lambda_handler(event, context):
    message = 'Hello {} {} {}! Keep being awesome!'.format(event['first_name'], event['last_name'],event['textMsg'])  

    #print to CloudWatch logs
    print(message)

    return { 
        'message' : message
    }