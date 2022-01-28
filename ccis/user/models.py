from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ClassInfo(models.Model):
    '''
    班级信息
    '''
    class_name = models.CharField(verbose_name='班名', max_length=30, null=True, unique=True)
    class_id = models.AutoField(verbose_name='班id', primary_key=True)
    class_leader_id = models.IntegerField(verbose_name='班长id', unique=True)
    class_leader_name = models.CharField(verbose_name='班长名', max_length=30, )
    # 班级人数，在人员出现增改的时候需要做变更
    class_count = models.IntegerField(verbose_name='班级人数', default=0)

    def __str__(self):
        return self.class_name

    class Meta:
        db_table = 'class_info'
        verbose_name = '班级信息'
        verbose_name_plural = '班级信息'


class SkillTable(models.Model):
    '''
    员工技能表格
    '''
    skill_id = models.AutoField(verbose_name='技能id', primary_key=True)
    skill_name = models.CharField(verbose_name='技能名称', max_length=30, unique=True)

    def __str__(self):
        return self.skill_name

    class Meta:
        db_table = 'skill_table'
        verbose_name = '技能'
        verbose_name_plural = '技能'


class UserInfo(AbstractUser):
    '''
    用户信息表
    '''
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女')
    )
    STATION_CHOICES = (
        ('general_staff', '普通员工'),
        ('group_leader', '组长'),
        ('squad_leader', '班长'),
        ('g_squad_leader', '大班长')
    )
    STAR_CHOICES = (
        ('one_star', '1星'),
        ('two_star', '2星'),
        ('three_star', '3星'),
        ('four_star', '4星'),
        ('five_star', '5星'),
        ('six_star', '6星')
    )
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    # 工号 / int
    operator_id = models.CharField(null=True, verbose_name='工号', max_length=20, unique=True)
    # 姓名 / string
    # django自带
    # 性别 / string
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='female', verbose_name='性别')
    # 所属班 / 外键 - 班
    # 根据组来对应
    # 所属组 / 外键 - 组
    user_group = models.ForeignKey('GroupInfo', related_name='group_member', to_field='group_id',
                                   on_delete=models.CASCADE, null=True)
    # 岗位 / string
    station = models.CharField(verbose_name='岗位', max_length=30, choices=STATION_CHOICES, default='general_staff')
    # 星级 / string
    star_level = models.CharField(verbose_name='星级', max_length=30, choices=STAR_CHOICES, default='one_star')
    # 此员工一周最多能排的晚班次数 / int / >= 0
    max_night_shift = models.IntegerField(verbose_name='一周最多能上的晚班数', null=True)
    # 技能 / 在技能表中有做多对多的关联
    # 是否请假 /
    vacate = models.BooleanField(verbose_name='是否处于请假状态', default=False)
    # 是否专席/默认为普席
    is_spe_seat = models.BooleanField(verbose_name='是否专席', default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_info'
        verbose_name = '员工信息'
        verbose_name_plural = '员工信息'


class GroupInfo(models.Model):
    '''
    小组信息
    '''
    GROUP_CATEGORY_CHOICES = (
        ('new_staff', '新员工班组'),
        ('old_staff', '非新员工班组'),
        ('other', '其他')
    )
    group_id = models.AutoField(verbose_name='组id', primary_key=True)
    group_name = models.CharField(verbose_name='组名', max_length=30)
    group_leader_id = models.IntegerField(verbose_name='组长id', null=True, unique=True)
    group_leader_name = models.CharField(verbose_name='组长名字', null=False, max_length=30)
    group_count = models.IntegerField(verbose_name='小组人数', default=0)
    group_category = models.CharField(verbose_name='小组类型', max_length=30, choices=GROUP_CATEGORY_CHOICES)
    group_class = models.ForeignKey(ClassInfo, related_name='group_members', on_delete=models.CASCADE,
                                    verbose_name='所属班')

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'group_info'
        verbose_name = '小组信息'
        verbose_name_plural = '小组信息'


class UserSkill(models.Model):
    user = models.ForeignKey('UserInfo', verbose_name='员工', on_delete=models.CASCADE)
    skill = models.ForeignKey('SkillTable', verbose_name='技能', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_skill'
        verbose_name = '员工-技能表'
        verbose_name_plural = '员工-技能表'




