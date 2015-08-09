from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                        url(r'^$',"blog.views.home", name='inicio'),
                        url(r'^boton_magico$',"blog.views.boton_magico",name='boton_magico'),
                        url(r'^calculadora$',"blog.views.calculadora",name='calculadora'),
                        url(r'^contactos$',"blog.views.contactos",name='contactos'),
                        url(r'^conversor$',"blog.views.conversor",name='conversor'),
                        url(r'^cronometro$',"blog.views.cronometro",name='cronometro'),
                        url(r'^cv$',"blog.views.cv",name='cv'),
                        url(r'^image$',"blog.views.image",name='image'),
                        url(r'^ver_post/(?P<id_post>[0-9]+)/$',"blog.views.verpost",name='verpost'),     
                        url(r'^mensaje/$',"blog.views.mensaje",name='mensaje'),  
)
