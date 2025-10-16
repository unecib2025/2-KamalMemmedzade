# # nomer 1
# password=input("Enter your password: ")
# if len(password)<8:
#     print("Слишком короткий пароль")
# if len(password)>=8:
#     print("Пароль принят")


# # nomer 2
# status = input("Введите состояние сервера (online/offline): ")
# if status == "online":
#     print("Связь установлена")
# else:
#     print("Связь потеряна")


# # nomer 3
# level = int(input("Введите уровень угрозы (1–100): "))
# if 1 <= level <= 30:
#     print("Низкий уровень угрозы")
# elif 31 <= level <= 70:
#     print("Средний уровень угрозы")
# elif 71 <= level <= 100:
#     print("Критический уровень угрозы")
# else:
#     print("Ошибка ввода")


# # nomer 4
# checksum_original = input()
# checksum_current = input()
# status = "Файл не изменён" if checksum_original == checksum_current else "Файл повреждён"
# print(status)


# # nomer 5
# event_code = input()
# match event_code:
#     case "ERR":
#         print("Ошибка системы")
#     case "WRN":
#         print("Предупреждение")
#     case "INF":
#         print("Информационное сообщение")
#     case _:
#         print("Неизвестный код события")
