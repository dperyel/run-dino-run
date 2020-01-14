class Effects():
    """
    Effect is ready to get an IO system to trigger side effects
    At the moment pyautogui interface is fallowed
    """

    def __init__(self, io_system):
        self.io_system = io_system

    def press_key(self, key_name):
        print(f'Pressing a {key_name}')
        self.io_system.press(key_name)
