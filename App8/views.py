from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic.base import View
from App8.forms import ProductForm
from App8.models import ProductModel
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


def view_all_products(request):
    all = ProductModel.objects.all()
    data = {}
    for x in all:
        d1 = {x.pno: {'product_name': x.pname, 'product_price': x.price, 'product_quantity': x.quantity}}
        data.update(d1)
    json_data = json.dumps(data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')


def view_one_product(request, one):
    try:
        res = ProductModel.objects.get(pno=one)
        d1 = {
            'product_no': res.pno,
            'product_name': res.pname,
            'product_price': res.price,
            'product_quantity': res.quantity
        }
        json_data = json.dumps(d1)
    except ProductModel.DoesNotExist:
        message = {'error': 'Searching Product is not Avil'}
        json_data = json.dumps(message)
    return HttpResponse(json_data, content_type='application/json')


class View_All_Products(View):
    def get(self, request):
        all = ProductModel.objects.all()
        json_data = serialize('json', all)
        # data=json.dumps(json_data)
        return HttpResponse(json_data, content_type='application/json')
        # return HttpResponse(data,content_type='application/data')


class View_One_Product(View):
    def get(self, request, one):
        try:
            res = ProductModel.objects.get(pno=one)
            data = serialize('json', [res])
        except ProductModel.DoesNotExist:
            message = {'error': 'Product Not Avaliable'}
            data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class InsertOneProduct(View):
    def post(self, request):
        # data = io.BytesIO(request.body)
        data = request.body
        print(data)
        x = json.loads(data)
        print(x)
        pf = ProductForm(x)
        if pf.is_valid():
            pf.save()
            msg = json.dumps({'success': 'Product is Saved'})
        else:
            msg = json.dumps(pf.errors)
        return HttpResponse(msg, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class InsertMultipleProducts(View):
    def post(self, request):
        data = request.body
        json_data = json.loads(data)
        # print(json_data)
        for x, y in json_data.items():
            pf = ProductForm(y)
            print(x)
            print(y)

            if pf.is_valid():
                pf.save()

            msg = json.dumps({'success': 'DATA SAVED'})
            return HttpResponse(msg, content_type='application/json')
        else:
            msg = json.dumps({'error': 'DATA NOT SAVED'})
            return HttpResponse(msg, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class UpdateProduct(View):
    def put(self, request, product):
        try:
            new_product = json.loads(request.body)
            old_product = ProductModel.objects.get(pno=product)
            print(old_product)
            pf = ProductForm(new_product, instance=old_product)
            print(pf)
            if pf.is_valid():
                pf.save()
                msg = json.dumps({'success': 'Product is Updated'})
            else:
                msg = json.dumps(pf.errors)
            return HttpResponse(msg, content_type='application/json')
        except ProductModel.DoesNotExist:
            msg = json.dumps({'exception': 'Invalid Product Details'})
            return HttpResponse(msg, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class DeleteProduct(View):
    def delete(self, request, product):
        try:
            res = ProductModel.objects.filter(pno=product).delete()
            if res[0] == 1:
                msg = json.dumps({'success': 'Product is Deleted'})
            else:
                msg = json.dumps({'error': 'Invalid Product No'})
            return HttpResponse(msg, content_type='application/json')
        except ProductModel.DoesNotExist:
            msg = json.dumps({'exception': 'Invalid Product Details'})
            return HttpResponse(msg, content_type='application/json')
