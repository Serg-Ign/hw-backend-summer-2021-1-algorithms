__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    #
    iSecondsInMinute = 60
    iSecondsInHour = iSecondsInMinute * 60
    iSecondsInTwentyFourHours = iSecondsInHour * 24
    #
    tSecs = seconds
    #
    iDays = tSecs // iSecondsInTwentyFourHours  # Полные дни
    tSecs = tSecs % iSecondsInTwentyFourHours  # Остаток для перевода в ЧЧ-ММ-СС
    iHours = tSecs // iSecondsInHour  # Полные часы
    tSecs = tSecs % iSecondsInHour  # Остаток для перевода в ММ-СС
    iMinutes = tSecs // iSecondsInMinute  # Полные минуты
    iSeconds = tSecs % iSecondsInMinute  # Секунды
    sDays = f"{iDays:02}d" if iDays > 0 else ""
    sHours = f"{iHours:02}h" if iHours > 0 or iDays > 0 else ""
    sMinutes = f"{iMinutes:02}m" if iMinutes > 0 or iHours > 0 or iDays > 0 else ""
    return sDays + sHours + sMinutes + f"{iSeconds:02}s"
    # raise NotImplementedError

