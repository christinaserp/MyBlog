from django.conf.urls import url
import blog
from blog import views


urlpatterns = [
    url(r'^$', blog.views.home, name='home'),
    url(r'^about/$', blog.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', blog.views.show_article, name='article'),
    url(r'^register/$', blog.views.RegisterFormView.as_view(), name='registration'),
    url(r'^logout/$', blog.views.logout_view, name='logout'),
    url(r'^login/$', blog.views.LoginFormView.as_view(), name='login'),
    url(r'^add/$', blog.views.AddArticle.as_view(), name='add'),
    url(r'^user/(?P<username>.+)/', blog.views.show_user, name='user'),
    url(r'^tag/(?P<tag>[-\w]+)/$', blog.views.home_by_tag, name='home_by_tag'),
    url(r'^search/$', blog.views.home_by_keyword, name='home_by_keyword'),
    # url(r'^subscribe_success.html$', blog.views.Subscribe.as_view(), name='subscribe'),
    url(r'^users/$', blog.views.show_users, name='users'),
    url(r'^subscribe_success.html$', blog.views.Subscribe.as_view(), name='subscribe'),

    # url(r'^subscribe/$', 'blog.views.subscribe', name='subscribe')
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
