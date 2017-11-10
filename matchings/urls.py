from django.conf.urls import url
from matchings import views

urlpatterns = [
	url(r'^$', views.datashow.as_view(), name='datashow'),
	
	url(r'^match_disease/$', views.match_disease, name='match_disease'),
	url(r'^match_disease/search_prescription/$', views.search_prescription, name='search_prescription'),
	url(r'^match_disease/search_disease/$', views.search_disease, name='search_disease'),

	url(r'^model_comparison/', views.ModelCompareFormView.as_view(), name='models_test'),

	url(r'^m4876_00/$', views.m4876_00.as_view(), name='m4876_00'),
	url(r'^m4876_01/$', views.m4876_01.as_view(), name='m4876_01'),
]
