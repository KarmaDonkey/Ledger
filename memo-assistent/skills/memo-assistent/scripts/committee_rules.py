"""Meeting rhythm, pre-read deadlines and Swedish public holidays for the committee path.

Order: TC -> GAC -> GEC -> RCC -> Board. The committee calendar always overrides these rules.
"""
import datetime as dt

ORDER = ["TC", "GAC", "GEC", "RCC", "Board"]


def easter(year):
    a, b, c = year % 19, year // 100, year % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = (h + l - 7 * m + 114) % 31 + 1
    return dt.date(year, month, day)


def swedish_holidays(year):
    """Public holidays plus the de-facto non-working eves (Midsummer, Christmas and New Year's Eve)."""
    e = easter(year)
    midsummer_eve = next(dt.date(year, 6, d) for d in range(19, 26) if dt.date(year, 6, d).weekday() == 4)
    return {
        dt.date(year, 1, 1), dt.date(year, 1, 6),
        e - dt.timedelta(2), e + dt.timedelta(1), e + dt.timedelta(39),
        dt.date(year, 5, 1), dt.date(year, 6, 6), midsummer_eve,
        dt.date(year, 12, 24), dt.date(year, 12, 25), dt.date(year, 12, 26), dt.date(year, 12, 31),
    }


_HOL = {}


def is_business_day(d):
    if d.year not in _HOL:
        _HOL[d.year] = swedish_holidays(d.year)
    return d.weekday() < 5 and d not in _HOL[d.year]


def prev_business_day(d):
    while not is_business_day(d):
        d -= dt.timedelta(1)
    return d


def minus_business_days(d, n):
    while n > 0:
        d -= dt.timedelta(1)
        if is_business_day(d):
            n -= 1
    return d


def nth_weekday(year, month, weekday, n):
    d = dt.date(year, month, 1)
    while d.weekday() != weekday:
        d += dt.timedelta(1)
    return d + dt.timedelta(weeks=n - 1)


def deadline(committee, meeting):
    """Pre-read deadline by rule: TC Monday same week, GAC Thursday week before,
    GEC Friday week before, RCC and Board 9 calendar days before. Moved to the previous business day."""
    offset = {"TC": 3, "GAC": 5, "GEC": 3, "RCC": 9, "Board": 9}[committee]
    return prev_business_day(meeting - dt.timedelta(offset))


def ordinary_meetings(start, end):
    """All ordinary meetings by rule between start and end (meetings on holidays are dropped)."""
    out = []
    d = start
    while d <= end:
        wd = d.weekday()
        if wd == 3: out.append(("TC", d))
        if wd == 1: out.append(("GAC", d))
        if wd == 0: out.append(("GEC", d))
        d += dt.timedelta(1)
    y, m = start.year, start.month
    while (y, m) <= (end.year, end.month):
        for com, wd in (("RCC", 2), ("Board", 3)):
            md = nth_weekday(y, m, wd, 3)
            if start <= md <= end:
                out.append((com, md))
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    out = [(c, d) for c, d in out if is_business_day(d)]
    out.sort(key=lambda r: (r[1], ORDER.index(r[0]) if r[0] in ORDER else 99))
    return [{"committee": c, "date": d, "deadline": deadline(c, d), "type": "Ordinary", "booked": ""} for c, d in out]
