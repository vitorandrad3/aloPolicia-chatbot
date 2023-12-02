def get_slot_value(event, key):

    value = event['interpretations'][0]['intent']['slots'][key]['value']['interpretedValue']
                    
    return value