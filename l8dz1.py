with open('dz.txt', 'r', encoding='utf-8') as f:
    def func_cook_book(f): 
        cook_book = {}
        for text in f.read().split('\n\n'):
            name, _, *args = text.split('\n')
            ingridients = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split('|'))
                ingridients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure })                
            cook_book[name] = ingridients
        return cook_book
    print(func_cook_book(f))


with open('dz.txt', 'r', encoding='utf-8') as f:
    def get_shop_list_by_dishes(dishes, person_count):  
        cook_book = {}
        list_by_dishes = {}
        for text in f.read().split('\n\n'):
            name, _, *args = text.split('\n')
            ingridients = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split('|'))   
                ingridients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity) * person_count, 'measure': measure })
            cook_book[name] = ingridients
        for key, value in cook_book.items():
            if key in dishes:
                list_by_dishes[key] = value 
        return list_by_dishes
        # print(cook_book) 
    print(get_shop_list_by_dishes(['Запеченный картофель' , 'Омлет', 'Фахитос'], 4))