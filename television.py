class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status
        self.__muted = False

    def mute(self):
        self.__muted = not self.__muted
        if self.__muted:
            self.__status = False

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__volume += 1
                if self.__volume > Television.MAX_VOLUME:
                    self.__volume = Television.MAX_VOLUME

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__volume -= 1
                if self.__volume < Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME

    def __str__(self):
        return "TV status: Power = " + str(self.__status) + ", Channel = " + str(self.__channel) + ", Volume = " + str(self.__volume)
