def is_loged(request):
    if not request.user.is_authenticated:
        return False
    return True