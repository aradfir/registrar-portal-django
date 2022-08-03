def add_request_to_context(request):
    context_data = dict()
    context_data['request'] = request
    return context_data
