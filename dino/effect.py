"""All effects should be declared in this module"""

class Effects():
    """
    Effect is ready to get an IO system to trigger side effects
    At the moment pyautogui interface is fallowed
    """

    def __init__(self, io_system):
        self.io_system = io_system

    def press_key(self, key_name):
        """Triggers effect pressing on a key"""
        self.io_system.press(key_name)

    def grab(self):
        """Take a screenshot"""
        self.io_system.grab()
