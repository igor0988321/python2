# import tkinter
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_weather():
#     req = requests.get("https://sinoptik.ua/ru/pohoda/mykolaiv")
#     soup = BeautifulSoup(
#         req.content,
#         "html.parser"
#     )
#
#     weather = soup.find(
#         "p",
#         class_="R1ENpvZz"
#     )
#
#     temp.config(
#         text = weather.text
#     )
#
# # print(weather.text)
#
# window = tkinter.Tk()
# window.geometry("300x300")
# window.title("Погода Миколаїв")
#
# title = tkinter.Label(
#     window,
#     text="Миколаїв",
#     font="Calibre 15"
# )
# title.pack(
#     pady=20
# )
#
#
#
# temp = tkinter.Label(
#     window,
#     text="0",
#     font="Consolas 30"
# )
# temp.pack(
#     pady=50
# )
#
#
# get_weather()
#
# update = tkinter.Button(
#     window,
#     text="Оновити інформацію",
#     font="Arial 15",
#     command=get_weather
# )
# update.pack()
#
# window.mainloop()