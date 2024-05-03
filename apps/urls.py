from django.urls import path
from apps.views import ListPage, Register, LoginView

urlpatterns = [
    path('login', LoginView.as_view(
        template_name='apps/login/login.html',
        next_page='list_page',
        redirect_authenticated_user=True),
        name='login_page'),
    path('register', Register.as_view(), name='register_page'),
    path('list', ListPage.as_view(), name='list_page'),
    # path('detail/<int:pk>', ProductdetailView, name='detail_view'),
]

# from django.conf.urls.i18n import i18n_patterns
# from django.core.mail import send_mail
# from django.http import HttpResponse
# from django.urls import path
#
# from apps.views import BlogDetailDetailView, LoginView
# from root import settings
# from . import views


# def send_email_to_user(request):
#     email = request.GET.get('email')
#     send_mail('Hello', 'Hello', settings.EMAIL_HOST_USER, [email])
#     return HttpResponse('sucessfully send')


# urlpatterns =[
#     # path('', BlogTemplateView.as_view(), name='blog_page'),
#     path('details/<uuid:pk>', BlogDetailDetailView.as_view(), name='blog_detail'),
#     path('send-email', send_email_to_user)
# ]

# ------------- email verification ---------
# urlpatterns += [
#     path('signup/', views.signup, name='signup'),
#     path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
#     path('activate/<uidb64>/<token>/', views.activate, name='activate'),
#     path('account_activation_complete/', views.account_activation_complete, name='account_activation_complete'),
#     path('accounts/login/', LoginView.as_view(), name='login'),  # Add this line for login
# ]
# -------------------------------------------------------------------------------

# { % if page_obj.has_previous %}
# < li
#
#
# class ="page-item" > < a href="?page={{ page_obj.previous_page_number }}"
#
#
# class ="page-link" > << < / a > < / li >
#
#
# { % endif %}
# { %
# for num in page_obj.paginator.page_range %}
# { % if page_obj.number == num %}
# < li
#
#
# class ="page-item" > < a href="?page={{ num }}"
#
#
# style = "background-color: aqua; color: red;"
#
#
# class ="page-link" > {{num}} < / a > < / li >
#
#
# { % elif page_obj.number | add: '-3' < num and num < page_obj.number | add:'3' %}
# < li
#
#
# class ="page-item" > < a href="?page={{ num }}" class ="page-link" > {{num}} < / a > < / li >
#
#
# { % endif %}
# { % endfor %}
# { % if page_obj.has_next %}
# < li
#
#
# class ="page-item" > < a href="page={{ page_obj.next_page_number }}" class ="page-link" >> > < / a >
#
# < / li >
# < li
#
#
# class ="?page-item" > < a href="#" class ="page-link" > < i
#
#
# class ="mdi mdi-chevron-right" > < / i > < / a >
#
# < / li >
# { % endif %}