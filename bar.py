#!/usr/bin/env python3

import tkinter as tk
import psutil
import time
import threading

class TopBar(tk.Tk):
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.overrideredirect(True)  # Без рамок
        self.geometry(f"{self.winfo_screenwidth()}x24+0+0")  # По ширине экрана, высота 24, вверху
        self.attributes("-topmost", True)  # Всегда сверху
        self.configure(bg="#1d1f21")

        # Метка для текста
        self.label = tk.Label(self, fg="#c5c8c6", bg="#1d1f21", font=("Monospace", 12))
        self.label.pack(fill=tk.BOTH, expand=1)

        # Запускаем обновление информации
        self.update_info()

    def update_info(self):
        # Получаем CPU загрузку в процентах
        cpu = psutil.cpu_percent(interval=None)

        # Свободная память в Мб
        mem = psutil.virtual_memory().available // (1024 * 1024)

        # Текущее время
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        # Формируем строку
        status = f"CPU: {cpu:.1f}% | MEM free: {mem} MB | {current_time}"

        # Обновляем метку
        self.label.config(text=status)

        # Обновляем каждую секунду
        self.after(1000, self.update_info)


if __name__ == "__main__":
    app = TopBar()
    app.mainloop()
