class Date:
    @staticmethod
    def is_date_valid(d):
        # 내 코드
        # date = d.split('-')
        # if int(date[1]) <= 12:
        #     if int(date[2]) <= 31:
        #         return True
        # return False

        # 코딩 도장 코드
        year, month, day = map(int, d.split('-'))
        return month <= 12 and day <= 31


if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')