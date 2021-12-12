class TV:
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    def __init__(self):
        self.channel = 0
        self.lenth = len(self.CHANNELS)

    def first_channel(self):
        self.channel = 0

    def last_channle(self):
        self.channel = -1

    def turn_channel(self, NUM):
        if 1 <= NUM <= self.lenth:
            self.channel = NUM - 1
        else:
            return False

    def next_channel(self):
        if self.channel + 1 == self.lenth:
            self.channel = 0
        else:
            self.channel += 1

    def previous_channel(self):
        if self.channel == 0:
            self.channel = self.lenth - 1
        else:
            self.channel -= 1

    def current_channel(self):
        return self.channel + 1

    def is_exist(self, channel):
        if isinstance(channel, str):
            if channel in self.CHANNELS:
                return True
            return False
        elif isinstance(channel, int):
            channel = int(channel)
            if 0 <= channel <= self.lenth:
                return True
            return False
        else:
            return None



