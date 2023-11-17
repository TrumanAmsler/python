class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default values.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status of the television if it is powered on.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Increase the channel by one if the television is powered on.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Decrease the channel by one if the television is powered on.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by one if the television is powered on and unmuted.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by one if the television is powered on and unmuted.
        """
        if self.__status:
            self.__muted = False
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """
        Return a string representation of the television's status.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

        