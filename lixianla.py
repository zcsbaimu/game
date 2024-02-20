# coding=utf-8
from DrissionPage import WebPage
import os
import ddddocr
def qiandao():
    try:
        ocr = ddddocr.DdddOcr()
        login_url = 'https://lixianla.com/user-login.htm'
        if os.path.exists('imgs/code.jpg'):
            os.remove('imgs/code.jpg')
        if os.path.exists('imgs/code2.jpg'):
            os.remove('imgs/code2.jpg')
        page = WebPage()
        page.set.headers({
            "authority": "lixianla.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "sec-ch-ua": "^\\^Not",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        })
        page.set.cookies('bbs_sid=a3glgk4f4v6t04ha3e6i2q2t5m')
        page.get(login_url)
        page.ele('#email').input('3276605184@qq.com')
        page.ele('#password').input('syq20010615')

        image_url = page.ele('.vcode').attr('src')
        print(image_url)
        page.download(image_url, r'.\imgs', rename='code', verify=False)
        os.rename('imgs/code.htm', 'imgs/code.jpg')
        with open('./imgs/code.jpg', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        page.ele('@placeholder=图形验证码').input(res)
        print(res)
        page.ele('.btn btn-primary btn-block').click()
        page.wait(15)
        page.ele('.icon icon-calendar-check-o').click()
        image_url = page.ele('.vcode').attr('src')
        page.download(image_url, r'.\imgs', rename='code2', verify=False)
        os.rename('imgs/code2.htm', 'imgs/code2.jpg')
        with open('./imgs/code2.jpg', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        page.ele('@placeholder=验证码').input(res)
        page.ele('.btn btn-block btn-primary axbutton').click()
        print(page.ele('.modal-body').text)
        if page.ele('.modal-body').text=='验证码错误!!!':
            return True
        else:
            return False
    except Exception as e:
        return  False
qiandao()
# while True:
#     if qiandao():
#         break