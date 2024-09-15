import pygame
import random
import time

# 初始化Pygame
pygame.init()

# 定义屏幕大小和颜色
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 创建屏幕对象
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("羊了个羊 - 动物版消除类小游戏")

# 加载支持中文的字体
font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 36)

# 加载动物图片
cat_img = pygame.image.load("image1.png")  
chicken_img = pygame.image.load("image2.png")  
dog_img = pygame.image.load("image3.png")  
cow_img = pygame.image.load("image6.png")  
lion_img=pygame.image.load("image4.png")
monkey_img=pygame.image.load("image5.png")
pig_img=pygame.image.load("image7.png")
sheep_img=pygame.image.load("image8.png")
Tiger_img=pygame.image.load("image9.png")

# 缩放图片
tile_size = 100  # 定义图片方块的大小
cat_img = pygame.transform.scale(cat_img, (tile_size, tile_size))
chicken_img = pygame.transform.scale(chicken_img, (tile_size, tile_size))
dog_img = pygame.transform.scale(dog_img, (tile_size, tile_size))
cow_img = pygame.transform.scale(cow_img, (tile_size, tile_size))
lion_img = pygame.transform.scale(lion_img, (tile_size, tile_size))
monkey_img = pygame.transform.scale(monkey_img, (tile_size, tile_size))
pig_img = pygame.transform.scale(pig_img, (tile_size, tile_size))
sheep_img = pygame.transform.scale(sheep_img, (tile_size, tile_size))
Tiger_img = pygame.transform.scale(Tiger_img, (tile_size, tile_size))

# 定义游戏变量
clock = pygame.time.Clock()
total_time = 160  # 倒计时160秒
start_time = time.time()
game_over = False
game_win = False
layer_count = 3  # 图案分层数

# 随机生成成对的动物图片
def generate_tiles(layer_count):
    tiles = []
    images = [cat_img, chicken_img, dog_img, cow_img,lion_img, monkey_img, pig_img, sheep_img, Tiger_img]  # 动物图片列表
    tile_pairs = []

    # 创建成对的图片
    for img in images:
        for _ in range(layer_count * 2):  # 每个动物生成两对
            tile_pairs.append({"image": img})

    # 随机打乱这些方块的位置
    random.shuffle(tile_pairs)

    # 为每个方块设置随机位置
    for i in range(len(tile_pairs)):
        x = random.randint(0, SCREEN_WIDTH - tile_size)
        y = random.randint(100, SCREEN_HEIGHT - tile_size)
        tile_pairs[i]["rect"] = pygame.Rect(x, y, tile_size, tile_size)
        tiles.append(tile_pairs[i])

    return tiles

# 绘制图案
def draw_tiles(tiles):
    for tile in tiles:
        screen.blit(tile["image"], tile["rect"])

# 主游戏循环
def game_loop():
    global game_over, game_win
    tiles = generate_tiles(layer_count)
    selected_tiles = []
    
    while not game_over:
        screen.fill(WHITE)
        elapsed_time = time.time() - start_time
        remaining_time = total_time - elapsed_time
        
        if remaining_time <= 0:
            game_over = True
            break
        
        # 绘制倒计时
        timer_text = font.render(f"剩余时间: {int(remaining_time)}", True, BLACK)
        screen.blit(timer_text, (10, 10))
        
        # 绘制图案
        draw_tiles(tiles)
        
        # 检测事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for tile in tiles:
                    if tile["rect"].collidepoint(pos):
                        if tile in selected_tiles:
                            selected_tiles.remove(tile)
                        else:
                            selected_tiles.append(tile)
        
        # 匹配逻辑：如果有两个选择的图案相同则消除
        if len(selected_tiles) == 2:
            if selected_tiles[0]["image"] == selected_tiles[1]["image"]:
                tiles.remove(selected_tiles[0])
                tiles.remove(selected_tiles[1])
            selected_tiles = []

        # 检测胜利条件
        if not tiles:
            game_win = True
            game_over = True

        pygame.display.update()
        clock.tick(30)

# 游戏结束界面
def end_game():
    screen.fill(WHITE)
    if game_win:
        end_text = font.render("你赢了！", True, BLACK)
    else:
        end_text = font.render("时间到！你输了！", True, BLACK)
    screen.blit(end_text, (SCREEN_WIDTH // 2 - end_text.get_width() // 2, SCREEN_HEIGHT // 2 - end_text.get_height() // 2))
    pygame.display.update()
    time.sleep(3)

# 主菜单
def main_menu():
    screen.fill(WHITE)
    title_text = font.render("羊了个羊 - 动物版消除类小游戏", True, BLACK)
    start_text = font.render("点击任意键开始游戏", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - title_text.get_height() // 2 - 50))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - start_text.get_height() // 2 + 50))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# 游戏入口
def main():
    main_menu()
    game_loop()
    end_game()

if __name__ == "__main__":
    main()



