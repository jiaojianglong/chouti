from django.shortcuts import render,HttpResponse
from app01 import models
from app01.forms import UsePhone,UseName,InfoFirst,InfoSedond
import json
import os
from django.core import serializers
# Create your views here.
import time
# def addcontent(request):
#     auther = models.User.objects.all().first()
#     f = open('F:/python/python_test/django_chouti/app01/static/css/output.txt').read()
#     datas = json.loads(f)
#     for data in datas:
#         for i in data:
#             models.Massage.objects.create(picture=os.path.join('images/touxiang/',i['img_name']),content=i['content'],href=i['href'],auther=auther,)
#     return HttpResponse('好')
#
# def deletemassage(request):
#     ret = models.Massage.objects.all()
#     for i in ret:
#         i.delete()
#
# def addmassage(request):
#     ret = models.User.objects.all().first()
#     models.Massage.objects.create(content='焦江龙',href='http://www.baidu.com',auther=ret)
#     r = models.Massage.objects.all().first()
#     return render(request,'addmassage.html',{'ret':r})


# def delete(request):
#     ret = models.User.objects.filter(id=request.session.get('id',None)).first()
#     ret.score = 100
#     ret.save()
#     return HttpResponse('成功')

def page(request,page):
    start_num = int(page)*20
    end_num = int(page)*20
    models.Massage.objects.all()[10:30]
    print(int(page))


def ceshi(request):
    return render(request,'ceshi.html')

def add_sicang(request):
    user_id = request.session.get('id')
    id = request.POST['id']
    ret = models.Massage.objects.filter(id=id).values('dianzan','dianzan_user').first()
    num = int(ret['dianzan'])+1
    user = str(ret['dianzan_user']+','+str(user_id))
    models.Massage.objects.filter(id=id).update(dianzan=num)
    models.Massage.objects.filter(id=id).update(dianzan_user=user)
    re = {'sta':'success','num':num,}
    r = json.dumps(re)
    return HttpResponse(r)



def get_content(request):
    id = request.session.get('id',None)
    contents = models.Massage.objects.all()[10:30]
    return render(request,'moban.html',{'data':contents,'id':id})


def fabu(request):
    id = request.session.get('id',None)
    user = models.User.objects.filter(id=id).first()
    contents = models.Massage.objects.filter(auther=user)

    return render(request,'moban.html',{'data':contents,'id':id})


def shezhi(request):
    login = request.session.get('login',False)
    if login:
        id = request.session.get('id',None)
        ret = models.User.objects.filter(id=id).first()
        return render(request,'shezhi.html',{'login':login,'item':ret})

def sicang(request):
    login = request.session.get('login',False)
    if login :
        id = request.session.get('id',None)
        ret = models.User.objects.filter(id=id).first()
        sex = ret.sex
        fabu_count = models.Massage.objects.filter(auther=ret).count()
        return render(request,'sicang.html',{'login':login,'item':ret,'sex':sex,'fabu_count':fabu_count})
    else:
        return HttpResponse('请先登录')




def index(request):
    f = UsePhone()
    p = UseName()
    y = InfoFirst()
    m = InfoSedond()
    login = request.session.get('login',False)
    if login:
        id = request.session.get('id',None)
        ret = models.User.objects.filter(id=id).values().first()
        name = ret['name']
        photo = ret['photo']
        return render(request,'index.html',{'form1':f,'form2':p,'form3':y,'form4':m,'login':login,'name':name,'photo':photo})
    else:
        return render(request,'index.html',{'form1':f,'form2':p,'form3':y,'form4':m,'login':login})


def info1(request):
    phone = request.POST['phone3']
    pwd = request.POST['pwd3']
    try:
        models.Phone.objects.create(phone = phone,pwd = pwd)
        id = models.Phone.objects.values('id').filter(phone=phone).first()
        request.session['id'] = id

    except:
        return HttpResponse('error')
    return HttpResponse('success')

