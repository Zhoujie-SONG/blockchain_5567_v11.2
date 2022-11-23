# @Written by LI Zijie 2022/11/23 16:25
# 需要用到的常变量
#
# from const.const import Const

class Const:
    # 基准挖掘时间 Mining time for per block
    BASE_MINETIME = 10

    # 基准难度
    BASE_DIFFICULTY = 1

    # 随机NONCE上限
    MAX_NONCE = 2 ** 256

    # actual_time小于 UPPER_LIMIT倍expected_time，difficulty增加
    UPPER_LIMIT = 2

    # actual_time大于 LOWER_LIMIT倍expected_time，difficulty减少
    LOWER_LIMIT = 0.5

    ADJUSTMENT_NUM = 10
    # # Sleep time when simulate double spending attacking
    # # Unit : second
    # SLEEP_TIME = 20

    # # The beginning index for double spending attacking
    # ATTACK_INDEX = 5
    #
    # # The first time flag of attacking
    # FIRST_FLAG = 1

    # 最大币值
    MAX_COIN = 21000000

    # 挖掘新区块的奖励
    REWARD = 20
