"""
设置类：存放游戏的相关配置信息
"""
class Setting():
    """存储《外星人入侵》的所有设置类"""
    #游戏屏幕的大小，颜色

    def __init__(self):
        #屏幕窗口大小
        self.screen_width = 1200
        self.screen_height = 600

        #银河系背景颜色
        self.bg_color = (230,230,230)

        """
        飞船的设置
        """
        #控制飞船速度
        self.ship_speed_factor = 1.5

        """
        子弹的设置
        """
        #子弹的大小
        self.bullet_width = 5
        self.bullet_heigh = 10
        #子弹的颜色
        self.bullet_color = (60,60,60)
        #子弹的移动速度
        self.bullet_speed = 5
        #限制子弹的数量
        self.bullets_allowed = 3

