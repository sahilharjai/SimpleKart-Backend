from carts.models import Cart
def jwt_response_payload_handler(token, user=None,request=None):
    return {
        'token': token,
        'user': user.first_name,
        'user_id': user.id,
        'username': user.username,
        'reg_complete': user.registration_complete,
        'reg_stage': user.registration_stage,
        'cart_id': Cart.objects.get(user=user).id,
        'cart_count': Cart.objects.get(user=user).items.count(),
        'profile_pic':request.build_absolute_uri(user.profile_pic.url)
    }