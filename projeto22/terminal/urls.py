from django.urls import path
from . import views

app_name="terminal"

urlpatterns=[
	path('',views.viewindex,name="index"),
	path('index/',views.viewindex,name="tindex"),
	# path('taluno/',views.viewtaluno,name="taluno"),
	path('tcadaluno/',views.viewtcadaluno,name="tcadaluno"),
	path('tpedir/',views.viewtpedir,name="tpedir"),
	path('tservidor/',views.viewtservidor,name="tservidor"),
	path('talunos/',views.viewtalunos,name="talunos"),
	path('tnvrefeicao/',views.viewtnvrefeicao,name="tnvrefeicao"),
	path('tall/',views.viewtall,name="tall"),
	path('tcafe/',views.viewtcafe,name="tcafe"),
	path('talmoco/',views.viewtalmoco,name="talmoco"),
	path('tjanta/',views.viewtjanta,name="tjanta"),


	path('defbtncadaluno/',views.defbtncadaluno,name="defbtncadaluno"),
	path('defbtndelaluno/<int:id>',views.defbtndelaluno,name="defbtndelaluno"),
	path('defbtnpedir/',views.defbtnpedir,name="defbtnpedir"),
	path('defbtnencerrarcafe/<int:id>',views.defbtnencerrarcafe,name="defbtnencerrarcafe"),
	path('defbtnencerraralmoco/<int:id>',views.defbtnencerraralmoco,name="defbtnencerraralmoco"),
	path('defbtnencerrarjanta/<int:id>',views.defbtnencerrarjanta,name="defbtnencerrarjanta"),
]
