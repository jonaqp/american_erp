from json import loads

from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import TemplateView

from core import constants as core_constants
from core.mixins import TemplateLoginRequiredMixin
from .forms import BrandForm
from .models import Brand


# Brand
class BrandView(TemplateLoginRequiredMixin, ListView):
    model = Brand
    template_name = 'pages/brand/brand.html'
    context_object_name = "brand_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = "Brand List"
        return context


class BrandListView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/brand/brand_list.html'

    def get(self, request, *args, **kwargs):
        self.brand = Brand.objects.all()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brand_list'] = self.brand
        return context


class BrandCreateView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/brand/brand_list.html'

    def get(self, request, *args, **kwargs):
        self.form_brand = BrandForm(auto_id='id_brand_%s')
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_form_brand = data['form']
        self.form_brand = BrandForm(data=data_form_brand, auto_id='id_brand_%s')
        if self.form_brand.is_valid():
            self.form_brand.save()
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_brand"] = self.form_brand
        return context


class BrandEditView(TemplateLoginRequiredMixin, TemplateView):
    template_name = 'pages/brand/brand_list.html'

    def get(self, request, *args, **kwargs):
        brand = request.GET['brand_id']
        self.brand = Brand.objects.get(pk=brand)
        self.form_brand = BrandForm(
            auto_id='id_brand_%s', instance=self.brand)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        data = loads(request.body.decode('utf-8'))
        data_brand_pk = data['form_pk']
        data_form_brand = data['form']
        self.brand = Brand.objects.get(pk=data_brand_pk)
        self.form_brand = BrandForm(
            data_form_brand, auto_id='id_brand_%s', instance=self.brand)

        if self.form_brand.is_valid():
            self.form_brand.save()
            messages.success(request, core_constants.STATUS_MSG_TAGS['success'])
        else:
            messages.error(request, core_constants.STATUS_MSG_TAGS['error'])
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_brand'] = self.form_brand
        context['form_pk'] = self.brand.id
        context['btn_edit'] = core_constants.CODE_TEXT_EDIT
        return context
