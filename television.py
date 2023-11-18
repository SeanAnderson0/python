class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default settings.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__temp_volume: int = 0

    def power(self) -> None:
        """
        Toggle the power status of the television and unmutes when powered off.
        """
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False

    def mute(self) -> None:
        """
        Toggle mute status.
        When muting, store the current volume, set volume to 0.
        When unmuting, restore the volume from the stored value.
        """
        if self.__status:
            if not self.__muted:
                self.__temp_volume = self.__volume
                self.__volume = 0
                self.__muted = True
            elif self.__muted:
                self.__volume = self.__temp_volume
                self.__muted = False

    def channel_up(self) -> None:
        """
        Increases the current channel by 1, wrapping around if the maximum is reached.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the current channel by 1, wrapping around if below the minimum.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume by 1, up to the maximum value, unless the television is muted.
        """
        if self.__status:
            if self.__muted is True:
                self.mute()
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1, down to the minimum value, unless the television is muted.
        """
        if self.__status:
            if self.__muted is True:
                self.mute()
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the Television object.
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
