from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from libraryApp import views

urlpatterns = [
        path('',views.login_fun,name='log'),
        path('logdata',views.logdata_fun),

        path('ajj',views.admin_fun,name='ajj'),
        path('admindata',views.admindata_fun),

        path('student',views.student_fun,name='student'),
        path('studata',views.studata_fun),

        path('adminhome',views.adminhome_fun,name='ahome'),
        path('stuhome',views.stuhome_fun,name='shome'),

        path('addbook',views.addbook_fun),
        path('book',views.book_fun,name='add'),

        path('displaybook',views.display_fun,name='displaybook'),

        path('Update/<int:id>',views.update_fun,name='Updt'),
        path('Delete/<int:id>',views.delete_fun,name='Dele'),


        path('assignbook',views.assignbook_fun,name='assignbook'),
        path('assigndata', views.assigndata_fun),
        path('issueread',views.issueread_fun),


        path('Updateissue/<int:id>',views.updateissue_fun,name='Update'),
        path('Deleteissue/<int:id>',views.delete_issue,name='Delete'),

        path('issuebook', views.issuebook_fun, name='issuebook'),
        path('issuedetail',views.issuedetail_fun,name='issuedetail'),

        path('log_out', views.log_out_fun, name='log_out'),

        path('profile/',views.profile_fun,name='profile'),
        path('updateprof/<int:id>',views.updateprof_fun,name='updateprof')



]



