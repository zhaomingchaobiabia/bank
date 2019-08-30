from django.forms.models import ModelForm
from front.models import *


class BorrowUserInfo(ModelForm):
    '''
    用户借款表单模型
    '''
    class Meta:
        model = Borrow
        fields = '__all__'