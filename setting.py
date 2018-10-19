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

        #控制飞船速度
        self.ship_speed_factor = 1.5