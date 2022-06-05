import tkinter as tk
from tkinter import ttk
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import threading


class Hollys(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        shops = list()

        for i in range(1, 55):
            url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
            print(f'{i} : {url}')
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, "html.parser")
            tbody = soup.find('tbody')
            trs = tbody.find_all('tr')

            for shop in trs:
                tds = shop.find_all('td')
                shop_name = tds[1].string  # 매장명
                shop_address = tds[3].string  # 주소
                shop_phone = tds[5].string  # 전화번호
                shops.append([shop_name] + [shop_address] + [shop_phone])

        hollys_df = pd.DataFrame(shops, columns=('매장명', '주소', '전화번호'))
        hollys_df.to_csv('hollys.csv', mode='w', encoding='cp949', index=True)


def hollys():
    # Hollys("할리스 매장정보").start()
    h = Hollys("할리스 매장정보")
    h.start()


def change_number(ev):
    lbl_disp.configure(text=f'슬라이더 값 : {int(scaled.get())}')


if __name__ == "__main__":
    w = tk.Tk()
    w.title("노트북, 프레임")
    w.geometry("300x400")

    nb_tab = ttk.Notebook(w)
    fr_tab1 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab1, text='슬라이더')

    lbl_disp = ttk.Label(fr_tab1, text="슬라이더 값 : ")
    scaled = tk.DoubleVar()
    s = ttk.Scale(fr_tab1, variable=scaled, from_=0, to=100, orient='h', command=change_number)
    lbl_disp.pack()
    s.pack(fill='x')

    fr_tab2 = ttk.Frame(nb_tab)
    nb_tab.add(fr_tab2, text='커피')

    btn_hollys = ttk.Button(fr_tab2, text='할리스 정보 다운로드', command=hollys)
    btn_hollys.pack(fill='x')

    nb_tab.pack(fill='both')
    w.mainloop()
