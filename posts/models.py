from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Post(models.Model):
    TargetChoices = (
        ("청년", "청년"),
        ("미성년자", "미성년자"),
        ("대학생", "대학생"),
        ("직장인", "직장인"),
        ("군인", "군인"),
        ("기혼", "기혼"),
        ("무주택자", "무주택자"),
        ("장애인", "장애인"),
        ("국가유공자", "국가유공자")
    )

    CategoryChoices = (
        ("지원 정책", "지원 정책"),
        ("금융 상품", "금융 상품"),
        ("주간 소식", "주간 소식")
    )

    IncomeChoices = (
        ('무소득', '무소득'),
        ('1~100만원', '1~100만원'),
        ('101~200만원', '101~200만원'),
        ('201~300만원', '201~300만원'),
        ('301만원~400만원', '301만원~400만원'),
        ('401만원초과', '401만원초과')
    )

    title = models.CharField(max_length=30)
    # term = models.CharField(max_length=20)
    end_date = models.DateField(blank=True, null=True)
    subhead = models.CharField(max_length=20)
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')
    # tag1 = models.CharField(blank=True, null=True, max_length=10)
    body = models.TextField()
    min_age = models.PositiveIntegerField(blank=True, null=True)
    max_age = models.PositiveIntegerField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CategoryChoices, default="지원 정책")
    loc1 = models.CharField(max_length=10, blank=True, null=True) # (일단 입력하는 방식으로 대체) 서울시, 경기도, 인천시, 강원도, 충청북도, 충청남도, 전라북도, 전라남도, 경상북도, 경상남도, 부산시, 대구시, 울산시, 제주도
    loc2 = models.CharField(max_length=10, blank=True, null=True) # 강남구, 강동구 ...
    target = MultiSelectField(max_length=60, choices=TargetChoices, default="청년", blank=True, null=True)
    income = MultiSelectField(max_length=60, choices=IncomeChoices, default="무소득", blank=True, null=True)
    count = models.PositiveBigIntegerField(default=0) # 조회수
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def update_counter(self):
        self.count = self.count + 1
        self.save()