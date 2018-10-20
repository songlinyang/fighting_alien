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

        """
        外星人的设置
        """
        #外星飞船的左右移动速度
        self.alien_speed_factor = 1
        #外星飞船向下移动速度
        self.fleet_drop_speed = 10
        #控制外星飞船向右还是左移动，向右为：1，向左为：-1,默认向右移动
        self.fleet_direction = 1


