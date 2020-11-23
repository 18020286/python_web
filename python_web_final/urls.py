from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


from hotel import views
from profiles import views as profiles_views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),
    path('room/', views.SiteRoomView.as_view(), name='room'),
    path('about/', views.about_view, name='about'),

    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', profiles_views.SiteLoginView.as_view(), name='login'),
    path('logout/', profiles_views.SiteLogoutView.as_view(), name='logout'),

    path('profile/', profiles_views.ProfileEditView.as_view(), name='profile'),
    path('register/', profiles_views.SiteRegisterView.as_view(), name='register'),
    path('register/ok/', profiles_views.SiteRegisterOkView.as_view(), name='register_ok'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