def info2(request):
    name = request.POST['name4']
    sex4 = request.POST['sex4']
    country = request.POST['country4']
    province = request.POST['province4']
    city = request.POST['city4']
    content = request.POST['content4']
    id = request.session.get('id',None)['id']
    ret = models.Phone.objects.filter(id=id).first()
    phone = ret.phone
    pwd = ret.pwd
    models.User.objects.create(name=name,phone=phone,pwd=pwd,sex=sex4,address_country=country,address_city_id=int(city),content=content,)
    return HttpResponse('success')

def denglu1(request):
    phone = request.POST['phone']
    pwd = request.POST['pwd']
    try:
        ret = models.User.objects.filter(phone=phone).values_list('pwd','phone','id').first()
    except:
        return HttpResponse('phone-error')
    if pwd == ret[0]:
        request.session['id'] = ret[2]
        request.session['login'] = True
        return HttpResponse('success')
    else:
        return HttpResponse('pwd-error')


def denglu2(request):
    name = request.POST['name']
    pwd = request.POST['pwd']
    try:
        ret = models.User.objects.filter(name=name).values_list('pwd','name','id').first()
    except:
        return HttpResponse('name-error')
    if pwd == ret[0]:
        request.session['id'] = ret[2]
        request.session['login'] = True
        return HttpResponse('log-success')
    else:
        return HttpResponse('pwd-error')





