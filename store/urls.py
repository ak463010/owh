from django.urls import path
from .views.index import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.oder import OderView
from store.middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='store'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('oders/', auth_middleware(OderView.as_view()), name='oders'),
]
