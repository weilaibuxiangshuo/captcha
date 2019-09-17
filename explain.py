views中调用

class CaptchaView(View):
    """
    获取图片验证码
    """
    def get(self, request):
        text, img = Captcha.generate_captcha()
        print(text,'text')
        # 返回图片
        return HttpResponse(img, content_type='image/jpg')
        
        
 html中展示
 
<img src="{% url 'ceshi:captchaview' %}" onclick="this.src='{% url "ceshi:captchaview" %}?'+Math.random()" alt="">
