from functools import wraps

from django.shortcuts import render
from django.views import generic
from django.http import (JsonResponse, QueryDict)
from django.db.models import (Sum, Max)
from django.views.decorators.csrf import csrf_exempt
from programmers_test.models import (Item, Ingredient, Gender, Category)


def resonpse_in_json(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)
        if str(type(result)) != "<class 'dict'>":
            result = {'result': result,
                'status': 200,
            }
        status = result.get('status', None)
        if status is None:
            status = 200
        return JsonResponse(
            result,
            json_dumps_params={
                'indent': 2, 
                'ensure_ascii': False
                }, 
            status=status,
        )
    return decorated_function

# Create your views here.
def index(request):
    return render(request, 'programmers_test/index.html')

@resonpse_in_json
def error403(request, exception):
    print('\n\n\n custom_forbidden request, exception', request, exception)
    return {'result': u'허용되지 않는 HTTP Request Method입니다.', 'status': 403}

@resonpse_in_json
def error404(request, exception):
    print('\n\n\n custom_page_not_found request&exception', request, exception)
    return {'result': u'그러한 페이지가 없습니다.', 'status': 404}

@resonpse_in_json
def error500(request):
    print('\n\n\n custom_server_error request, exception', request)
    return {'result': u'서버가 잘 모르나 봅니다.', 'status': 500}

class ItemView(generic.View):
    @resonpse_in_json
    def custom_permission_denied(self, requset):
        print('--------------------')
        return {'result': u'허용되지 않는 요청메소드입니다.'}

    def post(self, request, id):
        return self.custom_permission_denied(request)

    def put(self, request, id):
        return self.custom_permission_denied(request)

    def delete(self, request, id):
        return self.custom_permission_denied(request)

    @resonpse_in_json
    def get(self, request, id):
        skin_type_dict = {
            'oily': 'ingredients__oily', 
            'dry': 'ingredients__dry',
            'sensitive': 'ingredients__sensitive'
            }
        skin_type = request.GET.dict().get('skin_type', None)
        if skin_type not in skin_type_dict.keys():
            return {'result': 'Bad Request'}

        try:
            item = Item.objects.get(id=id)
            query_set = Item.objects.filter(category_id=item.category_id)
            query_set = query_set.values('id').annotate(
                    sum=Sum(skin_type_dict.get(skin_type, None)),
                    price=Max('price'),
                    category=Max('category_id'),
                    ).exclude(id=item.id)
            query_set = query_set.order_by('-sum', 'price')
            query_set = query_set[:3]

            recommanded_items = \
                    Item.objects.in_bulk(
                        [q_dict['id'] for q_dict in query_set]
                    )
            recommanded_items = \
                [item.get_json() for item in recommanded_items.values()]

            result = [item.get_json(info_level=2)]
            result.extend(recommanded_items)
            print(item.get_absolute_url())

        except Exception as sqlerr:
            print('\n\n\n ItemView.get().sqlerr >>>>>>> ', sqlerr)
            print('-------')
            print(item.get_absolute_url())
            result = {'msg': u'해당하는 상품이 없습니다. ' + str(sqlerr)}
            
        finally:
            return result

class ItemListView(generic.View):
    @resonpse_in_json
    def custom_permission_denied(self, requset):
        return JsonResponse({'result': u'허용되지 않는 요청메소드입니다.'}, status=403)

    def post(self, request, id):
        return self.custom_permission_denied(request)

    def put(self, request, id):
        return self.custom_permission_denied(request)

    def delete(self, request, id):
        return self.custom_permission_denied(request)

    def get_items_with_ingredients(self, ingredients_list):
        result = set()
        query_set= Item.ingredients.through.objects.values('item_id')

        for index, ingredeint_name in enumerate(ingredients_list):
            query_result = query_set.filter(ingredient__name=ingredeint_name)

            if index == 0:
                result.update([query['item_id'] for query in query_result])

            else:
                sub_set = set([query['item_id'] for query in query_result])
                result &= sub_set

        return result

    @resonpse_in_json
    def get(self, request):
        skin_type_dict = {
            'oily': 'ingredients__oily', 
            'dry': 'ingredients__dry',
            'sensitive': 'ingredients__sensitive',
        }
        required_query_parameter_list = ['skin_type', 'category']
        request_dictionary = request.GET.dict()

        try:
            for required_query_parameter in required_query_parameter_list:
                if required_query_parameter not in request_dictionary.keys():
                    raise Exception
    
            query_set = Item.objects.values().filter(
            category__category=request_dictionary.get('category', None)
            )

            query_set = query_set.values('id').annotate(
                    sum=Sum(
                        skin_type_dict.get(
                            request_dictionary.get('skin_type', None),
                            None
                            )
                        ),
                    price=Max('price'),
                    category=Max('category_id'),
                    )
            print('\n\n\n vvvv >>>>> ', str(query_set.query), query_set)

            try:
                include_ingredient = request_dictionary.get(
                    'include_ingredient', None
                )
                include_ingredient_id_set = set()
                if include_ingredient is not None:
                    include_ingredient = include_ingredient.split(',')
                    include_ingredient_id_set.update(
                        self.get_items_with_ingredients(include_ingredient)
                    )
                
                exclude_ingredient = request_dictionary.get(
                    'exclude_ingredient', None
                )
                exclude_ingredient_id_set = set()

                if exclude_ingredient is not None:
                    exclude_ingredient = exclude_ingredient.split(',')
                    exclude_ingredient_id_set.update(
                        self.get_items_with_ingredients(exclude_ingredient)
                    )
                    include_ingredient_id_set &= exclude_ingredient_id_set

                if len(include_ingredient_id_set) != 0:
                    query_set = query_set.filter(
                        id__in=include_ingredient_id_set
                    )
                
                query_set = query_set.order_by('-sum', 'price')
                page = int(request_dictionary.get('page', 0))
                query_set = query_set[50 * (page): 50 * (1 + page)]

                print('\n\n\n query_setquery_setquery_set >>>>> ', query_set, query_set.count())
                rrr = [q_dict['id'] for q_dict in query_set]
                print('\n\n\n rrrrrrrrrrrrrrrrrr ', rrr)
                result = Item.objects.in_bulk(
                    [q_dict['id'] for q_dict in query_set]
                )
                print('\n\n\n resultresultresult >>>>> ', result)
                result = [item.get_json(1) for item in result.values()]

                if len(result) == 0:
                    result = {'msg': u'해당하는 상품이 없습니다.'}

            except Exception as sqlerr:
                print('\n\n\n ItemListView.get().sqlerr >>>>>>> ', sqlerr)
                result = {'msg': u'해당하는 상품이 없습니다. ' + str(sqlerr)}

        except Exception as sqlerr:
            print('\n\n\n ItemListView.get().sqlerr >>>>>>> ', sqlerr)
            result = {'msg': u'잘못된 요청입니다. 상품의 카테고리나 피부타입을 지정해주세요.'}

        finally:
            return result