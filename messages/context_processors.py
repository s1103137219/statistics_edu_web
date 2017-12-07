from django.contrib.messages.api import get_messages


def messages(request):
    """Remove duplicate messages

    """
    messages = []
    unique_messages = []
    for m in get_messages(request):
        if m.message not in messages:
            messages.append(m.message)
            unique_messages.append(m)

    return {'messages': unique_messages}