# models.User.objects.create(name='焦江龙',pwd='447151999',phone=15192609673,address_city_id=32)
#     str1 = '''北京市卫星地图
# 朝阳区　 海淀区　 通州区　 房山区　 丰台区　 昌平区　 大兴区　 顺义区　 西城区　 延庆县　 石景山区　 宣武区　 怀柔区　 崇文区　 密云县　 东城区　 平谷区　 门头沟区　
#
# 广东省卫星地图
# 东莞市　 广州市　 中山市　 深圳市　 惠州市　 江门市　 珠海市　 汕头市　 佛山市　 湛江市　 河源市　 肇庆市　 清远市　 潮州市　 韶关市　 揭阳市　 阳江市　 梅州市　 云浮市　 茂名市　 汕尾市　
#
# 山东省卫星地图
# 济南市　 青岛市　 临沂市　 济宁市　 菏泽市　 烟台市　 淄博市　 泰安市　 潍坊市　 日照市　 威海市　 滨州市　 东营市　 聊城市　 德州市　 莱芜市　 枣庄市　
#
# 江苏省卫星地图
# 苏州市　 徐州市　 盐城市　 无锡市　 南京市　 南通市　 连云港市　 常州市　 镇江市　 扬州市　 淮安市　 泰州市　 宿迁市　
#
# 河南省卫星地图
# 郑州市　 南阳市　 新乡市　 安阳市　 洛阳市　 信阳市　 平顶山市　 周口市　 商丘市　 开封市　 焦作市　 驻马店市　 濮阳市　 三门峡市　 漯河市　 许昌市　 鹤壁市　 济源市　
#
# 上海市卫星地图
# 松江区　 宝山区　 金山区　 嘉定区　 南汇区　 青浦区　 浦东新区　 奉贤区　 徐汇区　 静安区　 闵行区　 黄浦区　 杨浦区　 虹口区　 普陀区　 闸北区　 长宁区　 崇明县　 卢湾区　
#
# 河北省卫星地图
# 石家庄市　 唐山市　 保定市　 邯郸市　 邢台市　 河北区　 沧州市　 秦皇岛市　 张家口市　 衡水市　 廊坊市　 承德市　
#
# 浙江省卫星地图
# 温州市　 宁波市　 杭州市　 台州市　 嘉兴市　 金华市　 湖州市　 绍兴市　 舟山市　 丽水市　 衢州市　
#
# 香港特别行政区卫星地图
#
# 陕西省卫星地图
# 西安市　 咸阳市　 宝鸡市　 汉中市　 渭南市　 安康市　 榆林市　 商洛市　 延安市　 铜川市　
#
# 湖南省卫星地图
# 长沙市　 邵阳市　 常德市　 衡阳市　 株洲市　 湘潭市　 永州市　 岳阳市　 怀化市　 郴州市　 娄底市　 益阳市　 张家界市　 湘西州　
#
# 重庆市卫星地图
# 江北区　 渝北区　 沙坪坝区　 九龙坡区　 万州区　 永川市　 南岸区　 酉阳县　 北碚区　 涪陵区　 秀山县　 巴南区　 渝中区　 石柱县　 忠县　 合川市　 大渡口区　 开县　 长寿区　 荣昌县　 云阳县　 梁平县　 潼南县　 江津市　 彭水县　 綦江县　 璧山县　 黔江区　 大足县　 巫山县　 巫溪县　 垫江县　 丰都县　 武隆县　 万盛区　 铜梁县　 南川市　 奉节县　 双桥区　 城口县　
#
# 福建省卫星地图
# 漳州市　 厦门市　 泉州市　 福州市　 莆田市　 宁德市　 三明市　 南平市　 龙岩市　
#
# 天津市卫星地图
# 和平区　 北辰区　 河北区　 河西区　 西青区　 津南区　 东丽区　 武清区　 宝坻区　 红桥区　 大港区　 汉沽区　 静海县　 塘沽区　 宁河县　 蓟县　 南开区　 河东区　
#
# 云南省卫星地图
# 昆明市　 红河州　 大理州　 文山州　 德宏州　 曲靖市　 昭通市　 楚雄州　 保山市　 玉溪市　 丽江地区　 临沧地区　 思茅地区　 西双版纳州　 怒江州　 迪庆州　
#
# 四川省卫星地图
# 成都市　 绵阳市　 广元市　 达州市　 南充市　 德阳市　 广安市　 阿坝州　 巴中市　 遂宁市　 内江市　 凉山州　 攀枝花市　 乐山市　 自贡市　 泸州市　 雅安市　 宜宾市　 资阳市　 眉山市　 甘孜州　
#
# 广西壮族自治区卫星地图
# 贵港市　 玉林市　 北海市　 南宁市　 柳州市　 桂林市　 梧州市　 钦州市　 来宾市　 河池市　 百色市　 贺州市　 崇左市　 防城港市　
#
# 安徽省卫星地图
# 芜湖市　 合肥市　 六安市　 宿州市　 阜阳市　 安庆市　 马鞍山市　 蚌埠市　 淮北市　 淮南市　 宣城市　 黄山市　 铜陵市　 亳州市　 池州市　 巢湖市　 滁州市　
#
# 海南省卫星地图
# 三亚市　 海口市　 琼海市　 文昌市　 东方市　 昌江县　 陵水县　 乐东县　 保亭县　 五指山市　 澄迈县　 万宁市　 儋州市　 临高县　 白沙县　 定安县　 琼中县　 屯昌县　
#
# 江西省卫星地图
# 南昌市　 赣州市　 上饶市　 吉安市　 九江市　 新余市　 抚州市　 宜春市　 景德镇市　 萍乡市　 鹰潭市　
#
# 湖北省卫星地图
# 武汉市　 宜昌市　 襄樊市　 荆州市　 恩施州　 黄冈市　 孝感市　 十堰市　 咸宁市　 黄石市　 仙桃市　 天门市　 随州市　 荆门市　 潜江市　 鄂州市　 神农架林区　
#
# 山西省卫星地图
# 太原市　 大同市　 运城市　 长治市　 晋城市　 忻州市　 临汾市　 吕梁市　 晋中市　 阳泉市　 朔州市　
#
# 辽宁省卫星地图
# 大连市　 沈阳市　 丹东市　 辽阳市　 葫芦岛市　 锦州市　 朝阳市　 营口市　 鞍山市　 抚顺市　 阜新市　 盘锦市　 本溪市　 铁岭市　
#
# 台湾省卫星地图
# 台北市　 高雄市　 台中市　 新竹市　 基隆市　 台南市　 嘉义市　
#
# 黑龙江卫星地图
# 齐齐哈尔市　 哈尔滨市　 大庆市　 佳木斯市　 双鸭山市　 牡丹江市　 鸡西市　 黑河市　 绥化市　 鹤岗市　 伊春市　 大兴安岭地区　 七台河市　
#
# 内蒙古自治区卫星地图
# 赤峰市　 包头市　 通辽市　 呼和浩特市　 鄂尔多斯市　 乌海市　 呼伦贝尔市　 兴安盟　 巴彦淖尔盟　 乌兰察布盟　 锡林郭勒盟　 阿拉善盟　
#
# 澳门特别行政区卫星地图
#
# 贵州省卫星地图
# 贵阳市　 黔东南州　 黔南州　 遵义市　 黔西南州　 毕节地区　 铜仁地区　 安顺市　 六盘水市　
#
# 甘肃省卫星地图
# 兰州市　 天水市　 庆阳市　 武威市　 酒泉市　 张掖市　 陇南地区　 白银市　 定西地区　 平凉市　 嘉峪关市　 临夏回族自治州　 金昌市　 甘南州　
#
# 青海省卫星地图
# 西宁市　 海西州　 海东地区　 海北州　 果洛州　 玉树州　 黄南藏族自治州　
#
# 新疆维吾尔自治区卫星地图
# 乌鲁木齐市　 伊犁州　 昌吉州　 石河子市　 哈密地区　 阿克苏地区　 巴音郭楞州　 喀什地区　 塔城地区　 克拉玛依市　 和田地区　 阿勒泰州　 吐鲁番地区　 阿拉尔市　 博尔塔拉州　 五家渠市　 克孜勒苏州　 图木舒克市　
#
# 西藏区卫星地图
# 拉萨市　 山南地区　 林芝地区　 日喀则地区　 阿里地区　 昌都地区　 那曲地区　
#
# 吉林省卫星地图
# 吉林市　 长春市　 白山市　 延边州　 白城市　 松原市　 辽源市　 通化市　 四平市　
#
# 宁夏回族自治区卫星地图
# 银川市　 吴忠市　 中卫市　 石嘴山市　 固原市 '''
#     list1 = str1.split('\n\n')
#     n = 0
#     for i in list1:
#         c = i.strip()
#         province1 = c.split('卫星地图')
#         models.Province.objects.create(province=province1[0])
#         n+=1
#         city = province1[1].split(' ')
#         for c in city:
#             ret = c.strip()
#             models.City.objects.create(city=ret,province_id=n)



    # return HttpResponse(list1[10])







