# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import time

import requests


# 按间距中的绿色按钮以运行脚本。

def start(class_id,seconds,user_id,cookies):
    total = seconds*60
    cookies = {
        'JSESSIONID': f'{cookies}',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'Origin': 'http://ycx-vod1.people-health.cn',
        'Referer': f'http://ycx-vod1.people-health.cn/video/play?videoId={class_id}&userId={user_id}&notifyUrl=http://train.people-health.cn/course/train/callback/5777048218894336',
    }
    for i in range(0,total,60):
        data = {
            'videoId': f'{class_id}',
            'userId': f'{user_id}',
            'currentTime': f'{i}',
            'interval': '1'
        }

        response = requests.post('http://ycx-vod1.people-health.cn/video/play/record', headers=headers, cookies=cookies,
                                 data=data, verify=False)
        print(response.text)
        time.sleep(0.1)


class_id_lst = ["5747227913487360","5747332568876032",
                "5747322157990912","5747324876997632",
                "5747343853814784","5747344958620672",
                "5757165937067008","5747341794460672"]


if __name__ == '__main__':
    userId = "rmwv2_909641"
    cookies = "EC83EA558A23C7FAD9BC054683A3D4C5"
    for id_ in class_id_lst:
        start(id_, 23,userId,cookies)
        print(id_, "学习完成！")