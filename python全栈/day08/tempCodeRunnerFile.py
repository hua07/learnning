cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C46555', '沪B25041']
locals = {'沪': '上海', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南', '京': '北京'}
dic = {}
for car in cars:
    if locals[car.strip()[0]] not in dic:
        dic[locals[car.strip()[0]]] = 1
    else:
        dic[locals[car.strip()[0]]] += 1
print(dic)