from superwires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)
space_image = games.load_image("space.jpg", transparent = 0)
games.screen.background = space_image

missile_sound = games.load_sound("missile.wav")
games.music.load("theme.mid")
choice = None
while choice != "0":
    print(
        """
        Звук и музыка
        0 - Выйти
        1 - Воспроизвести звук ракетного залпа
        2 - Циклизировать звук ракетного залпа
        3 - Остановить звук ракетного залпа
        4 - Воспроизвести музыкальную тему игры
        5 - Циклизировать музыкальную тему игры
        6 - Остановить музыкальную тему игры
        """
        )
    choice = input("Ваш выбор ")
    print()
    if choice == "0":
        print("До свидания.")

    elif choice == "1":
        missile_sound.play()
        print("Воспроизвожу звук ракетного залпа.")

    elif choice == "2":
        loop = int(input("Сколько ещё раз воспроизвести этот звук? (-1 = воспроизводить не переставая): "))
        missile_sound.play(loop)
        print("Циклизирую звук ракетного залпа.")

    elif choice == "3":
        missile_sound.stop()
        print("Останавливаю звук ракетного залпа.")

    elif choice == "4":
        games.music.play()
        print("Исполняю музыкальную тему игры.")

    elif choice == "5":
        loop = int(input("Сколько ещё раз воспроизвести эту музыку? (-1 = воспроизводить не переставая): "))
        games.music.play(loop)
        print("Циклизирую музыкальную тему игры.")

    elif choice == "6":
        games.music.stop()
        print("Останавливаю музыкальную тему игры.")
        
    else:
        print("Извините, в меню нет такого пункта", choice)
input("\n\nНажмите Enter, чтобы выйти.")      
         
