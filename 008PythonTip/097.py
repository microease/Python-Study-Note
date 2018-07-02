# 你是国际民用压缩技术公司（International Civil Pack-technical Company, ICPC）的产品测试员。
# 现在你有一项任务：测试包有特殊缓冲材料的玻璃围棋子的牢固度。
# 如果围棋子从某个足够高的楼层落下来就会碎，但如果没有碎，缓冲材料会自动修复损伤部分，
# 也就是说如果从6楼落下来不碎，从6楼把同一颗棋子丢1000次，它都不会碎（当然在现实中，围棋子从手中多落下几次就会碎）。
# 我们定义一个临界楼层：围棋子从这个楼层或更高落下来会碎，且围棋子从任何比这个楼层低的楼层落下都不会碎。
# 如果棋子从1楼丢下来也碎了，临界楼层就是1。
# 你的任务就是利用你面前这座偶然发现的大厦，寻找手中这种围棋子的临界楼层。
# 当然，大厦不一定足够高，我们规定如果你从最高层丢棋子仍然没有摔碎棋子，还是算找到了临界楼层。
# 策略1：如果你只有1颗棋子，那你不得不从1楼开始尝试丢，如果没碎就到2楼丢，还没碎就到3楼丢……
# 直到棋子碎了，那你现在所在的楼层就是临界楼层（显然这是只用一颗棋子确保能发现临界楼层的唯一方法）。
# 策略2：你现在有两颗棋子，你可以从10楼开始试，每次上升10层，直到第1颗棋子碎了（比如在60楼）；
# 然后用策略1，从51楼开始用第2颗棋子1层层试上去。这样，如果大厦共100层，你最多只要试20次就能找到这个临界楼层。
# 但是这不是最佳策略：最佳策略最多只要尝试14次（最佳策略指的是在最坏情况下能用最少次数测出临界楼层的策略）。
# 现在给出你面前的大厦的楼层数。请你构思出最佳测试策略，用你手中的两颗棋子最多测几次就能确保找到那个临界楼层？
# （注意：正如刚才提到的，因为大厦不一定足够高，即使在100层的大厦里你从99层丢棋子没有摔碎，
# 也不能认定100层一定是临界层，而至少要到100层丢一次。当然，这一次无论棋子是否摔碎都算是找到了临界层）。
# 现在给你楼层的高度n，输出对于高度为n层的大厦而言测量临界楼层的最佳策略所需的最多次数。
# 如n=5, 则输出3.