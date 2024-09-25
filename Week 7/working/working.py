import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    pattern = r'^(?:(1?[0-2]|\d):?([0-5][0-9])? (AM|PM)) to (?:(1?[0-2]|\d):?([0-5][0-9])? (AM|PM))$'
    if matches := re.search(pattern, s):
        hrs_list = [matches[1], matches[4]]
        mins_list = [matches[2], matches[5]]
        ampm_list = [matches[3], matches[6]]

        dict_am = {'12':'00', '1':'01', '2':'02', '3':'03',
                   '4':'04', '5':'05', '6':'06', '7':'07',
                   '8':'08', '9':'09', '10':'10', '11':'11'}

        dict_pm = {'1':'13', '2':'14', '3':'15','4':'16',
                    '5':'17', '6':'18', '7':'19', '8':'20',
                    '9':'21', '10':'22', '11':'23', '12':'12'}

        for i in range(len(hrs_list)):
            if ampm_list[i] == 'AM':
                hrs_list[i] = dict_am[hrs_list[i]]

            else:
                hrs_list[i] = dict_pm[hrs_list[i]]

            mins_list[i] = "00" if mins_list[i] is None else mins_list[i]

        return f'{hrs_list[0]}:{mins_list[0]} to {hrs_list[1]}:{mins_list[1]}'

    else:
        raise ValueError

if __name__ == "__main__":
    main()