# def test(request):
#     # list1 = ['北京市','广东省','山东省','江苏省','河南省','上海市','河北省','浙江省','香港特别行政区','陕西省',
#     #          '湖南省','重庆市','福建省','天津市','云南省','四川省','广西壮族自治区','安徽省','海南省',
#     #         '江西省','湖北省','山西省','辽宁省','台湾省','黑龙江','内蒙古自治区','澳门特别行政区','贵州省','甘肃省',
#     #          '青海省','新疆维吾尔自治区','西藏区','吉林省','宁夏回族自治区',]
#     # for i in list1:
#     #     models.Province.objects.create(province=i)
#     # return HttpResponse('添加成功')
#     #     (1, '北京市')(2, '广东省')(3, '山东省')(4, '江苏省')(5, '河南省')(6, '上海市')(7, '河北省')
#     #     (8, '浙江省')(9, '香港特别行政区')(10, '陕西省')(11, '湖南省')(12, '重庆市')(13, '福建省')
#     #     (14, '天津市')(15, '云南省')(16, '四川省')(17, '广西壮族自治区')(18, '安徽省')(19, '海南省')
#     #     (20, '江西省')(21, '湖北省')(22, '山西省')(23, '辽宁省')(24, '台湾省')(25, '黑龙江')
#     #     (26, '内蒙古自治区')(27, '澳门特别行政区')(28, '贵州省')(29, '甘肃省')(30, '青海省')
#     #     (31, '新疆维吾尔自治区')(32, '西藏区')(33, '吉林省')(34, '宁夏回族自治区')
#
#     # str1 = '银川市　 吴忠市　 中卫市　 石嘴山市　 固原市 '
#     # r = str1.split(' ')
#     # for i in r:
#     #     # models.City.objects.filter(city=i.strip()).delete()
#     #     models.City.objects.create(city=i.strip(),province_id='34')
#     # return HttpResponse('添加成功')
#
#     # ret = models.City.objects.filter(province__province='北京市')
#     # text = []
#     # for i in ret:
#     #     text.append(i.city)
#     # return HttpResponse(text)
#
#     models.User.objects.create(name='焦江龙',phone=15192609673,pwd='447151999')
#     return HttpResponse('ghjghjghj')



