__author__ = 'jx-pc'


class Urls(object):
    ALL_API = 'http://gank.io/api/data/all/{0}/{1}'
    FRONT_API = 'https://gank.io/api/data/\u524d\u7aef/{0}/{1}'
    FULI_API = 'https://gank.io/api/data/\u798f\u5229/{0}/{1}'
    XIATUIJIAN_API = 'https://gank.io/api/data/\u778e\u63a8\u8350/{0}/{1}'
    VIDEO_API = 'https://gank.io/api/data/\u4f11\u606f\u89c6\u9891/'
    APP_API = 'https://gank.io/api/data/App/{0}/{1}'
    ANDROID_API = 'https://gank.io/api/data/Android/{0}/{1}'
    IOS_API = 'http://gank.io/api/data/iOS/{0}/{1}'
    IMAGE_API = 'http://img.gank.io/6ade6383-bc8e-40e4-9919-605901ad0ca5?imageView2/0/w/1001'

    # 每日数据：
    DAY_API = 'http://gank.io/api/day/{0}/{1}/{2}'
#    RANDOM_API = 'http://gank.io/api/random/data/分类/个数'
    SEARCH_API = 'http://gank.io/api/search/query/listview/category/Android/count/10/page/1'

    # 获取某几日干货网站数据:
    LATEST_API = 'http://gank.io/api/history/content/2/1'

    # 获取特定日期网站数据:
    ONE_DATE_API = 'http://gank.io/api/history/content/day/2016/05/11'

    # 获取发过干货日期接口:
    DATE_API = 'http://gank.io/api/day/history'

    # 搜索电影：
    MOVIE_API = 'http://www.omdbapi.com/?t={0}&y={1}&plot={2}&r=xml'

    @staticmethod
    def get_all(count, page):
        return Urls.ALL_API.format(str(count), str(page))

    @staticmethod
    def get_android_all(count, page):
        return Urls.ANDROID_API.format(str(count), str(page))

    @staticmethod
    def get_ios_all(count, page):
        return Urls.IOS_API.format(str(count), str(page))

    @staticmethod
    def get_front_all(count, page):
        return Urls.FRONT_API.format(str(count), str(page))

    @staticmethod
    def get_app_all(count, page):
        return Urls.APP_API.format(str(count), str(page))

    @staticmethod
    def get_xiatuijian_all(count, page):
        return Urls.XIATUIJIAN_API.format(str(count), str(page))

    @staticmethod
    def get_day_ganks(year, month, day):
        return Urls.DAY_API.format(year, month, day)

    @staticmethod
    def get_date_all():
        return Urls.DATE_API

    @staticmethod
    def get_movie(title, year, plot):
        return Urls.MOVIE_API.format(title, year, plot)
