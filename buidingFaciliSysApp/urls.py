from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name=''),
    path('log_in', views.log_in, name='login'),
    path('logout', views.logout, name='logout'),
    path('public_reg', views.public_reg, name='public_reg'),
    path('admin_add_moderator', views.admin_add_moderator, name='admin_add_moderator'),

    path('admin_home', views.admin_home, name='admin_home'),
    path('block_moderator', views.block_moderator, name='block_moderator'),
    path('unblock_moderator', views.unblock_moderator, name='unblock_moderator'),
    path('admin_add_products', views.admin_add_products, name='admin_add_products'),
    path('admin_update_product', views.admin_update_product, name='admin_update_product'),
    path('admin_vw_reports', views.admin_vw_reports, name='admin_vw_reports'),
    path('public_vw_products', views.public_vw_products, name='public_vw_products'),
    path('public_vw_cart', views.public_vw_cart, name='public_vw_cart'),
    path('public_add_cart', views.public_add_cart, name='public_add_cart'),
    path('public_update_rofile', views.public_update_rofile, name='public_update_rofile'),
    path('public_change_password', views.public_change_password, name='public_change_password'),
    path('public_checkout', views.public_checkout, name='public_checkout'),
    path('public_vw_history', views.public_vw_history, name='public_vw_history'),
    path('fetch_cart_items', views.fetch_cart_items, name='fetch_cart_items'),
    path('public_view_bill', views.public_view_bill, name='public_view_bill'),
    path('public_enquire', views.public_enquire, name='public_enquire'),
    path('moderator_vw_enquires', views.moderator_vw_enquires, name='moderator_vw_enquires'),
    path('moderator_reply_enquires', views.moderator_reply_enquires, name='moderator_reply_enquires'),
    path('delete_product', views.delete_product, name='delete_product'),
    path('contractor_home', views.contractor_home, name='contractor_home'),
    path('worker_home', views.worker_home, name='worker_home'),
    path('public_home', views.public_home, name='public_home'),
    path('public_remove_cart', views.public_remove_cart, name='public_remove_cart'),

    path('admin_vw_public', views.admin_vw_public, name='admin_vw_public'),
    path('admin_vw_contractors', views.admin_vw_contractors, name='admin_vw_contractors'),
    path('admin_vw_workers', views.admin_vw_workers, name='admin_vw_workers'),
    path('admin_approve', views.admin_approve, name='admin_approve'),
    path('admin_reject', views.admin_reject, name='admin_reject'),
    path('admin_vw_contractor_reviews', views.admin_vw_contractor_reviews, name='admin_vw_contractor_reviews'),
    
    path('contractor_vw_workers', views.contractor_vw_workers, name='contractor_vw_workers'),
    path('contractor_vw_requests', views.contractor_vw_requests, name='contractor_vw_requests'),
    path('contractor_approve', views.contractor_approve, name='contractor_approve'),
    path('Contractor_vw_requests_more', views.Contractor_vw_requests_more, name='Contractor_vw_requests_more'),
    path('contractor_allocate_worker', views.contractor_allocate_worker, name='contractor_allocate_worker'),
    path('contractor_vw_worker_works', views.contractor_vw_worker_works, name='contractor_vw_worker_works'),
    path('contractor_pay_worker', views.contractor_pay_worker, name='contractor_pay_worker'),
    path('contractor_vw_debits', views.contractor_vw_debits, name='contractor_vw_debits'),
    path('contractor_vw_credits', views.contractor_vw_credits, name='contractor_vw_credits'),

    path('public_vw_contractors', views.public_vw_contractors, name='public_vw_contractors'),
    path('public_vw_contractor_more', views.public_vw_contractor_more, name='public_vw_contractor_more'),
    path('public_vw_my_requests', views.public_vw_my_requests, name='public_vw_my_requests'),
    path('public_vw_req_more', views.public_vw_req_more, name='public_vw_req_more'),
    path('public_pay_contractor', views.public_pay_contractor, name='public_pay_contractor'),
    path('public_vw_my_payments', views.public_vw_my_payments, name='public_vw_my_payments'),

    path('worker_vw_works', views.worker_vw_works, name='worker_vw_works'),
    path('worker_mark_completed', views.worker_mark_completed, name='worker_mark_completed'),
    path('worker_vw_payments', views.worker_vw_payments, name='worker_vw_payments'),
]