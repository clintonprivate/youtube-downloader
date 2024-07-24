cipher = "uEqlI1IEPQ0NY5gqGSn3Izk7zJ%3Dgwlhh2YJnKGMkbKG-AEiAufzspOV-oDRAlRGB5w6AdpcsX4GrjW9m5aLNWV8To1IAhIgAwsSdQfJ0"
url = "https://rr1---sn-uxaxjva0hc0n-nm46.googlevideo.com/videoplayback%3Fexpire%3D1721881178%26ei%3D-n2hZqT6ILbUi9oPwP6hgAI%26ip%3D2a02%253A2454%253A7d9d%253A9400%253A7048%253A8421%253A98eb%253A12ab%26id%3Do-AJmFEEfyxrc1uFaJQjvxUY-uuywHfQGHWRgHXKd3PhC8%26itag%3D137%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26xpc%3DEgVo2aDSNQ%253D%253D%26mh%3DK5%26mm%3D31%252C29%26mn%3Dsn-uxaxjva0hc0n-nm46%252Csn-4g5lzner%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D1%26pl%3D34%26initcwndbps%3D2242500%26bui%3DAXc671LcbLdn0DzHXYrovRRDcTvHp7NIQh99RZU9YPgWmv63VJpWiw-H7FYm7YeVy7XLJg6Tgi_l-CYr%26spc%3DNO7bAZpLfKYylSj2_YHUKYyDfeP9oxaKPHU6NUFwuN8S95Lnbz3uc-4mrRHC%26vprv%3D1%26svpuc%3D1%26mime%3Dvideo%252Fmp4%26ns%3D0CDd7BsT2CboDQM-AI4wPf0Q%26rqh%3D1%26gir%3Dyes%26clen%3D13153453%26dur%3D188.730%26lmt%3D1709635576154970%26mt%3D1721858715%26fvip%3D5%26keepalive%3Dyes%26c%3DWEB%26sefc%3D1%26txp%3D4535434%26n%3DqnpW-GRD0pTrVWM%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cxpc%252Cbui%252Cspc%252Cvprv%252Csvpuc%252Cmime%252Cns%252Crqh%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAGtxev0wRAIgKVEreTKp8OIL1OBDKPNWt2fxLInPI_gWPb2sqA9dKoECIAVCDmHkdAsjmH4eFay4aReG0HQlQbtVAvDElH3fxGo9"

def HBa(a):
    a = list(a)
    cL.WL(a, 26)
    cL.JE(a)
    cL.WL(a, 45)
    cL.WL(a, 8)
    return ''.join(a)

class cL:
    @staticmethod
    def WL(a, b):
        c = a[0]
        a[0] = a[b % len(a)]
        a[b % len(a)] = c

    @staticmethod
    def JE(a):
        a.reverse()

    @staticmethod
    def iB(a, b):
        del a[:b]

# Example usage:
result = HBa(cipher)
print(result)
